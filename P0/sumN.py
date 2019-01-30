def sum(n):
    sum = 0
    for e in range(n+1):
        sum += e
    return sum
number = int(input("Please introduce a number:"))
sum_total = sum(number)
print("The total sum is:", sum_total)
