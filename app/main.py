from typing import Union

from fastapi import FastAPI

import os

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": f"from: {os.environ.get('HOSTNAME', 'DEFAULT_ENV')}"}


