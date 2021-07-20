def my_recursive_func(count, depth):
    if count >= depth:
        return count
    count += 1
    return my_recursive_func(count, depth)


print(my_recursive_func(0, 5))
