# Milestone-Project-Four - Earth Images

![Earth Images](https://github.com/ShaunWard/Milestone-Project-Four/blob/master/media/general_images/Home_page.png?raw=true)

Earth Images is an e-commerce website that allows users to view and buy prints of images from all around the world. Taken by the community and sold on Earth Images, this is the place to come for high quality images from all around the world.
Users can also discuss there favourite images on our community form with other like minded people.

## UX

### Goals for the Project

The main goal of this project is to complete the requirements of the final project for the Code Institues Full Stack Web Developer Programme.
The project is to build a fully functioning e-commerce website using Python and Django, it will be hosted on Heroku and use AWS to handle files as well as use a Postgres database.

### User Stories

#### A user viewing/buying products
- As a user I want to, view the site on a mobile, tablet or PC/Laptop.
- As a user I want to, easily be able to see how to navigate the site.
- As a user I want to, view products available to buy.
- As a user I want to, view individual products with more information such as dimentions.
- As a user I want to, be able to add a product to my basket
- As a user I want to, be able to adjust my basket by accessing it and removing unwanted items.
- As a user I want to, be able to see a breakdown of the cost of the item including any shipping costs.
- As a user I want to, be able to purchase items using a form for my shipping details and card information.
- As a user I want to, receive confirmation of the order right away, on screen and then with a follow up email.

#### A user creating/changing account information
- As a user I want to, be able to create an account.
- As a user I want to, be able to return to my account and log in.
- As a user I want to, be able to view and update my billing/shipping address information.
- As a user I want to, view past orders.
- As a user I want, my information to be pre populated at checkout if I have it on my profile.
- As a user I want to, change or rest my password easily.

#### A site owner
- As a site owner I want to, add, update or delete product information such as price, size etc.

## Features

### Features currently on the site

#### Navigation bar

![navbar](https://github.com/ShaunWard/Milestone-Project-Four/blob/master/media/general_images/Navigation%20Bar.png?raw=true)

- The navigation bar contains:
    1. A logo and home link, both which, when clicked, take the user back to the main page
    2. A shop link taking the user to the page to view available prints to buy.
    3. A register link which takes the user to the page to create an account.
    4. A login link which takes the user to the page to sign in to a current account.
    5. A search bar which allows the user to search for prints.
- When logged in the register and login links are removed and replaced by:
    1. A profile link to take the user to their user profile.
    2. A community link to take the user to the community where they can view and make comments.
    3. A logout link which logs the user out of their account.
    4. A basket link which takes the user to their basket.
  
#### Account Creation/Login Ability

![register page](https://github.com/ShaunWard/Milestone-Project-Four/blob/master/media/general_images/Sign%20Up%20page.png?raw=true)

- The register page can create an account by filling in the form with an email, username and password.
- The login page can log a current user in by providing their username or email and password.
- On the login page the user can click the 'Forgot Password?' link to reset their password.
- The users account can be used to view past order information and update and save billing/shipping information.

#### Shop (app) page

![the shop](https://github.com/ShaunWard/Milestone-Project-Four/blob/master/media/general_images/Products%20in%20shop.png?raw=true)

- The shop app allows users to view all of the prints available to purchase
- Clicking on the print image will take the user to a larger image of the print with more information and a button to add the print to the users basket.

#### Profile (app) page

![user profile](https://github.com/ShaunWard/Milestone-Project-Four/blob/master/media/general_images/Profile%20with%20order%20history.png?raw=true)

- The profile app presents the user with a form to update their Default Delivery Information, which when submitted is saved to their profile so it can be pre populated at checkout.
- The user can view prevous orders on the profile page. Clicking the order number will give the user more details about the order.

#### Community (app) page

![community page](https://github.com/ShaunWard/Milestone-Project-Four/blob/master/media/general_images/Community%20Page.png?raw=true)

- The Community page show the user current topics that other user have chosen to start a conversation about. The user can click on any of these cards to either read or contribute to the conversation.
- Each card contains a title, the subject which is an image from the shop, and a description of the topic being discussed. The date and user who started the topic are also shown.
- Clicking the topic of interest takes the user to the comments page where they can read and add to the discussion.

#### Responsive Design

- The application is able to be used in a web browser on any size device ranging from smartphone to large screens such as desktops.

### Features left to implement

There is an 'is_sold' line item in the product model that has not yet been implemented. 
The idea being that when a print is sold it can be automactially either taken down from the site or label as is sold. 

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
| product | ForeignKey 'Product' | null=False, blank=False, on_delete=models.CASCADE |
| quantity | IntegerField | null=False, blank=False, default=0 |
| line_item_total | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False |

### Community Form

#### Post

| Database Key | Field Type | Validation |
| ------------ | --------- | ----------- |
| title | CharField | max_length=200 |
| content | TextField |
| author | ForeignKey 'User' | on_delete=models.CASCADE | null=True |
| subject | ForeignKey 'Product' | on_delete=models.SET_NULL | null=True |
| date_of_post | DateTimeField | default=timezone.now |

#### Comment

| Database Key | Field Type | Validation |
| ------------ | --------- | ----------- |
| post | ForeignKey 'Post' | related_name="comments" on_delete=models.CASCADE | null=True)
| name | ForeignKey 'User' | on_delete=models.CASCADE | null=True |
| body | TextField |
| date_of_post | DateTimeField |default=timezone.now |

### Products App

#### Product

| Database Key | Field Type | Validation |
| ------------ | --------- | ----------- |
| name | CharField | max_length=254 |
| description | TextField |
| dimensions | CharField | max_length=70, null=True, blank=False |
| price | models.DecimalField | max_digits=6, decimal_places=2 |
| sku | CharField | max_length=254, null=True, blank=True |
| category | ForeignKey | 'Category', null=True, blank=True, on_delete=models.SET_NULL |
| image | ImageField | null=True, blank=True |

### Profiles App

| Database Key | Field Type | Validation |
| ------------ | --------- | ----------- |
| user | OneToOneField | User, on_delete=models.CASCADE |
| default_phone_number | CharField | max_length=20, null=True, blank=True |
| default_street_address1 | CharField | max_length=80, null=True, blank=True |
| default_street_address2 | CharField | max_length=80, null=True, blank=True |
| default_town_or_city | CharField | max_length=40, null=True, blank=True |
| default_county | CharField | max_length=80, null=True, blank=True |
| default_postcode | CharField | max_length=20, null=True, blank=True |
| default_country | CountryField | blank_label='Country', null=True, blank=True |

#### UserProfile

## Testing

### Testing user stories

The site was tested manually using Google Developer tools in the chrome broswer throughout the project as an efficient error checking method.

Further manual testing was done to ensure each aspect of the application worked as expected.

### Homepage

#### Navigation
- All navigation links were tested and all work as expected, taking the user to the correct webpage.
- The navigation links change correctly when the user registers and logs in.
- The basket link becomes bold and the basket total is calculated and shown correctly.
- The product management link only appears when a superuser is logged in.
- The navigation collaspes into the 'burger' icon at the expected screensize.
- The search box can be used at anytime to search in the shop, the search returns any items containing the keyword.
- The navigation links perform as required by there related user stories.

### Shop
- The shop displays a list of products available to buy for the user.
- Clicking on any card either image or information takes the user to the products detail page as required.
- The detail page correctly gives the user a link to register if they are not logged in instead of an add to basket link.
- When logged in the user has buttons on the product detail page to add the item to their basket or return to the shop.
- Clicking add to basket gives the user feedback in the form of a pop up saying the item has been added to basket.
- When the user searches the shop the items are filter and display only showing related items to the keyword. A button is available to take the user back to the full shop.

### Basket
- The basket correctly shows the user what has been added to their basket
- The remove button informs the user of what has been removed and when the basket is empty a message is displayed on the page as expected. The shop button then takes the user back.
- The go to checkout button takes the user to the checkout screen

### Checkout
- The checkout form is displayed correctly on the page.
- The user is alerted if they have not filled in a required field.
- If the user has saved information in their profile it is automatically populated as expected.
- The basket total is calculated correctly along with the shipping and grand total.
- The Stripe section warns the user when card information is invalid.
- If the order fails the user is warned in red text that the payment method has failed and to try a different method.
- Email confirmation is sent to the users address after checkout.

### Profile
- The profile page shows the user a form to save their details.
- The saved information the user has put in stays in the boxes until changed.
- Any completed orders are shown on this page.
- Clicking any of the order numbers will take the user to a breakdown of that order and warn them it is a past order using a pop up. This also has a return to shop button.

### Register/Loggin page
- If the user isn't logged in they have limited navigation buttons, one being to register.
- The registration form requires the form to be filled in correctly in the required fields.
- A verification email is sent requiring a link to be clicked to set up the account.
- Going to the login page and using this information now logs the user in correctly.

### Community
- The user is shown any topics currently in the system
- Clicking the topic takes the user to the topic comments page.
- The community home button takes the user back, the add a comment take the user to the comments form.
- The comment button submits the form correctly or the cancel button takes the user back.
- If the user owns either the topic or any comments, edit and delete buttons are shown as expected.
- The edit and delete buttons work as they are expected to.

### Product management
- Logged in as a superuser displays the edit and delete buttons on all shop items.
- Delete works as expected, edit takes the superuser to a form that is prefilled and can be edited as required.
- Clicking product management in the navigation bar goes to the add product page.
- The add product page has a blank form requiring a name, description, dimensions and a price.
- The is sold box at this moment does not work as mention in the features left to implement.
- The added product appears in the shop with the rest of the items as expected.

### Responsiveness
- The site has been tested using chrome developer tools and the webpages compress as expected to a good size.

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

I am thankful for the massive amount of information available on the web to learn from.
One of the video series I used to create some of the apps was:
https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi
I have done my best to use only what I needed to and change it to suit my needs.
