import turtle


def draw_pifagor_tree(t, branch_length, level):
    if level == 0:
        return
    t.forward(branch_length)
    t.left(45)
    draw_pifagor_tree(t, branch_length * 0.6, level - 1)
    t.right(90)
    draw_pifagor_tree(t, branch_length * 0.6, level - 1)
    t.left(45)
    t.backward(branch_length)


def main():
    # Відкриття вікна для малювання
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Фрактал 'Дерево Піфагора'")

    # Створення черепахи
    t = turtle.Turtle()
    t.speed(0)  # Швидкість малювання

    # Позиціонування черепахи
    t.penup()
    t.setpos(0, -200)
    t.pendown()

    # Введення користувачем рівня рекурсії
    level = int(input("Введіть рівень рекурсії (ціле число): "))

    # Малювання дерева Піфагора з вказаним рівнем рекурсії
    draw_pifagor_tree(t, 100, level)

    # Закриття вікна після кліку
    screen.mainloop()


if __name__ == "__main__":
    main()
