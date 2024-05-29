import random
import statistics

num1 = random.randint(1,100)
num2 = random.randint(1,100)

print("the numbers are", num1, "and", num2)

avg = statistics.mean([num1, num2])
print("the avg is",avg)
