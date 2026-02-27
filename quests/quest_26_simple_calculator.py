def add(a, b): return a + b
def subtract(a, b): return a - b

num1 = int(input("First number: "))
num2 = int(input("Second number: "))
op = input("Choose (add/subtract): ")

if op == "add":
    print(f"Result: {add(num1, num2)}")
elif op == "subtract":
    print(f"Result: {subtract(num1, num2)}")
