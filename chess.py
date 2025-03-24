
"""
Фигура должна содержать такие атрибуты:
Цвет (белый или черный).
Место на доске (тут есть варианты, или два отдельных поля, для описания
координат или одно, но, например, кортеж из двух чисел). И такие методы как:
Изменить цвет (ничего не принимает, только меняет цвет на противоположный).
Изменить место на доске (принимает или две переменные, или один кортеж из двух элементов),
не забудьте проверить, что мы не пытаемся поставить фигуру за пределы доски
(оба значения от 0 до 7).
Абстрактный метод проверки потенциального хода (детали ниже).
На данном этапе фигуры могут стоять на одной и той же клетке, пока нам это не важно.
Опишите классы для пешки, коня, офицера, ладьи, ферзя и короля.
Все, что в них нужно добавить - это один метод для проверки,
возможно, ли за один ход поменять место фигуры на доске
(все ходят по-разному, у пешек будет еще и разница от цвета).
Метод принимает опять же или две цифры, или один кортеж.
И опять же проверяем, не выходит ли значение за пределы доски
(Так как нам необходим этом функционал дважды,
я бы делал его как отдельный защищенный метод в родительском классе)
И функцию, которая принимает список фигур и потенциальную новую клетку,
а возвращает список из фигур. Но только тех, которые могут
за один ход добраться до этой клетки.
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

