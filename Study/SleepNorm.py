a = int(input())
b = int(input())
h = int(input())
if a <= h <= b:
 print("Это нормально")
elif a > h:
 print('Недосып')
elif h > b:
 print('Пересып')