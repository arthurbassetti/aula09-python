from timer import time_measure_decorator


@time_measure_decorator
def soma (x,y):

    return x+y

soma(2,3)