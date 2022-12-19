# Python Data Model 

## Special Method 

문자열 길이를 구할려면 java의 경우 String 객체의 length() 메소드를
호출 해야된다
```java
        String s = "test ";
        int s_len = s.length();  //길이 구하기
```
하지만 python의 경우 
```python
s = "my test"
len(s)
```
함수 len()을 호출하면 된다

예를들어서 
```python
import collections

BsCard = collections.namedtuple('BsCard',['name', 'number'])

class BsDeck :
    names = "Choi Kwang Kang Jin".split()
    numbers ="5451 6781 9412 4432".split()
    
    def __init__(self) :
        self._bs_cards = [BsCard(name, number) for name, number in zip(self.names, self.numbers)]
    def __len__(self) : 
        return len(self._bs_cards)
    def __getitem__(self, position) :
        return self._bs_cards[position]
```
__(double underscores)가 맨앞 맨뒤에 둘러 쌓여있는 특별 메소드를 클래스에서 정의하면 ```len(BsDeck object) ```의 ```BsCard```의 개수를 반환하도록 정의할 수 있고 ```__getitem__```은 ```BsDeck object[0]```의 값을 불러 올 수 있게한다.
이를 통해서 다른 객체지향 언어처럼 메서드를 새로 정의해서 구현할 필요가 없다.
