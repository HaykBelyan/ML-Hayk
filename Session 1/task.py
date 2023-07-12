import matplotlib.pyplot as plt
import random

date = []
summ = 0
summm = 0
for i in range(1, 13):
	date.append(i)
step_count = [5023, 6201, 7542, 4908, 7020, 5832, 4312, 6789, 5231, 7392, 6091, 5667]
calories_burned = [230, 285, 320, 225, 310, 270, 200, 305, 240, 330, 275, 260]
for i in step_count:
	summ += i
for i in calories_burned:
	summm += i
a = summm/len(calories_burned)
b = summ/len(step_count)
print(a)
print(b)
print(b/a)
plt.bar(date, step_count, color = "blue")
plt.xlabel("Date")
plt.ylabel("Step Count")
plt.title("Fitness Tracking")
plt.show()
