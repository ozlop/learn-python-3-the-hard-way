def while_fun(a, b):
    numbers = []
    i = 0

    while i < a:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + b
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    return numbers

def print_results(nums):
    print("The numbers: ")
    for num in nums:
        print(num)

print("What would you like the range to be?")
many = int(input("> "))
print("At what increment")
jump = int(input("> "))
print_results(while_fun(many, jump))
