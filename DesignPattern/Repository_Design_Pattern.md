# Repository Design Pattern
The Repository Design Pattern separates service logic from data repository logic. It is commonly used in API servers (backend servers) and is a distinct layer separate from the Controller in the MVC Pattern.

## Features
1. Separates data access logic from service/business logic.
2. Facilitates easy unit testing.
3. Reduces migration costs by abstracting data access details.
## Example

### Datamodel(VO)
Value Object (VO) is immutable, meaning its state cannot be modified after creation. 
When changes are required, a new VO instance should be created instead of modifying the existing object. 
VO is typically used to represent and compare data in a consistent and reliable manner.
```python 
@class
UserVo:
    id: str
    password: str
    email: str

```
### Datamodel(DAO)
A Data Access Object(DAO) is a design pattern that provides an interface to interact with a database.
```python
from sqlmodel import SQLModel, Field

class UserDAO(SQLModel, table=True):
    id: str = Field(default=None, primary_key =True)
    password: str
    email:str 
```
### Repository
A repository in the Repository pattern is an abstraction layer 
that mediates between the domain model and the data access layer 
```python
from typing import Protocol
import UserDAO
class IUserRepo(Protocol):
    def save(self, user :UserVo):
        pass
    def update_by_id(self, user: UserVo, user_id: str):
        pass
    def delete_by_id(self,user_id:str):
        pass
    def find_by_id(self,user_id:str):
        pass


class DBUserRepo(IUserRepo):
    def __init__(self, session_maker):
        self.session_maker = session_maker
    def save(self, user: UserVo):
        user = UserDAO(id = UserVo.id, password= UserVo.password, email= UserVo.email)
        with self.session_maker() as session:
            try:
                session.add(user)
                session.commit(user)
            except Exception as e:
                session.rollback()
                raise e 


```
### Service
```python
class UserService:
    def __init__(self,user_repo: IUserRepo):
        self.user_repo = user_repo

    def save(self, user_id : str, password : str, email: str):
        
        if self.user_repo.find_by_id(user_id):
            raise HTTPException(409,"already exist")
        user = UserVo(
            id = id, 
            password = password,
            email = email 
        )
        self.user_repo.save(user)
    
```