DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Accenture',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Accenture',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Accenture',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Accenture',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']
    all_Accenture_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Accenture']
    adults = list(filter(lambda worker: worker['age'] > 18, DATA))
    adults= list(map(lambda worker: worker['name'], adults))

    # La forma de unir diccionarios es usando el simbolo |, para unir listas se usa el +

    # La función lambda va crear un nuevo diccionario uniendo el diccionario "base" con el que se está creando {'old': worker['age] > 70}
    # old_people = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA))
    old_validation = lambda worker_age: worker_age > 70
    old_people = [worker | {'old': old_validation(worker['age'])} for worker in DATA]

    for worker in old_people:
        print(worker)
        # {'name': 'Facundo', 'age': 72, 'organization': 'Accenture', 'position': 'Technical Coach', 'language': 'python', 'old': True}
        # {'name': 'Luisana', 'age': 33, 'organization': 'Globant', 'position': 'UX Designer', 'language': 'javascript', 'old': False}

if __name__ == '__main__':
    run()