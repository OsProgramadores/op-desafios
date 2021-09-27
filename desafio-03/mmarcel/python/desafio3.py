print ("Digite o numero incial:")
inicial = int(input())
print ("Digite o numero final:")
final = int(input())

for i in range(inicial,final):
    #print (i)
    t = str(i)
    #print (t)
    #print (t[::-1])
    if t == t[::-1]:
        print (t)
