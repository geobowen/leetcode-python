import os
import math


def sol(x, y):
    n = len(x)
    points = set(zip(x, y))
    max_area = 0

    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = x[i], y[i]
            x2, y2 = x[j], y[j]

            dx = x2-x1
            dy = y2-y1

            # Two possibilities for the other two coners of the square
            x3a, y3a = x2-dy, y2+dx
            x4a, y4a = x1-dy, y1+dx
            x3b, y3b = x2+dy, y2-dx
            x4b, y4b = x1+dy, y1-dx

            # Check bothe potential squares
            for (x3, y3, x4, y4) in [(x3a, y3a, x4a, y4a), (x3b, y3b, x4b, y4b)]:
                if (x3, y3) in points and (x4, y4) in points:
                    side_length = math.sqrt((x1-x2)**2+(y1-y2)**2)
                    area = side_length ** 2
                    perimeter = side_length*4

                    if (area*10 + perimeter*40) <= 2000000:
                        max_area = max(max_area, area)

    return round(max_area)


# print(sol([-4, -4, 0, 0, 0, 4], [0, 4, 4, 0, -4, 0]))


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     x_count = int(input().strip())

#     x = []

#     for _ in range(x_count):
#         x_item = int(input().strip())
#         x.append(x_item)

#     y_count = int(input().strip())

#     y = []

#     for _ in range(y_count):
#         y_item = int(input().strip())
#         y.append(y_item)

#     fptr.write(str(result)+'\n')

#     fptr.close()
