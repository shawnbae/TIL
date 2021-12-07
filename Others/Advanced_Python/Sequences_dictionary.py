# 해시 테이블, Dictionary, Set
# 중복을 처리한다는 것은, 자동으로 중복을 제거하고 있다는 뜻이다.
# 이를 해시 테이블이라고 하며,Python의 해시 테이블은 그에 해당한다.

# Dict 구조
#print(__builtins__.__dict__) # 기본적인 builtin 함수를 dictionary 형태로 조회하기

# Hash 값 확인하기
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

#print(hash(t1)) # 할당된 t1의 hash값 조회하기
#print(hash(t2)) # 에러 발생 --> list는 가변적인 type이므로 hash값이 존재할 수 없음.

# 지능형 딕셔너리 (Comprehending Dictionary)
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
n_code2 = {country.upper(): code for country, code in NA_CODES}
#print(n_code1)
#print(n_code2)

# Dict Setdefault : 성능 향상의 좋은 방법
# Key값이 중복되므로 이를 dictionary로 변환할 경우 문제가 생긴다.
source = (('k1', 'val1'),
            ('k1', 'val2'),
            ('k2', 'val3'),
            ('k2', 'val4'),
            ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# setdefault 함수를 사용하지 않는 경우
# --> 중복되는 경우, 아닌 경우 나누어 알고리즘을 짜줘야 함.
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

#print(new_dict1)

# setdefault 함수를 사용하는 경우
# key, value list를 할당한 뒤 value를 append하면 됨.
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

#print(new_dict2)

# 사용자 정의 dictionary 상속하기 (사용자 정의 Class)
class UserDict(dict):
    def __missing__(self, key):
        print('Called: __missing__')
        if isinstance(key, str):
            raise KeyError(key)
        return self