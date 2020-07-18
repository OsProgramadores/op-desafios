"""
Author > Teiji Watanabe
Obtain the quantity of each piece without using a conditional or multiple choice structure
"""

PIECES = [
    [4, 3, 2, 5, 6, 2, 3, 4],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [4, 3, 2, 5, 6, 2, 3, 4],
]

PIECES_NAMES = {
    "Peão": 1,
    "Bispo": 2,
    "Cavalo": 3,
    "Torre": 4,
    "Rainha": 5,
    "Rei": 6
}


def main():
    """Main Function"""
    pieces_count = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
    }
    for i, _ in enumerate(PIECES):
        for j in range(0, 7):
            pieces_count[j] += PIECES[i].count(j)

    for key in PIECES_NAMES:
        print("{}: {} peça(s)".format(key, pieces_count[PIECES_NAMES[key]]))


if __name__ == "__main__":
    main()
