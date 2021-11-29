import random
import time


base = ['i', 'a', 'm', 'h', 'a', 'n', 'd', 's', 'o', 'm', 'e']
mail = []

for i in range(0, 5):
    n = random.randint(1, 10)
    mail.append(base[n])

mail.append(str(time.time_ns())[-6:-1])
mail.append("@test.com")

print("".join(mail))
