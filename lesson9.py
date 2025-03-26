"""
Описываем телефон:

Класс телефон. У него должны быть:

Поле для описания номера.
Метод, чтобы задать номер телефона.
Защищенное поле для счетчика входящих звонков.
Метод, который вернет нам количество принятых звонков.
Метод принять звонок, который добавляет к счетчику единицу.
Создайте три разных объекта телефона.

Поменяйте всем изначальный номер.

Примите по несколько звонков на каждом (разное количество)

Напишите функцию, которая принимает список из объектов телефонов, а возвращает общее количество принятых звонков со всех телефонов.
"""


class Phone:
    number: str = ""
    _call_count: int = 0

    def set_number(self, new_number:str)->None:
        self.number = new_number

    def calls(self) -> int:
        return self._call_count

    def call_accept(self) -> None:
        self._call_count+=1

ph1 = Phone
ph2 = Phone
ph3 = Phone

ph1.set_number("13123")
ph2.set_number("31318")
ph3.set_number("86970")


def make_n_calls(n:int, ph:Phone)->None:
    for _ in range(n):
        ph.call_accept()

make_n_calls(4, ph1)
make_n_calls(6, ph2)
make_n_calls(8, ph3)

def total_calls(phones: list[Phone]) -> int:
    return sum(ph.calls() for ph in phones) #! Разобраться

"""
Опишите класс для шахматной фигуры.

Фигура должна содержать такие атрибуты:

Цвет (белый или черный).
Место на доске (тут есть варианты, или два отдельных поля, 

для описания координат или одно, но, например, кортеж из двух чисел). И такие методы как:
Изменить цвет (ничего не принимает, только меняет цвет на противоположный).
Изменить место на доске (принимает или две переменные, или один кортеж из двух элементов), 

не забудьте проверить, что мы не пытаемся поставить фигуру 
за пределы доски (оба значения от 0 до 7).

Абстрактный метод проверки потенциального хода (детали ниже). 

На данном этапе фигуры могут стоять на одной и той же клетке, пока нам это не важно.
Опишите классы для пешки, коня, офицера, ладьи, ферзя и короля. 
Все, что в них нужно добавить - это один метод для проверки, возможно, 
ли за один ход поменять место фигуры на доске (все ходят по-разному, у пешек будет еще и разница от цвета). 
Метод принимает опять же или две цифры, или один кортеж. 
И опять же проверяем, не выходит ли значение за пределы доски 
(Так как нам необходим этом функционал дважды, я бы делал 
его как отдельный защищенный метод в родительском классе)

И функцию, которая принимает список фигур и потенциальную новую клетку, 
а возвращает список из фигур. Но только тех, которые могут за один ход добраться до этой клетки.
"""

class Figure:


    def __init__(self, color: str, x:int, y:int)->None:
        if color not in ["white", "black"]:
            raise ValueError("Цвет может быть либо белый либо черный")
        if not self.is_on_board(x, y):
            raise ValueError("Введите другие значения, фигура ушла за пределы доски")

        self.color = color
        self.x_position = x
        self.y_position = y

    def change_color(self)->None:
        self.color = "black" if self.color == "white" else "white"

    def move(self, new_x:int, new_y:int)-> None:
        if self.is_on_board(new_x, new_y):
            self.x_position = new_x
            self.y_position = new_y
        else:
            print("Значения заданы неверно!!")

    def is_on_board(self, x:int, y:int)->bool:
        return 0 <= x <= 7 and 0 <= y <= 7

    def check_next_step(self, step_x:int, step_y: int)->bool:
        return self.is_on_board(step_x, step_y)



class Pawn(Figure): #Пешка -> Ходит вперед на одну клетку (две клетки при первом ходе).

    def __init__(self, color: str, x: int, y: int):
        super().__init__(color, x, y)
        self.first_move = True
    def check_step(self, color:str, step_x:int, step_y:int) -> bool:
        direction = 1 if self.color == "white" else -1

        if step_x == self.x_position and step_y == self.y_position + direction:
            return True
        if self.first_move and step_x == self.x_position and step_y == self.y_position + 2 * direction:
            self.first_move = False
            return True
        if not self.first_move and step_x == self.x_position and step_y == self.y_position + 2 * direction:
            return False
        if step_x - self.x_position == 1 and step_y == self.y_position + direction:
            return True


    def move(self, new_x:int, new_y:int) -> None:
        if self.check_step(new_x, new_y):
            super().move(new_x, new_y)
            self.first_move = False
            print(f"Новая позиция x = {new_x} ; y = {new_y}")
        else:
            print("Введите корректное значение")


