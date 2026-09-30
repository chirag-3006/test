n = int(input("enter number: "))

temp=n
sum_digits=0
count=0
reverse=0

digit=int(n% 10)
largest=digit
smallest=digit

while n>0:
    digit=n% 10

    sum_digits+= digit
    count += 1

    if digit >largest:
        largest = digit

    if digit <smallest:
        smallest= digit

    reverse=reverse*10+digit 

    n=n//10

if temp == reverse:
    palindrome="yes"
else:
    palindrome="no"

print("sm of digits:", sum_digits)
print("number of digits:", count)
print("largest digit:", largest)
print("smallest digit:", smallest)
print("paldrome:", palindrome)