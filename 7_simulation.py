import random


# Функція для проведення симуляції методом Монте-Карло.
def monte_carlo_simulation(num_trials):
    # Ініціалізуємо словник для підрахунку кількості випадків для кожної суми
    results = {i: 0 for i in range(2, 13)}

    # Виконуємо симуляцію
    for _ in range(num_trials):
        # Кидаємо перший кубик
        dice1 = random.randint(1, 6)
        # Кидаємо другий кубик
        dice2 = random.randint(1, 6)
        # Обчислюємо суму
        total = dice1 + dice2

        # Збільшуємо лічильник випадків для поточної суми
        results[total] += 1

    # Обчислюємо ймовірності для кожної суми
    probabilities = {total: results[total] / num_trials * 100 for total in results}

    return results, probabilities


# Функція для виведення ймовірностей сум на екран.
def print_probabilities(probabilities, results, num_trials):
    print("Таблиця ймовірностей сум при киданні двох кубиків 100000 разів:")
    print("Сума")
    for total, probability in probabilities.items():
        print(f"{total}\t{probability:.2f}% ({results[total]}/{num_trials})")


# Виконання симуляції з 100000 кидків
num_trials = 100000
results, probabilities = monte_carlo_simulation(num_trials)

# Виведення результатів
print_probabilities(probabilities, results, num_trials)
