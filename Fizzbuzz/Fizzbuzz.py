x = [i for i in range(1, 101)]

x[2::3] = ["fizz" for j in range(len(x[2::3]))]
x[4::5] = ["buzz" for k in range(len(x[4::5]))]
x[14::15] = ["fizzbuzz" for l in range(len(x[14::15]))]

for m in x:
    print(m)