# COLLATZ SEQUENCE
def collatz(number):
    number = int(number)
    if number % 2 == 0:
        return number //2
    else:
        return number * 3 +1

print("Enter your number: ")
num = input()
while(num != 1):
    num = collatz(num)
    print(num)

