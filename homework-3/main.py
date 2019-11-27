# This function checks equality between three parameters

def checkEquality(num1, num2, num3):
  num1, num2, num3 = int(num1), int(num2), int(num3)
  return num1 == num2 or num2 == num3 or num3 == num1

result = checkEquality(1, 4, 3)
print(result)

result = checkEquality(1, 4, "3")
print(result)

result = checkEquality(1, 4, 4)
print(result)

result = checkEquality(1, 4, "4")
print(result)
