
class Animal:
    def __init__(self, name):
           self.name = name         
    def eat(self):
            print("Eating...")
    def bark(self):
             print("Barking..")


animal1 = Animal("dog")
animal1.eat()
animal1.bark()

class Dog(Animal):
       def sound(self):
              print("Barking..")

class Cat(Animal):
       def sound(self):
              print("Meow...")


dog1 = Dog("Bear")
dog1.eat()
dog1.sound()

cat1 = Cat("cat")
cat1.eat()
cat1.sound()















 







# def add(x, y):
#     return x + y

# sum = add(4, 5)
# print(sum)
    