class Knight(Figure): #Конь -> Двигается буквой "Г" (два шага в одном направлении и один в другом).
    def __init__(self, color: str, x: int, y: int):
        super().__init__(color, x, y)

    def check_step(self, step_x: int, step_y: int) -> bool:

        possible_moves = [
            (self.x_position + 1, self.y_position + 2),
            (self.x_position - 1, self.y_position + 2),
            (self.x_position + 2, self.y_position + 1),
            (self.x_position + 2, self.y_position - 1),
            (self.x_position - 2, self.y_position + 1),
            (self.x_position - 2, self.y_position - 1),
            (self.x_position + 1, self.y_position - 2),
            (self.x_position - 1, self.y_position - 2),
        ]

        if (step_x, step_y) in possible_moves and self.is_on_board(step_x, step_y):
            return True

        return False

    def move(self, new_x:int, new_y:int)->None:
        if self.check_step(new_x, new_y):
            super().move(new_x, new_y)
            print(f"Новая позиция x = {new_x} ; y = {new_y}")

class Bishop(Figure):  # Слон -> Ходит по диагоналям на любое количество клеток.
    def __init__(self, color: str, x: int, y: int):
        super().__init__(color, x, y)
    def check_step(self, step_x: int, step_y: int) -> bool:

        possible_moves = []
        for i in range(1, 8):
            possible_moves.append((self.x_position - i, self.y_position + i))
            if not self.is_on_board(self.x_position - i, self.y_position + i):
                break


        for i in range(1, 8):
            possible_moves.append((self.x_position + i, self.y_position + i))
            if not self.is_on_board(self.x_position + i, self.y_position + i):
                break


        for i in range(1, 8):
            possible_moves.append((self.x_position - i, self.y_position - i))
            if not self.is_on_board(self.x_position - i, self.y_position - i):
                break


        for i in range(1, 8):
            possible_moves.append((self.x_position + i, self.y_position - i))
            if not self.is_on_board(self.x_position + i, self.y_position - i):
                break


        if (step_x, step_y) in possible_moves and self.is_on_board(step_x, step_y):
            return True

        return False

    def move(self, new_x:int, new_y:int)->None:
        if self.check_step(new_x, new_y):
            super().move(new_x, new_y)
            print(f"Новая позиция x = {new_x} ; y = {new_y}")

class Rook(Figure):  # Лодья -> Ходит по горизонтали или вертикали на любое количество клеток.
    def __init__(self, color: str, x: int, y: int):
        super().__init__(color, x, y)

    def check_step(self, step_x: int, step_y: int) -> bool:

        possible_moves = []


        for i in range(1, 8):
            possible_moves.append((self.x_position, self.y_position + i))
            if not self.is_on_board(self.x_position, self.y_position + i):
                break


        for i in range(1, 8):
            possible_moves.append((self.x_position, self.y_position - i))
            if not self.is_on_board(self.x_position, self.y_position - i):
                break


        for i in range(1, 8):
            possible_moves.append((self.x_position + i, self.y_position))
            if not self.is_on_board(self.x_position + i, self.y_position):
                break


        for i in range(1, 8):
            possible_moves.append((self.x_position - i, self.y_position))
            if not self.is_on_board(self.x_position - i, self.y_position):
                break

        return False

    def move(self, new_x: int, new_y: int) -> None:
            if self.check_step(new_x, new_y):
                super().move(new_x, new_y)
                print(f"Новая позиция x = {new_x} ; y = {new_y}")

