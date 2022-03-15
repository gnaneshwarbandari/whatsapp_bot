from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
import os
from PIL import Image

def scan_wait(key):
    while wait("//div[@class='_3GlyB']") != True:
        try:
            val = s.find_element(By.XPATH, "//div[@class='_2UwZ_']")
            n_key = val.get_attribute("data-ref")
            if n_key != key:
                print("new_key")
                s.save_screenshot('qr_code.png')
                key = n_key
        except:
            pass
        
def wait(xpath):
    while True:
        try:
            k = s.find_element(By.XPATH, xpath)
            if k.is_displayed() == True:
                break
        except:
            pass
    return True

def automate(filename):
    s.find_element(By.XPATH, "//div[@class='_2jitM']//div[@class='_2cNrC']").click()
    wait("//span[@data-testid='attach-image']")
    #//span[@data-testid='attach-document']
    img = s.find_element(By.XPATH, "//span[@data-testid='attach-image']").click()
    print(img)
    img.send_keys(filename)
    wait("//div[@aria-label='Send']")
    k1.find_element(By.XPATH, "//div[@aria-label='Send']").click()

filename = "C:/Users/USER/Desktop/New folder/smartinternz.png"
contact = "C:/Users/USER/Desktop/New folder/Book1.xlsx"
message = "Hello sir"
file_s = "image/*,video/mp4,video/3gpp,video/quicktime"

dir_path = os.getcwd()
profile = os.path.join(dir_path, "profile", "wpp")

ser = Service(r'chromedriver')
op = webdriver.ChromeOptions()
op.add_argument(r"user-data-dir={}".format(profile))
s = webdriver.Chrome(service=ser, options=op)

web = s.get("https://web.whatsapp.com/")

while True:
    try:
        scan = s.find_element(By.XPATH, "//canvas[@aria-label='Scan me!']")
        if scan.is_displayed() == True:
            val = s.find_element(By.XPATH, "//div[@class='_2UwZ_']")
            key = val.get_attribute("data-ref")
            s.save_screenshot('qr_code.png')
            scan_wait(key)
            break
    except:
        try:

            login = s.find_element(By.XPATH, "//div[@class='_3GlyB']")
            if login.is_displayed() == True:
                break
        except:
            pass
    
data1 = pd.read_excel(contact)
df = pd.DataFrame(data1, columns= ['Name','Mobile'])

for i in range(0,len(df)):
    name = df.loc[i][0]
    no = int(df.loc[i][1])
    print(no)
    try:
        s.get("https://web.whatsapp.com/send?phone=+91"+str(no)+"&text&app_absent=0")
    except Exception as e:
        print(e)
    wait("//span[@data-testid='clip']")
    automate(filename)

print("done")

s.quit()
