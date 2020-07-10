#lambda
#람다식 : 함수의 형태를 더욱 짧게 쓸 수 있도록 해주는 문법.
# map(): 다수의 원소에 대한 함수의 결과를 한번에 얻을 수 있도록 해줌.
#        각원소를 하나씩 화면하며 결과가 반환되도록함.
# object: 리스트를 통해 리스트의 값을 볼수 있도록 변환처리함.

add = lambda x, y: x + y
print(add(1, 2))

lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 10]

lambda_fnc = lambda a, b: a + b
result = map(lambda_fnc, lst1, lst2)
print(list(result))