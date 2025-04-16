def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        n=fibo(n-1)+fibo(n-2)
        return n
while True:
    try:
        n=int(input("Enter the number to finonaaci sequence of:"))
        if n<0:
            print("Fibonacci sequence is calculated only of \"POSITIVE NUMBERS\"!")
        elif n<=25:
            print(f"The fibonacci sequence of {n} is:",fibo(n))
        else:
            print("Fibonacci sequence of numbers greater than 25 can be calculated but doing so this might take time!")
        b=input("Would you like to continue? yes/no:").lower()
        if b=="yes":
            continue
        elif b=="no":
            break
        else:
            print("Enter valid input yes or no!")
            break
    except ValueError:
        print("Only POSITIVE INTEGERS are ACCEPTED")