class Quenn(Figure): # Ферзь -> Ходит как слон и ладья вместе — по диагонали, горизонтали и вертикали.
    def __init__(self, color: str, x: int, y: int):
        super().__init__(color, x, y)

    def check_step(self, step_x: int, step_y: int) -> bool:
        possible_moves = []

        for i in range(1, 8):
            possible_moves.append((self.x_position, self.y_position + i))
            if not self.is_on_board(self.x_position, self.y_position + i):
                break

        for i in range(1, 8):
            possible_moves.append((self.x_position, self.y_position - i))
            if not self.is_on_board(self.x_position, self.y_position - i):
                break

        for i in range(1, 8):
            possible_moves.append((self.x_position + i, self.y_position))
            if not self.is_on_board(self.x_position + i, self.y_position):
                break

        for i in range(1, 8):
            possible_moves.append((self.x_position - i, self.y_position))
            if not self.is_on_board(self.x_position - i, self.y_position):
                break

        # Слон: диагональные ходы
        for i in range(1, 8):
            possible_moves.append((self.x_position - i, self.y_position + i))
            if not self.is_on_board(self.x_position - i, self.y_position + i):
                break

        for i in range(1, 8):
            possible_moves.append((self.x_position + i, self.y_position + i))
            if not self.is_on_board(self.x_position + i, self.y_position + i):
                break

        for i in range(1, 8):
            possible_moves.append((self.x_position - i, self.y_position - i))
            if not self.is_on_board(self.x_position - i, self.y_position - i):
                break

        for i in range(1, 8):
            possible_moves.append((self.x_position + i, self.y_position - i))
            if not self.is_on_board(self.x_position + i, self.y_position - i):
                break

        return False

    def move(self, new_x: int, new_y: int) -> None:
            if self.check_step(new_x, new_y):
                super().move(new_x, new_y)
                print(f"Новая позиция x = {new_x} ; y = {new_y}")

class King(Figure): #Король -> Двигается на одну клетку в любом направлении.
    def __init__(self, color: str, x: int, y: int):
        super().__init__(color, x, y)

    def check_step(self, step_x: int, step_y: int) -> bool:

        possible_moves = [
            (self.x_position + 1, self.y_position),
            (self.x_position - 1, self.y_position),
            (self.x_position, self.y_position + 1),
            (self.x_position, self.y_position - 1),
            (self.x_position + 1, self.y_position + 1),
            (self.x_position - 1, self.y_position + 1),
            (self.x_position + 1, self.y_position - 1),
            (self.x_position - 1, self.y_position - 1),
        ]

        if (step_x, step_y) in possible_moves and self.is_on_board(step_x, step_y):
            return True

        return False

    def move(self, new_x:int, new_y:int)->None:
        if self.check_step(new_x, new_y):
            super().move(new_x, new_y)
            print(f"Новая позиция x = {new_x} ; y = {new_y}")

"""
Создайте класс Student с такими полями:

Имя
Возраст
Список оценок

И класс Group:
список Student
название
Эти два класса нам понадобятся на следующем занятии


1)К созданному на прошлом занятии классу студент, 
задаем ему имя, возраст и оценки, через __init__

2)Добавляем метод для добавления оценки
3)Добавляем метод(ы) вычисления среднего балла

4)Прописываем меджик метод (или методы) которые 
позволяют найти студента с наилучшим средним балом из списка

5)Берем класс группы из прошлого занятия
6)Добавляем возможность добавить студента к группе
7)Добавляем возможность удалить студента из группы
8)Добавляем возможность найти группу в которой учится студент 
с самым высоким средним баллом
"""

class Student:

    def __init__(self, name: str, age: int, marks:list[int]) -> None:
        self.marks = marks
        self.name = name
        self.age = age

    def is_possible_to_add_new_mark(self, marks: list) -> bool:
        if len(self.marks) >= 7:
            print("У этого студента слишком много оценок")
            return False
        else:
            print("Добавление оценки разрешено")
            return True

    def _append_marks(self, marks:list, mark:int)->None:
        if self.is_possible_to_add_new_mark(self.marks):
            self.marks.append(mark)
        else:
            raise ValueError("Нельзя добавить оценку")

    def average_mark(self, marks:list) -> float:
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

    def __gt__(self, other: "Student") -> bool:
        return self.average_mark() > other.average_mark()

class Group:

    def __init__(self, name: str, students: list[Student] = None) -> None:
        self.name = name
        self.students = students if students else []

    def add_student(self, student: Student) -> None:
        self.students.append(student)
    def delete_student(self, student: Student)->None:
        self.students.remove(student)
    def best_student(self)-> Student:
        return max(self.students, key=lambda student: student.average_mark())
