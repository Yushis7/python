import requests
from twilio.rest import Client
import schedule
import time
import asyncio
import datetime

# Twilio 설정
ACCOUNT_SID = ''  # Twilio 콘솔에서 가져온 Account SID
AUTH_TOKEN = ''  # Twilio 콘솔에서 가져온 Auth Token
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'  # Twilio에서 구매한 전화번호
TO_PHONE_NUMBER = 'your_phone_number'  # 알림을 받을 수신자 전화번호

# Alpha Vantage API 설정
ALPHA_VANTAGE_API_KEY = 'your_alpha_vantage_api_key'  # Alpha Vantage API 키

# Twilio 클라이언트 초기화
client = Client(ACCOUNT_SID, AUTH_TOKEN)

def get_stock_data(symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={ALPHA_VANTAGE_API_KEY}'
    response = requests.get(url)
    data = response.json()
    if 'Time Series (1min)' in data:
        latest_time = next(iter(data['Time Series (1min)']))
        latest_data = data['Time Series (1min)'][latest_time]
        return {
            'time': latest_time,
            'price': latest_data['4. close']
        }
    else:
        return None

def get_exchange_rate(from_currency, to_currency):
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={ALPHA_VANTAGE_API_KEY}'
    response = requests.get(url)
    data = response.json()
    if 'Realtime Currency Exchange Rate' in data:
        exchange_rate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
        return exchange_rate
    else:
        return None

def send_sms(message):
    message = client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,
        to=TO_PHONE_NUMBER
    )
    print(f"Message sent: {message.sid}")

def daily_report():
    symbols = ['AAPL', 'GOOGL', 'AMZN']  # 예시 주식 심볼
    exchange_pairs = [('USD', 'KRW'), ('EUR', 'USD')]  # 예시 환율 쌍
    messages = []

    for symbol in symbols:
        stock_data = get_stock_data(symbol)
        if stock_data:
            messages.append(f"주식: {symbol}\n시간: {stock_data['time']}\n가격: {stock_data['price']}")

    for from_currency, to_currency in exchange_pairs:
        exchange_rate = get_exchange_rate(from_currency, to_currency)
        if exchange_rate:
            messages.append(f"환율: {from_currency}/{to_currency} = {exchange_rate}")

    send_sms("\n\n".join(messages))

def real_time_alert():
    symbols = ['AAPL', 'GOOGL', 'AMZN']  # 예시 주식 심볼
    exchange_pairs = [('USD', 'KRW'), ('EUR', 'USD')]  # 예시 환율 쌍

    for symbol in symbols:
        stock_data = get_stock_data(symbol)
        if stock_data:
            message = f"주식: {symbol}\n시간: {stock_data['time']}\n가격: {stock_data['price']}"
            send_sms(message)

    for from_currency, to_currency in exchange_pairs:
        exchange_rate = get_exchange_rate(from_currency, to_currency)
        if exchange_rate:
            message = f"환율: {from_currency}/{to_currency} = {exchange_rate}"
            send_sms(message)

# 매일 오전 9시에 실행될 작업 예약
schedule.every().day.at("09:00").do(daily_report)

# 실시간 알림을 위한 주기적 실행 (예: 5분마다)
async def main():
    while True:
        real_time_alert()
        await asyncio.sleep(300)  # 5분 대기

# 이벤트 루프에서 메인 비동기 함수 실행
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, schedule.run_pending)
    loop.run_until_complete(main())
