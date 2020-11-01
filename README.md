# Web Scraping of flipkart product reviews

![1](https://github.com/IMsumitkumar/Web-Scraper-for-flipkart-product-reviews/blob/main/static/project_image_live/flipscrapper2.png)
---
![2](https://github.com/IMsumitkumar/Web-Scraper-for-flipkart-product-reviews/blob/main/static/project_image_live/flipscrapper3.png)
---

- This is a web app written using (HTML, CSS, Bootstrap) for the frontend and (Django python framework) for backend.

1. This app simply takes a search String (productName) 
2. Scrap all the reviews(Name, Rating, Comment Heeading, Comment) available for the specific product 
3. Store all the records in MongoDB database 
4. and Finally display in a HTML table.

- It is deployed on Heroku Cloud so you can use the webapp using https://flip-review-scrapper.herokuapp.com/`
---
LINK (DEPLOYED ON HEROKU) using Django : https://flip-review-scrapper.herokuapp.com/
LINK (DEPLOYED ON HEROKU) using Flask : https://flipkart-review-scrapper-flask.herokuapp.com/

Django version of the same app can be found here : https://github.com/IMsumitkumar/flipkart-product-reviews-scrapper-FLASK
---
### Instructions to run in your local machine:

##### Create a virtual env
    
    RUN ->
    1. conda create -n <env_name> python=3.x
    2. conda activate <env_name>
    

##### Clone repo in your local machine
    
    1. open terminal and go inside in your desired directory
    2. RUN -> git clone https://github.com/IMsumitkumar/Web-Scraper-for-flipkart-product-reviews.git
    

##### Install dependecies
    
    RUN ->
    1. pip install -r requirements.txt
    

##### Migrate Database
     
    RUN ->
    1. python manage.py makemigrations
    2. python manage.py migrate
    

##### Final step
    
    RUN ->
    1. python manage.py runserver
    
##### Make MongoDB available
    
    1. Go to scrapper Folder -> Views.py -> uncomment the scrap function and comment down the another scrap funtion 
    2. make sure mongoDb is installed in your machine and running otherwise it will show 'Something went wrong'
