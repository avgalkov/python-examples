# Сумма факториалов от 1! до n!
n = int(input())
for j in range(1, n + 1):
  k = 0
  s = 1
  for i in range(1, j + 1):
    s *= i 
    k += s  
print(k)
