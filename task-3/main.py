def task_1():
    from flask import Flask

    # задание 1
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello, World!'


    if __name__ == '__main__':
         app.run()

# задание 2
def task_2():
    filepath = "task.txt"
    with open(filepath, "w") as file:
        while True:
            string = str(input())
            if string == "стоп":
                break
            file.write(string + "\n")


# задание 3
def task_3():
    from flask import Flask, render_template, request
    app = Flask(__name__)
    # маршрут для главной страницы
    @app.route("/")
    def index():
        return render_template("index1.html")

    # маршрут для записи строки в файл
    @app.route("/write", methods=["POST"])
    def write():
        # считываем текст из формы
        text = request.form.get("text")
        # записываем текст в файл
        with open("output.txt", "a") as f:
            f.write(text + "\n")

        return render_template("index1.html", message="Text written to file successfully!")

    # маршрут для чтения содержимого файла
    @app.route("/read")
    def read():
        # читаем содержимое файла
        with open("output.txt", "r") as f:
            text = f.read()

        return render_template("result.html", text=text)

    if __name__ == '__main__':
        app.run(debug=True)

# задание 4
def task_4():
    import sqlite3
    def create_table():
        conn = sqlite3.connect('personal_info.db')
        cur = conn.cursor()
        cur.execute(
            """CREATE table IF NOT EXISTS INFO(
            [name] text,
            birthday_year int,
            profession text)"""
        )
        conn.commit()
        conn.close()
    def insert(name, year , prof):
        conn = sqlite3.connect('personal_info.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO INFO (name, birthday_year, profession) VALUES (?, ?, ?)", (name, year, prof))
        conn.commit()
        conn.close()

    def print_users():
        conn = sqlite3.connect('personal_info.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM INFO")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        conn.close()

    create_table()

    while True:
        name = str(input("Введите имя: "))
        if name == 'стоп':
            break;
        year = int(input("Ввелите год рождения: "))
        profession = str(input("Введите род деятельности: "))
        insert(name,year,profession)

    print_users()

# задание 5
def task_5():
    from flask import Flask, render_template, request
    import sqlite3
    import random
    import string

    app = Flask(__name__)
    DB_NAME = 'test.db'

    def create_table():
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT)''')
        conn.commit()
        conn.close()

    def insert_data(text):
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("INSERT INTO data (text) VALUES (?)", (text,))
        conn.commit()
        conn.close()

    def delete_data(id):
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("DELETE FROM data WHERE id=?", (id,))
        conn.commit()
        conn.close()

    def get_data():
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("SELECT * FROM data")
        data = c.fetchall()
        conn.close()
        return data

    @app.route('/')
    def home():
        create_table()
        data = get_data()
        return render_template('task5.html', data=data)

    @app.route('/add', methods=['POST'])
    def add():
        text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        insert_data(text)
        return home()

    @app.route('/delete', methods=['POST'])
    def delete():
        id = request.form['id']
        delete_data(id)
        return home()

    if __name__ == '__main__':
        app.run()

# задание 6
def task_6():
    from flask import Flask, render_template, request, redirect, session

    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/page_1', methods=['GET', 'POST'])
    def page_1():
        if request.method == 'POST':
            last_name = request.form['last_name']
            first_name = request.form['first_name']
            middle_name = request.form['middle_name']
            birth_date = request.form['birth_date']
            occupation = request.form['occupation']

            session['last_name'] = last_name
            session['first_name'] = first_name
            session['middle_name'] = middle_name
            session['birth_date'] = birth_date
            session['occupation'] = occupation.split(',')

            return redirect('/')

        return render_template('page_1.html')

    @app.route('/page_2', methods=['GET', 'POST'])
    def page_2():
        if request.method == 'POST':
            salaries = {}

            for occupation in session['occupation']:
                salary = request.form.get(occupation)
                salaries[occupation] = salary

            session['salaries'] = salaries

            return redirect('/')

        return render_template('page_2.html', occupations=session['occupation'])

    @app.route('/page_3')
    def page_3():
        data = {
            'last_name': session['last_name'],
            'first_name': session['first_name'],
            'middle_name': session['middle_name'],
            'occupation_salaries': session['salaries']
        }

        return render_template('page_3.html', data=data)

    if __name__ == '__main__':
        app.secret_key = 'supersecretkey'
        app.run(debug=True)