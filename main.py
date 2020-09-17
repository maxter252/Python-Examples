import requests

from decorators import timeit

@timeit
def standard_loop():
    for i in range(100):
        print (i, end='')


def main():
    print ("main")