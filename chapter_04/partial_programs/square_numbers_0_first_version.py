squares = []
for value in range(1, 11):
    square = value ** 2   #제곱
    squares.append(square)

print(type(squares))   #type()안에 넣으면 타입을 알 수 있음.
for i, v in enumerate(squares):
    print("{}는 {}".format(i, v))   #7, 8라인 자주 사용하게 될것   #f-format대신 .format()을 사용, 각 자리에 i와 v가 들어감
