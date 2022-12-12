# Markdown 문서 기초


\# 글제목

\## 2번재 큰 제목

\### 3번째 큰 제목

\#### 4번째 큰 제목

\##### 5번째 큰제목 

\###### 6번째 큰제목

## 리스트

### 순서가 있는 리스트 (ordered list)

1. 손 씻기
   1. 또먹기
   2. 또 또 먹기   


2. 밥 먹기
   1. 밥 먹어
3. 식판 반납
4. 계산 
5. 양치

### 순서가 없는 리스트(unodered list)
* 짜장면
* 돈까스
* 김밥
* 라면
  * 먹고 싶다
  * 끓여 먹기
    * 더 먹기
      * 더욱더 먹기
        1. 물넣기
        2. 끓이기

## 인라인 강조
- 중요한 것은 굵게 표시하고, \** Bold \** examples) **Bold**

- 주의할 것은 기울이고, \*(esterlink) Italic \* examples)  *Italic*

- 코드 혹은 명령어는 따로 표시하고 싶다. \`(backtick) Codes \` 감싸면된다 
- 코드 여러줄을 입력하고 싶으면 \``` (script language) 
  
  Codes 
  
  \```

examples
```java
import System.out.*;
 package examples;

public class Car{
    Car()
    {
        System.out.println("car");
    }
}
public class ElectronicCar extends Car{

    ElectronicCar()
    {
        System.out.println("This is Electronic Car");
    }
}
public class Example {

	public static void main(String[] args) {
	
        String arg[0];
        arg[0]=args[0];

		int x = 10;
		int y = 20;
		int a = 123;
		char b = 'A';
		String c = "Code"; 
        System.out.println("test"+ args[0]);
    }
}

```
---
## 블록 강조

### 표
파이프(|)로 구분하여 테이블 헤더를 생선한다.

|명령어|설명|예시|
|-|-|-|
|`$`| 터미널에 명령어 입력 받을 준비가 됨 | |
|`mkdir`|디렉토리를 생성한다|`$ mkdir <name>` |
|`touch`|파일을 생성한다|`$ touch <name>` |
|`rm`|파일을 삭제한다|`$ rm <name>` |
|`rm -r`|파일과 디렉토리를 삭제한다|`$ rm <name>` |
|`ls`|현재 디렉토리의 파일과 하위 디렉토리를 표시한다|`$ ls` |
|`cd`|디렉토리의 위치를 변경한다 |`$ cd <directory location>`
|`ctrl + l`| 터미널 내용을 지운다 clear 핫키||
|`ctrl + c`| 명령어 수행을 강제 종료 핫키 ||
|`~`|home directory |`$ ls ~`|
|`/`| 루트 디렉토리|`$ ls /`|
|`.`| 현재 디렉토리|`$ ls .`|
|`..`| 현재 디렉토리의 상위 디렉토리 |`$ ls ..`|


### 코드

```c++

#include <iostream>

int main()
{
    std::out<<"테스트"<<"중"<<std::endl;
}
```

```c
#include <stdio.h>
int main()
{
    printf("나중에 만나");
}
```

## 기타

### 인용문
> reference

### 수식 블럭
-인라인 수식 \$ 내용 \$

$E(x-\mu)^2= E(x^2)-\mu^2$

$E(x^2)=\sigma^2-\mu^2$

$N(\mu,\sigma^2) =\sqrt2\pi$

$\sigma^2=E(x-\mu)^2$

$\Gamma$

### 이미지 / 하이퍼링크
하이퍼링크 : \[표시 텍스트](링크)

examplse : [구글](https://google.com)

이미지 : \![img]\(링크)

examples : ![img]()


