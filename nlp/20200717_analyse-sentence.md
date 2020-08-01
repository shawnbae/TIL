# 문장 구조 분석

## 문장의 중의성

> 동사 shot의 의미에 따라 두 가지 형태의 문장 구조가 존재한다.

```python
import nltk

groucho_grammar= nltk.CFG.fromstring(
    """
    S -> NP VP
    PP -> P NP
    NP -> Det N | Det N PP | 'I'
    VP -> V NP | VP PP
    Det -> 'an' | 'my'
    N -> 'elephant'|'pajamas'
    V -> 'shot'
    P -> 'in'
    """)

sent= ['I','shot','an','elephant','in','my','pajamas']
parser= nltk.ChartParser(groucho_grammar)
for tree in parser.parse(sent):
    print(tree)
```

```
(S
  (NP I)
  (VP
    (VP (V shot) (NP (Det an) (N elephant)))
    (PP (P in) (NP (Det my) (N pajamas)))))
(S
  (NP I)
  (VP
    (V shot)
    (NP (Det an) (N elephant) (PP (P in) (NP (Det my) (N pajamas))))))
```

이 때 CFG는 context free grammar 즉 문맥 자유 문법을 의미한다. groucho_grammar에서 규칙을 정의한 것이다.



- word-salad: 문법적으로는 완전히 맞으나 아무 의미도 없는 문장

## 구성성분 구조 (Constituent structure)

중의성을 가진 문장

The man saw the dog with a telescope.

- The man saw [the dog with a telescope]
- The man saw [the dog] [with a telescope]

와 같이, 한 단위의 구성성분(constituent)에 따라 달라질 수 있다.

묶인 부분이 구성성분이 되는지의 여부는 대명사(substitution)로 바꾸어보는 방법이 있다.



## 형식 언어 이론 (Formal Language Theory)

형식적으로 언어란 유한개의 철자로 무한개의 단어와 문장을 조합한 것이므로, 무한한 언어를 유한하게 서술할 수 있도록 언어를 형식화함으로써 인공 언어로 변환할 수 있다.



### 촘스키의 계층 구조(Chomsky Hierarchy)

내용에 관계 없이 문장의 형태가 구성되는 과정만으로 문장을 설명했다. 촘스키의 형식 언어는 오토마타 이론과 결합하여 인공언어 처리에 큰 역할을 하였다.

촘스키의 계층 구조는 4단계로 이루어져있다.

- Unrestricted Languages(Grammar): 제약되지 않은 인간의 언어. NLP의 영역이 아닌 유일한 계층이다.
- Context-sensitive Languages(Grammar): 정제되지 않은 언어에 개수 제한을 두어 문장의 맥락까지 고려한 계층이다.
- Context-free Languages(Grammar): 단어들의 의미는 고려하되 주변 맥락까지는 고려하지 않은 형태의 계층이다. PDA(Push down Automata)에 의해 판별된다.
- Regular Languages(Grammar): 제한된 알파벳에 따라 철저히 정제된 형태의 계층이다. FSA(Finite state Automata)에 의해 판별된다.



#### 유한 상태 인식기(FSA) 예시

```python
init_state= 0
final_state= [1]
trap_state= 2
delta= {0: {'a':0, 'b':1},
       1: {'a':2, 'b':1}}

def FSA(string):
    state= init_state
    for s in string:
        state= delta[state][s]
        if state == trap_state:
            break
    return state in final_state

print(FSA('aabbb'))
print(FSA('aabba'))
```

```
True
False
```



### 문맥 자유 문법 parsing 예시들

```python
import nltk

grammar1= nltk.CFG.fromstring(
    """
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V | V NP | V NP PP
    PP -> P NP
    Det -> "the" | "a"
    N -> "man" | "park" | "dog" | "telescope"
    V -> "saw" | "walked"
    P -> "in" | "with"
    """)

sent= " the dog saw a man in the park".split()
rd_parser= nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
    print(tree)
```

```
(S
  (NP (Det the) (N dog))
  (VP
    (V saw)
    (NP (Det a) (N man) (PP (P in) (NP (Det the) (N park))))))
(S
  (NP (Det the) (N dog))
  (VP
    (V saw)
    (NP (Det a) (N man))
    (PP (P in) (NP (Det the) (N park)))))
```



