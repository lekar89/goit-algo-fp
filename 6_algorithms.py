# Жадібний алгоритм для вибору страв з найбільшою калорійністю за обмежений бюджет.
def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )
    chosen_items = []
    total_cost = 0

    for item, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            chosen_items.append(item)
            total_cost += info["cost"]

    return chosen_items


# Алгоритм динамічного програмування для вибору страв з найбільшою калорійністю за обмежений бюджет.
def dynamic_programming(items, budget):
    dp = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]
    selected_items = [[] for _ in range(len(items) + 1)]

    for i, (item, info) in enumerate(items.items(), start=1):
        for j in range(1, budget + 1):
            if info["cost"] <= j:
                if info["calories"] + dp[i - 1][j - info["cost"]] > dp[i - 1][j]:
                    dp[i][j] = info["calories"] + dp[i - 1][j - info["cost"]]
                    selected_items[i] = selected_items[i - 1] + [item]
                else:
                    dp[i][j] = dp[i - 1][j]
                    selected_items[i] = selected_items[i - 1]
            else:
                dp[i][j] = dp[i - 1][j]
                selected_items[i] = selected_items[i - 1]

    return selected_items[-1]


# Задання даних про страви
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}

budget = 100  # Обмежений бюджет

# Виклик функцій та вивід результатів
print("Жадібний алгоритм:")
print(greedy_algorithm(items, budget))

print("\nАлгоритм динамічного програмування:")
print(dynamic_programming(items, budget))
