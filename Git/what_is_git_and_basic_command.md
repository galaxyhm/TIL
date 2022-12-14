# git 기초

VCS(Version control System)의 일종 중 하나



## 등장 배경

Git가 나오기 전에는 강력한 상용 소프트 BitKeeper VCS와 무료 소프트인 RCS, CVS와 같은 소프트웨어가 있었지만 BitKeeper VCS가 무료 버전의 제약을 강화했기 때문에 Git가 개발이 됨



## 주요 특성



### 분산 개발의 용이함

중앙에 있는 저장소만 있으면 많은 개발자가 동시에 동기화를 시도하면 서버에 부화가 많이 일어남 하지만 분산 서버나 오프라인 환경에서 개발을 할 수 있음

### 원자적 커밋(atomic commit)

커밋이 제대로 끝나기 전에 실패 한게 있으면 되돌려짐 DBMS의 트랜잭션이랑 비슷한 기능을 지원

### 분할 개발 지원 

개발라인 `branch`를 활용해 개발, 테스트를 동시에 하고 다시 합칠 수 있다.

### DBMS 와 같이 무결성 과 신뢰성을 유지 

Git 내에 데이터베이스가 존재하고 그 객체를 구별하기 위해서 SHA1 해시 함수 를 사용함 

### 책임성

누가 수정했는지, 어떤 파일을 수정했는지, 알 수 있어서 이유 없는 버전이 올라감을 표기 하지 않음



## git의 기초 명령어들



| 명령어          | 설명                                   | 예시                         |
| --------------- | -------------------------------------- | ---------------------------- |
| `git --version` | git의 버전확인                         | `$ git --version`            |
| `git init`      | 현재 디렉토리를  git repository로 만듬 | `$ git init`                 |
| `git add`       | 파일을 stage에 올림                    | `$ git add <filename>`       |
| `git commit`      | stage에 올라온 파일들을 커밋함 ,       | `$ git commit -m <message> ` |
| `git status`      | git의 현재상태를 표시함                | `$ git status`               |
| `git add .`       | 현재 디렉토리의 파일들을 stage에 올림  | `$ git add . `               |
|`git remote add`| 원격 디렉토리를 추가함|`$ git remote add <name> <location address>`
|`git pull` | 원격 디렉토리에서 가져옴|`$ git pull <location name> <branch>`  
|`git clone` |원격 디렉토리에서 그대로 갱신함 |`$ git clone <location name> `
|`git remote -v`|현재 원격 디렉토리를 표기|`git remote -v`

### Recommendations

1. 커밋은 짧지만 내용은 자세하게
2. README.md, .gitignore를 추가함



