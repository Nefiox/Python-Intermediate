def divisors(number):
    divisors = []

    for i in range(1, number +1 ):
        if number % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = int(input('Ingresa un número: '))
    print(divisors(num))
    print('Terminó el programa')

if __name__ == '__main__':
    run()