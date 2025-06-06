# swap two variables values

def swap(item1:int, item2:int):
    # taking temp for the temapary to save number for the item1
    temp = item1
    # here is swaping the number1 will be replaced by numner2
    item1 = item2
    # item2 will taking the number from tempory 
    item2 = temp
    # here catching both item to swap together
    return item1, item2
    
number1 = 10

number2 = 20

print(f"Before swap: values of number1 = {number1} and number2 = {number2}")

number1, number2 = swap(number1, number2)

print(f"after swaping: value of number1 = {number1} and number2 = {number2}")

