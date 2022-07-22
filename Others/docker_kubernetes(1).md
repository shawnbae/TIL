# docker 사용하기

## docker란

container로, 서로 다른 os간의 충돌 / 버전 충돌 / 파일 손실 등 개발에 있어 직면할 수 있는 다양한 충돌 문제를 해결할 수 있는 방법이다.

.dockerfile에 이미지를 로드하여 해당 이미지 파일에서 정의된 os, runtime environment, application files, third-party libraries, environment variables 등을 제어한 환경에서 개발한다.

Git에 Github이 있는 것과 마찬가지로, docker는 dockerhub가 있으며 dockerhub에 정의된 image를 가져와 하나의 container로 정의하여 사용할 수 있다.

## docker/docker-compose/kubernetes download
```bash
# macOS에서 설치하는 경우
$brew install --cask docker
$brew install kubectl
$brew install kustomize
$brew install minikube
```

```bash
# Ubuntu에서 설치하는 경우
## install aws cli
set -euf -o pipefail

# Install dependencies
sudo apt-get install -y curl unzip

pushd /tmp

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

popd

## install docker
set -euf -o pipefail

DOCKER_USER=ubuntu

# Install dependencies
sudo apt-get update && sudo apt-get install -y \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg \
  lsb-release

# Add Docker’s official GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Set up the stable repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker CE
sudo apt-get update && sudo apt-get install -y docker-ce docker-ce-cli containerd.io

# Use Docker without root
sudo usermod -aG docker $DOCKER_USER

## install docker-compose
set -euf -o pipefail

DOCKER_COMPOSE_VERSION=v2.1.1

# Download and install
sudo curl -L "https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

## install kubectl
set -euf -o pipefail

# Install dependencies
sudo apt-get update && sudo apt-get install -y \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg \
  lsb-release

# Add kubectl's official GPG key
curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/kubernetes-archive-keyring.gpg

# Set up the repository
echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list

# Install kubectl
sudo apt-get update && sudo apt-get install -y kubectl

## install kustomize
set -euf -o pipefail

KUSTOMIZE_VERSION=v4.4.1

# Download kustomize binary
curl -s "https://raw.githubusercontent.com/kubernetes-sigs/kustomize/kustomize/${KUSTOMIZE_VERSION}/hack/install_kustomize.sh"  | bash

# Install to /usr/local/bin
sudo install -o root -g root -m 0755 kustomize /usr/local/bin/kustomize

## install minikube
set -euf -o pipefail

curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```
## docker process

1. docker image 생성하기

```bash
$docker pull *directory*
```

2. docker image 확인하기

```bash
$docker image ls
```

3. docker 실행하기

```bash
$docker run *directory*
```

## 기본 명령어들

- docker version check

```bash
$docker version
```

- Dockerfile 예시 (node.js를 기반으로 app을 실행시키는 예시)
- node:alpine의 app.js로 image가 생성됨

```Dockerfile
FROM node:alpine
COPY . /app
WORKDIR /app
CMD node app.js
```

- docker에게 애플리케이션을 패키징하도록 지시 (build)

```bash
$docker build -t hello-docker
```

- docker의 이미지 확인하기

```bash
$docker images
$docker image ls
```

- docker로 패키징된 앱을 컨테이너 위에서 실행하기

```bash
$docker run hello-docker
```

## docker의 다양한 명령어들 예시

- 이미지 가져오기(pull)

```bash
$docker pull mcr.microsoft.com/mssql/server:2017-latest
```

- 이미지 확인하기(images / image ls)

```bash
$docker images
```

- 컨테이너 확인하기(ps)

```bash
$docker ps
```

- 이미지 실행하기 (run)

```bash
$docker run --name mssqlserver -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=<your password>' -p 1433:1433 --platform linux/amd64 -d mcr.microsoft.com/mssql/server:2019-latest

```

- 이미지 삭제하기 (rmi)

```bash
$docker rmi mcr.microsoft.com/mssql/server:2017-latest
```