from random import randint
import time


# ЗАДАНИЕ 1
def job1():
    a = int(input("Введите первое число: "))
    action = str(input("Введите действие: "))
    b = int(input("Введите второе число: "))
    if action == "+":
        print(a + b)
    elif action == "-":
        print(a - b)
    elif action == "*":
        print(a * b)
    elif action == "/":
        if b == 0:
            print("ERROR")
        else:
            print(a / b)
    elif action == "^":
        print(a ** b)
    elif action == "%":
        print(a % b)
    elif action == "//":
        print(a // b)


# ЗАДАНИЕ 2
def job2():
    stop_word_1 = True
    stop_word_2 = True
    list_noun = []
    list_verb = []

    while stop_word_1:
        check = str(input("Введите существительное: "))
        if check == "stop":
            stop_word_1 = False
        else:
            list_noun.append(check)

    while stop_word_2:
        check = str(input("Введите глагол: "))
        if check == "stop":
            stop_word_2 = False
        else:
            list_verb.append(check)

    if len(list_verb) == 0:
        print("ERROR")
    if len(list_noun) == 0:
        print("ERROR")

    phrases = int(input("Введите кол-во фраз: "))

    for i in range(0, phrases):
        number = randint(0, 3)
        if number == 1:
            print(f"{list_noun[randint(0, len(list_noun) - 1)]} {list_noun[randint(0, len(list_noun) - 1)]}"
                  f" {list_verb[randint(0, len(list_verb)) - 1]}")
        elif number == 0:
            print(f"{list_verb[randint(0, len(list_verb) - 1)]} {list_noun[randint(0, len(list_noun) - 1)]}"
                  f" {list_noun[randint(0, len(list_noun) - 1)]}")
        else:
            print(f"{list_noun[randint(0, len(list_noun) - 1)]} {list_verb[randint(0, len(list_verb) - 1)]}"
                  f" {list_noun[randint(0, len(list_noun) - 1)]}")


# ЗАДАНИЕ 3
def job3():
    flag = True
    list_right_words = []

    print("Введите \"правильные\" слова, после напишите stop: ")

    while flag:
        check = str(input())
        if check == "stop":
            flag = False
        else:
            list_right_words.append(check)

    string = str(input("Введите строку: "))

    list_doubt_words = string.split(sep=" ")

    for i in range(0, len(list_right_words)):
        for j in range(0, len(list_doubt_words)):
            wrong_counter = 0

            if len(list_right_words[i]) == len(list_doubt_words[j]):
                wrong_word = ""

                for w in range(0, len(list_right_words[i])):
                    if list_right_words[i][w] != list_doubt_words[j][w]:
                        wrong_word += f" {list_doubt_words[j][w]} "
                        wrong_counter += 1
                    else:
                        wrong_word += f"{list_doubt_words[j][w]}"

                if wrong_counter == 1:
                    print(wrong_word)


# ЗАДАНИЕ 4
def job4():
    num_hours = int(input("Введите кол-во часов: "))
    num_min = int(input("Введите кол-во минут: "))
    num_secs = int(input("Введите кол-во секунд: "))
    num_secs += num_hours * 3600 + num_min * 60
    flag = True

    while flag:
        m, s = divmod(num_secs, 60)
        h, m = divmod(m, 60)
        clock_format = '{:02d}:{:02d}:{:02d}'.format(h, m, s)
        print(clock_format)
        time.sleep(1)
        num_secs -= 1


# Задание 5
def job5():
    book = "qwertyuiopasdfghjklzxcvbnm"

    main_classes = ("warrior", "savage", "thief", "leader", "lucky", "nerd")
    main_skills = ("big guns", "small guns", "traps", "explosives", "athletics", "repair", "steal")
    main_specifications = ("strength", "perception", "endurance", "charisma", "intelligence", "agility", "luck")

    your_name = ""
    skills = []

    for i in range(2, randint(2, 10)):
        your_name += book[randint(0, len(book) - 1)]

    your_class = main_classes[randint(0, len(main_skills) - 1)]
    your_age = randint(18, 60)
    your_param = (
    randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
    num_of_skills = randint(1, 4)

    for i in range(0, num_of_skills):
        check = randint(0, len(main_skills) - 1)
        flag = True
        while flag:
            if main_skills[check] in skills:
                check = randint(0, len(main_skills) - 1)
            else:
                flag = False
        skills.append(main_skills[check])

    print(f"Имя: {your_name} \nВозраста: {your_age} \nКласс: {your_class} \nПараметры:"
          f"\n  -{main_specifications[0]}: {your_param[0]}"
          f"\n  -{main_specifications[1]}: {your_param[1]}"
          f"\n  -{main_specifications[2]}: {your_param[2]}"
          f"\n  -{main_specifications[3]}: {your_param[3]}"
          f"\n  -{main_specifications[4]}: {your_param[4]}"
          f"\n  -{main_specifications[5]}: {your_param[5]}"
          f"\n  -{main_specifications[6]}: {your_param[6]}"
          f"\nНавыки:")
    for i in range(0, len(skills)):
        print(f"  -{skills[i]}")


# ЗАДАНИЕ 6
def job6():
    print("Введите заказ, после напишите stop")
    flag = True
    order = []

    balk_50 = 0
    balk_100 = 0
    board_25 = 0
    board_50 = 0
    plywood = 0

    while flag:
        check = str(input())
        if check != "stop":
            order.append(check.split(sep=" "))
        else:
            flag = False

    for i in range(0,len(order)):
        if order[i][1] == "брус" and float(order[i][2]) == 50:
            balk_50 += int(order[i][0][:-1]) * float(order[i][3][:-1])
        if order[i][1] == "брус" and int(order[i][2]) == 100:
            balk_100 += int(order[i][0][:-1]) * float(order[i][3][:-1])
        if order[i][1] == "доска" and int(order[i][2]) == 25:
            board_25 += int(order[i][0][:-1]) * float(order[i][3][:-1])
        if order[i][1] == "доска" and int(order[i][2]) == 50:
            board_50 += int(order[i][0][:-1]) * float(order[i][3][:-1])
        if order[i][1] == "фанера":
            ply = str(order[i][3][:-1]).split(sep="*")
            plywood += int(order[i][0][:-1]) * float(ply[0]) * float(ply[1])

    print(f"Вам нужно купить:")
    if balk_50 != 0:
        print(f"{int(balk_50 // 3 + 1)}x брус 50 3м")
    if balk_100 != 0:
        print(f"{int(balk_100 // 6 + 1)}x брус 100 6м")
    if board_25 != 0:
        print(f"{int(board_25 // 6 + 1)}x доску 25 6м")
    if board_50 != 0:
        print(f"{int(board_50 // 6 + 1)}x доску 50 6м")
    if plywood != 0:
        print(f"{int(plywood // 1.5*1.5 + 1)}x фанеру 1.5*1.5м")

# ЗАДАНИЕ 7
def job7():
    countries = []
    republic_name = ["Азербайджан", "Армения", "Беларусь", "Грузия", "Казахстан", "Киргизия", "Латвия",
                     "Литва", "Молдова", "Россия", "Таджикистан", "Туркмения", "Узбекистан", "Украина", "Эстония"]


    farming_stat = [0, 0, 0, "farming"]
    light_industry_stat = [0, 0, 0, "light_industry"]
    heavy_industry_A_stat = [0, 0, 0, "heavy_industry_A"]
    heavy_industry_B_stat = [0, 0, 0, "heavy_industry_B"]
    military_industry_stat = [0, 0, 0, "military_industry"]
    science_stat = [0, 0, 0, "science"]
    chemical_industry_stat = [0, 0, 0, "chemical_industry"]

    statistic = [farming_stat, light_industry_stat, heavy_industry_A_stat, heavy_industry_B_stat,
                 military_industry_stat, science_stat, chemical_industry_stat]

    class Republic:
        def __init__(self):
            self.name = republic_name[randint(0, len(republic_name) - 1)]
            republic_name.remove(self.name)
            self.farming = randint(-1, 1)
            self.light_industry = randint(-1, 1)
            self.heavy_industry_A = randint(-1, 1)
            self.heavy_industry_B = randint(-1, 1)
            self.military_industry = randint(-1, 1)
            self.science = randint(-1, 1)
            self.chemical_industry = randint(-1, 1)

            self.dev_statistic = self.farming + self.light_industry + self.heavy_industry_A \
                                 + self.heavy_industry_B + self.military_industry + \
                                 self.science + self.chemical_industry

    number = int(input("Введите кол-во стран: "))

    for i in range(0, number):
        countries.append(Republic())

    for i in range(0, number):
        statistic[0][countries[i].farming + 1] += 1
        statistic[1][countries[i].light_industry + 1] += 1
        statistic[2][countries[i].heavy_industry_A + 1] += 1
        statistic[3][countries[i].heavy_industry_B + 1] += 1
        statistic[4][countries[i].military_industry + 1] += 1
        statistic[5][countries[i].science + 1] += 1
        statistic[6][countries[i].chemical_industry + 1] += 1

    lagged = 0
    lagged_name = ""
    advanced = 0
    advanced_name = ""
    balanced = 0
    balanced_name = ""

    for i in range(0,7):
        if statistic[i][0] > lagged:
            lagged = statistic[i][0]
            lagged_name = statistic[i][3]
        if statistic[i][1] > balanced:
            balanced = statistic[i][1]
            balanced_name = statistic[i][3]
        if statistic[i][2] > advanced:
            advanced = statistic[i][2]
            advanced_name = statistic[i][3]

    print(f"Самая отстающая отрасль в союзных республиках - {lagged_name}. Она остает в {lagged} республиках\n"
          f"Самая сбалансированная отрасль в союзных республиках - {balanced_name}. Она сбалансирована в {balanced} республиках\n"
          f"Самая передовая отрасль в союзных республиках - {advanced_name}. Она является опережающей в {advanced} республиках")

    for i in range(0,number):
        print(f"Коэффициент развития в {countries[i].name} - {countries[i].dev_statistic}")


# job1();
# job2()
# job3()
# job4()
# job5()
job6()
# job7()




