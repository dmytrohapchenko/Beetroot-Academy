def drawing_triangle():
    fill = '*'
    base = 10

    def draw_data():
        for i in range(1, base // 2 + 2):
            print(fill * i)
        for j in range(base // 2, 0, -1):
            print(fill * j)

    return draw_data()


drawing_triangle()
