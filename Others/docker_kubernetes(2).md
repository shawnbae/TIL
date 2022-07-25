# minikube 설치 및 쿠버네티스 클러스터 구성
## minikube 구동하기
```bash
$minikube start --driver docker
$cat ~/.kube/config # minikube cluster 보기
$minikube status # 상태 보기
$kubectl cluster-info # 클러스터 확인
```

# docker 구성요소
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

### 컨테이너 종료
    - 컨테이너 안전 종료(SIGTERM 시그널 전달)
      $docker stop [container]
    - 컨테이너 강제 종료(SIGKILL 시그널 전달)
      $docker kill [container]
    - 모든 컨테이너 종료
      $docker stop $(docker ps -a -q) # docker ps -a -q는 모든 컨테이너 지칭, 이를 변수화하여 삭제

### 컨테이너 삭제
    - 컨테이너 삭제 (실행중인 컨테이너 불가)
      $docker rm [container]
    - 컨테이너 강제 종료 후 삭제 (SIGKILL 시그널 전달)
      $docker rm -f [container]
    - 컨테이너 실행 종료 후 자동 삭제
      $docker run --rm
    - 중지된 모든 컨테이너 삭제
      $docker container prune

# 도커를 이용한 컨테이너 관리
## 엔트리포인트 및 커맨드
    - 엔트리포인트
      - 도커 컨테이너가 실행할 때 고정적으로 실행되는 스크립트 혹은 명령어
      - 생락할 수 있으며, 생략될 경우 커맨드에 지정된 명령어로 수행
    - 커맨드
      - 도커 컨테이너가 실행할 때 수행할 명령어 혹은 엔트리포인트에 지정된 명령어에 대한 인자 값

## 환경변수 다루기
    - docker 실행 시 -e에 환경변수를 옵션으로 지정할 수 있음
      $docker run -i -t -e MY_HOST=test.com ubuntu:focal bash
    - docker 실행 시 --env-file에 환경변수 파일을 옵션으로 지정할 수 있음
      $docker run -i -t --env-file ./sample.env ubuntu:focal env

## 명령어 실행
    - docker exec [container] [command]
    - issue 발생 시 실행 중인 컨테이너의 이슈를 해결하기 위한 용도로 사용
      $docker exec -i -t my-nginx bash # my-nginx 컨테이너에 Bash 셸로 접속하기
      $docker exec my-nginx env # my-nginx 컨테이너에 환경변수 확인하기

## 도커의 네트워크
    - 도커 엔진에 의해 기본 생성되는 docker0를 통해 네트워크를 브릿징한다.
    - 컨테이너 포트를 호스트의 IP:PORT와 연결하여 서비스를 노출하는 방법
    $docker run -p [HOST IP:PORT] : [CONTAINER PORT] [container]
    $docker run -d -p 80:80 nginx # nginx컨테이너의 80번 포트를 호스트 모든 IP의 80번 포트와 연결하여 실행
    $docker run -d -p 127.0.0.1:80:80 nginx # nginx 컨테이너의 80번 포트를 호스트 127.0.0.1 IP의 80번 포트와 연결하여 실행
    $docker run -d -p 80 nginx # nginx 컨테이너의 80번 포트를 호스트의 사용 가능한 포트와 연결하여 실행
    - expose: 실제로 연결하지 않고 별다른 기능 없이 문서화만 함 (주석)
    - publish: 살재 포트를 바인딩
    $docker run -d --expose 80 nginx # nginx # expose 옵션은 그저 문서화 용도로 사용
    $docker run -d -p 80 nginx # publish 옵션은 실제 포트를 바인딩

    - Native하게 지원되는 네트워크 드라이버: Bridge, Host, None, Overlay 등
    - Remote Driver: 다양한 Plugin들을 설치해서 사용하는 방법

    - Single Host Networking: bridge, host, none
      - 단일 호스트로 네트워크를 호스팅할 때 사용함
    - Multi Host Networking: overlay
      - 여러 서버들이 존재할 때 그 서버들을 연결시키는 가상의 네트워크
      - 멀티호스트로 작동하므로 orchestration 시스템에 많이 쓰임 (docker swarm 많이 사용)
    $docker network ls # 연결된 네트워크들의 목록을 보여줌
