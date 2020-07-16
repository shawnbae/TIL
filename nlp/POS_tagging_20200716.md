# POS tagging

> nltk 패키지 불러오기

```python
import nltk
```

## 기본적인 문장에 품사 태깅해보기

```python
text= "And now for something completely different"
token= nltk.word_tokenize(text)
nltk.pos_tag(token)

text2= "They refuse to permit us to obtain the refuse permit"
token2= nltk.word_tokenize(text2)
nltk.pos_tag(token2)
```

```
[('And', 'CC'),
 ('now', 'RB'),
 ('for', 'IN'),
 ('something', 'NN'),
 ('completely', 'RB'),
 ('different', 'JJ')]
```

```
[('They', 'PRP'),
 ('refuse', 'VBP'),
 ('to', 'TO'),
 ('permit', 'VB'),
 ('us', 'PRP'),
 ('to', 'TO'),
 ('obtain', 'VB'),
 ('the', 'DT'),
 ('refuse', 'NN'),
 ('permit', 'NN')]
```

> text를 설정하여 tokenize한 후, token들에 대해 품사를 태깅해본다.

## 학습용 Corpus들 품사 태깅해보기

#### Penn Treebank Corpus

```python
penn= nltk.corpus.treebank.tagged_words()
print(penn[:20])
```

```
[('Pierre', 'NNP'), ('Vinken', 'NNP'), (',', ','), ('61', 'CD'), ('years', 'NNS'), ('old', 'JJ'), (',', ','), ('will', 'MD'), ('join', 'VB'), ('the', 'DT'), ('board', 'NN'), ('as', 'IN'), ('a', 'DT'), ('nonexecutive', 'JJ'), ('director', 'NN'), ('Nov.', 'NNP'), ('29', 'CD'), ('.', '.'), ('Mr.', 'NNP'), ('Vinken', 'NNP')]
```



#### Brown Corpus

```python
brown1= nltk.corpus.brown.tagged_words()
print(brown1[:20])

brown2= nltk.corpus.brown.tagged_words(tagset= 'universal')
print(brown2[:20])
```

```
[('The', 'AT'), ('Fulton', 'NP-TL'), ('County', 'NN-TL'), ('Grand', 'JJ-TL'), ('Jury', 'NN-TL'), ('said', 'VBD'), ('Friday', 'NR'), ('an', 'AT'), ('investigation', 'NN'), ('of', 'IN'), ("Atlanta's", 'NP$'), ('recent', 'JJ'), ('primary', 'NN'), ('election', 'NN'), ('produced', 'VBD'), ('``', '``'), ('no', 'AT'), ('evidence', 'NN'), ("''", "''"), ('that', 'CS')]
```

```
[('The', 'DET'), ('Fulton', 'NOUN'), ('County', 'NOUN'), ('Grand', 'ADJ'), ('Jury', 'NOUN'), ('said', 'VERB'), ('Friday', 'NOUN'), ('an', 'DET'), ('investigation', 'NOUN'), ('of', 'ADP'), ("Atlanta's", 'NOUN'), ('recent', 'ADJ'), ('primary', 'NOUN'), ('election', 'NOUN'), ('produced', 'VERB'), ('``', '.'), ('no', 'DET'), ('evidence', 'NOUN'), ("''", '.'), ('that', 'ADP')]
```



#### NPS chat Corpus

```python
chat= nltk.corpus.nps_chat.tagged_words()
print(chat[:20])
```

```
[('now', 'RB'), ('im', 'PRP'), ('left', 'VBD'), ('with', 'IN'), ('this', 'DT'), ('gay', 'JJ'), ('name', 'NN'), (':P', 'UH'), ('PART', 'VB'), ('hey', 'UH'), ('everyone', 'NN'), ('ah', 'UH'), ('well', 'UH'), ('NICK', 'NN'), (':', ':'), ('U7', 'NNP'), ('U7', 'NNP'), ('is', 'VBZ'), ('a', 'DT'), ('gay', 'JJ')]
```



#### CONLL Corpus

```python
conll= nltk.corpus.conll2000.tagged_words()
print(conll[:20])
```

