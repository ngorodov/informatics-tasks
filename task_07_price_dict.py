# Задача 7: «Прайс-лист материалов».
# Работа со словарём: добавление, изменение, удаление и статистика.

# 1. Создаём словарь с 5 материалами и ценами (в рублях).
prices = {
    "Кирпич": 15.50,
    "Цемент": 450.00,
    "Песок": 800.00,
    "Доска": 1200.00,
    "Гвозди": 85.00,
}

# 2. Выводим исходный прайс-лист.
print("=" * 50)
print("ПРАЙС-ЛИСТ МАТЕРИАЛОВ")
print("=" * 50)
print("Исходный прайс-лист:")
for material, price in prices.items():
    print(f"  {material}: {price:.2f} руб.")

# 3. Добавляем 2 новых материала.
prices["Щебень"] = 950.00
prices["Рубероид"] = 1400.00
print("-" * 50)
print("После добавления:")
for material, price in prices.items():
    print(f"  {material}: {price:.2f} руб.")

# 4. Изменяем цену одного материала (+10%).
old_price = prices["Цемент"]
prices["Цемент"] = old_price * 1.10
print("-" * 50)
print(f"Изменение цены Цемента: {old_price:.2f} -> {prices['Цемент']:.2f} руб. (+10%)")

# 5. Удаляем один материал из словаря.
removed = prices.pop("Гвозди")
print(f"Удалён материал: Гвозди (был {removed:.2f} руб.)")

# 6. Рассчитываем среднюю цену и выводим итоговую статистику.
average_price = sum(prices.values()) / len(prices)
print("-" * 50)
print("ИТОГОВЫЙ ПРАЙС-ЛИСТ:")
for material, price in prices.items():
    print(f"  {material}: {price:.2f} руб.")
print("-" * 50)
print(f"Количество материалов: {len(prices)}")
print(f"Средняя цена: {average_price:.2f} руб.")
print("=" * 50)
