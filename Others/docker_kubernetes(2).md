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