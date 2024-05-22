#создание класса воин
class Warrior():
    #создание характеристик воина
    def __init__(self, name, power, endurance, hair_color):
        self.name = name#имя
        self.power = power#сила
        self.endurance = endurance#выносливость
        self.hair_color = hair_color#цвет волос

    #создание метода воина
    def sleep(self):
        print(f'{self.name} лег спать и выносливость увеличилась на 2')
        self.endurance += 2

    #создание метода воина
    def eat(self):
        print(f'{self.name} сел покушать и сила увеличилась на 1')
        self.power += 1

    #создание метода воина
    def hit(self):
        print(f'{self.name} ударил противника')
        self.endurance -= 6

    #создание метода воина
    def walk(self):
        print((f"{self.name} гуляет "))

    def info(self):
        print(f'имя война: {self.name}')
        print(f'сила: {self.power}')
        print(f'выносливость: {self.endurance}')
        print(f'цвет волос: {self.hair_color}')