```python
grammar2= nltk.CFG.fromstring(
    """
    S -> NP VP
    NP -> Det Nom | PropN
    Nom -> Adj Nom | N
    VP -> V Adj | V NP | V S | V NP PP
    PP -> P NP
    PropN -> 'Buster' | 'Chatterer' | 'Joe'
    Det -> 'the' | 'a'
    N -> 'bear' | 'squirrel' | 'tree' | 'fish' | 'log'
    Adj -> 'angry' | 'frightened' | 'little' | 'tall'
    V -> 'chased' | 'saw' | 'said' | 'thought' | 'was' | 'put'
    P -> 'on'
    """)
    
sent2= "the angry bear chased the frightened little squirrel".split()
rd_parser= nltk.RecursiveDescentParser(grammar2)
for tree in rd_parser.parse(sent2):
    print(tree)
```

```
(S
  (NP (Det the) (Nom (Adj angry) (Nom (N bear))))
  (VP
    (V chased)
    (NP
      (Det the)
      (Nom (Adj frightened) (Nom (Adj little) (Nom (N squirrel)))))))
```



```python
grammar3= nltk.CFG.fromstring(
    """
    S -> NP VP
    VP -> V NP | V NP PP
    PP -> P NP
    V -> "saw" | "ate" | "walked"
    NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
    Det -> "a" | "an" | "the" | "my"
    N -> "man" | "dog" | "cat" | "telescope" | "park"
    P -> "in" | "on" | "by" | "with"
    """)

rd_parser= nltk.RecursiveDescentParser(grammar3)
sent4= 'Mary saw a dog'.split()
for tree in rd_parser.parse(sent4):
    print(tree)
```

```
(S (NP Mary) (VP (V saw) (NP (Det a) (N dog))))
```

위는 대표적인 parsing 방법 중 하나인 Recursive Descent Parsing이다.



```python
sr_parser= nltk.ShiftReduceParser(grammar3)
for treee in sr_parser.parse(sent4):
    print(tree)
```

```
(S (NP Mary) (VP (V saw) (NP (Det a) (N dog))))
```

위는 대표적인 parsing 방법 중 하나인 Shift Reduce Parsing이다.



## 구성 성분의 종속성

문장에서 단어들의 연관 관계 (종속 관계)를 분석한다.



```python
groucho_dep_grammar= nltk.DependencyGrammar.fromstring(
    """
    'shot' -> 'I' | 'elephant' | 'in'
    'elephant' -> 'an' | 'in'
    'in' -> 'pajamas'
    'pajamas' -> 'my'
    """)
print(groucho_dep_grammar)
```

```
Dependency grammar with 7 productions
  'shot' -> 'I'
  'shot' -> 'elephant'
  'shot' -> 'in'
  'elephant' -> 'an'
  'elephant' -> 'in'
  'in' -> 'pajamas'
  'pajamas' -> 'my'
```

```python
pdp= nltk.ProjectiveDependencyParser(groucho_dep_grammar)
sent= 'I shot an elephant in my pajamas'.split()
trees= pdp.parse(sent)
for tree in trees:
    print(tree)
```

```
(shot I (elephant an (in (pajamas my))))
(shot I (elephant an) (in (pajamas my)))
```



> Penn Treebank Corpus

```python
import nltk
from nltk.corpus import treebank

t= treebank.parsed_sents('wsj_0001.mrg')[0]
print(t)
```

```
(S
  (NP-SBJ
    (NP (NNP Pierre) (NNP Vinken))
    (, ,)
    (ADJP (NP (CD 61) (NNS years)) (JJ old))
    (, ,))
  (VP
    (MD will)
    (VP
      (VB join)
      (NP (DT the) (NN board))
      (PP-CLR (IN as) (NP (DT a) (JJ nonexecutive) (NN director)))
      (NP-TMP (NNP Nov.) (CD 29))))
  (. .))
```

```python
print(treebank.parsed_sents())
```

```
[Tree('S', [Tree('NP-SBJ', [Tree('NP', [Tree('NNP', ['Pierre']), Tree('NNP', ['Vinken'])]), Tree(',', [',']), Tree('ADJP', [Tree('NP', [Tree('CD', ['61']), Tree('NNS', ['years'])]), Tree('JJ', ['old'])]), Tree(',', [','])]), Tree('VP', [Tree('MD', ['will']), Tree('VP', [Tree('VB', ['join']), Tree('NP', [Tree('DT', ['the']), Tree('NN', ['board'])]), Tree('PP-CLR', [Tree('IN', ['as']), Tree('NP', [Tree('DT', ['a']), Tree('JJ', ['nonexecutive']), Tree('NN', ['director'])])]), Tree('NP-TMP', [Tree('NNP', ['Nov.']), Tree('CD', ['29'])])])]), Tree('.', ['.'])]), Tree('S', [Tree('NP-SBJ', [Tree('NNP', ['Mr.']), Tree('NNP', ['Vinken'])]), Tree('VP', [Tree('VBZ', ['is']), Tree('NP-PRD', [Tree('NP', [Tree('NN', ['chairman'])]), Tree('PP', [Tree('IN', ['of']), Tree('NP', [Tree('NP', [Tree('NNP', ['Elsevier']), Tree('NNP', ['N.V.'])]), Tree(',', [',']), Tree('NP', [Tree('DT', ['the']), Tree('NNP', ['Dutch']), Tree('VBG', ['publishing']), Tree('NN', ['group'])])])])])]), Tree('.', ['.'])]), ...]
```

