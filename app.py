# Імпортування необхідних модулів з бібліотеки flask
from flask import Flask, request

# Ініціалізація Flask-додатку
app = Flask(__name__)

# Тіло додатку - функція отримання та повертання значень
@app.route('/', methods=['GET'])
def MultiplicationOfTwo():
    # Блок з запитом чисел та їх добутком
    try:
        first_num = int(request.args.get('first_num'))
        second_num = int(request.args.get('second_num'))
        res = first_num * second_num
        return f"The result of {first_num} * {second_num} is {res}"
    # Except кейс з обробкою некоректних значень
    except (TypeError, ValueError):
        return "Copy this with your numbers to find their multiplication: ?first_num=1&second_num=2"

# Запуск додатку
if __name__ == '__main__':
    app.run(host='0.0.0.0')
