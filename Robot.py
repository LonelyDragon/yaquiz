'''Напишите класс Robot, который инициализируется с начальными координатами – положением Робота на плоскости, обе координаты заключены в пределах от 0 до 100.
Робот может передвигаться на одну клетку вверх (N), вниз (S), вправо (E), влево (W). Выйти за границы плоскости Робот не может.
Метод move() принимает строку – последовательность команд перемещения робота, каждая буква строки соответствует перемещению на единичный интервал в направлении, 
указанном буквой. Метод возвращает кортеж координат – конечное положение Робота после перемещения.

Метод path() вызывается без аргументов и возвращает список кортежей координат точек, по которым перемещался Робот при последнем вызове метода move. 
Если метод не вызывался, возвращает список с одним кортежем – начальным положением Робота.'''


class Robot:
    
    def __init__(self, pos = (0, 0)):
        self.pos = pos
        self.res = list()
        self.res.append(pos)

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, pos):
        if ((0 <= pos[0] <= 100) and (0 <= pos[1] <= 100)):
            self._pos = pos
        else:
            raise ValueError("Value out of range")

    def move(self, direction):
        mas = list(self.pos)
         
        direct = {
            "N": [0, 1],
            "S": [0, -1],
            "E": [1, 0],
            "W": [-1, 0]
        }

        for step in direction:

            mas[0] += direct[step][0]
            mas[1] += direct[step][1]
            if ((0 <= mas[0] <= 100) and (0 <= mas[1] <= 100)):
                self.res.append(tuple(mas))
            else:
                mas[0] -= direct[step][0]
                mas[1] -= direct[step][1]
                continue
        return self.res[-1]
    
    def path(self):
        return ''.join(map(lambda x: str(x), self.res))