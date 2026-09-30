n = int(input("Enter number: "))

temp = n
sum_digits = 0
count = 0
reverse = 0

digit = int(n % 10)
largest = digit
smallest = digit

while n > 0:
    digit = n % 10

    sum_digits += digit
    count += 1

    if digit > largest:
        largest = digit

    if digit <smallest:
        smallest= digit

    reverse = reverse * 10 + digit

    n = n // 10

if temp == reverse:
    palindrome="Yes"
else:
    palindrome="No"

print("Sm of digits:", sum_digits)
print("Number of digits:", count)
print("Largest digit:", largest)
print("Smallest digit:", smallest)
print("Palindrome:", palindrome)