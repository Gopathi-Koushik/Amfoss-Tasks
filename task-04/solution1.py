from collections import Counter

def find_missing_numbers(n, list_a, m, list_b):
    count_a = Counter(list_a)
    missing_numbers = set()
    
    for number in list_b:
        if count_a[number] <= 0:
            missing_numbers.add(number)
        else:
            count_a[number] -= 1  
    return sorted(missing_numbers)

n = int(raw_input())  # size of list A
list_a = map(int, raw_input().split())  # the elements of list A
m = int(raw_input())  # size of list B
list_b = map(int, raw_input().split())  # the elements of list B

missing_numbers = find_missing_numbers(n, list_a, m, list_b)

print " ".join(map(str, missing_numbers))
