# surfScrapper


surfScrapper is a web application designed to provide users with the latest rankings of the best surfing beaches along the Algarve coast. It operates by scraping data from various surfing ranking portals for this region, updating its database every hour, and then sorting the information using a specific algorithm.

Demo-link: https://surfscrapper-production.up.railway.app/

## Features

- Hourly updates of surfing beach rankings along the Algarve coast.
- User-friendly interface displaying the top beaches for surfing.
- Subscription feature allowing users to receive email updates for specific beaches.
- Email confirmation for subscription to ensure security.
- Worker based on Celery and Redis for sending email updates.
- Technologies used: Python, Django, SQLite, Celery, and Redis.

## Installation

To run surfScrapper locally, follow these steps:

1. Clone this repository: `git clone https://github.com/marcin1997garbarczyk/surfScrapper.git`
2. Navigate into the project directory: `cd surfScrapper`
3. Install dependencies: `pip install -r requirements.txt`
4. Make migrations: `python manage.py makemigrations` followed by `python manage.py migrate`
5. Run the server: `python manage.py runserver`
6. Access the application at `http://127.0.0.1:8000/`
7. *If you have redisCli and redisServer on your PC* - Run workers (`celery -A coreDjangoApp.celery beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler & celery -A coreDjangoApp.celery worker --loglevel=info -P solo`)


## Usage

1. Visit the homepage to view the current rankings of the best surfing beaches along the Algarve coast.
2. Subscribe to receive email updates for specific beaches:
   - Navigate to the subscription page.
   - Enter your email address and select the beaches you want to follow.
   - An email with an activation link will be sent to your email address.
   - Click on the activation link to confirm your subscription.
3. Once confirmed, you will start receiving daily emails with the top three surfing beaches among your subscribed ones.

## Main technology stack 

- Python 
- Beautifulsoup
- Django
- SQLite
- Celery
- Redis
- 
## Screenshots

Demo version: https://surfscrapper.onrender.com

![surfScrapper Screenshot](/readmeScreens/homePage.png)
![surfScrapper Screenshot](/readmeScreens/form.png)
![surfScrapper Screenshot](/readmeScreens/formSuccess.png)
![surfScrapper Screenshot](/readmeScreens/emailForm.png)
![surfScrapper Screenshot](/readmeScreens/conditionTemp.png)
