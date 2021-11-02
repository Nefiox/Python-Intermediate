def run():
    # my_dict = {}
    # # for i in range (1,101):
    # #     if i % 3 != 0:
    # #         my_dict[i] = i**3

    # Dictionary comprehension:
    # {key: value for value in iterable if condition}

    # my_dict = {i: i**3 for i in range(1,101) if i % 3 != 0}

    my_dict = {i: round(i**(1/2), 2) for i in range(1,1001)}


    print(my_dict)


if __name__ == '__main__':
    run()