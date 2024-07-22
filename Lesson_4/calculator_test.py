from calculator import Calculator

calculator = Calculator()

# + +
# - -
# - +
# , ,
# n 0

calculator.sum

print("start")
res = calculator.sum(4, 5)
assert res == 9

res = calculator.sum(-4, -5)
assert res == -9

res = calculator.sum(-4, 5)
assert res == 1

res = calculator.sum(10, 0)
assert res == 10

print("finish")

