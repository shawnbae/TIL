# 해시 테이블, Dictionary, Set

# Dict 구조
#print(__builtins__.__dict__) # 기본적인 builtin 함수를 dictionary 형태로 조회하기

# Hash 값 확인하기
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

#print(hash(t1)) # 할당된 t1의 hash값 조회하기
#print(hash(t2)) # 에러 발생 --> list는 가변적인 type이므로 hash값이 존재할 수 없음.

# 지능형 딕셔너리 (Comprehending Dict)
import csv

# 외부 csv파일을 List of tuple형태로 만들기

with open('./Others/Advanced_Python/resources/test1.csv', 'r', encoding='UTF-8') as f:
    temp = csv.reader(f) # Generator
    # header Skip
    next(temp)
    # 변환하기
    NA_CODES = [tuple(x) for x in temp]

#print(NA_CODES)

n_code1 = {country: code for country, code in NA_CODES} # 각각을 key, value로 맵핑해줌
print(n_code1)