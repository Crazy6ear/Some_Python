"""Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:

1-(x + 2)**2 при x≤−2; (-1)*x/2 при −2<x≤2; ((x - 2)**2)+1 при 2<x

Требуется реализовать только функцию, решение не должно осуществлять операций ввода-вывода."""
def f(x):
    answer = None
    if x <= (-2):
        answer = 1 - (x + 2) ** 2
        return answer
    elif 2 < x:
        answer = ((x - 2) ** 2) + 1
        return answer
    else:
        answer = (-1) * x / 2
        return answer