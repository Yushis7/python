import requests
import schedule
import time
from datetime import datetime


def get_exchange_rate(api_key):
    base_currency = 'KRW'
    target_currency = 'USD'
    url = f'https://open.er-api.com/v6/latest/{base_currency}?apikey={api_key}'
    
    try:
        response = requests.get(url)
        data = response.json()
        exchange_rate = data['rates'][target_currency]
        return exchange_rate
    except Exception as e:
        print(f"Error getting exchange rate: {e}")
        return None

def notify_telegram(token, chat_id, message):
    # 텔레그램 봇 API를 사용하여 메시지를 전송합니다.
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    params = {'chat_id': chat_id, 'text': message}
    
    try:
        response = requests.post(url, params=params)
        data = response.json()
        if data['ok']:
            print(f"Telegram message sent successfully.")
        else:
            print(f"Failed to send Telegram message: {data['description']}")
    except Exception as e:
        print(f"Error sending Telegram message: {e}")

def job(api_key, telegram_token, telegram_chat_id, target_rate):
    print("Checking exchange rate...")
    current_rate = get_exchange_rate(api_key)

def main(api_key, telegram_token, telegram_chat_id, target_rate):
    while True:
        current_rate = get_exchange_rate(api_key)
        
        if current_rate is not None:
            print(f"현재 환율: 1 USD = {current_rate} KRW")
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"{current_time}\n현재 환율: 1 USD = {int(1 / current_rate)} KRW"
            print(message)
            notify_telegram(telegram_token, telegram_chat_id, message)
                
            break
                
            # if current_rate <= target_rate:
            #     message = f"환율이 {target_rate} KRW 이하로 떨어졌습니다!"
                # print(message)
                
                # 수정된 부분: Pushbullet 대신 텔레그램으로 알림을 보냅니다.
                # notify_telegram(telegram_token, telegram_chat_id, message)
                
                # break

if __name__ == "__main__":
    # 텔레그램 봇의 토큰과 채팅 ID를 설정합니다.
    telegram_bot_token = '★텔레그램 토큰을 받아서 입력해주세요★(영문혼합)'
    telegram_chat_id = '★마이너스로 시작하는 -100숫자를 입력해주세요★'  # 변경된 부분: 채팅 ID 형식을 변경
    
    # Open Exchange Rates API 키를 설정합니다.
    open_exchange_rates_api_key = '★실시간 환율을 받을 수 있는 오픈API사이트에서 키를 받아주세요★'  # 수정된 부분: API 키 설정
    
    # 지정값은 프로그램을 중단하고 알림을 보낼 환율을 의미합니다.
    target_exchange_rate = 1200  # 예시: 1 USD = 1200 KRW
    
    main(open_exchange_rates_api_key, telegram_bot_token, telegram_chat_id, target_exchange_rate)


    # 아침 7시에 작업을 실행하는 스케줄을 설정합니다.
schedule.every().day.at("17:41").do(job, open_exchange_rates_api_key, telegram_bot_token, telegram_chat_id, target_exchange_rate)
#시간 자체는 vscode가 꺼져있으면 보낼 수 없다 클라우드를 써야한다

# 무한 루프로 스케줄을 실행합니다.
while True:
    schedule.run_pending()
    time.sleep(1)


 

    