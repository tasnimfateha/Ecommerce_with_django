# Ecommerce_with_django
This is an E commerce project for online learning developed for Enterprise Software Development CS551Q.
This project is developed with Django and deployed in Render.

# Main features of the website:


1.User Authentication: The website allows users to create accounts, log in, and log out.
2.Products: The website allows users to view a list of products.
3.Shopping cart: The website allows users to add products to a shopping cart and remove products from the cart.
4.Order placement: The website allows users to place orders and view their order history.
5.Admin panel: The website has an admin panel for managing products, orders, and customer information.

# About dataset:

This dataset was collected from kaggle  (Jil Kothari. (2020). <i>Development Category (10k courses) from Udemy</i> [Data set]. Kaggle. https://doi.org/10.34740/KAGGLE/DSV/1482021) from Udemy consists of approximately 10,000 courses related to development available on their website. 
The first 5,102 elements from the original dataset of 9,933 entries were taken out due to cloud's poor 
ability to handle big dataset. 
The original source of this dataset is udemy. can be found from this link: (https://www.udemy.com/?utm_source=adwords-brand&utm_medium=udemyads&utm_campaign=Brand-Udemy_la.EN_cc.INDIA&utm_term=_._ag_78279294239_._ad_450776424635_._de_c_._dm__._pl__._ti_kwd-310556426868_._li_1007785_._pd__._&utm_term=_._pd__._kw_udemy_._&matchtype=e&gclid=EAIaIQobChMI8vq95bvj6wIVR6SWCh38_QIqEAAYASAAEgI9E_D_BwE)

# Basic setup of the virtual environment

Go to codio terminal and write cd Ecommerce_with_django
pyenv local 3.10.7 # this sets the local version of python to 3.10.7
python3 -m venv .venv # this creates the virtual environment for you
source .venv/bin/activate # this activates the virtual environment

# Start the server
For starting the server in local machine, run the following command in terminal:

python3 manage.py runserver

For starting the server in Codio, run the following command in Codio terminal:

python3 manage.py runserver 0.0.0.0:8000

# Reset database
For database regeneration, use the following command after deleting the file db.sqlite3

python3 manage.py migrate
To generate migration folder and files, use the following command:

python3 manage.py makemigrations

To run the generated migration, use the following command:

python3 manage.py migrate

To parse the data from csv files in data folder into the database, run the following command:

python3 manage.py import_data

# User category:
    # admin 
There are two type of user. Customer and admin. I have created a test admin user to test the website. you can access the admin panel by going to the 
<site_link/admin>
The credentials of test admin are:

Username: tasnim
Email:t.fateha.22@abdn.ac.uk
pass:12345@6789

You can create admin by typing in terminal: python3 manage.py createsuperuser

    #test customer:
I have created few demo customer to test the website. Credentials of them are:
Test customer:
email:abc@gmail.com
password: 12345
first name: test
second name: one
Phone: 0000093838


# Maintenance

Latest code is pulled from GitHub for Render deployment.
At most two websites can be opened at once from the Render deployed link.
The number of rows of data in the csv files can be increased and include data from more number of years.
However, the server ability on Render should also be considered when doing such decision.

Generate git log using the following command:

git log --pretty=format:"%h - %an, %ad : %s" --graph > git-log.txt

# BDD Testing:

For running behave, run the following command in the terminal:

behave

However, chromedriver is not compatible with codio, so expected result might not be seen.