# Day4- Challenge 4 If-else, for/while loops, break/continue
#  Check if a user-entered number is prime


num = int(input("Enter the Number:"))
if num <= 1:
    print("Not Prime Number")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime Number")
    else:
        print("Not Prime Number")