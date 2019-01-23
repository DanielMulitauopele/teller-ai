# Teller AI
Module 4 | Team: Autumn Martin, Daniel Mulitauopele, Dina Caraballo, Nick Dambrosio
Cross-Pollination Capstone: a project where back-end and front-end students collaborate and build an app together. This app encompasses separate back-end and front-end apps that communicate to each other via API requests.

## About
### Intro
Would you like to find out the most recent attitudes towards a particular cryptocurrency? Teller AI retrieves relevant tweets, and runs Watson sentiment analysis to discover sentiment towards a coin.

Teller AI is deployed [here](https://teller-ai.herokuapp.com/).

### Background
Teller AI is a Python Django API. It consumes tweet data from [Twitter](https://developer.twitter.com/en/docs.html) and accesses [Watson Sentiment Analysis](https://console.bluemix.net/docs/services/tone-analyzer/index.html#about) to analyze tweets.

Teller AI is a microservice for our Teller project, which also includes a Ruby on Rails back-end, [Teller Api](https://teller-api.herokuapp.com/), and a React front-end, [Teller](https://teller.netlify.com/).

### Tech Stack
Python 3.7.1, Django 2.1.4, Heroku, Django-Nose testing

### Relevant Links
##### [Deployed App](https://teller-ai.herokuapp.com/)

##### Teller (Front-End) [GitHub](https://github.com/DanielMulitauopele/teller) | [Heroku](https://teller.netlify.com/)

##### Teller API (Back-End) [GitHub](https://github.com/DanielMulitauopele/teller-api) | [Heroku](https://teller-api.herokuapp.com/)

## Endpoints

### Get **/teller/watson_analysis?coin=#{search_params}**

Example Request:
```
GET /teller/watson_analysis?coin=dogecoin
```

Example Response:
```
{ "document_tones": ["joy", "tentative"] }
```

## Getting Started

First, clone down this project by running `git clone git@github.com:DanielMulitauopele/teller-ai.git` in the CLI.

If you are new to Python and Django, [this](https://realpython.com/django-setup/) may be helpful for setting up.

This app uses Python 3.7.1O and Django 2.1.4. Other requirements for this app are located [here](https://github.com/DanielMulitauopele/teller-ai/blob/master/requirements.txt).

### Development
For development, you may either start the [Django development server](https://docs.djangoproject.com/en/2.1/intro/tutorial01/) or start the [Gunicorn server](https://github.com/benoitc/gunicorn) server.

To start the Django server, run `python manage.py runserver 8080`. The default port is 8000, but this last command-line argument will change it to port 8080.

To start the Gunicorn server locally (that's right--it's a Green Unicorn!) run `gunicorn tellerai.wsgi`

### Staging & Production
This app is deployed to Heroku. We use [beta-teller-ai](https://beta-teller-ai.herokuapp.com/) for staging prior to production, and [teller-ai](https://teller-ai.herokuapp.com/) for production.

Changes can only be pushed to beta-teller-ai by accepted collaborators from the master branch. From there, this build may be manually promoted to production on teller-ai.

### Testing
To see if tests pass and what test coverage is, run `python manage.py test`.

This command already includes command line arguments, `--with-coverage --cover-package=teller --verbosity=1`, due to our settings. This runs coverage for files within the `teller` directory. The output will be similar to this one:

<img width="728" alt="test coverage output" src="https://user-images.githubusercontent.com/36902512/50577839-5a4ec500-0dee-11e9-899d-97b7dc6dab2e.png">

If you would like more detailed test coverage information, run `coverage run manage.py`. To view the results in terminal run `coverage report`.

For a more elegant presentation, run `coverage html`. This will create or update a folder called `htmlcov`. View the file path `htmlcov/index.html`, and open this file in your browser. For example, right click on `index.html` within `htmlcov`. Choose `open with` and click on your browser of choice (note: you may need to view it in finder first).
