import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/Apple-iPad-10-2-Inch-Wi-Fi-Cellular/dp/B07XL7G5CK/ref=sr_1_1_sspa?dchild=1&keywords=ipad&qid=1593045964&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFGMEFTSENQT01GNlMmZW5jcnlwdGVkSWQ9QTA1NDk3ODUyR0JOVU41T0cxQ0tDJmVuY3J5cHRlZEFkSWQ9QTA3NzQxNDUzTUpSVVM5VjhJOVUzJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()

    converted_price = float(price[1:4])

    if(converted_price < 420):
        send_mail()

    print(converted_price)
    print(title.strip())


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('beminshaker@gmail.com', 'ubbfijpjlowiqpcs')

    subject = 'Price Dropped!'
    body = 'Check the Amazon link https://www.amazon.com/Apple-iPad-10-2-Inch-Wi-Fi-Cellular/dp/B07XL7G5CK/ref=sr_1_1_sspa?dchild=1&keywords=ipad&qid=1593045964&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFGMEFTSENQT01GNlMmZW5jcnlwdGVkSWQ9QTA1NDk3ODUyR0JOVU41T0cxQ0tDJmVuY3J5cHRlZEFkSWQ9QTA3NzQxNDUzTUpSVVM5VjhJOVUzJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        'beminshaker@gmail.com',
        'beminshaker@outlook.com',
        msg
    )

    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()

check_price()

while(True):
    check_price()
    time.sleep(60 * 60)