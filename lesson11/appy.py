print("\n")

name = "Dave"
count = 1


def another():
    color = "blue"
    global count
    count += 3
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("Dave")


another()


print("\n")
