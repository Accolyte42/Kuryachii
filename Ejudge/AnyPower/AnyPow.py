def list_divisers(n):
	# Функция вывода списка всех повторяющихся делителей числа n
    cur_num = 2
    list_div = []
    while True:
        if cur_num == n:
            list_div.append(cur_num)
            break
        elif n % cur_num == 0:
            list_div.append(cur_num)
            n //= cur_num
        else:
            cur_num += 1
    return list_div


def num_power(list_div):
	# Функция вывода делителей со степенями, с которыми они входят в число
    dct = {list_div[0]: 1}
    for i in range(1, len(list_div)):
        if list_div[i] == list_div[i - 1]:
            dct[list_div[i]] += 1
        else:
            dct[list_div[i]] = 1
    return dct


def gcd_fun(x, y):
    # Функция нахождения НОД
    if y == 0:
        return x
    else:
        return gcd_fun(y, x % y)


# N = 1024
N = int(input())

list_div = list_divisers(N)
dct = num_power(list_div)
min_pow = min(dct.values())

if min_pow == 1:
    print('NO')
else:
    for i in dct.values():
        if gcd_fun(min_pow, i) == 1:
            print('NO')
            break
    else:
        print('YES')
