from queue import Queue
import random

queue = Queue()
num_request = 0

request_descriptions = [
    "Ремонт ноутбука",
    "Заміна акумулятора",
    "Налаштування принтера",
    "Відновлення доступу до облікового запису",
    "Встановлення програми",
    "Діагностика комп’ютера",
]

def generate_request():
    global num_request
    num_request += 1
    description = random.choice(request_descriptions)
    request = {'id':num_request,'description':description}
    print(f"Створено заявку №{num_request}: {description}")
    queue.put(request)

def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Оброблюю заявку №{request['id']}: {request['description']}")
    else:
        print("Заявки відсутні.")

while True:
    command = input(
        "\nНатисніть Enter для створення заявки або q для виходу: "
    )

    if command.lower() == "q":
        print("Програму завершено.")
        break

    generate_request()
    process_request()