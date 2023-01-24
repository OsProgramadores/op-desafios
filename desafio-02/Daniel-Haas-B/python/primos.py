def run():
    for i in range (2, 10001):
        if is_prime(i):
            print(i)

def is_prime(i):
    for j in range(1, i):
        if i % j == 0:
            if i != j and j != 1:
                return False
    return True

if __name__ == "__main__":
    run()
