# Домашнее задание по уроку "Пространство имен"


#from name_spaces import d
#d = 15


def test_function(x):
    d = x ** 2 / 3
    pass

    def inner_function(x):
        if d == int(x) or d == float(x):
            print("Я в области видимости функции test_function")

    inner_function(d)
    return d


res = test_function(6)

print(res)
