# Задача 10: «Система учёта склада».
# Учёт материалов с контролем критических остатков и моделированием выдачи.

# 1. Исходные данные склада.
warehouse = {
    "Кирпич": {"quantity": 5000, "price": 12.50, "min_quantity": 1000},
    "Цемент": {"quantity": 120, "price": 450.00, "min_quantity": 50},
    "Песок": {"quantity": 8, "price": 800.00, "min_quantity": 10},
    "Арматура": {"quantity": 30, "price": 48000.00, "min_quantity": 20},
    "Бетон": {"quantity": 45, "price": 4200.00, "min_quantity": 15},
}


def print_warehouse_table(warehouse_data):
    """Вывод таблицы материалов склада и итоговой статистики."""
    print("=" * 75)
    print("СИСТЕМА УЧЁТА СКЛАДА")
    print("=" * 75)
    print(f"{'Материал':<12} | {'Кол-во':<8} | {'Цена':<10} | {'Мин.':<6} | {'Стоимость':<12}")
    print("-" * 75)

    total_cost = 0
    critical_materials = []
    max_cost_material = None
    max_cost = 0

    for name, data in warehouse_data.items():
        quantity = data["quantity"]
        price = data["price"]
        min_qty = data["min_quantity"]
        cost = quantity * price
        total_cost += cost

        # Определяем материал с максимальной стоимостью остатка.
        if cost > max_cost:
            max_cost = cost
            max_cost_material = name

        # Проверяем критический остаток.
        is_critical = quantity < min_qty
        if is_critical:
            critical_materials.append((name, quantity, min_qty))

        # Печатаем строку таблицы.
        critical_flag = "КРИТИЧ! " if is_critical else ""
        print(f"{critical_flag}{name:<12} | {quantity:<8} | {price:<10.2f} | {min_qty:<6} | {cost:<12.2f}")

    print("-" * 75)
    print(f"{'ОБЩАЯ СТОИМОСТЬ:':<40} {total_cost:<12.2f} руб.")
    print(f"Самый дорогой: {max_cost_material} ({max_cost:.2f} руб.)")

    # Печатаем список критических остатков.
    print(f"КРИТИЧЕСКИЕ ОСТАТКИ ({len(critical_materials)}):")
    for name, qty, min_qty in critical_materials:
        print(f"  - {name}: {qty} < {min_qty}")

    print("=" * 75)
    return total_cost


def issue_material(warehouse_data, material_name, amount):
    """Выдача материала со склада с валидацией входных данных."""
    if material_name not in warehouse_data:
        print(f"Ошибка: Материал '{material_name}' не найден!")
        return False

    if amount <= 0:
        print("Ошибка: Количество должно быть положительным!")
        return False

    current_qty = warehouse_data[material_name]["quantity"]
    if amount > current_qty:
        print(f"Ошибка: Недостаточно '{material_name}' на складе!")
        return False

    warehouse_data[material_name]["quantity"] = current_qty - amount
    print(f"√ Выдано {amount} единиц '{material_name}'")
    print(f"  Остаток: {current_qty} → {warehouse_data[material_name]['quantity']}")
    return True


# 2. Основная программа.
if __name__ == "__main__":
    # Печатаем стартовое состояние склада.
    print_warehouse_table(warehouse)

    # Моделируем выдачу материалов.
    print("\n" + "=" * 75)
    print("ВЫДАЧА МАТЕРИАЛА")
    print("=" * 75)
    issue_material(warehouse, "Цемент", 25)

    print()
    issue_material(warehouse, "Песок", 5)

    # Печатаем финальное состояние склада.
    print("\n" + "=" * 75)
    print("ФИНАЛЬНОЕ СОСТОЯНИЕ СКЛАДА")
    print_warehouse_table(warehouse)
