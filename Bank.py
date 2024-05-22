# class Account:
#     def __init__(self,id , name, balance=0):
#         self.id = id
#         self.name = name
#         self.balance = balance
#
#     def deposit(self, money):
#         if money >= 0:
#             self.balance += money
#             print(f'Счет успешно пополнен, ваш баланс: {self.balance}')
#         else:
#             print('Некорректное значение')
#
#     def withdraw(self, money):
#         if money <= self.balance:
#             self.balance -= money
#             print(f'Вы успешно сняли {money} рублей, ваш баланс: {self.balance}')
#         else:
#             print('Некорректное значение')
#
#     def get_balance(self):
#         print(f'Текущий баланс счёта: {self.balance}')
#
# My = Account(1, 'Max')
# My.deposit(100)
# My.withdraw(50)
# My.deposit(1000)
# My.get_balance()
#
#
#
# #создание класса воин
# class Warrior():
#     #создание характеристик воина
#     def __init__(self, name, power, endurance, hair_color):
#         self.name = name#имя
#         self.power = power#сила
#         self.endurance = endurance#выносливость
#         self.hair_color = hair_color#цвет волос
#
#     #создание метода воина
#     def sleep(self):
#         print(f'{self.name} лег спать и выносливость увеличилась на 2')
#         self.endurance += 2
#
#     #создание метода воина
#     def eat(self):
#         print(f'{self.name} сел покушать и сила увеличилась на 1')
#         self.power += 1
#
#     #создание метода воина
#     def hit(self):
#         print(f'{self.name} получил урон от противника')
#         self.endurance -= 6
#
#     #создание метода воина
#     def walk(self):
#         print((f"{self.name} гуляет "))
#
#     def info(self):
#         print(f'имя война: {self.name}')
#         print(f'сила: {self.power}')
#         print(f'выносливость: {self.endurance}')
#         print(f'цвет волос: {self.hair_color}')
#
# war1 = Warrior('Харик', 55, 100, 'коричневый')
#
# war1.sleep()
# war1.eat()
# war1.hit()
# war1.walk()
# war1.info()

