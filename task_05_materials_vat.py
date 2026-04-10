# Задача 5: «Калькулятор скидки».
# Расчёт стоимости покупки материалов с прогрессивной системой скидок.

# 1. Ввод исходных данных.
price = float(input("Введите цену товара (руб): "))
quantity = int(input("Введите количество товара: "))

# 2. Расчёт начальной стоимости.
initial_cost = price * quantity

# 3. Определение размера скидки по прогрессивной шкале.
if initial_cost < 1000:
    discount_rate = 0
    discount_name = "0%"
elif initial_cost <= 5000:
    discount_rate = 5
    discount_name = "5%"
else:
    discount_rate = 10
    discount_name = "10%"

# 4. Расчёт суммы скидки и итоговой стоимости.
discount_amount = initial_cost * discount_rate / 100
final_cost = initial_cost - discount_amount

# 5. Вывод всех этапов расчёта в читаемом виде.
print("=" * 50)
print("КАЛЬКУЛЯТОР СКИДКИ")
print("=" * 50)
print(f"Цена товара: {price:.2f} руб.")
print(f"Количество: {quantity} шт.")
print("-" * 50)
print(f"Начальная стоимость: {initial_cost:.2f} руб.")
print(f"Применена скидка: {discount_name}")
print(f"Сумма скидки: {discount_amount:.2f} руб.")
print("-" * 50)
print(f"ИТОГО К ОПЛАТЕ: {final_cost:.2f} руб.")
print("=" * 50)
