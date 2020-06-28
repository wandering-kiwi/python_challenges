n = 1000
q  =
p = 
x = [i for i in range(1, n + 1)]

x[q - 1::3] = ["fizz" for j in range(len(x[2::3]))]
x[4::5] = ["buzz" for k in range(len(x[4::5]))]
x[14::15] = ["fizzbuzz" for l in range(len(x[14::15]))]

for m in x:
    print(m)
#hello, this is a change