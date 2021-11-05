def divisors(number):
    try:
        divisors = []
        if number < 0:
            raise ValueError('Ingresa un número positivo')
        for i in range(1, number +1 ):
            if number % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        print(ve)
        return False

def run():
    try:
        num = int(input('Ingresa un número: '))
        print(divisors(num))
        print('Terminó el programa')
    except ValueError:
        print('Debes ingresar un número')

if __name__ == '__main__':
    run()