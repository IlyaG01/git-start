import time

def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter()
        res = function(*args)
        print(time.perf_counter() - start_time)
        return res
    return wrapped

#@time_of_function
def func(first, second):
    print(first+second)
    return (first+second)

@time_of_function
def func2(name1,name2):
    x = open(name1, 'r')
    a=int(x.readline())
    b = int(x.readline(2))
    c=a+b
    f = open(name2, 'w')  # открытие в режиме записи
    f.write(str(c))
    return c
#func(2, 3)
func2('input','output')
