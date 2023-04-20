import random

from fastapi import APIRouter
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.core.settings import settings
from app.schemas.mail import MailTo
route = APIRouter()


@route.post("/send-email")
async def send_email(mail: MailTo):
    sender_email = "nvdluan@gmail.com"
    receiver_email = mail.email
    password = settings.PASSWORD_EMAIL

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "MA XAC THUC"
    verify_code = random.randint(100000, 999999)
    message = f"""
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      </head>
    
      <body
        style="
          margin: 0;
          padding: 0;
          box-sizing: border-box;
          background-color: #f2f2f2;
          font-family: Arial, sans-serif;
          text-align: center;
        "
      >
        <div
          style="
            max-width: 100%;
            margin: 0 auto;
            padding: 20px;
            height: 100vh;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
          "
        >
          <h1
            style="
              color: #333;
              margin-top: 50px;
              margin-bottom: 20px;
              text-transform: uppercase;
            "
          >
            Xác thực thông tin
          </h1>
          <span style="font-size: 20px; font-weight: bold; color: #333"
            >Mã bảo mật:</span
          >
          <p
            style="font-size: 22px; margin-bottom: 10px; font-weight: 600"
            class="password_style"
          >
            {verify_code}
          </p>
          <p style="font-size: 22px; margin-bottom: 10px">
            Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi.
          </p>
          <p style="font-size: 22px; margin-bottom: 10px">The Project as is mcn</p>
        </div>
      </body>
    </html>
    """

    msg.attach(MIMEText(message, 'html'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

    return {
        "code": verify_code,
        "meta": {
            "status": 200,
            "message": "sent mail success"
        }
    }
