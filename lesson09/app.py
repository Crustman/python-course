

def hello():
    
    print("\nHello Word!!")
    
hello()

def rusty():
    
    print("\nHey, I'm Rusty!!")
    
rusty()




def sum(num1=0, num2=0):
    if (type(num1) is not int or (type(num2) is not int)):
        return 0
    return num1 + num2

total = sum(2, 7)
print(total)

def multriplet_items(*args):
    print(args)
    print(type(args))
    
    

multriplet_items("Dave", "Alice", "Ted")

def mult_name_items(**kargs):
        print(kargs)
        print(type(kargs))
        
mult_name_items(first="Dave", last="Grey")




