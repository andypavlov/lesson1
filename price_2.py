def format_price(price):
    try:
        price = int(price)
        total = 'Цена: {} руб.'.format(price)
        return total
    except (TypeError, ValueError):
        return ('Неверный формат введенных данных')

result = format_price("sdfsdf")
print(result)