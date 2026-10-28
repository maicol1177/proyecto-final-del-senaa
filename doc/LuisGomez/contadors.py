prin = input("digite un texto ")
dicc = {}
for a in prin:
    dicc [a] = dicc.get(a,0) + 1
print(dicc)