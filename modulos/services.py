import tweepy
from modulos.segredos import CONSUMER_KEY, CONSUMER_SECRET, ACESS_TOKEN, ACESS_TOKEN_SECRET
from typing import List,Dict, Any
from modulos.constants import BRAZIL_WOE_ID
from modulos.connection import *

def _get_trends(woe_id: int) ->  List[Dict[str, Any]]:
    """ 
    Recebe os trending topics 
    Retorna as trends
    """
    # oauth twitter/tweepy
    auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
    
    auth.set_access_token(ACESS_TOKEN, ACESS_TOKEN_SECRET)

    # cria a conexão
    api = tweepy.API(auth)

    # armazena os tweets
    trends = api.get_place_trends(id = woe_id)

    return trends[0]["trends"]

def get_trends_from_mongo() ->  List[Dict[str, Any]]:
    """ 
    Procura as trends do twitter
    Retorna as trends encontradas 
    """
    trends = tweets_collection.find({})

    # retorna as trends para a rota
    return List(trends)

def save_trends() -> None:
    trends = _get_trends(woe_id=BRAZIL_WOE_ID)
    # insere na coleção as trends
    tweets_collection.insert_many(trends)
