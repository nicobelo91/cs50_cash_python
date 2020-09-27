  
from cs50 import get_int
from cs50 import get_float


def main():
    money = get_money()
    cents = round(money * 100)
    coins = 0
    while cents >= 25:
        cents = cents - 25
        coins = coins + 1
    while cents >= 10:
        cents = cents - 10
        coins = coins + 1
    while cents >= 5:
        cents = cents - 5
        coins = coins + 1
    while cents >= 1:
        cents = cents - 1
        coins = coins + 1
    print(f"{coins}")


def get_money():
    while True:
        n = get_float("Changed owed: ")
        if n > 0:
            break
    return n


main()