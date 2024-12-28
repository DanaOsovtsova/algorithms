def area(left, top, right, bottom):
    return (right - left) * (top - bottom)

def main():
    with open("input.txt", "r") as infile:
        n, w, h = map(int, infile.readline().strip().split())

        x_tree = []
        y_tree = []
        y_coordinate = set()

        for _ in range(n):
            x, y = map(int, infile.readline().strip().split())
            x_tree.append(x)
            y_tree.append(y)

            if y not in y_coordinate:
                y_coordinate.add(y)
                x_tree.append(0)
                y_tree.append(y)
                x_tree.append(w)
                y_tree.append(y)

        size = len(x_tree)
        top_xy = [h] * size
        bottom_xy = [0] * size
        same_y = [False] * size

        # Сортировка по x-координатам
        points = list(zip(x_tree, y_tree))
        points.sort()
        x_tree, y_tree = zip(*points)

        max_area = 0

        if n == 0:
            max_area = h * w
        else:
            for i in range((size - n) // 2, size):
                max_area = max(max_area, area(x_tree[i - 1], top_xy[i], x_tree[i], bottom_xy[i]))
                for j in range(i):
                    y_i = y_tree[i]
                    y_j = y_tree[j]

                    if y_i > y_j and y_i <= top_xy[j]:
                        if same_y[j]:
                            max_area = max(max_area, area(x_tree[j], top_xy[j], x_tree[i], y_j))
                        else:
                            max_area = max(max_area, area(x_tree[j], top_xy[j], x_tree[i], bottom_xy[j]))
                        top_xy[j] = y_i
                    elif y_i < y_j and y_i >= bottom_xy[j]:
                        if same_y[j]:
                            max_area = max(max_area, area(x_tree[j], y_j, x_tree[i], bottom_xy[j]))
                        else:
                            max_area = max(max_area, area(x_tree[j], top_xy[j], x_tree[i], bottom_xy[j]))
                        bottom_xy[j] = y_i
                    elif y_i == y_j:
                        if same_y[j]:
                            max_area = max(max_area, area(x_tree[j], y_i, x_tree[i], bottom_xy[j]))
                            max_area = max(max_area, area(x_tree[j], top_xy[j], x_tree[i], y_i))
                        else:
                            max_area = max(max_area, area(x_tree[j], top_xy[j], x_tree[i], bottom_xy[j]))
                        same_y[j] = True

    with open("output.txt", "w") as outfile:
        outfile.write(str(max_area))

if __name__ == "__main__":
    main()
