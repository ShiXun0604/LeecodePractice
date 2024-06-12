import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, app_password, recipient_email, subject, body):
    # 設定 SMTP 伺服器及其埠號
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls

    # 建立 MIMEMultipart 物件
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject

    # 添加郵件正文內容
    message.attach(MIMEText(body, "plain"))

    try:
        # 建立與 Gmail SMTP 伺服器的連接
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()  # 升級連接到加密的 TLS
        server.login(sender_email, app_password)  # 登入 Gmail 帳戶
        server.sendmail(sender_email, recipient_email, message.as_string())  # 發送郵件
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()  # 關閉連接

# 使用範例
sender_email = "tomcruise890604@gmail.com"
app_password = "hrmm egho mggo oarx"
recipient_email = "shixun.chen@expertos.com.tw"
subject = "Test Email"
body = "This is a test email sent from Python."

send_email(sender_email, app_password, recipient_email, subject, body)