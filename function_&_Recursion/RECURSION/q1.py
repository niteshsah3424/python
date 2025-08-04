def countdown(n):
    if n == 0:
        print("Time's up!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)
