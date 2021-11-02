def run():
    my_list = [1, "Hi", True, 8.7]
    my_dict = {'firstname': 'John', 'lastname': 'McLane'}

    super_list = [
        {'firstname': 'John', 'lastname': 'McLane'},
        {'firstname': 'Laura', 'lastname': 'Rodelo'},
        {'firstname': 'Rebeca', 'lastname': 'García'},
        {'firstname': 'Pedro', 'lastname': 'Torres'},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.5, 3.4, -6.74, 8.21]
    }

    for key, value in super_dict.items():
        print(key, '-', value)

    for item in super_list:
        print(item["firstname"], "-" ,item["lastname"])


if __name__ == '__main__':
    run()