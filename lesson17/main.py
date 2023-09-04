
#squared = lambda num : num * num
def squared(num): return num * num


print(squared(2))


def add_two(num): return num + 2
# lambda num : num + 2

print(add_two(12))

def sum_total(a, b): return a + b
#lambda a, b : a + b


print(sum_total(10, 8))

#######################################

def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))


#################################################



numbers = [3,7,12,18,20,21]

squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))

#########################################################



odd_nums = filter(lambda num : num % 2 != 0, numbers)

print(list(odd_nums))


