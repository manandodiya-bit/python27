#3) write a program to findout simple interest of given amount rate and year 

price =int(input("Enter price"))
rate =int(input("Enter rate"))
year = int(input("Enter year"))


simple = price*rate*year/100 

print(simple)