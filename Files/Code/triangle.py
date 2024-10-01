import random

def kub():
    x = random.randint(1, 6)
    print(x)
    if x == 5 or x == 6:
        print('Победа!')
    elif x == 3 or x == 4:
        kub()
    elif x == 1 or x == 2:
        print('Вы проиграли :(')

if __name__ == '__main__':
    kub()