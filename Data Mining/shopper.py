
import csv
import parameters
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import urllib.request as urllib2
from bs4 import BeautifulSoup
import login


driver = webdriver.PhantomJS() #('C:/Users/Yash/Downloads/chromedriver_win32/chromedriver')
# driver.get method() will navigate to a page given by the URL address
#driver.get('https://www.linkedin.com/uas/login?trk=guest_homepage-basic_nav-header-signin')
driver.get('https://www.amazon.co.uk/')
file = open("list.txt", "r")
line = file.read()
list1 = line.split("\n")

opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]

try:
    check = driver.find_element_by_id("nav-link-yourAccount")
    name = driver.find_element_class_name("nav-line-1")
    print(name)
except:
    
    log = driver.get("https://www.amazon.co.uk/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.co.uk%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=gbflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
    print("Navigating to Amazon Website")
    email = driver.find_element_by_id("ap_email")
    email.send_keys(login.email)

    password = driver.find_element_by_id("ap_password")
    password.send_keys(login.password)

    submit = driver.find_element_by_id("signInSubmit")
    submit.click()

sleep(1)
try:
    name = driver.find_element_by_id("nav-link-accountList")
    print(name.text)
except:
    name = driver.find_element_by_id("nav-link-yourAccount")
    print(name.text[0])

sleep(2)


def shopping(list1):
    for name in list1:
        
            
        # locate email form by_class_name
        textBox = driver.find_element_by_id('twotabsearchtextbox')


        # send_keys() to simulate key strokes
        textBox.send_keys(name)

        #button = driver.find_element_by_id("nav-search-submit-text")
        try:
            button = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[3]/div/form/div[2]/div/input")
        except:
            try:
                button = driver.find_element_by_xpath("//*[@id=\"nav-search\"]/form/div[2]/div/input")
            except:
                button = driver.find_element_by_xpath("//*[@id=\"nav-search-submit-text\"]")
        
        button.click()

        sleep(2)
        #print(driver.current_url)
        url = driver.current_url
        page = opener.open(url)
        illa = []
        soup = BeautifulSoup(page, 'html.parser')
        illa = soup.findAll("a", class_="a-link-normal a-text-normal")
        #print(illa)
        #print(illa[2]["href"])

        driver.get("https://www.amazon.co.uk/{}".format(illa[2]["href"]))

        addCart = driver.find_element_by_xpath("//*[@id=\"add-to-cart-button\"]")
        addCart.click()
        print("{} has been added to your cart.".format(name))
        sleep(2)
        try:

            cancel = driver.find_element_by_xpath("//*[@id=\"attach-close_sideSheet-link\"]")
            cancel.click()
        except:
            pass

        try:
            nothanks = driver.find_element_by_xpath("//*[@id=\"attachSiNoCoverage-announce\"]")
            nothanks.click()
        except:
            pass


if __name__ == "__main__":
    shopping(list1)


