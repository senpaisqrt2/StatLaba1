import matplotlib.pyplot as plt
import math as math
with open("data.txt", "r", encoding="UTF-8") as data:
    element=list(map(int, data.readlines()))

    element.sort()

    age = list()
    crimes = list()
    crimes_add = list()
    for i in range(min(element), max(element)+1):
        age.append(i)
        crimes.append(element.count(i))
        crimes_add.append(element.count(i))

for i in range(1, len(age)):
    crimes_add[i]+=crimes_add[i-1]
    print(crimes_add)
for i in range(len(crimes_add)):
    crimes_add[i] = crimes_add[i]/sum(crimes)
x = age
y = crimes_add
plt.plot(x, y)


probability = sum(crimes)
average = sum(element)/(len(element))
print('Среднее', average)

expectation = 0
for i in range(len(age)):
    expectation+=((age[i])*(crimes[i]/probability))
    #print(age[i], crimes[i])

expectation_squared = 0
for i in range(len(age)):
    expectation_squared+=(((age[i])**2)*(crimes[i]/probability))

dispersion = expectation_squared - expectation**2
print('Дисперсия', dispersion)

average_squared_deviation = math.sqrt(dispersion)
print('Среднее кв. отклонение', average_squared_deviation)

coefficient_of_variation = average_squared_deviation/average * 100
print('Вариация', coefficient_of_variation)

m = max(crimes)
mode = 0
for i in range(len(age)):
    if crimes[i] == m:
        print('Мода и частота', age[i], m)
        mode = age[i]

median = element[int(len(element)/2)]
print('Медиана', median)

maxx = max(age)
minn = min(age)
span = max(age) - min(age)
print('Размах', span)


m = average
n = len(element)
m3 = sum((x - m)**3 for x in element) / n
print('Ассиметрия', (m3/(average_squared_deviation**3)))

m = average
n = len(element)
m4 = sum((x - m)**4 for x in element) / n
print('Эксцесс', (m4/(average_squared_deviation**4))-3)

three_sigma_minus = expectation - average_squared_deviation
three_sigma_plus = expectation + average_squared_deviation
crime_sum = 0
for i in range(len(age)):
    if three_sigma_minus <= age[i] <= three_sigma_plus:
        crime_sum+=crimes[i]
three_sigma_rule_percentage = crime_sum/sum(crimes)
print('Сигма68', (three_sigma_rule_percentage))

three_sigma_minus2 = expectation - 2*average_squared_deviation
three_sigma_plus2 = expectation + 2*average_squared_deviation
crime_sum2 = 0
for i in range(len(age)):
    if three_sigma_minus2 <= age[i] <= three_sigma_plus2:
        crime_sum2+=crimes[i]
three_sigma_rule_percentage2 = crime_sum2/sum(crimes)
print('Сигма95', (three_sigma_rule_percentage2))

three_sigma_minus3 = expectation - 3*average_squared_deviation
three_sigma_plus3 = expectation + 3*average_squared_deviation
crime_sum3 = 0
for i in range(len(age)):
    if three_sigma_minus3 <= age[i] <= three_sigma_plus3:
        crime_sum3+=crimes[i]
three_sigma_rule_percentage3 = crime_sum3/sum(crimes)
print('Сигма99', (three_sigma_rule_percentage3))

if three_sigma_rule_percentage == 0.6825 and three_sigma_rule_percentage2 == 0.95 and three_sigma_rule_percentage3 == 0.997:
    print('График совпадает с нормальным распределением')
else:
    print('График не совпадает с нормальным распределением')

plt.show()