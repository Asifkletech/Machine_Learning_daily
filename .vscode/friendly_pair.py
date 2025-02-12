def sum_of_divisors(n):
    total = 0
    for i in range(1, n // 2 + 1):  # Check up to n/2 (excluding n itself)
        if n % i == 0:
            total += i
    return total

def are_friendly_pair(a, b):
    sum_a = sum_of_divisors(a)
    sum_b = sum_of_divisors(b)
    
    return (sum_a / a) == (sum_b / b)  # Check if both have the same divisor sum ratio

# Example usage
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if are_friendly_pair(num1, num2):
    print(f"{num1} and {num2} are a friendly pair.")
else:
    print(f"{num1} and {num2} are not a friendly pair.")
