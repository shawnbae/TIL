# Information Extraction from Text

## Chunking

> 여러 개의 품사로 구(phrase)를 만드는 것을 chunking이라고 한다.
>
> 또한 이렇게 묶인 구(phrase)를 chunk라고 한다.

```python
sentence= [("the","DT"), ("little", "JJ"), ("yellow","JJ"),
           ("dog","NN"), ("barked","VBD"), ("at","IN"),
           ("the", "DT"), ("cat", "NN")]

grammar= "NP: {<DT>?<JJ>*<NN>}"

cp= nltk.RegexpParser(grammar)
result= cp.parse(sentence)
print(result)
```

```
(S
  (NP the/DT little/JJ yellow/JJ dog/NN)
  barked/VBD
  at/IN
  (NP the/DT cat/NN))
```



```python
result.draw()
```

![image-20200717121218066](C:/Users/soohan/TIL_study/nlp/markdown-images/image-20200717121218066.png)



```python
grammar= """
    NP: {<DT|PP\$>?<JJ>*<NN>}
        {<NNP>}
"""

cp= nltk.RegexpParser(grammar)
sentence= [("Rapunzel", "NNP"), ("let","VBD"), ("down","RP"),
           ("her", "PP$"), ("long","JJ"), ("golden","JJ"),
           ("hair", "NN")]

result= cp.parse(sentence)
print(result)
```

```
(S
  (NP Rapunzel/NNP)
  let/VBD
  down/RP
  (NP her/PP$ long/JJ golden/JJ hair/NN))
```



```python
result.draw()
```

![image-20200717133734736](C:/Users/soohan/TIL_study/nlp/markdown-images/image-20200717133734736.png)



```python
nouns= [("money","NN"), ("market","NN"),("fund","NN")]
grammar= "NP: {<NN><NN>} # Chunk two consecutive nouns"
cp= nltk.RegexpParser(grammar)
print(cp.parse(nouns))
```

```
(S (NP money/NN market/NN) fund/NN)
```



```python
sentence= [("the","DT"), ("little","JJ"),("yellow","JJ"),
           ("dog","NN"),("barked","VBD"),("at","IN"),
           ("the","DT"),("cat","NN")]

grammar= "NP: {<DT>?<JJ>*<NN>}"
cp= nltk.RegexpParser(grammar)
tree= cp.parse(sentence)
print(tree)
```

```
(S
  (NP the/DT little/JJ yellow/JJ dog/NN)
  barked/VBD
  at/IN
  (NP the/DT cat/NN))
```

> tree들의 subtree POS확인하기

```python
for subtree in tree.subtrees():
    print(subtree.label())
```

```
S
NP
NP
```

> 원하는 형태의 시퀀스 발췌하기

```python
cp= nltk.RegexpParser('CHUNK: {<V.*> <TO> <V.*>}')
brown= nltk.corpus.brown
i=0
for sent in brown.tagged_sents():
    tree= cp.parse(sent)
    for subtree in tree.subtrees():
        if subtree.label() == "CHUNK":
            print(subtree)
            i += 1
    if i > 10: break
```

```
(CHUNK combined/VBN to/TO achieve/VB)
(CHUNK continue/VB to/TO place/VB)
(CHUNK serve/VB to/TO protect/VB)
(CHUNK wanted/VBD to/TO wait/VB)
(CHUNK allowed/VBN to/TO place/VB)
(CHUNK expected/VBN to/TO become/VB)
(CHUNK expected/VBN to/TO approve/VB)
(CHUNK expected/VBN to/TO make/VB)
(CHUNK intends/VBZ to/TO make/VB)
(CHUNK seek/VB to/TO set/VB)
(CHUNK like/VB to/TO see/VB)
```



#### Chinking

> 특정 부분을 chunk 밖으로 빼내는 것을 chinking이라고 한다. chink는 문장에서 chunk를 제외한 나머지 부분을 의미한다.

```python
grammar= r"""
    NP:
    {<.*>+} # CHUNK everything
    }<VBD|IN>+{
"""

sentence= [("the","DT"), ("little","JJ"),("yellow","JJ"),
           ("dog","NN"),("barked","VBD"),("at","IN"),
           ("the","DT"),("cat","NN")]
cp= nltk.RegexpParser(grammar)
print(cp.parse(sentence))
```

