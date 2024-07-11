import os 
import smtplib 
from email.message import EmailMessage 
from email.utils import formataddr 
from pathlib import Path 
# gmail 
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart 
from email.mime.base import MIMEBase 
from email import encoders 

from dotenv import load_dotenv 
import ssl 

# Setup port number and server name 
smtp_port = 587                   # Standard secure SMTP port
smtp_server = "smtp.gmail.com"    # Google SMTP Server 

sender_email = os.getenv("EMAIL")
pswd = os.getenv("PASSWORD")


# Load the environment variables 
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd() 
envars = current_dir / ".env" 
load_dotenv(envars) 

 
sender_email = os.getenv("EMAIL")
pswd = os.getenv("PASSWORD")

# print(sender_email) 
# print(pswd) 

receiver_email=["drpreetyrai@gmail.com", "preetyrai406@gmail.com"]


subject = "New email from TIE with attachments!!" 
   
body11 = "Hi, how are you"

def send_email(subject, receiver_email, name, due_date, invoice_no, amount, body): 
      
      msg = MIMEText(body) 
      msg['Subject'] = subject 
      msg['From'] = sender_email 
      msg['To'] = ','.join(receiver_email) 
      with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender_email, pswd)
        smtp_server.sendmail(sender_email, receiver_email, msg.as_string())
      print("Message sent!")




send_email(subject, receiver_email, 544,353, 88, 11,body11) 



