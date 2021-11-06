def divisors(number):
        divisors = []
        for i in range(1, number +1 ):
            if number % i == 0:
                divisors.append(i)
        return divisors


def run():
        num = input('Ingresa un número: ')
        assert num.isnumeric(), 'Debes ingresar un número'
        print(divisors(int(num)))
        print('Terminó el programa')


if __name__ == '__main__':
    run()