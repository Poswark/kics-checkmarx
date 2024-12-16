from fastapi import FastAPI
from logging.config import dictConfig
import logging
from .config import LogConfig
logger = logging.getLogger("mycoolapp")
import time 

START = time.time()
app = FastAPI()

def elapsed():
    running = time.time() - START
    minutes, seconds = divmod(running, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)



@app.get("/")
def read_root():
    logger.info("Example")
    return {"Hello": "World"}


@app.get('/time')
def read_root():
    return {"Start time": "%s" % elapsed()}


logger = logging.getLogger("mycoolapp")