lst = [10, 501, 22, 37, 100, 999, 87, 351]
even_numbers = [num for num in lst if num % 2 == 0]
odd_numbers = [num for num in lst if num % 2 != 0]

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
###########

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

lst = [10, 501, 22, 37, 100, 999, 87, 351]
prime_numbers = [num for num in lst if is_prime(num)]

print("Prime numbers:", prime_numbers)
print("Total prime numbers:", len(prime_numbers))
###########
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d)**2 for d in str(n))
    return n == 1

lst = [10, 501, 22, 37, 100, 999, 87, 351]
happy_numbers = [num for num in lst if is_happy(num)]

print("Happy numbers:", happy_numbers)
print("Total happy numbers:", len(happy_numbers))
#########

def sum_first_last(n):
    n_str = str(n)
    return int(n_str[0]) + int(n_str[-1])


num = 12345
print("Sum of first and last digit:", sum_first_last(num))
#####

total = 10
ways = 0

for i in range(total + 1):
    for j in range((total // 2) + 1):
        for k in range((total // 5) + 1):
            if i * 1 + j * 2 + k * 5 == total:
                print(f"1x{i}, 2x{j}, 5x{k}")
                ways += 1

print("Total ways:", ways)
####

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]


duplicates = set(list1) & set(list2) & set(list3)

print("Duplicates in all three lists:", list(duplicates))
######

def first_non_repeating(lst):
    for num in lst:
        if lst.count(num) == 1:
            return num
    return None

numbers = [4, 5, 1, 2, 0, 4, 5, 2]
result = first_non_repeating(numbers)
print("First non-repeating element:", result)

##########

sorted_list = [10, 20, 30, 40, 50]

minimum = sorted_list[0]

print("Minimum element:", minimum)