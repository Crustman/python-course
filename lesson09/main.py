print("\n\n\n")


def hello():
    print("Hello World!\n")


hello()


def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2


total = sum(7, 2)
print(total)


def multiplet_items(*args):
    print(args)
    print(type(args))


multiplet_items("Dave", "John", "Sara")


def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


mult_named_items(first="Dave", last="Gray")


print("\n\n\n\n")
