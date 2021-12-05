# COMMA CODE

#user input
spam_list = []
print("Please enter items in list:")
item = input()
while(item != ""):
    spam_list.append(item)
    item = input()

def comma(list):
    display = ""
    for i in range(len(list)-1):
        display += str(list[i]) + ", "
    display += list[-1]
    return display

print(comma(spam_list))# Write your code here :-)
