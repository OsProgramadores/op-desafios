# Solução desafio 7 unix tac em Go

Executar:

```bash
go build tac.go
./tac 1GB.txt > out.txt
md5sum out.txt
2b4fd25f11d75c285ec69ecac420bd07  out.txt
```

Para testar os 512MB de memória com control groups v1:

```bash
# install cgroup
sudo apt-get install cgroup-tools

# setup cgroup
export CGROUP=osProgramadoresD7
export CGROUPP="memory/$CGROUP"
sudo cgcreate -t $USER:$USER -a $USER:$USER -g memory:"$CGROUP"
echo 512M > "/sys/fs/cgroup/$CGROUPP/memory.limit_in_bytes"
echo 0 > "/sys/fs/cgroup/$CGROUPP/memory.swappiness"

# run in cgroup
cgexec -g memory:$CGROUP ./tac 1GB.txt > out.txt
md5sum out.txt
2b4fd25f11d75c285ec69ecac420bd07  out.txt

# check max mem used
cat "/sys/fs/cgroup/$CGROUPP/memory.max_usage_in_bytes" | numfmt --to=iec
512M
```
