from bs4 import BeautifulSoup
import requests
import time
import smtplib

def CheckPrice():
    URL = 'https://www.flipkart.com/hp-victus-core-i5-12450h-12th-gen-8-gb-512-gb-ssd-windows-11-home-4-graphics-nvidia-geforce-gtx-1650-144-hz-15-fa0070tx-gaming-laptop/p/itm7faab3efcce20?pid=COMGGKKZHDJBZXJX&lid=LSTCOMGGKKZHDJBZXJXJSQPVS&marketplace=FLIPKART&q=hp+victus&store=6bo%2Fb5g&srno=s_1_3&otracker=AS_Query_PredictiveAutoSuggest_4_0_na_na_na&otracker1=AS_Query_PredictiveAutoSuggest_4_0_na_na_na&fm=Search&iid=1feeca62-5585-4cfb-992c-c1213dfd5e93.COMGGKKZHDJBZXJX.SEARCH&ppt=pp&ppn=pp&ssid=yb8v09air40000001693401914724&qH=8fa28d763aa5c003'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
    request = requests.get(URL, headers=headers)
    soup = BeautifulSoup(request.content, 'lxml')
    global title, price
    price = soup.find('div', class_='_30jeq3 _16Jk6d').text.strip()
    title = soup.find('span', class_='B_NuCI').text.strip()
    modified_price = float(price[1:].replace(",",""))
    print(f"Product Name: {title}")
    with open('PresentPrice.txt', 'w+') as f1:
        if(f1.read() == ''):
            f1.write(str(modified_price))
        f1.seek(0)
        content = f1.read()
        currentPrice = float(content)
        if(modified_price < currentPrice):
            SendMail()
            print("Price Reduced! Check your mail")
        else:
            print("Price is same or greater! Try again later")
    f1.close()

def SendMail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    subject = '!!!PRICE FELL DOWN!!!'
    body = f"The price of your product {title} fell down below {price}!\nCheck out the amazon link: https://www.flipkart.com/hp-victus-core-i5-12450h-12th-gen-8-gb-512-gb-ssd-windows-11-home-4-graphics-nvidia-geforce-gtx-1650-144-hz-15-fa0070tx-gaming-laptop/p/itm7faab3efcce20?pid=COMGGKKZHDJBZXJX&lid=LSTCOMGGKKZHDJBZXJXJSQPVS&marketplace=FLIPKART&q=hp+victus&store=6bo%2Fb5g&srno=s_1_3&otracker=AS_Query_PredictiveAutoSuggest_4_0_na_na_na&otracker1=AS_Query_PredictiveAutoSuggest_4_0_na_na_na&fm=Search&iid=1feeca62-5585-4cfb-992c-c1213dfd5e93.COMGGKKZHDJBZXJX.SEARCH&ppt=pp&ppn=pp&ssid=yb8v09air40000001693401914724&qH=8fa28d763aa5c003"
    message = f"Subject: {subject}\n\n{body}"   # doing that Subject: will make the subject variable as the actual sibject in the mail. without it, it wont work
    message = message.encode("utf-8")  # Encode the message with UTF-8
    server.login("sendersmail@gmail.com", "password")    #this is randomly generated password using google 2 step verifcation and google app password.
    server.sendmail('sendersmail@gmail.com', 'receiversmail@gmail.com', message)
    server.quit()

if __name__ == '__main__':
    while True:
        CheckPrice()
        time.sleep(60*60)    #one hour in seconds

# To create a .exe file for this code, run the following command in the terminal
# pyinstaller --add-data "priceTracker.py;." priceTracker.py
