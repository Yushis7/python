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

    if current_rate is not None:
        # 현재 날짜 및 시간을 가져옵니다.
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"현재 환율: 1 USD = {current_rate} KRW")

        # 메시지를 변경하여 현재 날짜, 시간 및 환율 정보를 포함합니다.
        message = f"{current_time}\n현재 환율: 1 USD = {current_rate} KRW"

        if current_rate <= target_rate:
            message += f"\n환율이 {target_rate} KRW 이하로 떨어졌습니다!"
            print(message)
            
            # 수정된 부분: Pushbullet 대신 텔레그램으로 알림을 보냅니다.
            notify_telegram(telegram_token, telegram_chat_id, message)

def main(api_key, telegram_token, telegram_chat_id, target_rate):
    # 아침 7시에 작업을 실행하는 스케줄을 설정합니다.
    schedule.every().day.at("07:00").do(job, api_key, telegram_token, telegram_chat_id, target_rate)

    # 무한 루프로 스케줄을 실행합니다.
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    # 텔레그램 봇의 토큰과 채팅 ID를 설정합니다.
    telegram_bot_token = 'API'
    telegram_chat_id = '-API_id'  # 변경된 부분: 채팅 ID 형식을 변경
    
    # Open Exchange Rates API 키를 설정합니다.
    open_exchange_rates_api_key = 'API등록'
    
    # 지정값은 프로그램을 중단하고 알림을 보낼 환율을 의미합니다.
    target_exchange_rate = 1200  # 예시: 1 USD = 1200 KRW
    
    main(open_exchange_rates_api_key, telegram_bot_token, telegram_chat_id, target_exchange_rate)
