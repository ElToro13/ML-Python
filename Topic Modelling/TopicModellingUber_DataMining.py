from selenium.webdriver import Firefox
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from selenium.webdriver.firefox.options import Options
import codecs
from time_keeper import count
from multiprocessing import Pool


driver  = Firefox()
driver.get("https://www.glassdoor.com")
WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"_evidon-accept-button\"]"))).click()
time.sleep(1)
WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".google"))).click()
time.sleep(20)


filename = "test8.csv"

driver.get("https://www.glassdoor.co.uk/Reviews/Uber-Reviews-E575263.htm")
page=1
while page < 700:
    print("Scrapping page {}..".format(str(page)))
    time.sleep(1)

    html = driver.find_element_by_tag_name('html')
    html.send_keys(Keys.END)

    #print("Scrapping page {}..".format(str(page)))
    time.sleep(1)
    #driver.execute_script("window.scrollTo(0,1050)")
    for i in range(1,11):
        #driver.execute_script("window.scrollTo(0, 1050)")
        try:
            title = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div/div[1]/div[1]/div/div[1]/article[2]/div[5]/main/div/div[1]/div[5]/div/ol/li[{}]/div/div[2]/div[2]/h2/a/span".format(i)))).text
        except:
            title = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div/div[1]/div[1]/div/div[1]/article[2]/div[5]/main/div/div[1]/div[6]/div/ol/li[{}]/div/div[2]/div[2]/h2/a/span".format(i)))).text
                                                                                   
        try:
            pros = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[1]/div[1]/div/div[1]/article[2]/div[5]/main/div/div[1]/div[6]/div/ol/li[{}]/div/div[2]/div[2]/div[4]/p[2]".format(i)).text
            cons = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[1]/div[1]/div/div[1]/article[2]/div[5]/main/div/div[1]/div[6]/div/ol/li[{}]/div/div[2]/div[2]/div[5]/p[2]".format(i)).text
        except:
            try:
                pros = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[1]/div[1]/div/div[1]/article[2]/div[5]/main/div/div[1]/div[6]/div/ol/li[{}]/div/div[2]/div[2]/div[5]/p[2]".format(i)).text
                cons = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[1]/div[1]/div/div[1]/article[2]/div[5]/main/div/div[1]/div[6]/div/ol/li[{}]/div/div[2]/div[2]/div[6]/p[2]".format(i)).text
            except:
                try:
                    pros = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[1]/div[1]/div/div[1]/article[2]/div[5]/main/div/div[1]/div[5]/div/ol/li[{}]/div/div[2]/div[2]/div[5]/p[2]".format(i)).text
                    cons = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[1]/div[1]/div/div[1]/article[2]/div[5]/main/div/div[1]/div[5]/div/ol/li[{}]/div/div[2]/div[2]/div[6]/p[2]".format(i)).text
                except:
                    pros=""
                    cons=""            
            
        try:
            mng = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[1]/div[1]/div/div[1]/article[2]/div[5]/main/div/div[1]/div[6]/div/ol/li[{}]/div/div[2]/div[2]/div[6]/p[2]".format(i)).text
        except:
            try:
                mng = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[1]/div[1]/div/div[1]/article[2]/div[5]/main/div/div[1]/div[6]/div/ol/li[{}]/div/div[2]/div[2]/div[7]/p[2]".format(i)).text
            except:
                try:
                    mng = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[1]/div[1]/div/div[1]/article[2]/div[5]/main/div/div[1]/div[5]/div/ol/li[{}]/div/div[2]/div[2]/div[7]/p[2]".format(i)).text
                except:
                    mng= ""
            
        #print(pros)        
        #print(cons)
        title = title.replace(",","")
        title = title.replace("\n","")

        pros = pros.replace(",","")
        pros = pros.replace("\n","")

        cons = cons.replace(",","")
        cons = cons.replace("\n","")

        mng = mng.replace(",","")
        mng = mng.replace("\n","")
        
        ff = codecs.open(filename, 'a', encoding='utf-8-sig')
        ff.write("{}, {}, {}, {}\n".format(title, pros, cons, mng))
        ff.close()
        #print("------")

    time.sleep(1)
    page+=1
    try:
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[1]/div[1]/div/div[1]/article[2]/div[5]/main/div/div[1]/div[7]/ul/li[7]/a").click()
    except:
        driver.get("https://www.glassdoor.co.uk/Reviews/Uber-Reviews-E575263_P{}.htm".format(str(page)))
    
#driver.quit()
##driver.execute_script("window.scrollTo(0, 450)")

    











