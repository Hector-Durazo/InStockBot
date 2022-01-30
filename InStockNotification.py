import time
import smtplib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


sdr_email = "#########@gmail.com"
rec_email1 = "########@gmail.com"
rec_email2 = "########@gmail.com"
rec_email3 = "########@gmail.com"
rec_email4 = "########@gmail.com"
password = "#############"

subject = "3070 IN STOCK"
body = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442"

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(sdr_email, password)
print("Login success")

msg = f'Subject: {subject} \n\n{body}'
browser = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
browser.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442")
#browser.get("https://www.bestbuy.com/site/macbook-air-13-3-laptop-apple-m1-chip-8gb-memory-256gb-ssd-latest-model-gold/6418599.p?skuId=6418599")


buyButton = False

while not buyButton:
    try:
        addToCartBtn = browser.find_element_by_class_name("btn-disabled")
        browser.execute_script("window.stop();")
            
        print("Button isnt ready yet.")

        time.sleep(10)
        browser.refresh()

    except:
        addToCartBtn = addButton = browser.find_element_by_class_name("btn-primary")

        print("IS AVAILABLE")
        server.sendmail(rec_email1, rec_email1, msg)
        server.sendmail(rec_email1, rec_email2, msg)
        server.sendmail(rec_email1, rec_email3, msg)
        server.sendmail(rec_email1, rec_email4, msg)
        time.sleep(300)

