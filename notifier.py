import requests
import re
import os
from dotenv import load_dotenv
load_dotenv()

class NotificationEngine:
    def __init__(self, tg_token: str, tg_chat_id: str):
        self.tg_token = tg_token
        self.tg_chat_id = tg_chat_id

    def send_telegram_alert(self, message: str):
        if not self.tg_token or not self.tg_chat_id:
            print(f"[*] [通知模拟] Telegram Token 未配置，已拦截外发。目标账号: {os.environ.get('TELEGRAM_HANDLE', 'N/A')}")
            return
        
        url = f"https://api.telegram.org/bot{self.tg_token}/sendMessage"
        payload = {
            "chat_id": self.tg_chat_id,
            "text": message,
            "parse_mode": "Markdown"
        }
        try:
            response = requests.post(url, json=payload, timeout=10)
            if response.status_code == 200:
                print("[*] Telegram 实时警报发送成功。")
            else:
                print(f"[!] Telegram 发送失败: {response.text}")
        except Exception as e:
            print(f"[!] Telegram 网络异常: {e}")
