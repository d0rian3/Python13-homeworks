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


def load_tasks():
    tasks = {}
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                parts = line.strip().split(" | ")
                if len(parts) == 5:
                    task_id, title,description, priority, status =parts
                    tasks[task_id] = {
                        "Заголовок": title,
                        "Описание": description,
                        "Приоритет": priority,
                        "Статус": status
                    }
    except FileNotFoundError:
        pass
    return tasks

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task_id, task in tasks.items():
            file.write(
                f"{task_id} | {task['Заголовок']} | {task['Описание']} | {task['Приоритет']} | {task['Статус']}\n")

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
    save_tasks(tasks)
    print(f"Задача номер {task_number} была успешно добавлена")

def view_task(tasks):
    if not tasks:
        print("Данной задачи нет, увы(")
    for task_id, task_info in tasks.items():

        print(f"Задача {task_id}: \n{task_info['Заголовок']}: {task_info['Описание']}, \n Приоритет задачи: {task_info['Приоритет']},\n Статус задачи: {task_info['Статус']}")

def edit_task(tasks):
    view_task(tasks)
    task_to_edit = input("Выберите задачу для редактирования: ")


    if task_to_edit in tasks:
        task_title = input("Введите заголовок задачи: ")
        task_description = input("Введите описание задачи: ")
        task_priority = input("Введите приоритет (1 - низкий, 2 - средний, 3 - высокий): ")
        task_status = input("Введите статус задачи (1 - новая, 2 - в процессе, 3 - завершена): ")

        tasks[task_to_edit] = {
            "Заголовок": task_title,
            "Описание": task_description,
            "Приоритет": PRIORITY.get(task_priority, "low"),
            "Статус": STATUS.get(task_status, "new")
        }
        save_tasks(tasks)
        print("Задача была успешно обновлена!")
    else:
        print("Такой задачи нет(")

def delete_task(tasks):
    view_task(tasks)
    task_to_delete = input("Выберите задачу для удаления: ")

    if task_to_delete in tasks:
        del tasks[task_to_delete]
        save_tasks(tasks)
        print("Задача была успешно удалена!")
    else:
        print("Такой задачи нет( ")

def main(): #! Функция для общения с пользователем и вызовом остальных функций
    tasks = load_tasks()
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
                edit_task(tasks)
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

if __name__ == "__main__":
    main()