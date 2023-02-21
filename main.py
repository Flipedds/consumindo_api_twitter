from typing import List

from modulos.segredos import *

from fastapi import FastAPI

from modulos.services import get_trends_from_mongo, save_trends

from modulos.responses import TrendItem


app = FastAPI()


@app.get('/trends', response_model=List[TrendItem])
def get_trends_route():
    return get_trends_from_mongo()


trends = get_trends_from_mongo()

if not trends:
    save_trends()

