# Apache Kafka의 주요 요소들
## Topic
**Kafka 안에서 메시지가 저장되는 장소의 논리적인 표현**


## Producer
**메시지를 생산(Produce)해서 Kafka의 Topic으로 메시지를 보내는 애플리케이션**


## Consumer Group
**Topic의 메시지를 사용하기 위해 협력하는 Consumer들의 집합**


## Commit Log
- 추가만 가능하고 변경 불가능한 데이터 스트럭쳐
- 데이터는 항상 로그 끝에 추가되고 변경되지 않음


## Offset
**Commit Log에서 Event의 위치**

## Topic
Kafka 안에서 메시지가 저장되는 장소를 논리적으로 표현한 것

## Partition
- Commit Log, 하나의 Topic은 하나 이상의 Partition으로 구성
- 병렬 처리를 위해서는 다수의 Partition을 사용

## Segment
- 메시지가 저장되는 실제 물리 File
- Segment File이 지정된 크기보다 크거나 지정된 기간보다 오래되면 새 파일이 열리고 메시지는 새 파일에 추가됨
  
## 