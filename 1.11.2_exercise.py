num = int(input("Enter four digit number "))


first = num // 1000
mid1 = (num // 100)%10
mid2 = (num // 10)%10
last = num % 10
words = ['zero','one','two','three','four','five','six','seven','eight','nine']

print(words[first],words[mid1],words[mid2],words[last])
