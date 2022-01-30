# 파이프라인이란?
> 컴퓨터과학에서 파이프라인은 한 데이터 처리 단계의 출력이 다음 단계의 입력으로 이어지는 형태로 연결된 구조를 가리킨다.

# Data Pipeline Architecture
> 데이터 생성 -> 수집 -> 전처리 및 저장 -> 분석 및 시각화
- 데이터 생성 단계
    - User들을 통해 데이터가 수집됨

- 수집 단계
    - Stream을 사용하는 이유 중 하나로, 이용자가 App을 Navigation할 때 느려짐을 방지한다는 점을 꼽을 수 있다.
    - RDBMS의 경우 많은 Traffic이 제공되면 리소스가 한정되어있기 때문에 저장이 안되면 속도가 느려지는 문제가 발생한다.
    - Amazon Kinesis Streams: Queue 서비스, 흘러가는 데이터를 처리. 우리가 원하는 데이터를 Window 사이즈로 캡쳐하여 저장하는 방식. RDMS와 다르게 Stream 서비스를 모두 받아들이므로 Traffic으로 인한 속도 저하가 없다.
    - Amazon Kinesis Firehose: Queue에 있는 데이터를 S3에 코딩 없이 저장할 수 있도록 지원하는 서비스
    - Amazon API Gateway: 외부에서 발생하는 Event를 AWS와 연결하는 API, 마이크로서비스(서로 간에 영향을 주지 않는 서비스)의 근간
    - Lambda function: Event-Driven

- 전처리 및 저장
    - DB 서비스에 AWS Glue, Amazon S3등이 있음
    - AWS Glue: 데이터가 어느 위치에 있고, 버전 정보 및 Catalog등의 관리 제공
    - Amazon EMR: 전처리 및 저장, Hadoop Ecosystem을 가지고 있는 환경. Hadoop 구성을 Setup해주는 컴퓨팅 요소.

- 분석 및 시각화 관련 Tools
    - Amazon Athena: Ad-hoc 데이터 분석 제공
    - 현업 담당자들을 위한 Visualization Tools
        - Apache Zeppelin
        - tableau
        - Periscope Data
        - Superset

# Data Pipeline 구성 방안
- 회사 내의 데이터적 요구사항(Use Case)에 대한 빠른 대응
- 지속적이고 에러가 없어야 한다.
- 시스템적으로 발생하는 문제에 대해서 유연한 Scability 해야한다.
- Scale up과 Scale Out이 자유로워야 한다.
    - 리소스 문제로 인해 부하가 생길 때 리소소를 조정할 수 있어야 한다는 의미
    - 여러 Node(서버)를 운영하다가 5대로 축소시키는 등
- 이벤트성 데이터 부하에도 처리가 가능해야 한다. (마케팅 이벤트, 푸시 발송, 서비스 오픈)
    - 가장 issue가 많이 생기는 항목
    - 많은 Event의 부하를 유연하게 처리할 수 있어야 함.
- 데이터 쌓이는 공간에 문제가 없어야 한다.
    - RDMS를 쓰는 등 온프레미스 환경에서 DB서버를 운영하는 경우 백업정책들을 마련하고 리소스를 분배해야 한다.
- 수집데이터(저장데이터)의 유연성
- 쉬운 분석데이터 Format
    - 수집할 때 변경이 다수 발생하므로 초기에 설정해야 하는데, json이 가장 좋음.

# Data Lambda Architecture
> Raw Data Store -> Batch-Processing Engine / Real-Time Processing Engine -> Serving Data Store
- AWS S3 Data Lake는 위 Process를 모두 지원한다.

- Raw Data Store
    - Amazon API Gateway
    - Amazon Kinesis Streams
    - Amazon Kinesis Firehose
    - Amazon Pinpoint: CRM 서비스, Real-Real-Time 마케팅 Toolkit

- Batch-Processing Engine
    - Spark: AWS EMR이 지원
    - AWS DMS: 운영계에 부담을 적게 주면서 마스터 데이터를 가져올 수 있다.

- Real-Time Processing Engine
    - Spark Streaming
    - Amazon Kinesis Analytics

- Serving Data Store
    - Amazon ES: 엘라스틱서치, 데이터량이 지속적으로 많아지는 서비스에는 적합하지 않음
    - Amazon DynamoDB: NoSQL
    - Amazon RDS: MySQL 등의 DBMS
    - Amazon Redshift: Column Base 분석 툴
    - presto: EMR서비스 안에 존재.

- Analytical Sandboxes
    - Amazon SageMaker: Data Discovery, Predictive Modeling