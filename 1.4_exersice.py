#4) write a program to calculate GST tax amount from given bill amount and tax rate

price = int(input("Enter price"))
#tax = price *0.10
gst = int(input("Enter gst rate"))

amount=price+(price*gst/100)
print(amount)