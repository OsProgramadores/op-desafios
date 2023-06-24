#!/bin/bash

# Verifica se o arquivo existe, se não, baixa por wget
if [ ! -f d14.txt ]; then
  echo "Error: Aquivo não existe!!!"
  echo "Fazendo download..."
  
  wget https://osprogramadores.com/files/d14/d14.txt.gz
  gzip -d d14.txt.gz
fi

dotnet run d14.txt
