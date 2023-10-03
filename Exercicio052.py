n = int(input("Digite um número e descubra esse é primo ou não: "))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print("\033[33m", end="")
        tot += 1
    else:
        print("\033[31m", end="")
    print("{} ".format(c), end="")
print("\n\033[m0 número {} foi divisível {} vezes".format(n, tot))
if tot == 2:
    print("É por isso que ele é PRIMO!!")
else:
    print("É por isso que ele não é PRIMO!!")