```
(S
  (NP the/DT little/JJ yellow/JJ dog/NN)
  barked/VBD
  at/IN
  (NP the/DT cat/NN))
```

#### Chunked Sentence

> 사전에 chunking된 사전

```python
from nltk.corpus import conll2000

print(conll2000.chunked_sents('train.txt')[99])
```

```
(S
  (PP Over/IN)
  (NP a/DT cup/NN)
  (PP of/IN)
  (NP coffee/NN)
  ,/,
  (NP Mr./NNP Stone/NNP)
  (VP told/VBD)
  (NP his/PRP$ story/NN)
  ./.)
```

```python
print(conll2000.chunked_sents('train.txt', chunk_types=['NP'])[99])
```

```
(S
  Over/IN
  (NP a/DT cup/NN)
  of/IN
  (NP coffee/NN)
  ,/,
  (NP Mr./NNP Stone/NNP)
  told/VBD
  (NP his/PRP$ story/NN)
  ./.)
```

> test.txt로 chunk 성능을 평가한다.

```python
test_sents= conll2000.chunked_sents('test.txt', chunk_types=['NP'])
grammar= r"NP: {<[CDJNP].*>+}"
cp= nltk.RegexpParser(grammar)
score= cp.evaluate(test_sents)
print(score)
```

```
ChunkParse score:
    IOB Accuracy:  87.7%%
    Precision:     70.6%%
    Recall:        67.8%%
    F-Measure:     69.2%%
```

>여러 척도들을 score의 메서드들로 조회가 가능하다.

```python
score.accuracy()
score.precision()
score.recall()
score.f_measure()
```

#### Recursion in Linguistic Structure

> 문법에 절(clause)을 정의함

```python
grammar= r"""
    NP: {<DT|JJ|NN.*>+}
    PP: {<IN><NP>}
    VP: {<VB.*><NP|PP|CLAUSE>+$}
    CLAUSE: {<NP><VP>}
    """
cp= nltk.RegexpParser(grammar)
sentence= [("Mary","NN"),("saw","VBD"),("the","DT"),("cat","NN"),
           ("sit","VB"),("on","IN"),("the","DT"),("mat","NN")]
print(cp.parse(sentence))
```

```
(S
  (NP Mary/NN)
  saw/VBD
  (CLAUSE
    (NP the/DT cat/NN)
    (VP sit/VB (PP on/IN (NP the/DT mat/NN)))))
```

![image-20200717145912648](C:/Users/soohan/TIL_study/nlp/markdown-images/image-20200717145912648.png)



> Clause안에 또 다른 Clause가 들어 있는 경우 

```python
sentence= [("John", "NNP"),("thinks","VBZ"),
           ("Mary","NN"),("saw","VBD"),
           ("the","DT"),("cat","NN"),
           ("sit","VB"),
           ("on","IN"),("the","DT"),
           ("mat","NN")]
print(cp.parse(sentence))
```

```
(S
  (NP John/NNP)
  thinks/VBZ
  (NP Mary/NN)
  saw/VBD
  (CLAUSE
    (NP the/DT cat/NN)
    (VP sit/VB (PP on/IN (NP the/DT mat/NN)))))
```

```python
cp.parse(sentence).draw()
```

![image-20200717150527835](C:/Users/soohan/TIL_study/nlp/markdown-images/image-20200717150527835.png)



> loop 지정을 통한 재귀적(recursion) 분석

```python
cp= nltk.RegexpParser(grammar, loop=2)
print(cp.parse(sentence))
```

```
(S
  (NP John/NNP)
  thinks/VBZ
  (CLAUSE
    (NP Mary/NN)
    (VP
      saw/VBD
      (CLAUSE
        (NP the/DT cat/NN)
        (VP sit/VB (PP on/IN (NP the/DT mat/NN)))))))
```

```python
cd.parse(sentence).draw()
```

![image-20200717163039905](C:/Users/soohan/TIL_study/nlp/markdown-images/image-20200717163039905.png)

이와 같이 문장에 맞게 트리를 깊게 구성하는 방식을 cascaded chunking이라고 부른다.