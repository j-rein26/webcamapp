import smtplib
from PIL import Image
import io
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_SENDER = os.getenv("EMAIL")
PASSWORD = os.getenv("PSWD")
RECEIVER = os.getenv("RECEIVER_EMAIL")

def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New Customer just arrived!"
    email_message.set_content("Hey! A new customer just walked in.")

    with open(image_path, "rb")as file:
        content = file.read()
    try:
        with Image.open(io.BytesIO(content)) as img:
            subtype = img.format.lower()
    except IOError:
        subtype = None
 
    email_message.add_attachment(content, maintype="image", subtype=subtype)

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(EMAIL_SENDER, PASSWORD)
    gmail.sendmail(EMAIL_SENDER, RECEIVER, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email(image_path="images/19.png")