```
[('Confidence', 'NN'), ('in', 'IN'), ('the', 'DT'), ('pound', 'NN'), ('is', 'VBZ'), ('widely', 'RB'), ('expected', 'VBN'), ('to', 'TO'), ('take', 'VB'), ('another', 'DT'), ('sharp', 'JJ'), ('dive', 'NN'), ('if', 'IN'), ('trade', 'NN'), ('figures', 'NNS'), ('for', 'IN'), ('September', 'NNP'), (',', ','), ('due', 'JJ'), ('for', 'IN')]
```



#### Brown Corpus에서 Tag의 빈도 확인하기

```python
from nltk.corpus import brown
brown_news_tagged= brown.tagged_words(categories='news', tagset= 'universal')
tag_fd= nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
tag_fd.most_common()
```

```
[('NOUN', 30654),
 ('VERB', 14399),
 ('ADP', 12355),
 ('.', 11928),
 ('DET', 11389),
 ('ADJ', 6706),
 ('ADV', 3349),
 ('CONJ', 2717),
 ('PRON', 2535),
 ('PRT', 2264),
 ('NUM', 2166),
 ('X', 92)]
```



## Hidden Markov Model

#### HMM의 parameter 추정하기(Transition, Emission probability)

```python
tagged_words= []
all_tags= []

for sent in nltk.corpus.brown.tagged_sents(tagset= 'universal'):
    tagged_words.append(("START","START"))
    all_tags.append("START")
    for (word, tag) in sent:
        all_tags.append(tag)
        tagged_words.append((tag, word))
    tagged_words.append(("END","END"))
    all_tags.append("END")
```

> 추정 후의 Transition Probability

```python
cfd_tags= nltk.ConditionalFreqDist(nltk.bigrams(all_tags))
cpd_tags= nltk.ConditionalProbDist(cfd_tags, nltk.MLEProbDist)

print("Count('DET','NOUN') =", cfd_tags['DET']['NOUN'])
print("P('NOUN' | 'DET') =", cpd_tags['DET'].prob('NOUN'))
```

```
Count('DET','NOUN') = 85838
P('NOUN' | 'DET') = 0.6264678621213117
```

> 추정 후의 Emission Probability

```python
cfd_tagwords= nltk.ConditionalFreqDist(tagged_words)
cpd_tagwords= nltk.ConditionalProbDist(cfd_tagwords,nltk.MLEProbDist)

print("Count('DET','the') =", cfd_tagwords['DET']['the'])
print("P('the' | 'DET') =", cpd_tagwords['DET'].prob('the'))
```

```
Count('DET','the') = 62710
P('the' | 'DET') = 0.45767375327509324
```

#### 명사 앞에 많이 오는 품사 확인하기

```python
word_tag_pairs= nltk.bigrams(brown_news_tagged)
bigram= [(a,b) for (a,b) in word_tag_pairs]
bigram[:10]
```

```
[(('The', 'DET'), ('Fulton', 'NOUN')),
 (('Fulton', 'NOUN'), ('County', 'NOUN')),
 (('County', 'NOUN'), ('Grand', 'ADJ')),
 (('Grand', 'ADJ'), ('Jury', 'NOUN')),
 (('Jury', 'NOUN'), ('said', 'VERB')),
 (('said', 'VERB'), ('Friday', 'NOUN')),
 (('Friday', 'NOUN'), ('an', 'DET')),
 (('an', 'DET'), ('investigation', 'NOUN')),
 (('investigation', 'NOUN'), ('of', 'ADP')),
 (('of', 'ADP'), ("Atlanta's", 'NOUN'))]
```

```python
word_tag_pairs= nltk.bigrams(brown_news_tagged)
noun_preceders= [a[1] for (a,b) in word_tag_pairs if b[1] == 'NOUN']
fdist= nltk.FreqDist(noun_preceders)
[tag for (tag, _) in fdist.most_common()]
```

```
['NOUN','DET','ADJ','ADP','.','VERB','CONJ','NUM','ADV','PRT','PRON','X']
```

#### 가장 많이 쓰이는 동사 확인하기

```python
wsj= nltk.corpus.treebank.tagged_words(tagset= 'universal')
word_tag_fd= nltk.FreqDist(wsj)
word_tag_fd.most_common()[:10]
```

```
[((',', '.'), 4885),
 (('the', 'DET'), 4038),
 (('.', '.'), 3828),
 (('of', 'ADP'), 2319),
 (('to', 'PRT'), 2161),
 (('a', 'DET'), 1874),
 (('in', 'ADP'), 1554),
 (('and', 'CONJ'), 1505),
 (('*-1', 'X'), 1123),
 (('0', 'X'), 1099)]
```

