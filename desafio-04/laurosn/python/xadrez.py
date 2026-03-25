#!/usr/bin/python
import numpy as np

def main():
    f = open('xadrez.txt', 'r')
    l = [[int(num) for num in line.split(' ')] for line in f]
    y = np.array(l)
    print("Peão:" + str(np.count_nonzero(y == 1)) + " peça(s)")
    print("Bispo:" + str(np.count_nonzero(y == 2)) + " peça(s)")
    print("Cavalo:" + str(np.count_nonzero(y == 3)) + " peça(s)")
    print("Torre:" + str(np.count_nonzero(y == 4)) + " peça(s)")
    print("Rainha:" + str(np.count_nonzero(y == 5)) + " peça(s)")
    print("Rei:" + str(np.count_nonzero(y == 6)) + " peça(s)")
if __name__ == "__main__":
  main()