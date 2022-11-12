from peewee import *

# Название базы, чтобы не писать его руками каждый раз
db_name = 'test.db'
db = SqliteDatabase(db_name)

# Объявление моделей для создания таблиц
class BaseModel(Model):
    class Meta:
        database = db
           
class StudentGroup(BaseModel):
    name = CharField()
    faculty = CharField()
    
class Student(BaseModel):
    name = CharField()
    surname = CharField()
    spec = CharField()
    group = ForeignKeyField(StudentGroup)
    
class Teacher(BaseModel):
    name = CharField()
    surname = CharField()
    faculty = CharField()

# Если в db_name указана база, которая еще не создана, то peewee создаст новую базу с именем db_name
# Строчка ниже создает таблицы в базе данных по модели
# Если база с таблицами уже создана, то заново создавать их не надо. Если база новая, то раскомментируй строку ниже

#db.create_tables([StudentGroup, Student, Teacher])

input_ = 0                                                                      
while input_ != 9:                                                              
    print("Введите номер запроса:")
    print("1- вставка новых данных;")
    print("2 - вывод всех записей;")
    print("3 - запрос на выборку данных по условию;")
    print("4 - запрос на изменение объектов в БД;")
    print("9 - выход")
    input_ = int(input())

    if input_ == 1:
        print("Выберите таблицу для вставки:")
        print("1: Группы")
        print("2: Студенты")
        print("3: Преподаватели")
        table_name = int(input())                                            
        print("Введите значения полей:")
          
        if table_name == 1:
            print('Название: ')
            name = input()
            print('Факультет: ')
            faculty = input()
            StudentGroup.insert(name = name, faculty = faculty).execute()
            
        elif table_name == 2:
            print('Имя:')
            name = input()
            print('Фамилия:')
            surname = input()
            print('Специальность:')
            spec = input()
            print('Номер группы:')
            group = input()
            Student.insert(name = name, surname = surname, spec = spec, group = group).execute()
            
        elif table_name == 3:
            print('Имя:')
            name = input()
            print('Фамилия:')
            surname = input()
            print('Предмет:')
            faculty = input()
            Teacher.insert(name = name, surname = surname, faculty = faculty).execute()
                                         

    if input_ == 2:
        print("Студенты:")
        students = Student.select().execute()
        for student in students:
            print(student.name + '|' + student.surname + '|' + student.spec + '|' + str(student.group))
            
        print("Преподаватели:")
        teachers = Teacher.select().execute()
        for teacher in teachers:
            print(teacher.name + '|' + teacher.surname + '|' + teacher.faculty)           
            
        print("Группы:")
        groups = StudentGroup.select().execute()
        for group in groups:
            print(group.name + '|' + group.faculty)
            
    if input_ == 3:
        print("Напишите запрос на выборку вида: SELECT * FROM students WHERE spec = 'мат'")
        print("Выберите таблицу:")
        print("1: Группы")
        print("2: Студенты")
        print("3: Преподаватели")
        table_number = int(input()) 
        if table_number == 1:
            print("Выберите столбец:")
            print("1: Название")
            print("2: Факультет")
            column_number = int(input()) 
            
            print("Введите значение столбца")
            column_value = input() 
            
            if column_number == 1:
                groups = StudentGroup.select().where(StudentGroup.name == column_value).execute()
                for group in groups:
                    print(group.name + '|' + group.faculty)
            if column_number == 2:
                groups = StudentGroup.select().where(StudentGroup.faculty == column_value).execute()
                for group in groups:
                    print(group.name + '|' + group.faculty)
            
        elif table_number == 2:
            print("Выберите столбец:")
            print("1: Имя")
            print("2: Фамилия")
            print("3: Специальность")
            print("4: Группа")
            column_number = int(input()) 
            
            print("Введите значение столбца")
            column_value = input()
            
            if column_number == 1:
                students = Student.select().where(Student.name == column_value).execute()
                for student in students:
                    print(student.name + '|' + student.surname + '|' + student.spec + '|' + str(student.group))
            if column_number == 2:
                students = Student.select().where(Student.name == column_value).execute()
                for student in students:
                    print(student.name + '|' + student.surname + '|' + student.spec + '|' + str(student.group))
            if column_number == 3:
                students = Student.select().where(Student.name == column_value).execute()
                for student in students:
                    print(student.name + '|' + student.surname + '|' + student.spec + '|' + str(student.group))
            if column_number == 4:
                students = Student.select().where(Student.name == column_value).execute()
                for student in students:
                    print(student.name + '|' + student.surname + '|' + student.spec + '|' + str(student.group))
                    
        elif table_number == 3:
            print("Выберите столбец:")
            print("1: Имя")
            print("2: Фамилия")
            print("3: Факультет")
            
            print("Введите значение столбца")
            column_value = input()
            if column_number == 1:
                teachers = Teacher.select().where(Teacher.name == column_value).execute()
                for teacher in teachers:
                    print(teacher.name + '|' + teacher.surname + '|' + teacher.faculty) 
            if column_number == 2:
                teachers = Teacher.select().where(Teacher.name == column_value).execute()
                for teacher in teachers:
                    print(teacher.name + '|' + teacher.surname + '|' + teacher.faculty) 
            if column_number == 3:
                teachers = Teacher.select().where(Teacher.name == column_value).execute()
                for teacher in teachers:
                    print(teacher.name + '|' + teacher.surname + '|' + teacher.faculty) 
                    
    if input_ == 4:
        print("Напишите запрос на выборку вида: UPDATE teachers SET name = 'Андрей' WHERE name = 'Анри'")
        print("Выберите таблицу:")
        print("1: Группы")
        print("2: Студенты")
        print("3: Преподаватели")
        table_number = int(input()) 
        
        if table_number == 1:
            print("Выберите столбец:")
            print("1: Название")
            print("2: Факультет")
            column_number = int(input()) 
            
            print("Введите новое значение")
            new_value = input()
            
            print("Выберите столбец для выборки (если оставить пустым, то изменения применятся для всех записей)")
            print("1: Название")
            print("2: Факультет")
            column_where = int(input()) 
            
            if column_number == 1:
                if column_where == 1: 
                    print("Введите значения столбца для выборки")
                    column_where_value = input()
                    query = StudentGroup.update(name = new_value).where(StudentGroup.name == column_where_value)
                    query.execute()
                
                elif column_where == 2:
                    print("Введите значения столбца для выборки")
                    column_where_value = input()
                    query = StudentGroup.update(name = new_value).where(StudentGroup.faculty == column_where_value)
                    query.execute()
                else:
                    groups = StudentGroup.update(name = new_value)
                    query.execute()
                
            if column_number == 2:
                if column_where == 1: 
                    print("Введите значения столбца для выборки")
                    column_where_value = input()
                    query = StudentGroup.update(faculty = new_value).where(StudentGroup.name == column_where_value)
                    query.execute()
                
                elif column_where == 2:
                    print("Введите значения столбца для выборки")
                    column_where_value = input()
                    query = StudentGroup.update(faculty = new_value).where(StudentGroup.faculty == column_where_value)
                    query.execute()
                else:
                    groups = StudentGroup.update(faculty = new_value)
                    query.execute()

        if table_number == 2:
            print("Выберите столбец:")
            print("1: Имя")
            print("2: Фамилия")
            print("3: Специальность")
            print("4: Группа")
            column_number = int(input()) 
            
            print("Введите новое значение")
            new_value = input()
            
            print("Выберите столбец для выборки (если оставить пустым, то изменения применятся для всех записей)")
            print("1: Имя")
            print("2: Фамилия")
            print("3: Специальность")
            print("4: Группа")
            column_where = int(input()) 
            
            if column_number == 1:
                if column_where == 1: 
                    print("Введите значения столбца для выборки")
                    column_where_value = input()
                    query = Student.update(name = new_value).where(Student.name == column_where_value)
                    query.execute()
                
                elif column_where == 2:
                    print("Введите значения столбца для выборки")
                    column_where_value = input()
                    query = Student.update(name = new_value).where(Student.surname == column_where_value)
                    query.execute()
                    
                elif column_where == 3: 
                    print("Введите значения столбца для выборки")
                    column_where_value = input()
                    query = Student.update(name = new_value).where(Student.spec == column_where_value)
                    query.execute()
                
                elif column_where == 4:
                    print("Введите значения столбца для выборки")
                    column_where_value = input()
                    query = Student.update(name = new_value).where(Student.group == column_where_value)
                    query.execute()
                else:
                    query = Student.update(name = new_value)
                    query.execute()
                
            if column_number == 2:
                if column_where == 1: 
                    print("Введите значения столбца для выборки")
                    column_where_value = input()
                    query = Student.update(surname = new_value).where(Student.name == column_where_value)
                    query.execute()
                
                elif column_where == 2:
                    print("Введите значения столбца для выборки")
                    column_where_value = input()
                    query = Student.update(surname = new_value).where(Student.surname == column_where_value)
                    query.execute()
                    
                elif column_where == 3: 
                    print("Введите значения столбца для выборки")
                    column_where_value = input()
                    query = Student.update(surname = new_value).where(Student.spec == column_where_value)
                    query.execute()
                
                elif column_where == 4:
                    print("Введите значения столбца для выборки")
                    column_where_value = input()
                    query = Student.update(surname = new_value).where(Student.group == column_where_value)
                    query.execute()
                else:
                    query = Student.update(surname = new_value)
                    query.execute()
                    
            if column_number == 3:
                if column_where == 1: 
                    print("Введите значения столбца для выборки")
                    column_where_value = input()
                    query = Student.update(spec = new_value).where(Student.name == column_where_value)
                    query.execute()
                
                elif column_where == 2:
                    print("Введите значения столбца для выборки")
                    column_where_value = input()
                    query = Student.update(spec = new_value).where(Student.surname == column_where_value)
                    query.execute()
                    
                elif column_where == 3: 
                    print("Введите значения столбца для выборки")
                    column_where_value = input()
                    query = Student.update(spec = new_value).where(Student.spec == column_where_value)
                    query.execute()
                
                elif column_where == 4:
                    print("Введите значения столбца для выборки")
                    column_where_value = input()
                    query = Student.update(spec = new_value).where(Student.group == column_where_value)
                    query.execute()
                else:
                    query = Student.update(spec = new_value)
                    query.execute()
                    
            if column_number == 4:
                if column_where == 1: 
                    print("Введите значения столбца для выборки")
                    column_where_value = input()
                    query = Student.update(group = new_value).where(Student.name == column_where_value)
                    query.execute()
                
                elif column_where == 2:
                    print("Введите значения столбца для выборки")
                    column_where_value = input()
                    query = Student.update(group = new_value).where(Student.surname == column_where_value)
                    query.execute()
                    
                elif column_where == 3: 
                    print("Введите значения столбца для выборки")
                    column_where_value = input()
                    query = Student.update(group = new_value).where(Student.spec == column_where_value)
                    query.execute()
                
                elif column_where == 4:
                    print("Введите значения столбца для выборки")
                    column_where_value = input()
                    query = Student.update(group = new_value).where(Student.group == column_where_value)
                    query.execute()
                else:
                    query = Student.update(group = new_value)
                    query.execute()
            
        if table_number == 3:
            print("Выберите столбец:")
            print("1: Имя")
            print("2: Фамилия")
            print("3: Факультет")
            column_number = int(input()) 
            
            print("Введите новое значение")
            new_value = input()
            
            print("Выберите столбец для выборки (если оставить пустым, то изменения применятся для всех записей)")
            print("1: Имя")
            print("2: Фамилия")
            print("3: Факультет")
            column_where = int(input()) 
            
            if column_number == 1:
                if column_where == 1: 
                    print("Введите значения столбца для выборки")
                    column_where_value = input()
                    query = Teacher.update(name = new_value).where(Teacher.name == column_where_value)
                    query.execute()
                
                elif column_where == 2:
                    print("Введите значения столбца для выборки")
                    column_where_value = input()
                    query = Student.update(name = new_value).where(Teacher.surname == column_where_value)
                    query.execute()
                    
                elif column_where == 3: 
                    print("Введите значения столбца для выборки")
                    column_where_value = input()
                    query = Student.update(name = new_value).where(Teacher.faculty == column_where_value)
                    query.execute()
                
                else:
                    query = Teacher.update(name = new_value)
                    query.execute()
                    
            if column_number == 2:
                if column_where == 1: 
                    print("Введите значения столбца для выборки")
                    column_where_value = input()
                    query = Teacher.update(surname = new_value).where(Teacher.name == column_where_value)
                    query.execute()
                
                elif column_where == 2:
                    print("Введите значения столбца для выборки")
                    column_where_value = input()
                    query = Student.update(surname = new_value).where(Teacher.surname == column_where_value)
                    query.execute()
                    
                elif column_where == 3: 
                    print("Введите значения столбца для выборки")
                    column_where_value = input()
                    query = Student.update(surname = new_value).where(Teacher.faculty == column_where_value)
                    query.execute()
                
                else:
                    query = Teacher.update(surname = new_value)
                    query.execute()
                    
            if column_number == 3:
                if column_where == 1: 
                    print("Введите значения столбца для выборки")
                    column_where_value = input()
                    query = Teacher.update(faculty = new_value).where(Teacher.name == column_where_value)
                    query.execute()
                
                elif column_where == 2:
                    print("Введите значения столбца для выборки")
                    column_where_value = input()
                    query = Student.update(faculty = new_value).where(Teacher.surname == column_where_value)
                    query.execute()
                    
                elif column_where == 3: 
                    print("Введите значения столбца для выборки")
                    column_where_value = input()
                    query = Student.update(faculty = new_value).where(Teacher.faculty == column_where_value)
                    query.execute()
                
                else:
                    query = Teacher.update(faculty = new_value)
                    query.execute()
            
   
db.close()





