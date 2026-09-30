start = int(input("enter start: "))
end = int(input("enter end: "))
count=0
print("prime numbers:")

for num in range(start, end+1):

    if num < 2:
        continue
    prime = True

    for i in range(2, num):
        if num%i==0:
            prime = False
            break

    if prime:
        print(num, end=" ")
        count += 1

print("total prime numbers:", count)