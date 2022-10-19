import pandas as pd
import sqlite3


def run_script(db, script):                                                     #функция run_script с параметром script
    try:
        sqlite_connection = sqlite3.connect(db)                                 #подключение к бд
        cursor = sqlite_connection.cursor()                                     #создание объекта курсора
        #print("База данных подключена к SQLite")

        cursor.execute(script)                                                  #выполнение скрипта
        sqlite_connection.commit()                                              #сохранить изменения
        out = cursor.fetchall()                                                 #возвращает все строки в ходе выполнения скрипта в виде списка
        #print("Скрипт SQLite успешно выполнен")
        print(out)                                                              #вывод результата
        cursor.close()                                                          #закрытие курсора

    except sqlite3.Error as error:                                              #в случае ошибки
        print("Ошибка при подключении к sqlite", error)

    finally:
        if (sqlite_connection):
            sqlite_connection.close()                                           #закрываем соединение с бд
       #     print("Соединение с SQLite закрыто")


print("Введите название файла бд")
db = input()                                                                    #переменная с названием бд

input_ = 0                                                                      #переменная ввода пользователя
while input_ != 9:                                                              #в случае 9 выходим из программы
    print("\n Введите номер запроса: 1- вставка новых данных")
    print("2 - вывод всех записей, 3 - запроса на изменение одного и нескольких объектов в БД;")
    print("4 - запроса на выборку данных по условию, 9 - выход;")
    input_ = int(input())

    if input_ == 1:
        print("Напишите запрос на вставку вида: INSERT INTO teachers VALUES (5, 'Анри', 'Пуанкаре', 'мат')")
        input_ = input()                                               #пользовательский ввод
        run_script(db, input_)                                         #запускаем скрипт

    if input_ == 2:
        print("Студенты:")
        run_script(db, "SELECT * FROM students")                         #запускаем скрипт
        print("Преподаватели:")
        run_script(db, "SELECT * FROM teachers")                        #запускаем скрипт
        print("Факультеты:")
        run_script(db, "SELECT * FROM subject")

    if input_ == 3:
        print("Напишите запрос на выборку вида: UPDATE teachers SET name = 'Андрей' WHERE name = 'Анри'")
        input_ = input()  # пользовательский ввод
        run_script(db, input_)  # запускаем скрипт

    if input_ == 4:
        print("Напишите запрос на выборку вида: SELECT * FROM students WHERE spec = 'мат'")
        input_ = input()  # пользовательский ввод
        run_script(db, input_)  # запускаем скрипт






