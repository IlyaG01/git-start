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
def print_sum(sum):
    print(sum)
def sum(first,second):
    total=first+second
    return total


@time_of_function
def sum_and_print(first, second):
    total=sum(first,second)
    print_sum(total)
    return(total)

@time_of_function
def read_sum_and_write(file_for_digitals,file_for_sum):
    a,b=read_file(file_for_digitals)
    total=sum(a,b)
    write_file(file_for_sum,total)
    return sum

#sum_and_print(2, 3)
read_sum_and_write('input','output')
