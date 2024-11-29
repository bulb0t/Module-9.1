def apply_all_func(int_list, *functions):
    try:
        results = {}
        for fun in functions:
            results[fun.__name__] = fun(int_list)
        return results
    except TypeError as exc:
        return f'В вашем списке содержится некорректный тип данных, из-за этого возникает ошибка: {exc}'

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))