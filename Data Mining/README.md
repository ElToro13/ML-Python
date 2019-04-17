# Auto Adding products to our Cart on E-commerce site
### Introduction
Nowadays, we can almost buy anything we need from just click of a button. Digital Space have given  traders an alternative way to offer their goods to customers a lot faster and convinently. In such a scenario, Many tools have been developed to automate the task of buying the product that we need online. One such library is *Selenium*. In this project we will demonstrate how we can leverage this library with *Python Programming Language* to automatically add item from ***list.txt*** file to our cart on **amazon.co.uk**.

### How to Use: </br>
Clone this project. </br>
Write all the products you want to buy in the text file. Enter your Amazon account details in that login.py file. Once that is done, just run the ***shopper.py***. 

If you wish to see the the whole automation process you can replace the following line,
```python
driver = webdriver.PhantomJS() 

```
with, 

```python
driver = webdriver.Chrome('../chromedriver_win32/chromedriver') # location of your selenium chrome driver.
```
If you dont have PhantomJS, you can get it from [here](http://phantomjs.org/download.html) </br>
Put the phantomjs.exe file in the same folder as shopper.py

We use of PhantomJS, which is a headless browser, as it allows us to do all our task without opening an actual browser. Everything runs in the background and we can print or log the process along the way. 

## Files Description
[shopper.py](https://github.com/ElToro13/ML-Python/blob/master/Data%20Mining/shopper.py) - Python Script to automatically add items to your cart </br>
[List](https://github.com/ElToro13/ML-Python/blob/master/Data%20Mining/list.txt) - List all the products you wish to buy here </br>
[login.py](https://github.com/ElToro13/ML-Python/blob/master/Data%20Mining/login.py) - Account Credentials

## Libraries Used

* Selenium
* PhantomJS
* BeautifulSoup
* time
* Urllib

## Author

* **Yash Soni**
