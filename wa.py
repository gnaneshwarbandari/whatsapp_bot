from selenium import webdriver
from selenium.common.exceptions import ElementNotSelectableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
import pywhatkit
import pandas as pd
import time
import os

def process(path,file,message):
    print(path+"........."+file+"............."+message)
    dir_path = os.getcwd()
    profile = os.path.join(dir_path, "profile", "wpp")

    file_s = "image/*,video/mp4,video/3gpp,video/quicktime"
        
    ser = Service(r'chromedriver')
    op = webdriver.ChromeOptions()
    op.add_argument(r"user-data-dir={}".format(profile))
    s = webdriver.Chrome(service=ser, options=op)

    s.get("https://web.whatsapp.com/")

    while True:
        try:
            k = s.find_element(By.XPATH, "//div[@id='side']")
            if k.is_displayed() == True:
                break
        except:
            pass

    data1 = pd.read_excel (path)
    df = pd.DataFrame(data1, columns= ['Name','Mobile'])

    filename = file
    message = message

    def automate(filename):
        k1.find_element(By.XPATH, "//div[@title='Attach']").click()
        k1.find_element(By.XPATH, "//button[@aria-label='Photos & Videos']")
        img = k1.find_element(By.XPATH, "//input[@accept='"+file_s+"']")
        img.send_keys(filename)
        time.sleep(4)
        k1.find_element(By.XPATH, "//div[@class='_1w1m1']").click()
        time.sleep(4)
        #k1.find_element(By.XPATH, "//button[@class='_4sWnG']").click()
        
    for i in range(0,len(df)):
        name = df.loc[i][0]
        no = int(df.loc[i][1])
        print(no)
        try:
            s.get("https://web.whatsapp.com/send?phone=+91"+str(no)+"&text&app_absent=0")
        except Exception as e:
            print(e)
            
        while True:
            try:
                k1 = s.find_element(By.XPATH, "//div[@title='Type a message']")
                if k1.is_displayed() == True:
                    break
            except:
                pass
        #k1.send_keys(message)
        automate(filename)
        time.sleep(3)

    #s.get("https://web.whatsapp.com/send?phone=+918919971215&text")
    time.sleep(4)
    s.quit()
