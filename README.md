# Milestone-Project-Four - Earth Images
    
## Description



## User Design/Experience



### Design



### User Stories

- As a user I want to, have an easy way to keep track of things that I have watched and view them easily.


## Features

### Features currently on the site

#### Navigation bar


  
#### Account Creation


  
#### Login Ability



#### Responsive Design

- The application is able to be used in a web browser on any size device ranging from smartphone to large screens such as desktops.

### Features left to implement

- An ability for one user to share their entry with another using to suggest a programme/film.
- A page containing data about the entries such as:
  1. numbers of entries against a certain streaming service
  2. a quick view of all the ratings given, and an average rating
- Using an API it may also be possible to suggest programmes/films to the user based on their entries.

## Links

### Wireframes



## Testing

### Manual Testing

Google Developer tools in the chrome broswer was used extensively throughout the project as an efficient error checking method.

Further manual testing was done to ensure each aspect of the application worked as expected.

#### Front/Home Page



#### Login Page



#### Register Page



#### My List Page



#### Add to list Page



#### Edit page



#### Testing user stories



### Online testing tools

- [HTML Validator](https://validator.w3.org/) has been used to validate the HTML.
- [CSS Validator](https://jigsaw.w3.org/css-validator/)
- [Pep8](http://pep8online.com/) to check code for PEP8 requirements

## Technologies

### Languages/Technologies/Tools Used

#### Languages

- HTML
- CSS
- Python

#### Frameworks



#### Technologies/Tools

- [Heroku](https://www.heroku.com) to deploy the application
- [Gitpod IDE](https://www.gitpod.io)
- Git & [Github](https://github.com/) for version control
- [Balsamiq](https://balsamiq.com/) to create wireframes
- [Am I Responsive](http://ami.responsivedesign.is/#)

## Deployment

The project has been deployed using Heroku, and is available to view [here](https://milestone-project-four-ecom.herokuapp.com/)

### Local Deployment

To deploy locally:

1. Go to the applications [repository](https://github.com/ShaunWard/Milestone-Project-Four) on github.
2. Click on the 'code' button to access the dropdown and click 'download zip'.
3. Unzip the downloaded file and open into your development environment.
4. Start by installing the required systems listed in the requirements.txt file using
  ```
  pip3 install -r requirements.txt
  ```
5. Create an env.py file at the same level as the app.py file, this should contain the following information:
  ```
  import os

os.environ["SECRET_KEY"] = "YOUR_DJANGO_SECRET_KEY"

os.environ["STRIPE_PUBLIC_KEY"] = "YOUR_STRIPE_PUBLIC_KEY"
os.environ["STRIPE_SECRET_KEY"] = "YOUR_STRIPE_SECRET_KEY"
os.environ["STRIPE_WH_SECRET"] = "YOUR_STRIPE_WEBHOOK_SECRET"

os.environ["DEVELOPMENT"] = "True"
  ```
8. You will be required to fill in the SECRET_KEY with a key of your choice. The Stripe information will come from your stripe account under the Developers - API keys section.
9. In the terminal run the following commands:
```
  python3 manage.py makemigrations
  python3 manage.py migrate
  python3 manage.py loaddata categories
  python3 manage.py loaddata products
  ```
10. It is also possible to create a super user that will allow access to the admin panel by running:
```
python3 manage.py createsuperuser
```
Then following the intructions in the terminal.
11. Finally run
```
python3 manage.py runserver
```
to run the applpication.

Please note that if you wish to then push this project to a public repository such as your github then you must create a .gitignore file and make sure you add the env.py file into this to stop your valuable inforamtion being pushed.


### Heroku via Github Deployment



## Acknowledgements

I'd like to acknowledge my mentor, Felipe Souza Alarcon, for his support throughout this project.
