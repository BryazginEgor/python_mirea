import os
import random as rn
import shutil


def task1(x0, v, t=0, a=0):
    return x0 + v * t + (a * (t * t)) / 2


def task2(x):
    sum = 0
    while x != 0:
        sum += x % 10
        x = x // 10
    return sum

def task3():
    list_of_goods = [
        'стол',
        'стул',
        'кровать',
        'кресло',
        'диван',
        'стена',
        'дом',
        'окно',
        'дерево',
        'фанера',
        'молоток',
        'гвозди',
        'орех',
        'конфета',
        'трактор',
        'енот'
    ]

    set1 = rn.sample(list_of_goods, rn.randint(1, len(list_of_goods)))
    set2 = rn.sample(list_of_goods, rn.randint(1, len(list_of_goods)))

    return list(set(set1) ^ set(set2))

def task4():
    employee_database = {
        "Andrei B.D.": {
            "age": 11,
            "post": "Manager",
            "workplace_number": 1,
            "access_to_secret": "yes",
        },
        "Danil D.D.": {
            "age": 10,
            "post": "Manager",
            "workplace_number": 2,
            "access_to_secret": "no",
        },
        "Aleksei D.K.": {
            "age": 9,
            "post": "Manager",
            "workplace_number": 3,
            "access_to_secret": "no",
        },
        "Kirill T.D.": {
            "age": 8,
            "post": "Manager",
            "workplace_number": 4,
            "access_to_secret": "yes",
        },
    }
    return employee_database

def task5():
    number = rn.randint(0,1)

    try:
        return 10 / number
    except Exception:
        print('Деление на 0')

def task6(file_path, string):
    with open(file_path, "a") as file:
        file.write(string + "\n")

def task7(file_path):
    try:
        with open(file_path, "r") as file:
            file_content = file.read()
            print(file_content)
    except Exception:
        print("No file")

def task8(file_path, copy_file_path):
    try:
        shutil.copy(file_path, copy_file_path)
        os.remove(file_path)
    except Exception:
        print("No file")