```python
v =[wt[0] for (wt,_) in word_tag_fd.most_common() if wt[1] == 'VERB']
print(v[:20])
```

```
['is', 'said', 'was', 'are', 'be', 'has', 'have', 'will', 'says', 'would', 'were', 'had', 'been', 'could', "'s", 'can', 'do', 'say', 'make', 'may']
```

#### 특정 단어에 부여된 품사 빈도 확인하기

```python
cfd1= nltk.ConditionalFreqDist(wsj)
list(cfd1.items())[:10]
```

````
[('Pierre', FreqDist({'NOUN': 1})),
 ('Vinken', FreqDist({'NOUN': 2})),
 (',', FreqDist({'.': 4885})),
 ('61', FreqDist({'NUM': 5})),
 ('years', FreqDist({'NOUN': 115})),
 ('old', FreqDist({'ADJ': 24})),
 ('will', FreqDist({'VERB': 280, 'NOUN': 1})),
 ('join', FreqDist({'VERB': 4})),
 ('the', FreqDist({'DET': 4038, 'ADJ': 5, 'NOUN': 1, 'NUM': 1})),
 ('board', FreqDist({'NOUN': 30}))]
````

```
cfd1['yield'].most_common()

cfd1['cut'].most_common()
```

```
[('VERB', 28), ('NOUN', 20)]

[('VERB', 25), ('NOUN', 3)]
```

#### 특정 품사로 상용된 품사 확인하기

> VBN(과거분사형) 단어들 확인하기

```python
wsj= nltk.corpus.treebank.tagged_words()
cfd2= nltk.ConditionalFreqDist((tag,word) for (word, tag) in wsj)
print(list(cfd2['VBN'])[:20])
```

```
['been', 'expected', 'made', 'compared', 'based', 'used', 'priced', 'sold', 'named', 'designed', 'held', 'fined', 'taken', 'paid', 'traded', 'increased', 'said', 'filed', 'reached', 'called']
```

> 과거분사형 동사의 앞 부분 context를 확인하기

```python
idx1= wsj.index(('kicked','VBD'))
wsj[idx1]
```

```
('kicked', 'VBD')
```

```python
wsj[idx1-4:idx1+1]
```

```
[('While', 'IN'),
 ('program', 'NN'),
 ('trades', 'NNS'),
 ('swiftly', 'RB'),
 ('kicked', 'VBD')]
```

```python
idx2= wsj.index(('kicked','VBN'))
wsj[idx2-4:idx2+1]
```

```
[('head', 'NN'),
 ('of', 'IN'),
 ('state', 'NN'),
 ('has', 'VBZ'),
 ('kicked', 'VBN')]
```

#### 특정 단어로 단어와 품사 조회하기

```python
brown_learned_text= brown.words(categories= 'learned')
v= sorted(set(b for (a,b) in nltk.bigrams(brown_learned_text) if a=='often'))
print(v[:20])
```

```
[',', '.', 'accomplished', 'analytically', 'appear', 'apt', 'associated', 'assuming', 'became', 'become', 'been', 'began', 'call', 'called', 'carefully', 'chose', 'classified', 'colorful', 'composed', 'contain']
```

> tabulate 메서드로 자주 나오는 품사들 조회하기

```python
brown_lrnd_tagged= brown.tagged_words(categories='learned', tagset='universal')
tags= [b[1] for (a,b) in nltk.bigrams(brown_lrnd_tagged) if a[0]=='often']
fd= nltk.FreqDist(tags)
fd.tabulate()
```

```
VERB  ADV  ADP  ADJ    .  PRT 
  37    8    7    6    4    2 
```

> Verb to Verb형태로 사용된 사례 10개 확인하기

```python
from nltk.corpus import brown
def process(sentence):
    for (w1,t1),(w2,t2),(w3,t3) in nltk.trigrams(sentence):
        if (t1.startswith('V') and t2=='TO' and t3.startswith('V')):
            print(w1,w2,w3)
            return True
    return False

i=0
for tagged_sent in brown.tagged_sents():
    r=process(tagged_sent)
    if i>10: break
    if r: i+=1
```

