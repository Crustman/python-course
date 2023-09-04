

name = "Rusty"
count = 2

print(name)


def another():
    color = "blue"
    global count
    count *= 10
    print(count)
    print(name)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("Dave")


another()
