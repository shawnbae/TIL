# Word Embedding

## 개요

기존의 빈도에 기반한 벡터화 방식(TF-IDF, BOW, Doc2BOW, cooccurence Matrix)들은 단어에 의미를 부여하지 못하고 형식적인 단어 임베딩만 가능하였다. 따라서 확률적인 통계 기반의 이론들로 설명되었다. 그러나 Word Embedding 방식은 단어의 의미를 고려하여 벡터화하는 방법을 설명한다. 또한 이는 학습 기반으로 임베딩된다.

현재 NLP분야의 원리는 단어 기반의 NLP(POS-tag / stemmer 등)가 주류이다. 현재는 Character-based NLP가 Embedding방식의 새로운 방법론으로 의논되고 있다.

> Word Embedding Layer의 구성은 아래와 같다.

- 입력층
  - 문장이 I love you very much라고 한다면, 단어 기준으로 5개로 구분되므로 입력층을 5개로 구성한다.
- 은닉층
  - 총 vocabulary size로 one-hot 벡터화한다.
  - 예를 들어 500개의 vocabulary size를 가진다면, 입력층의 W matrix는 5X500이 된다.
  - one-hot vector로 바꿀 때 to_categorical 함수를 이용하며, one-hot vector로 바꾼다는 의미는 모든 단어의 의미를 초기화하여 벡터화시킨다는 뜻이다.
- 출력층
  - 64개의 출력층을 가졌다고 한다면, 학습에 의해 나오는 결과물의 크기는 (5 X 500) X (500 X 64) = (5 X 64)일 것이다.
  - 위 결과물의 행들은 한 단어의 의미를 지닌 벡터로 Embedding된다. 이는 유사도 측정이 가능해졌음을 의미하기도 한다.