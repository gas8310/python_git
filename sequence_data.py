#시퀀스 자료형
#문자열, 리스트, 튜플 등 인덱스를 가지는 자료형

#기본적 사용법?
#1.
string = "hello - world"

list = ['h', 'e', 'l', 'l', 'o', '-', 'w', 'o', 'r', 'l', 'd']
tuple = ('h', 'e', 'l', 'l', 'o', '-', 'w', 'o', 'r', 'l', 'd')

print(string[0:5])
print(list[0:5])
print(tuple[0:5])

for i in string:
    # print(string[i])
    print(i)
print(len(string))

#조건문의 사용.
if 'h' in string:
    print("h가 포함되어있습니다.")
