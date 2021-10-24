# 컨테이너(Container : 서로다른 자료형[list, tuple, collections.deque], Flat : 한 개의 자료형[str,bytes,bytearray,array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque) vs 불변(tuple, str, bytes)

# 지능형 리스트, List Comprehension
chars = '!@#$%^&*()_+'
codes1 = []

for s in chars:
    codes1.append(ord(s)) # Unicode값 반환
#print(codes1)

# Comprehending Lists
codes2 = [ord(s) for s in chars]
#print(codes2)

codes3 = [ord(s) for s in chars if ord(s) > 40] # 조건부 list comprehension
#print(codes3)

codes4 = list(filter(lambda x : x > 40, map(ord, chars))) # filter와 map을 활용한 방식
#print(codes4)

# Generator : 한 번에 한 개의 항목을 생성 (메모리 유지X --> 성능 압도적)
import array

# tuple 안에 List comprehension과 같이 구문을 작성하면 Generator가 된다.
# List의 경우 메모리에 일단 모든 값들을 할당한다. 따라서 데이터가 큰 경우 메모리 할당량이 높다.
# Generator의 경우 메모리를 사용하지 않고 데이터를 만들기를 기다리는 상태이다.
tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))

#print(next(tuple_g)) # generator object 반환, next라는 함수를 써야 그제서야 값이 등장함. --> 하나의 값만 메모리 할당.
#print(next(tuple_g)) # 그 다음 값이 존재함. --> 새로운 값만 메모리에 할당
#print(array_g)
#print(type(array_g))
#print(array_g.tolist())

# 제너레이터 예시
#print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)))
for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)):
    #print('EX3-2 -', s)
    pass

# Advanced Tuple (Packing & Unpacking)
# Packing method: divmod
#print(divmod(100, 9))
#print(divmod(*(100, 9)))
#print(*(divmod(100, 9)))

# Unpacking 방식
x, y, *rest = range(10) # x, y에 값 대응하고 나머지 묶어서 반환
#print(x, y, rest)

x, y, *rest = range(2)
#print(x, y, rest)

x, y, *rest = 1, 2, 3, 4, 5
#print(x, y, rest)

# Mutable(가변) vs Immutable(불변)
l = (10, 15, 20)
m = [10, 15, 20]

print(l, id(l))
print(m, id(m))

l = l * 2
m = m * 2

print(l, id(l))
print(m, id(m))

l *= 2
m *= 2

print(l, id(l)) # id값이 변함. 다른 객체로 재할당이 이루어졌음을 알 수 있음.
print(m, id(m)) # id값이 변하지 않음. 덮어쓰기가 이루어짐.