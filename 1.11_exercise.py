num = int(input("Enter three digit number "))


first = num // 100
mid = (num // 10)% 10
last = num % 10
words = ['zero','one','two','three','four','five','six','seven','eight','nine']

print(words[first],words[mid],words[last])
