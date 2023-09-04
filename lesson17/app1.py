



numbers = [3,7,18,20,21]

squared_nums = map(lambda num : num * num, numbers)

print(list(squared_nums))

#################################################



odd_nums = filter(lambda num : num % 2 != 0, numbers)

print(list(odd_nums))

####################################################

from functools import reduce



numbers = [1,2,3,4,5,1]

total = reduce(lambda acc, curr: acc + curr, numbers)

print(total)



