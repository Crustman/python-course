# r = Read
# a = Append
# w = Write
# x = Create
import os


f = open("names.txt", "r")
#print(f.read())
#print(f.read(4))

# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f = open("names.txt")
    print(f.read())
except:
    print("The file you want to read doesn't exist")
finally:
    f.close()

# Append

f = open("names.txt" , "a")
f.write("Neil")
f.close()
f = open("namesl.txt", "a")
f.write("Neil")
f.close() 


f = open("context.txt", "w")
#print(f.read())
f.write("I deleted all of the context")

f.close() 

# Write (overwrite)

f = open("name_list.txt", "w")
f.close()

if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()

if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("The file you wish to delete does not exit")











        