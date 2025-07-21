from flask import Flask, send_file
from datetime import datetime
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

# وقت الانتهاء (UTC)
END_TIME = datetime(2025, 7, 25, 20, 59, 59)  # عدّله حسب وقتك

@app.route('/countdown.png')
def countdown_image():
    now = datetime.utcnow()
    diff = END_TIME - now
    if diff.total_seconds() < 0:
        diff = datetime.utcfromtimestamp(0) - datetime.utcfromtimestamp(0)

    hours = int(diff.total_seconds() // 3600)
    minutes = int((diff.total_seconds() % 3600) // 60)
    seconds = int(diff.total_seconds() % 60)

    text = f"{hours:02}:{minutes:02}:{seconds:02}"

    img = Image.new("RGB", (400, 100), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text((100, 40), text, font=font, fill=(0, 0, 0))

    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return send_file(buffer, mimetype="image/png")

@app.route('/')
def home():
    return "Countdown timer is running!"
