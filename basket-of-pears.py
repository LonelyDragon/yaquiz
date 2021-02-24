'''
Итак, у вас есть корзина с грушами и несколько детей. Нужно поделить груши так, чтобы никому из детей не было обидно, то есть поровну. 
(Теперь понятно, почему в задаче дети?)
Напишите класс PearsBasket, экземпляр которого при инициализации получает целое число – количество груш в корзине.
В классе должны быть методы:

pb // n – деление нацело, возвращает список объектов класса со значениями количества груш в каждой корзинке, если есть остаток – он должен находиться в 
дополнительной последней корзинке.
pb % n – получение остатка от деления, возвращает число: остаток от деления.
pb_1 + pb_2 – складываются две корзинки, получается новая корзина;
pb_1 - n – число вычитается из корзинки, если там есть такое количество груш; если нет – вычитается сколько есть, остается 0;
 __str__ – возвращает количество груш в корзине;
 __repr__ – возвращает строку в формате PearsBasket(<количество>).

from solution import PearsBasket

pb = PearsBasket(17)
array = pb // 4
print(array)
pb_2 = PearsBasket(13)
pb_3 = pb + pb_2
print(pb_3)
print(pb_3 % 7)
pb - 2
print([pb])


[PearsBasket(4), PearsBasket(4), PearsBasket(4), PearsBasket(4), PearsBasket(1)]
30
2
[PearsBasket(15)]

'''


class PearsBasket:
    
    def __init__(self, count) -> None:
        self.count = int(count)

    def __str__(self) -> str:
        return str(self.count)

    def __repr__(self) -> str:
        return self.__class__.__name__ + f'({self.count})'
    
    # % 
    def __mod__(self, other) -> int:
        return self.count % other.count
    
    # //
    def __floordiv__(self, other):
        return [self, other, PearsBasket(self.count // other.count)]

    # +
    def __add__(self, other) -> object:
        return PearsBasket(self.count + other.count)
    
    # -
    def __sub__(self, other) -> object:
        return PearsBasket(self.count + other.count)

    