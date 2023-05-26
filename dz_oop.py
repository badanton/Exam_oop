# Класс Alphabet
# 1. Создайте класс Alphabet
# 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства:
# 1) lang - язык и 2) letters - список букв. Начальные значения свойств берутся из входных параметров метода.
# 3. Создайте метод print(), который выведет в консоль буквы алфавита
# 4. Создайте метод letters_num(), который вернет количество букв в алфавите
#
import string



class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)

# Класс EngAlphabet
# 1. Создайте класс EngAlphabet путем наследования от класса Alphabet
# 2. Создайте метод __init__(), внутри которого будет вызываться родительский метод __init__().
# В качестве параметров ему будут передаваться обозначение языка(например, 'En') и строка,
# состоящая из всех букв алфавита(можно воспользоваться свойством ascii_uppercase из модуля string).
# 3. Добавьте приватное статическое свойство __letters_num, которое будет хранить количество букв в алфавите.
# 4. Создайте метод is_en_letter(), который будет принимать букву в качестве параметра и определять,
# относится ли эта буква к английскому алфавиту.
# 5. Переопределите метод letters_num() - пусть в текущем классе классе он будет возвращать значение
# свойства __letters_num.
# 6. Создайте статический метод example(), который будет возвращать пример текста на английском языке.


class EngAlphabet(Alphabet):
    def __init__(self):
        super().__init__('En', string.ascii_uppercase)
        self.__letters_num = len(string.ascii_uppercase)

    def is_en_letter(self, letter):
        if letter.upper() in self.letters:
            print('Относится')
        else:
            print('Не относится')


    def letters_num(self):
        print(self.__letters_num)

    @staticmethod
    def example():
        print('Пример текста на английском - fatal: not a git repository (or any of the parent directories)')


class RuAlphabet(Alphabet):
    def __init__(self):
        super().__init__('Ru', 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
        self.__letters_num = len('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')

    def is_ru_letter(self, letter):
        if letter.upper() in self.letters:
            print('Относится к русскому алфавиту')
        else:
            print('Не относится к русскому алфавиту')


    def letters_num(self):
        print(self.__letters_num)

    @staticmethod
    def example():
        print('Пример текста на русском :)')


object1 = EngAlphabet()
object1.print()
object1.letters_num()
object1.is_en_letter('F')
object1.is_en_letter('Щ')
EngAlphabet.example()

object2 = RuAlphabet()
object2.print()
object2.letters_num()
object2.is_ru_letter('Д')
object2.is_ru_letter('G')
RuAlphabet.example()