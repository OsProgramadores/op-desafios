# Desafio 4 - OsProgramadores
# Nicholas Borba
# 12/07/2018

qtdP = {"Pawn":0, "Rock":0, "Knight":0, "Bishop":0, "Queen":0, "King":0}
board = [[4,3,2,5,6,2,3,4],
        [1,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1],
        [4,3,2,6,5,2,3,4]]

def setPieces():
    line = 1
    for i in board:
        column = 0
        for y in enumerate(i):
            print("\nDo it slowly, if you type a space/tabs, none or letter, it will stop. I haven't yet found a way to validate the input without IF.")
            print("\nPawn: 1 | Rock: 4 | Knight: 3 | Bishop: 2 | Queen: 5 | King: 6")
            i[column] = int(input("Type the piece number who should be on line "+str(line)+" column "+str(column+1)+": "))
            column+=1
        line+=1

def countBoard():
    for i in board:
        for y in i:
            #print(y) #FOR DEBUG
            qtdP["Pawn"]    +=bool(y==1)
            qtdP["Rock"]    +=bool(y==4)
            qtdP["Knight"]  +=bool(y==3)
            qtdP["Bishop"]  +=bool(y==2)
            qtdP["Queen"]   +=bool(y==5)
            qtdP["King"]    +=bool(y==6)
    print("\n")
    for i, y in qtdP.items():
        print(i, "\t= ", y)

def printCurrentBoard():
    print("\n")
    for i, y in enumerate(board):
        print(i+1, y)

print("\nDo you want to see it running right now or insert your pieces into the board?")
print("WARNING: Typing your pieces could be BORING! It's a chess board 8x8")
print("\n1 - Run now! | 2 - Insert pieces")

opt = int(input())

if opt == 1:
    countBoard()
    printCurrentBoard()
elif opt == 2:
    setPieces()
    countBoard()
    printCurrentBoard()
