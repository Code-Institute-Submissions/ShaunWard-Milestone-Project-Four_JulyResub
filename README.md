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

## Database Modelling

### Checkout App

#### Order

| Database Key | Field Type | Validation |
| ------------ | ---------- | ---------- |
| order_number | CharField | max_length=32, null=False, editable=False |
| use_profile | ForeignKey 'Profile' | on_delete=models.SET_NULL, null=True, blank=True, related_name='orders' |
| full_name | CharField | max_length=50, null=False, blank=False |
| email | EmailField | max_length=254, null=False, blank=False |
| phone_number | CharField | max_length=20, null=False, blank=False |
| country | CountryField | blank_label='Country*', null=False, blank=False |
| postcode | CharField | max_length=20, null=True, blank=True |
| town_or_city | CharField | max_length=40, null=False, blank=False |
| address_line1 | CharField | max_length=80, null=False, blank=False |
| address_line2 | CharField | max_length=80, null=False, blank=True |
| county | CharField | max_length=80, null=True, blank=True |
| date | DateTimeField | auto_now_add=True |
| delivery_cost | DecimalField | max_digits=6, decimal_places=2, null=False, default=0 |
| order_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0 |
| grand_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0 |
| original_bag | TextField | null=False, blank=False, default='' |
| stripe_pid | CharField | max_length=254, null=False, blank=False, default='' |

#### OrderLineItem

| Database Key | Field Type | Validation |
| ------------ | --------- | ----------- |
| order | ForeignKey 'Order' | null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems' |
| product | ForeignKey 'Product' | null=False, blank=False, on_delete=models.PROTECT |
| quantity | IntegerField | null=False, blank=False, default=1 |
| line_item_total | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False |

#### Testing user stories

### Manual Testing

Google Developer tools in the chrome broswer was used extensively throughout the project as an efficient error checking method.

Further manual testing was done to ensure each aspect of the application worked as expected.

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
- Javascript

#### Frameworks, Libraries

- Django
- Sweetalert
- Stripe
- Django-allauth
- Django-crispy forms

#### Technologies/Tools

- [Heroku](https://www.heroku.com) to deploy the application
- [AWS](https://aws.amazon.com/) to host static and media files
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

To Deploy to [Heroku](https://www.heroku.com) via Github

1. Sign Up/Login into Heroku.
2. Create a new app using a relevant region and app title.
3. In your IDEs terminal create a new requirements.txt file using:
  ```
  pip3 freeze --local > requirements.txt
  ```
  This will be used by Heroku to install all dependancies for the application.
4. Create a Procfile at root level, ensuring it contains the following:
  ```
  web: gunicorn art_i_al.wsgi:application
  ```
5. Now these files have been created, add them to the staging area, give them a commit message and push them to github.
6. In your Heroku app click on the 'deploy' tab and under deployment method select Github.
7. Make sure your github name, repository and correct branch are selected and click connect.
8. Next go back to the tabs near the top and click on the settings button.
9. Under Config Vars click the Reveal Config Vars button.
10. Add the following information into the revealed config vars:
  ```
AWS_ACCESS_KEY_ID | ACCESS_KEY_ID_PROVIDED_BY_AWS
AWS_SECRET_ACCESS_KEY | SECRET_ACCESS_KEY_PROVIDED_BY_AWS
DATABASE_URL | YOUR_DATABASE_URL
EMAIL_HOST_PASS | YOUR_EMAIL_PASSWORD
EMAIL_HOST_USER | YOUR_EMAIL_USER
SECRET_KEY | YOUR_DJANGO_SECRET_KEY
STRIPE_PUBLIC_KEY | YOUR_STRIPE_SECRET_KEY
STRIPE_SECRET_KEY | YOUR_STRIPE_PUBLIC_KEY
STRIPE_WH_SECRET | YOUR_STRIPE_WH_SECRET
  ```
You will be required to fill in the SECRET_KEY with a key of your choice. 
The Stripe information will come from your stripe account under the Developers - API keys section.
Signing up for Amazon Web services and creating an S3 bucket will provide the AWS details.

11. Once this information is filled in, go back to the Deploy tab and at the bottom of the page under Maunal Deploy click Deploy Branch.
12. Once your have a message to say the app was deployed you can click the open app button.
13. (Optional) You can also enable automatic deploys from the data you push to the chosen Github repo under Automatic deploys.

## Acknowledgements

I'd like to acknowledge my mentor, Felipe Souza Alarcon, for his support throughout this project.
