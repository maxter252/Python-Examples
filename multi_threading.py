from threading import Thread


def square_numbers():
    pass


def get_product(array, i):
    for i, item in enumerate(array):
        print(f"{i},{item}")


# get_product([5,1,4,2],1)


def mergeOverlappingIntervals(intervals):
    # Write your code here.
    intervals.sort(key=lambda x: x[0])
    print(intervals)
    return [[]]


mergeOverlappingIntervals([[4, 5], [1, 7]])
