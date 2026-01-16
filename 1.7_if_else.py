#7) write a program to decide which is cheaper approach to go from ahmedabad to delhi. 
#by car or by train. 
# consider person has his own petrol car  and he prefer to travel by 1st class train .

print("Enter Information which is cheaper approach to go from ahmedabad to delhi. ")
# distance between Ahmedabad to Delhi 986 kilometers.

car = int (input("Enter cost to travel between ahmedabad to delhi "))

train = int (input("Enter train ticket price "))

if(train < car):
    print("Train traveling is cheaper than car traveling")
else:
    print("car traveling is cheaper than train traveling ")