# a = 100
# sum = 0
# i = 0
# while True:
#     if i == 2000:
#         break
#     sum += a
#     a += 100
#     i += 1
#     print('第{0}天产出的 psersent is {1}'.format(i, sum/100000000))


def fib():
    a, b = 0, 1
    while 1:
        if b > 100000000000:
            break
        yield b
        a, b = b, a+b

for i in fib():
    print(i," ")


print("hello world")