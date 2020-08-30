def range_sum(numbers, start, end):
    r_sum = 0
    for i in numbers:
        if start <= i <= end:
            r_sum += i
    return r_sum


input_numbers = [int(x) for x in input().split()]
a, b = [int(x) for x in input().split()]
print(range_sum(input_numbers, a, b))
