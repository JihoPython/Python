import sys
from typing import Optional

from fastapi import FastAPI

from dynamic_import import load_module

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/run")
def run():
    return { "result": load_module("strategy").hello() }


@app.get("/read")
def read():
    """
    dynamic loading
    """
    import sys,imp

    # 전략 파일 읽기
    my_code = open("strategy.py", 'r').read()

    # imp 모듈 통해서 빈 모듈 생성
    strategy = imp.new_module('strategy')

    # 읽은 파일 String을 모듈에 욱여넣기
    exec(my_code, strategy.__dict__)
    keys = strategy.__dict__.keys()
    print(keys)
    for key in keys:
        if "__" in key: continue
        print(key, strategy.__getattribute__(key))

    # 모듈의 메서드 실행 가능
    return strategy.hello()
