def greet():
    return "Hello, World!"

def add(a, b):
    return a + b

def greet_user(name="Guest"):
    return f"Hello, {name}!"

def get_stats(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return total, avg

def sum_all(*args):
    return sum(args)

def print_info(**kwargs):
    return ", ".join(f"{key}: {value}" for key, value in kwargs.items())

square = lambda x: x ** 2

print(greet())
print(add(5, 3))
print(greet_user("Alice"))
print(get_stats([1, 2, 3, 4]))
print(sum_all(1, 2, 3, 4, 5))
print(print_info(name="John", age=25))
print(square(6))
