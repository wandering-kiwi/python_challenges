n = 1000
q  = 3
p = 5
x = [i for i in range(1, n + 1)]

x[(q - 1)::q] = ["fizz" for j in range(len(x[2::3]))]
x[(p - 1)::p] = ["buzz" for k in range(len(x[4::5]))]
x[(q * p - 1)::(q * p)] = ["fizzbuzz" for l in range(len(x[14::15]))]

for m in x:
    print(m)
