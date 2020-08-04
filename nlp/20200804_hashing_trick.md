# Hashing trick

## 개요

Database에 대한 내부 알고리즘에서 견출지라는 개념이 있다. Indexing 방법론으로, 몇 장마다 인덱싱을 붙일 지 미리 정해야하며, memory 비효율성도 존재하는데 key의 범위가 넓다면 더욱 심해진다. 검색 속도가 빠르므로 나중에 찾기에 좋다는 장점을 가지고 있다.

Hashing trick이라는 것은 암호화를 통해 검색하는 방법이다. 예를 들어 apple이라는 단어를 수치 변환하여 584라는 숫자를 만들어내고 임의의 숫자 84page 36line을 할당하여 기록한다. 이는 메모리 차원에서 효율적인 단어 표현에 사용될 수 있지만, 동시에 우연히 완전히 다른 단어가 같은 hash를 가지고 있을 수 있다는 문제점을 가지기도 한다. 이를 collision문제라 한다.



## python 구현

> 필요한 패키지들과 sample을 지정한다.

```python
import tensorflow as tf
from tensorflow.keras.preprocessing.text import hashing_trick
from tensorflow.keras.layers import Input, Embedding, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
import numpy as np
    
samples = ['너 오늘 이뻐 보인다', 
           '나는 오늘 기분이 더러워', 
           '끝내주는데, 좋은 일이 있나봐', 
           '나 좋은 일이 생겼어', 
           '아 오늘 진짜 짜증나', 
           '환상적인데, 정말 좋은거 같아']
labels = [[1], [0], [1], [1], [0], [1]]
```



> hash 테이블로 문서를 수치화한다.

```python
VOCAB_SIZE = 10 # vocabulary 크기 (hash table)를 10개로 한정한다.
sequences = [hashing_trick(s, VOCAB_SIZE) for s in samples]
sequences = np.array(sequences)
labels = np.array(labels)
print(sequences)
```

```
[[6 1 7 9]
 [5 1 3 6]
 [4 6 3 8]
 [9 6 3 7]
 [2 1 5 8]
 [2 2 9 6]]
```

결과를 보면, '아' '환상적인데' '정말'이 모두 같은 hash가 되었음을 알 수 있다. 이는 전체 vocabulary 개수가 작아 collision문제가 발생했음을 의미한다.



