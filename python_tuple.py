#python tuple
#python에서 기본적으로 제공하는 자료형
#list와 비슷한 형태이지만 한번 입력된 자료는 변경할 수 없다.
#2차원배열등의 기법을 그대로 사용할 수 있다.
#tuple의 값은 변경할 수 없지만, tuple의 원소가 list인 경우 list의 값을 변경하는 것이므로 가능하다

tuple = (1, 2, 3)

print(tuple)

print(tuple[0])

list1 = [1, 2, 3]
list2 = [6, 7, 8]

tuple = (list1, list2)

print(tuple)

#이건안되
# tuple[0] = [9, 0, 5]

#이건 됨
tuple[0][0] = 7
tuple[0][1] = 7
tuple[0][2] = 7
print(tuple)

#print 될때만 2번찍음.
print(tuple[:]*2)

print(tuple[:])