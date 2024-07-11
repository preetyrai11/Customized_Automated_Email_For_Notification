import os
from datetime import date # core python module 
import pandas as pd   # pip install pandas 
from send_email import send_email  # local python module 
from datetime import datetime, timedelta
from email.mime.text import MIMEText 
# code 
import os 
import smtplib 

from pathlib import Path 
# gmail 
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart 
from email.mime.base import MIMEBase 
from email import encoders 

from dotenv import load_dotenv 
import ssl 

# Public GoogleSheets url - not secure! 
SHEET_ID = "1QPj5r7GF_8AVK9w7zmr6Tk7U9g0Wj4UN"
SHEET_NAME = "Sheet2" 
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"


# https://docs.google.com/spreadsheets/d/1QPj5r7GF_8AVK9w7zmr6Tk7U9g0Wj4UN/edit?gid=255292232#gid=255292232



def load_df(url):
    parse_dates = ["expiration_date"] 
    df = pd.read_csv(url, parse_dates=parse_dates) 
    df = pd.read_csv(url) 
    return df 


print(load_df(URL)) 
 

 
sender_email = os.getenv("EMAIL")
pswd = os.getenv("PASSWORD")

subject_for_gaining_customers = "Exclusive Discount Just for You – Limited Time Offer!"

def send_email_for_gaining_customers(subject_for_gaining_customers, name, receiver_email, discount, product_name): 
      body = f"""
          Hi {name},
          We hope this email finds you well! As a valued customer, we are thrilled to offer you an exclusive discount on your next purchase.For a limited time, enjoy a {discount} discount on {product_name}  in our store. This is our way of saying thank you for being a loyal customer. Don’t miss out on this fantastic opportunity to save on your favorite products.
          Use code: WELCOME20 at checkout.
         Hurry, this offer is only valid until [Expiration Date]. Shop now and take advantage of this special deal!
        Best regards,
        CAS 
        """ 
      msg = MIMEText(body) 
      msg['Subject'] = subject_for_gaining_customers 
      msg['From'] = sender_email 
      msg['To'] = ','.join(receiver_email) 
      with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender_email, pswd)
        smtp_server.sendmail(sender_email, receiver_email, msg.as_string())
      print("Message sent!")



subject_for_cleaning_stocks = "Clearance Sale – Up to 50% Off on Selected Items!"

def send_email_for_cleaning_stocks(subject_for_cleaning_stocks, name, receiver_email, discount, product_name): 
      body = f"""
          Hi {name},
          Great news! Our clearance sale is here, and we are offering up to {discount}% off on {product_name} items. It’s the perfect time to grab those products you’ve had your eye on before they’re gone for good.
          Whether you’re looking for the latest trends or timeless classics, we have something for everyone. Our clearance items are limited in quantity, so don’t wait too long to snag these incredible deals. Shop now and save big: [Link to Clearance Section]
         Thank you for being a valued customer. We look forward to seeing you soon!
         Warm regards,
         CAS

        """ 
      msg = MIMEText(body) 
      msg['Subject'] = subject_for_cleaning_stocks
      msg['From'] = sender_email 
      msg['To'] = ','.join(receiver_email) 
      with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender_email, pswd)
        smtp_server.sendmail(sender_email, receiver_email, msg.as_string())
      print("Message sent!")






def query_data_and_send_emails(df):
    present = date.today() 
    email_counter = 0 
    # Convert the 'expiration_date' column to datetime
    # df['expiration_dates'] = pd.to_datetime(df['expiration_date'], format='%m/%d/%y')

    for  _, row in df.iterrows():
        if row['should_send_mail_for_cleaning_stock']=="Yes" :
          subject_for_cleaning_stocks = "Clearance Sale – Up to 50% Off on Selected Items!"

          send_email_for_cleaning_stocks(subject_for_cleaning_stocks, row['names'], row['email'], row['discount_for_cleaning_stocks'], row['ITEMS'])

        
        else:
           subject_for_gaining_customers = "Exclusive Discount Just for You – Limited Time Offer!"

           send_email_for_gaining_customers(subject_for_gaining_customers, row['names'], row['email'], row['discount_for_gaining_customer'], row['ITEMS'])

    
        email_counter += 1 
    
    return f"Total Emails Sent: {email_counter}" 
 

df = load_df(URL) 
result = query_data_and_send_emails(df) 
print(result) 

