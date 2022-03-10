def add(a, b):
    return a+b
def minus(a,b):
    return a-b
def multi(a,b):
    return a*b
def divide(a,b):
    return a/b

print("두개의 숫자와 연산자는 공백 하나를 두고 작성")
print("종료는 0 + 0 입력")
print("ex 1 + 2")
while True:
    a,b,c = input("수식 입력 : ").split(" ")
    a = int(a)
    c = int(c)
    if a == 0 and c == 0:
        break;

    if b == '+':
        print(add(a,c))
        
    elif b == '-':
        print(minus(a,c))
        
    elif b == '*':
        print(multi(a,c))

        
    elif b == '/':
        print(divide(a,c))
        
    else:
        print("수식이 잘못되었습니다")
                  
