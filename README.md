# ScraperOnFlask
a simple web scraper that logs in to temple university's Dars and scrapes data. runs on flask, uses selenium and beautiful soup


## build instructions 

The following dependecies should be installed in the virtual environment

**dependencies**
- python selenium
- python requests module
- python beautifulsoup module 
- chromedriver
- chromedriver_magnager
- flask 

**Steps to build** 
<br>
Download the chromedriver for use with selinum <br>
[chromedriver downloads](https://chromedriver.chromium.org/downloads)
<br>
Next you should make a directory like
~~~
C:/webDriver/bin
~~~
and add the exe to this 
<br>
Add this directory to your system environment Path variable. 

-create a virtual environment in root directory by typing in a terminal:
~~~
python3 -m venv venv
~~~
- open virtual environment  on windows like so :
~~~
venv\Scripts\activate
~~~
or if you are on mac
~~~
source venv/bin/activate
~~~
Now install dependencies :
~~~
pip install flask
pip install selenium
pip install webdriver_manager
pip install pip install beautifulsoup4
~~~
or if beautifulsoup gives problems 
~~~
pip install pip install bs4
~~~
while in root directory of project path for main python script  <br>
if on windows
~~~
set FLASK_APP=flaskGrav.py
~~~
<br> 
if on mac

~~~
export FLASK_APP=flaskGrav.py
~~~

## Instructions to run
while in root directory of project
~~~
flask run
~~~
you should get output somthing like this
~~~
(venv) C:\Users\brahm\Documents\flaskGrav>flask run
 * Tip: There are .env or .flaskenv files present. Do "pip install python-dotenv" to use them.
 * Serving Flask app "flaskGrav.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

~~~

Copy the url in to your browser to display site.
