n=int(input("Enter number: "))

temp=n
sum_digits= 0
count=0
largest =0
smallest= 9
reverse=0

while n>0:
    digit=n%10
    sum_digits+=digit
    count+=1

    if digit > largest:
        largest = digit

    if digit < smallest:
        smallest = digit
    reverse = reverse * 10 + digit

    n=n//10

if temp == reverse:
    palindrome = "Yes"
else:
    palindrome = "No"

print("Sum of digits:", sum_digits)
print("Number of digits:", count)
print("Largest digit:", largest)
print("Smallest digit:", smallest)
print("Palindrome:", palindrome)