```
combined to achieve
continue to place
serve to protect
wanted to wait
allowed to place
expected to become
expected to approve
expected to make
intends to make
seek to set
like to see
```

#### 3개 이상의 품사로 사용된 단어 10개 조회하기

```python
brown_news_tagged= brown.tagged_words(categories= 'news', tagset='universal')
data= nltk.ConditionalFreqDist((word.lower(), tag)
                               for (word, tag) in brown_news_tagged)
i=0
for word in sorted(data.conditions()):
    if len(data[word]) >=3:
        tags= [tag for (tag, _) in data[word].most_common()]
        print(word, ' '.join(tags))
        i+=1
        if i>=10: break
```

```
a DET NOUN X
about ADP ADV PRT
above ADP ADJ ADV
advance VERB NOUN ADJ
back ADV NOUN VERB
best ADJ ADV VERB NOUN
better ADJ ADV VERB
close ADV ADJ VERB NOUN
down PRT ADP NOUN
even ADV ADJ VERB
```

## N-gram tagging

#### Unigram Tagger를 이용하여 품사 태깅 후 시험 데이터를 이용하여 결과 평가하기

```python
from nltk.corpus import brown
brown_tagged_sents= brown.tagged_sents(categories='news')
brown_sents= brown.sents(categories='news')
unigram_tagger= nltk.UnigramTagger(brown_tagged_sents)
print(unigram_tagger.tag(brown_sents[2007]))
```

```
[('Various', 'JJ'), ('of', 'IN'), ('the', 'AT'), ('apartments', 'NNS'), ('are', 'BER'), ('of', 'IN'), ('the', 'AT'), ('terrace', 'NN'), ('type', 'NN'), (',', ','), ('being', 'BEG'), ('on', 'IN'), ('the', 'AT'), ('ground', 'NN'), ('floor', 'NN'), ('so', 'QL'), ('that', 'CS'), ('entrance', 'NN'), ('is', 'BEZ'), ('direct', 'JJ'), ('.', '.')]
```

> 학습용 데이터로 평가한 결과

```python
unigram_tagger.evaluate(brown_tagged_sents)
```

```
0.9349006503968017
```

> 시험용 데이터로 평가한 결과

```python
size= int(len(brown_tagged_sents) * 0.9)

train_sents= brown_tagged_sents[:size]
test_sents= brown_tagged_sents[size:]
unigram_tagger= nltk.UnigramTagger(train_sents)
unigram_tagger.evaluate(test_sents)
```

```
0.8121200039868434
```

#### Bigram Tagger를 이용하여 품사 태깅 후 시험 데이터를 이용하여 결과 평가하기

```python
bigram_tagger= nltk.BigramTagger(train_sents)
bigram_tagger.tag(brown_sents[2007])
unseen_sent= brown_sents[4203]
print(bigram_tagger.tag(unseen_sent))
```

```
[('The', 'AT'), ('population', 'NN'), ('of', 'IN'), ('the', 'AT'), ('Congo', 'NP'), ('is', 'BEZ'), ('13.5', None), ('million', None), (',', None), ('divided', None), ('into', None), ('at', None), ('least', None), ('seven', None), ('major', None), ('``', None), ('culture', None), ('clusters', None), ("''", None), ('and', None), ('innumerable', None), ('tribes', None), ('speaking', None), ('400', None), ('separate', None), ('dialects', None), ('.', None)]
```

```python
bigram_tagger.evaluate(test_sents)
```

```
0.10206319146815508
```

Sparse problem으로 인해 accuracy가 낮다.

#### Backoff Tagger

> Bigram tagging을 시도하고 해당 시퀀스에 대한 확률이 0이라면 한 차원 낮은 n-gram tagging을 시도한다.

```python
t0= nltk.DefaultTagger('NN')
t1= nltk.UnigramTagger(train_sents, backoff= t0)
t2= nltk.BigramTagger(train_sents, backoff=t1)
t2.evaluate(test_sents)
```

```
0.8452108043456593
```

t2의 확률이 0이라면 t1 tagging을 적용하고, 이 확률도 0이라면 t0를 적용한다. 이 때 default tagger의 형태는 명사(NN)로 적용하였다.



> Trigram tagging을 시도하고, 확률이 0인 경우 Bigram tagging, Unigram tagging, default tagging을 시도한다.

