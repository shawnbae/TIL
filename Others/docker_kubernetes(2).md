# minikube 설치 및 쿠버네티스 클러스터 구성하기
## minikube 구동하기
```bash
$minikube start --driver docker
$cat ~/.kube/config # minikube cluster 보기
$minikube status # 상태 보기
$kubectl cluster-info # 클러스터 확인
```

## docker 구성요소
    - Client
      - docker build, docker pull, docker run을 시행하는 주체
    - DOCKER_HOST
      - Docker daemon, containers, images를 관리하는 주체
      - 이미지는 직접 build를 통해 만들 수도 있지만, pull을 통해 가져올 수도 있다    
    - Registry
      - Dokcer의 이미지 저장소

## docker image & container
    - 이미지와 컨테이너는 도커에서 사용하는 기본적인 단위
    - 이미지와 컨테이너는 1:N 관계를 가짐
    - 이미지
      - 컨테이너를 생성할 때 필요한 요소로 컨테이너의 목적에 맞는 바이너리와 의존성이 설치되어 있음
      - 여러 개의 계층으로 된 바이너리 파일로 존재함
    - 컨테이너
      - 호스트와 다른 컨테이너로부터 격리된 시스템 자원과 네트워크를 사용하는 프로세스
      - 이미지는 읽기 전용으로 사용하여 변경사항은 컨테이너 계층에 저장
      - 컨테이너에서 무엇을 하든 이미지는 영향을 받지 않음

    - Dockerfile을 통해 BUILD --> Docker Image 생성 --> RUN --> Docker Container생성

    - 도커 이미지 이름 구성
      - 저장소 이름 / 이미지 이름 / 이미지 태그
        - repository/nginx:1.21 # 3개가 모두 들어간 형태
        - nginx # 이미지 이름만 들어간 형태, 도커허브의 최신 버전을 default로 함

    - 도커 이미지 저장소
      - 도커 이미지를 관리하고 공유하기 위한 서버 어플리케이션
        - dockerhub가 가장 대표적인 private 저장소
        - 사내에서는 AWS ECR을 팀 내의 image를 private하게 관리
  
## docker container 라이프사이클
    - 도커 실행 방법 2가지
      - 1. run
      - 2. create -> start
    - 도커 중지
      - pause
    - 컨테이너 삭제
      - rm

## docker 명령어
### 컨테이너 시작
    - 컨테이너 생성
      $docker create [image]
    - 컨테이너 시작
      $docker start [container]
    - 컨테이너 생성 및 시작
      $docker run [image]
    - 주요 옵션
      $ docker run \
      -i # 호스트의 표준 입력을 컨테이너와 연결
      -t # TTY 할당
      --rm # 컨테이너 실행 종료 후 자동 삭제
      -d # 백그라운드 모드로 실행 (빈도 높음)
      --name hello-world # 컨테이너 이름 지정
      -p 80:80 # 호스트-컨테이너 간 포트 바인딩
      -v /opt/example:/example # 호스트-컨테이너 간 볼륨 바인딩
      # 실행할 이미지
      # 컨테이너 내에서 실행할 명령어

### docker 컨테이너 상태 확인
    - 실행 중인 컨테이너 상태 확인
      $docker ps
    - 전체 컨테이너 상태 확인
      $docker ps -a
    - 컨테이너 상세 정보 확인
      $docker inspect [container]

### 컨테이너 일시중지 및 재개
    - 컨테이너 일시중지
      $docker pause [container]
    - 컨테이너 재개
      $docker unpause [container]