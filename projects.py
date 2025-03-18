LOW = "1"
MEDIUM = "2"
HIGH = "3"
PRIORITY = {
    LOW: "low",
    MEDIUM: "medium",
    HIGH: "high"
}

NEW = "1"
IN_PROGRESS = "2"
DONE = "3"
STATUS = {
    NEW: "new",
    IN_PROGRESS: "in progress",
    DONE: "done"
}
"""
    Создание константных переменных для
    использования в дальнейшем
"""



def main(): #! Функция для общения с пользователем и вызовом остальных функций
    tasks = {}
    while True:
        first_choice = input("Выберите действие:\n- 1 - Создать новую задачу\n- 2 - Просмотреть задачи\n- 3 - Обновить задачу\n- 4 - Удалить задачу\n- 0 - Выйти из программы\n")
        match first_choice:
            case "1":
                print("Вы выбрали функцию создания новой задачи, сделайте следующие действия.")
                task_assembly(tasks)
            case "2":
                print("Вы выбрали функцию просмотра всех задач:")
                view_task(tasks)
            case "3":
                print("Вы выбрали функцию обновления задачи. Доступные задачи:\n")
                update_task(tasks)
            case "4":
                print("Вы выбрали функцию удаления задачи. Доступные задачи:\n")
                delete_task(tasks)
            case "0":
                print("Выход из программы...")
                break
            case _:
                print("Ошибка: Некорректный ввод. Попробуйте снова.")

"""
    Цикл дающий пользователю возможность
    выбора действий, при вводе некорректного
    значения цикл повторяется

"""

def task_assembly(tasks):
    task_number = len(tasks) + 1
    task_title = input("Введите заголовок задачи: ")
    task_description = input("Введите описание задачи: ")
    task_priority = input("Введите приоритет (1 - низкий, 2 - средний, 3 - высокий): ")
    task_status = input("Введите статус задачи (1 - новая, 2 - в процессе, 3 - завершена): ")

    tasks[task_number] = {
        "Заголовок": task_title,
        "Описание": task_description,
        "Приоритет": PRIORITY.get(task_priority, "low"),
        "Статус": STATUS.get(task_status, "new")
    }

    print(f"Задача номер ${task_number} была успешно добавлена")

def view_task(tasks):
    if not tasks:
        print("Данной задачи нет, увы(")
    for task_id, task_info in tasks.items():
        print(f"Задача {task_id}: \n{task_info['Заголовок']}: {task_info['Описание']}, \n Приоритет задачи: {task_info['Приоритет']},\n Статус задачи: {task_info['Статус']}")

def update_task(tasks):
    print("TIME")
def delete_task(tasks):
    print("tme")
if __name__ == "__main__":
    main()



