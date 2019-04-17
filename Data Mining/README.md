# Auto Adding products to our Cart on E-commerce site
### Introduction
Nowadays, we can lamost buy anything we need from click of a button. Digital Space have been giving traders an alternative way to offer their goods to customers a lot faster and convinently. In such a scenario, Many tools have been developed to automate the task of buying the product that we need online. One such library is *Selenium*. In this project we will demonstrate how we can leverage this library with *Python Programming Language* to automatically add item from ***list.txt*** file to our cart on **amazon.co.uk**.

First we begin with importing the necessary libraries

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

We use of PhantomJS which is a headless browser. It allows us to do all our task without opening an actual browser. Everything runs in he background and we can print or log the process along the way. 

## Files Description
[upwork1.py](https://github.com/ElToro13/ML-Python/blob/master/DDM-TwitterSentimentAnalysis/TwitterDataScrapping.ipynb) - Jupyter Notebook used for data collection

[ProductList](https://github.com/ElToro13/ML-Python/blob/master/DDM-TwitterSentimentAnalysis/DDM_NLP_SentimentAnalysis.ipynb) - Jupyter Notebook for Analysis and displaying of the Result

## Libraries Used

* Selenium
* PhantomJS
* BeautifulSoup
* time
* Urllib

## Author

* **Yash Soni**
