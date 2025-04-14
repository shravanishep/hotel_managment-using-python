# define menu of restrorent

our_menu={
    'coffee':30,
    'juice':40,
    'pizza':89,
    'pasta':45,
    'special ice-cream':30
}

print("welcome to our happy happy restaurant\n this is our menu\n enjoy!!!")
print("coffee:Rs 30\njuice:Rs 40\npizza:Rs 89\n pasta:Rs 45\nspecial ice-cream:Rs 30\n")

 
total_order=0
item1=input("please let us know what you want from our menu :")


if item1 in our_menu:
    total_order+=our_menu[item1]
    print(f"your item {item1} is added in your order")
else:
    print("sorry dish is not avaialable")


item2=input("do you want any thing else?(yes/no)")
if item2=="yes":
 second_order=input("enter the name of second item : ")
 if second_order in our_menu:
    total_order+=our_menu[second_order]
    print(f"your item {second_order} is added in your order")
else:
    print("sorry ,dish is not available")

print(f"the total amount you have to pay is {total_order}")

print("enjoy your meal")