```python
t0= nltk.DefaultTagger('NN')
t1= nltk.UnigramTagger(train_sents, backoff= t0)
t2= nltk.BigramTagger(train_sents, backoff=t1)
t3= nltk.TrigramTagger(train_sents, backoff=t2)
t3.evaluate(test_sents)
```

```
0.843317053722715
```

#### HMM Tagger

> Hidden Markov Model로 학습한다.

```python
from nltk.tag import hmm
trainer= hmm.HiddenMarkovModelTrainer()
hmm_tagger= trainer.train_supervised(train_sents)
hmm_tagger.evaluate(test_sents)
```

```
0.3166550383733679
```

#### Unknown Words Tagging

> Tagger가 학습 데이터에서 경험하지 못한 단어를 보면 어떻게 태깅해야 하는가?

```python
text= "I go to school in the morning"
token= text.split()
print(unigram_tagger.tag(token))
print(bigram_tagger.tag(token))
print(nltk.pos_tag(token))
```

```
[('I', 'PPSS'), ('go', 'VB'), ('to', 'TO'), ('school', 'NN'), ('in', 'IN'), ('the', 'AT'), ('morning', 'NN')] # unigram tagger
[('I', 'PPSS'), ('go', 'VB'), ('to', 'TO'), ('school', None), ('in', None), ('the', None), ('morning', None)] # bigram tagger
[('I', 'PRP'), ('go', 'VBP'), ('to', 'TO'), ('school', 'NN'), ('in', 'IN'), ('the', 'DT'), ('morning', 'NN')] # pos_tag(token)의 결과
```

pos_tag함수는 많은 corpus를 학습시켜 놓은 것으로, None이 많이 등장할 때 사용할 수 있다.

```python
text= "I go to school in the klaldkf"
token= text.split()
print(unigram_tagger.tag(token))
print(bigram_tagger.tag(token))
print(nltk.pos_tag(token))
```

```
[('I', 'PPSS'), ('go', 'VB'), ('to', 'TO'), ('school', 'NN'), ('in', 'IN'), ('the', 'AT'), ('klaldkf', None)] # unigram tagger
[('I', 'PPSS'), ('go', 'VB'), ('to', 'TO'), ('school', None), ('in', None), ('the', None), ('klaldkf', None)] # bigram tagger
[('I', 'PRP'), ('go', 'VBP'), ('to', 'TO'), ('school', 'NN'), ('in', 'IN'), ('the', 'DT'), ('klaldkf', 'NN')] # pos_tag
```

* Unigram Tagger는 unknown word에만 영향을 미침.
* Bigram Tagger는 unknown word가 다른 단어에도 영향을 미침. 따라서 None이 대다수 등장하게 됨
* pos_tag()를 사용한 사전 학습은 klaldkf를 명사로 태깅하고 있음.

#### N-gram tagging Confusion Matrix

> N-gram tagging의 학습 결과를 Confusion Matrix로 그린다.

```python
test_tags= [tag for sent in brown.sents(categories= 'editorial')
            for (word, tag) in t2.tag(sent)]
gold_tags= [tag for (word, tag) in brown.tagged_words(categories= 'editorial')]
cm= nltk.ConfusionMatrix(gold_tags, test_tags)
cm['NN','NN']
```

```
7317
```

```python
print(cm.pretty_format(truncate=10, sort_by_count= True))
```

```
    |                             N                     |
    |    N    I    A    J         N         V    N    C |
    |    N    N    T    J    .    S    ,    B    P    C |
----+---------------------------------------------------+
 NN |<7317>   1    .   98    .    4    .  137    1    . |
 IN |   30<5538>   .    .    .    1    .    .    .    9 |
 AT |    .    .<5299>   .    .    .    .    .    .    . |
 JJ | 1015    .    .<2475>   .    .    .    7   21    . |
  . |    .    .    .    .<2976>   .    .    .    .    . |
NNS |  901    .    .    .    .<2019>   .    .    1    . |
  , |    .    .    .    .    .    .<2735>   .    .    . |
 VB |  583    .    .   22    .    .    .<1486>   .    . |
 NP |  623    .    .   17    .    .    .    .<1161>   . |
 CC |    1    2    .    .    .    .    .    .    .<1818>|
----+---------------------------------------------------+
(row = reference; col = test)
```



