from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app=FastAPI()

@app.get("/")
async def index():
    return {'data':{'username':'Vishnu S'}}
            
@app.get("/about/{id}")
def aboutpage(id:int):
    return{'contact number':id}            

my_posts= [{"title":"Post 1","content":"Content of Post 1","Rating":4,"published":True},{"title":"Post 2","content":"C2","Rating":6,"published":True}]

class Post(BaseModel):
    title:  str
    content: str
    rating: Optional[int]= None
    published: bool=True 

@app.get("/Posts")
def getPost():
    return{"data":my_posts}

@app.post("/Posts")
def newpost(post : Post):
    n_post=Post.dict()
    my_posts.append(n_post)
    return{"data":n_post}

    