```python
def filter(tree):
    child_nodes= [child.label() for child in tree
                  if isinstance(child, nltk.Tree)]
    return (tree.label() == 'VP') and ('S' in child_nodes)

i=0
for tree in treebank.parsed_sents():
    for subtree in tree.subtrees(filter):
        print(list(subtree))
        
    i += 1
    if i > 10: break
```

```
[Tree('VBN', ['named']), Tree('S', [Tree('NP-SBJ', [Tree('-NONE-', ['*-1'])]), Tree('NP-PRD', [Tree('NP', [Tree('DT', ['a']), Tree('JJ', ['nonexecutive']), Tree('NN', ['director'])]), Tree('PP', [Tree('IN', ['of']), Tree('NP', [Tree('DT', ['this']), Tree('JJ', ['British']), Tree('JJ', ['industrial']), Tree('NN', ['conglomerate'])])])])])]
[Tree('VBD', ['said']), Tree(',', [',']), Tree('``', ['``']), Tree('S', [Tree('NP-SBJ', [Tree('DT', ['This'])]), Tree('VP', [Tree('VBZ', ['is']), Tree('NP-PRD', [Tree('DT', ['an']), Tree('JJ', ['old']), Tree('NN', ['story'])])])])]
```



```python
ruleset= set(rule for tree in
             nltk.corpus.treebank.parsed_sents()[:10]
             for rule in tree.productions())
rules= []
for rule in ruleset:
    rules.append(rule)

print(rules[:30])
```

```
[S -> NP-SBJ VP, NNS -> 'lungs', -NONE- -> '*-2', NP-SBJ -> -NONE-, NP-TMP -> NNP CD, CC -> 'and', SBAR -> -NONE- S, NNP -> 'Fields', NP-SBJ-1 -> NP , UCP ,, VP -> VBG NP PP-LOC-CLR PP-TMP, NP -> NN POS, PP-CLR -> IN NP, WHNP-2 -> WDT, NP -> NN NNS, NP -> PRP, NP-SBJ -> DT NNP NN, NP -> JJ NN, JJ -> 'questionable', VBZ -> 'enters', VBD -> 'heard', CD -> '29', NP -> RB JJ NNS, NP -> QP NNS, ADVP-TMP -> NP IN, NNP -> 'Pierre', NP -> DT NN, NNP -> 'Nov.', S-TPC-1 -> NP-SBJ VP, IN -> 'in', WHNP-1 -> WDT]
```



## 확률적 문맥 자유 문법

```python
grammar= nltk.PCFG.fromstring(
    """
    S    -> NP VP        [1.0]
    VP   -> TV NP        [0.4]
    VP   -> IV           [0.3]
    VP   -> DatV NP NP   [0.3]
    TV   -> 'saw'        [1.0]
    IV   -> 'ate'        [1.0]
    DatV -> 'gave'       [1.0]
    NP   -> 'telescopes' [0.8]
    NP   -> 'Jack'       [0.2]
    """)

print(grammar)
```

```
Grammar with 9 productions (start state = S)
    S -> NP VP [1.0]
    VP -> TV NP [0.4]
    VP -> IV [0.3]
    VP -> DatV NP NP [0.3]
    TV -> 'saw' [1.0]
    IV -> 'ate' [1.0]
    DatV -> 'gave' [1.0]
    NP -> 'telescopes' [0.8]
    NP -> 'Jack' [0.2]
```



> Viterbi 알고리즘으로 parsing한 결과

```python
viterbi_parser= nltk.ViterbiParser(grammar)
sent= "Jack saw telescopes".split()
for tree in viterbi_parser.parse(sent):
    print(tree)
```

```
(S (NP Jack) (VP (TV saw) (NP telescopes))) (p=0.064)
```

