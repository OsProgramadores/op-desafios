import tables, strutils, sequtils, strformat

let input = """
4 3 2 5 6 2 3 4
1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1
4 3 2 5 6 2 3 4
"""

let vals = input.splitWhitespace.map(parseInt)
let pieces = ["","Peão","Bispo","Cavalo","Torre","Rainha","Rei"]
var table = initCountTable[int]()

for elem in vals:
  table.inc(elem)

for key,vals in table:
  if key == 0 : continue
  echo &"{pieces[key]}: {vals} peça(s)"