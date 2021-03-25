with open("d14.txt", "r") as txt:
    for line in txt:
        op = line.replace("^", "**")
        try:
            print(int(eval(op)))
        except ZeroDivisionError:
            print("ERR DIVBYZERO")
        except SyntaxError:
            print("ERR SYNTAX")
            
