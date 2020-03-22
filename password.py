import random
n="abcdefghijklmnopqrstuvwxyz1234567890ABCEFGHIJKLMNOPQRSTUVWXVZ!@#$%^&*()_+=-"
passlen=8
p="".join(random.sample(n,passlen))
print(p)