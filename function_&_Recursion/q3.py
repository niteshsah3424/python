def print_length(lst):
    print("Length of the list:", len(lst))

def print_elements(lst):
    print("Elements:", " ".join(str(x) for x in lst))

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("Factorial of", n, "is", fact)

def usd_to_inr(usd):
    inr = usd * 83.0
    print(f"{usd} USD = {inr} INR")

# Example calls
print_length([1, 2, 3, 4])
print_elements([1, 2, 3, 4])
factorial(5)
usd_to_inr(10)
