b = input("Expression: ")

b = b.split(" ")

x = int(b[0])
y = b[1]
z = int(b[2])

if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z

print(round(float(result), 2))
