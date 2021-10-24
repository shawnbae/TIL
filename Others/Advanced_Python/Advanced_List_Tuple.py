# 컨테이너(Container : 서로다른 자료형[list, tuple, collections.deque], Flat : 한 개의 자료형[str,bytes,bytearray,array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque) vs 불변(tuple, str, bytes)

# 지능형 리스트, List Comprehension

chars = '!@#$%^&*()_+'
codes1 = []

for s in chars:
    codes1.append(ord(s)) # Unicode값 반환

print(codes1)

# Comprehending Lists
codes2 = [ord(s) for s in chars]
print(codes2)