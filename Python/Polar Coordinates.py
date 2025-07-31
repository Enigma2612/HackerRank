from cmath import phase
num = complex(input())

r = (num.real**2 + num.imag**2)**0.5
phi = phase(num)

print(r)
print(phi)

