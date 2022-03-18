import time

def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter()
        res = function(*args)
        print(time.perf_counter() - start_time)
        return res
    return wrapped

def read_file(name):
    x = open(name, 'r')
    a = int(x.readline())
    b = int(x.readline(2))
    return a,b

def write_file(name,data):
    f = open(name, 'w')  # открытие в режиме записи
    f.write(str(data))

@time_of_function
def summa_and_print(first, second):
    summa=first+second
    print(summa)
    return(summa)
@time_of_function
def read_summa_and_write(file_for_digitals,file_for_summa):
    a,b=read_file(file_for_digitals)
    summa=a+b
    write_file(file_for_summa,summa)
    return summa

summa_and_print(2, 3)
#read_summa_and_write('input','output')
