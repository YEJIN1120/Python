bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles[1] = 'genesis'   #바꿔치기
##추가 -> insert, append
bicycles.insert(1,'canival')
del bicycles[0]   #첫번째 요소 trek 삭제
print(bicycles)   #전체 출력
print(bicycles[-3].title())
