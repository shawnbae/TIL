# Git collaboration

> Git으로 협업하는 방법



## 개요

Git은 분산형 버전 관리 시스템으로, 개인 코드 및 파일들을 저장하기 위한 저장소 역할로도 사용할 수 있지만 버전 관리 시스템인 만큼 협업에 사용할 수 있다.

예를 들어 A와 B가 같은 코드 파일에 대해 작업한다고 가정하면, 어떤 부분을 수정했는지 그리고 어떤 부분이 겹치는지 등 일일히 파일을 수정하고 공유하는 과정은 굉장히 피곤할 것이다. 그나마 같은 코드 파일이라면 괜찮겠지만,  프로젝트 단위로 팀원들 모두 파일에 대한 수정 내역을 따로 관리하게 되는 것은 굉장히 비합리적인 일이다.

따라서 분산형 버전 관리 시스템을 협업에 이용한다는 것은 많은 사람들의 피로를 덜어주는 일이다.



## 과정

### 1. 공동 repository에 대해 각자의 branch 만들기

모든 사람들이 하나의 작업을 공유한다는 점에서 편리한 일일 수도 있겠으나 업무 분담이 되지 않는다면 그 또한 피곤할 일일 것이다. 즉, master라는 하나의 branch에서 모두가 작업하는 것이 아닌 각자의 branch에서 작업을 분담한 후 master라는 브랜치로 합치는 과정을 따로 수행하는 것이 합리적이다.



> 업무 / 수행하는 사람에 따라 브랜치를 생성한다.

```bash
# shawn이라는 브랜치 생성하기
$ git branch shawn
```



> 로컬에서 작업한 후, 생성한 branch로 git의 위치를 옮긴다.

```bash
# checkout이라는 함수는 branch를 옮기는 명령어이다.
$ git checkout shawn
```

```
@LAPTOP-53VM1A0B MINGW64 ~/bigcontest (master)
$ git checkout shawn
Switched to branch 'shawn'
M       EDA/20200820_EDA_SH.ipynb

@LAPTOP-53VM1A0B MINGW64 ~/bigcontest (shawn)
```

shawn이라는 브랜치로 작업 공간을 옮겼다. (master)가 (shawn)으로 바뀌었음을 볼 수 있다.



### 2. 로컬에서 작업한 내용을 branch로 푸쉬하기

내 로컬에서 작업한 내용을 나의 브랜치로 옮긴다. 과정은 로컬에서 저장소로 옮기는 과정과 똑같다. 다만 `git push origin master`가 아닌 `git push origin shawn(branch 이름)`

```bash
# add
$ git add .

# commit
$ git commit -m "message"

# push to branch
$ git push origin shawn
```

```
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 1.16 KiB | 237.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/~
   04de5d8..e14a856  shawn -> shawn
```



### 3. master로 checkout 후 merge하기

master 브랜치로 위치를 옮겨 내가 작업한 내역을 merge한다.

```bash
# master브랜치로 위치 옮기기
$ git checkout master

# master위치에서 sub-branch 병합하기
$ git merge shawn
```

```
Merge made by the 'recursive' strategy.
 EDA/20200812_EDA_SH.ipynb |  529 +----
 EDA/20200817_EDA_JM.ipynb |   72 +-
 EDA/20200820_EDA_SH.ipynb | 5407 +++++++++++++++++++++++++++++++++++++++++++++
 3 files changed, 5518 insertions(+), 490 deletions(-)
 create mode 100644 EDA/20200820_EDA_SH.ipynb
```

병합이 완료되었음을 알 수 있다.



### 4. pull-request 요청하기

branch를 merge 하기는 했지만, 멋대로 작업한 branch 내용을 master에 병합한다면 모두가 피해를 볼 것이다. 따라서 권한을 가진 master가 branch 내용이 master를 바꾸게 하는 과정이 필요하다.

github의 merge된 branch에 pull-request를 요청한다. 모두가 권한이 같다면 승인을 자신이 내리면 되지만, 그렇지 않은 경우 권한이 있는 사람이 merge를 confirm하면 된다.





