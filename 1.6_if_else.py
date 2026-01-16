#6) write a program to findout which is cheaper approach to buy IPhone 17 pro max.
#consider use is going usa should he buy iphone from usa or from india. 

print("Enter Iphone 17 pro max price ")
price_ind = int(input("Enter price in Indian Rupees "))

price_usa = int(input("Enter price in Usa Us Dollar "))

us_price = price_usa * 90

if price_ind < price_usa:
    print(f"Buying an Iphone in India is the cheaper then Usa Diffrence is ",us_price-price_ind)
else:
    print(f"Buying an Iphone in use is cheaper then  in India Diffrence is ",price_ind-us_price)
