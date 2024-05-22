# Задача: Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты: описание задачи,
# срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач,
# отметки выполненных задач и вывода списка текущих (не выполненных) задач.
class Task:
    def (self, description, deadline, status):
        self.description = description
        self.deadline = deadline
        self.status = status

    def add_task(self):
        print(f"Новая задача: {self.description}, срок выполнения: {self.deadline}, статус: {self.status}")

    def mark_as_done(self):
        self.status = "выполнено"
        print(f"Задача: {self.description}, срок выполнения: {self.deadline}, статус: {self.status}")

    def show_uncompleted_tasks(self):
        if self.status == "не выполнено":
            print(f"Задача: {self.description}, срок выполнения: {self.deadline}, статус: {self.status}")

my_business = Task("Закончить работу", "до 22.05.2024", "не выполнено")
my_business.add_task()
my_business.mark_as_done()
my_business.show_uncompleted_tasks()
