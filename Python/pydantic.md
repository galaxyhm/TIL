# Pydantic


## Pydantic이란
파이썬 타입 어노테이션을 이용한 데이터 검증과 설정관리를 쉽게할 수 있는 라이브러리


## 예시


python 3.7
```
from pydantic import BaseModel, PrivateAttr
from pydantic import Field
from typing import Any, ClassVar
import uuid


class User(BaseModel):
    id_num: ClassVar[int] = 1  # 클래스변수 선언
    id: uuid.UUID = Field(title='User ID',
                    description='User ID NUMBER ', default_factory=uuid.uuid4) # default_factory 생성시 실행되는 함수
                                                                            # 이걸로 다이나믹하게 값가능

    def __init__(self, **data: Any):
        super().__init__(**data)
        print(self.id, )

    @classmethod
    def up_num(cls):
        User.id_num += 1


if __name__ == '__main__':
    a = User()
    b = User()
    c = User()
    # print(a.id, b.id, c.id)
    print(User.id_num)
```
파이썬의 단점인 validation을  제한하고 변수 타입및 유형을 다른 사람들이 보기 쉽게 지정가능하고 검증 및 제한이 가능하도록해 
데이터 무결성을 지킬 수 있다.
