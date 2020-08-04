# Co-occurence matrix

## 개요

Co-occurence matrix는 빈도 기반(count-based)의 단어 표현 방법이다. 그렇다면 기존의 one-hot이나 TF-IDF과 다른 점은 무엇일까? 바로 단어들 간의 관계 정보를 내포하고 있다는 점이다. 또한 단어들 간의 관계 정보를 내포하고있기 때문에, 단어간 유사도가 존재할 수 있다. 다만 계산 비용이 많다는 단점이 존재한다.

Word Embedding Layer를 활용하여 단어를 벡터화했던 학습 기반의 단어 표현 방식이 아니라는 점도 중요한 의미를 지닌다. 또한 skip-gram과 결정적인 차이점으로 skip-gram은 주변 단어들에 한정되나 co-occurence matrix의 경우 모든 맥락에 대해 벡터화하였으므로 전체 단어를 고려하였다. 이 둘을 결합하여 Word Embedding을 구현할 수 있는데 이 모델이 GloVe이다. 

즉, GloVe는 빈도 기반의 방식과 학습 기반의 방식을 결합하여 사용한 방식이다.



## 구현

> 필요한 패키지들과 문장 셋을 입력한다.

```python
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

docs = ['성진과 창욱은 야구장에 갔다',
        '성진과 태균은 도서관에 갔다',
        '성진과 창욱은 공부를 좋아한다']
```



> scikit-learn의 내장 전처리 함수를 이용하여 벡터화한다. ngram_range= (1,1)는 Unigram임을 의미한다.

```python
count_model = CountVectorizer(ngram_range=(1,1))
x = count_model.fit_transform(docs)
print(count_model.vocabulary_) # 단어사전 조회
print(x) # index to count
```

```
{'성진과': 3, '창욱은': 6, '야구장에': 4, '갔다': 0, '태균은': 7, '도서관에': 2, '공부를': 1, '좋아한다': 5}

  (0, 3)	1
  (0, 6)	1
  (0, 4)	1
  (0, 0)	1
  (1, 3)	1
  (1, 0)	1
  (1, 7)	1
  (1, 2)	1
  (2, 3)	1
  (2, 6)	1
  (2, 1)	1
  (2, 5)	1
```



> index to count Series를 행렬로 표시한다.

```python
print(x.toarray())
print(x.T.toarray())
```

````
[[1 0 0 1 1 0 1 0]
 [1 0 1 1 0 0 0 1]
 [0 1 0 1 0 1 1 0]]
 
 [[1 1 0]
 [0 0 1]
 [0 1 0]
 [1 1 1]
 [1 0 0]
 [0 0 1]
 [1 0 1]
 [0 1 0]]
````

이 때, x.T의 의미를 행렬화하면 아래와 같다.

```
#          1 2 3  - 문장
#갔다    [[1 1 0] - '갔다'라는 단어는 문장-1과 문장-2에 쓰였음.
#공부를   [0 0 1] - '공부를'은 문장-3에만 쓰였음.
#도서관에 [0 1 0]
#성진과   [1 1 1]
#야구장에 [1 0 0]
#좋아한다 [0 0 1]
#창욱은   [1 0 1]
#태균은   [0 1 0]]
```



그러나 이 행렬은 co-occurence matrix가 아니다. 이 때 co-occurence table은 Transposed matrix와 matrix의 곱으로 구해낼 수 있다.

```python
xc = x.T * x # this is co-occurrence matrix in sparse csr format
xc.setdiag(0) # 대각선의 원소들을 0으로 만든다.
print(xc.toarray())
```

```
[[0 0 1 2 1 0 1 1]
 [0 0 0 1 0 1 1 0]
 [1 0 0 1 0 0 0 1]
 [2 1 1 0 1 1 2 1]
 [1 0 0 1 0 0 1 0]
 [0 1 0 1 0 0 1 0]
 [1 1 0 2 1 1 0 0]
 [1 0 1 1 0 0 0 0]]
```



## Co-occurence matrix를 이용하여 SVD 해보기

### SVD

```python
import numpy as np
C = xc.toarray()
U, S, VT = np.linalg.svd(C, full_matrices = True)
print(np.round(U, 2), '\n')
print(np.round(S, 2), '\n')
print(np.round(VT, 2), '\n')
```

```
# U matrix
[[-0.44 -0.39 -0.58  0.41  0.35  0.   -0.   -0.19]
 [-0.24 -0.12  0.29  0.41 -0.24  0.65 -0.29  0.35]
 [-0.24 -0.12 -0.29 -0.41 -0.24 -0.29 -0.65  0.35]
 [-0.56  0.8   0.   -0.    0.19  0.    0.    0.02]
 [-0.27 -0.01 -0.   -0.   -0.7   0.   -0.   -0.66]
 [-0.24 -0.12  0.29  0.41 -0.24 -0.65  0.29  0.35]
 [-0.44 -0.39  0.58 -0.41  0.35 -0.    0.   -0.19]
 [-0.24 -0.12 -0.29 -0.41 -0.24  0.29  0.65  0.35]] 

# S matrix
 [5.27 2.52 1.73 1.73 1.27 1.   1.   0.53]
 
# VT matrix
[[-0.44 -0.24 -0.24 -0.56 -0.27 -0.24 -0.44 -0.24]
 [ 0.39  0.12  0.12 -0.8   0.01  0.12  0.39  0.12]
 [-0.    0.5  -0.5  -0.    0.    0.5  -0.   -0.5 ]
 [-0.71  0.   -0.    0.    0.    0.    0.71 -0.  ]
 [-0.35  0.24  0.24 -0.19  0.7   0.24 -0.35  0.24]
 [-0.   -0.65  0.29 -0.    0.    0.65  0.   -0.29]
 [-0.    0.29  0.65 -0.    0.   -0.29 -0.   -0.65]
 [-0.19  0.35  0.35  0.02 -0.66  0.35 -0.19  0.35]] 
```



### Truncated SVD

> 특이값(S)이 큰 4개를 주 성분으로 C의 차원을 축소한다.

```python
from sklearn.decomposition import TruncatedSVD

svd = TruncatedSVD(n_components=4, n_iter=7)
D = svd.fit_transform(xc.toarray())

U = D / svd.singular_values_
S = np.diag(svd.singular_values_)
VT = svd.components_
```

```
# U matrix
[[ 0.44 -0.39 -0.58  0.41]
 [ 0.24 -0.12  0.29  0.41]
 [ 0.24 -0.12 -0.29 -0.41]
 [ 0.56  0.8   0.   -0.  ]
 [ 0.27 -0.01 -0.   -0.  ]
 [ 0.24 -0.12  0.29  0.41]
 [ 0.44 -0.39  0.58 -0.41]
 [ 0.24 -0.12 -0.29 -0.41]] 

# S matrix
[[5.27 0.   0.   0.  ]
 [0.   2.52 0.   0.  ]
 [0.   0.   1.73 0.  ]
 [0.   0.   0.   1.73]] 

# VT matrix
[[ 0.44  0.24  0.24  0.56  0.27  0.24  0.44  0.24]
 [ 0.39  0.12  0.12 -0.8   0.01  0.12  0.39  0.12]
 [-0.    0.5  -0.5  -0.    0.    0.5  -0.   -0.5 ]
 [-0.71  0.   -0.    0.    0.    0.    0.71 -0.  ]] 
```

