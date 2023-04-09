import math

def sum_digits(num):
    sum = 0
    digits = range(math.ceil((math.log10(num))))
    for i in digits:
        sum += num %10
        num = round(num/10)
    return sum

def cranes(sum):
    out = []
    if sum < 4:
        return out
    gcd = math.gcd(2, 4)
    if sum % gcd == 1:
        return out
    if sum % 3 == 1:
        return out
    base = round(sum//3//2)
    out.append([base*4,base,base])
    return out

def is_lucky_ticket(num):
    digits = math.ceil((math.log10(num)))
    head = math.floor(num / math.pow(10, digits/2))
    tail = math.floor(num % math.pow(10, digits/2))
    return sum_digits(head) == sum_digits(tail)

def chocolate(row, column, piece):
    return piece % row == 0 or piece % column == 0

print(sum_digits(1111111))
print(is_lucky_ticket(385916))
print(cranes(24))
print(chocolate(3, 2, 4))

