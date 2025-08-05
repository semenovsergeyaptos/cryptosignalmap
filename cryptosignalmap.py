import requests
import pandas as pd
from textblob import TextBlob
import random

def get_price_changes():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 50,
        'page': 1,
        'price_change_percentage': '1h'
    }
    response = requests.get(url, params=params)
    data = response.json()
    df = pd.DataFrame([{
        'symbol': coin['symbol'].upper(),
        'name': coin['name'],
        'price_change_1h': coin.get('price_change_percentage_1h_in_currency', 0)
    } for coin in data])
    return df

def get_sentiment_scores():
    # 🎭 Эмуляция: случайные значения, замените API Twitter/TwitterX при желании
    coins = ['BTC', 'ETH', 'DOGE', 'ADA', 'XRP', 'SOL', 'TRX', 'AVAX', 'LINK', 'DOT']
    sentiments = []
    for coin in coins:
        score = random.uniform(-1, 1)  # Подставить реальные данные через Tweepy или X API
        sentiments.append({
            'symbol': coin,
            'sentiment_score': score
        })
    return pd.DataFrame(sentiments)
