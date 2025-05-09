def is_leap_year(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

def compute_day_of_week(y, m, d):
    if m < 3:
        m += 12
        y -= 1
    k = y % 100
    j = y // 100
    return (d + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j) % 7

def count_sundays_on_first(y1, m1, d1, y2, m2, d2):
    y, m = y1, m1
    count = 0
    while (y < y2) or (y == y2 and m <= m2):
        if (
            (y > y1 or (y == y1 and m > m1)) or
            (y == y1 and m == m1 and 1 >= d1)
        ) and (
            (y < y2 or (y == y2 and m < m2)) or
            (y == y2 and m == m2 and 1 <= d2)
        ):
            if compute_day_of_week(y, m, 1) == 1:
                count += 1
        if m == 12:
            m = 1
            y += 1
        else:
            m += 1
    return count

t = int(input())
for _ in range(t):
    y1, m1, d1 = map(int, input().split())
    y2, m2, d2 = map(int, input().split())
    print(count_sundays_on_first(y1, m1, d1, y2, m2, d2))