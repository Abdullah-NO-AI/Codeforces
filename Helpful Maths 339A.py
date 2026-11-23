# Helpful Maths 339A 

equation = list(map(int, input().split("+")))
eq_order = sorted(equation)

print(*eq_order, sep = '+')
