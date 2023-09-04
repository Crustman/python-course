first = "Dave"
last = "Gray"


# Concatenation
fullname = first + " " + last
print(fullname)

fullname += '!'
print(fullname)

# Casting
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)


multiline = '''
Hey how are you?                                                                                                                                               

I was just checking in.             

             All good?
OK

'''
print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'

print(sentence)

# String Methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffie".ljust(16, ".") + "$1".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))


# String index
print(first[1])
print(first[-1])
print(first[1: -1])
print(first[1:])

# Some boolean
print(first.startswith("D"))
print(first.endswith("Z"))
