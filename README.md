<p align="center">
  <img src="https://github.com/Honey20103/BrewMaster/blob/master/homebrew_app/project/static/images/brewmaster3.1.png" style="margin: 0;" width="300" height="200" >
</p>

# Brew Master 
> Home beer brewing logs and recipes. 
This repo hosts the assets used to build the Brew Master website/web application. A web application focused on offering passionate home beer brewers a platform they could utilise to log the entire process and steps taken during the brew day. 

>The Brew Master app will help homebrewers improve on their brewing process and the result of the beer batches, by having a log/diary of each recipe they will be able to defer to for future brew days.

***

### Background
The idea of this application was birthed from my boyfriend who does homebrew as a hobby. During a normal brew day, he would have a notebook logging and taking notes on the entire process of the specific recipe on the day, these would include temperatures etc. Notes would be taken for each process such as the mashing, lautering, boiling, cooling, fermenting, maturing(carbonation) and packaging steps.
When he needed to repeat the same brew, or after tasting the batch he would go back to his notebook to review notes and look at ways to improve or change some of the parameters in the brew such as temperatures for boiling and cooling and ingredient amounts. 

Hence, this is where the app idea stemmed from. And thus away with the notebook, and hello 21st-century logging or technology. He will now be able to write done his brew day notes in the application, easily return to recipes to edit and make changes, and have his recipe logs available on a database online. No fear of loss of the notebook and easy access.

The application will be available to the public in the future as a beer brewing recipe site and the ability to review the recipes.


***

### Website
A live demo can be found [here](https://the-brew-master.herokuapp.com/)

[Home iPhone](xxx)

[Home iPad](xxx)

[Recipe iPhone](xxx)

[Recipe iPad](xxx)

[Form iPhone](xxx)



***

## UX

### User stories
- As an amateur homebrewer, it is important to take a record of the entire process of brew day,
to learn from my previous mistakes and help improve my future batches.

- I often record my brew day notes or logs on a physical notebook, or sometimes the closest paper I
can find, and in some cases, I lose it and there goes my brew record, no recollection of what was done.

- As a fairly confident home brewer, I need an application to store my recipes and eventually start a microbrewery or make a profit from my homemade recipes.

- I am quite new to brewing, and I often make mistakes and need to change things in my notes, my notebook ends up looking like a child's scrapbook. Having a digital notebook will help with keeping my notes neat and easily editable.

- As a user I would like to be able to see other brewer's processes, mistakes and results to improve my brewing techniques.

- Beer brewing is quite an expensive hobby, having to view other brewers recipes saves me the need to buy brew recipes from companies.

- I'd like the ability to rate the different brew recipes I make, to know which ones to repeat.

- As a user, I can view all brew recipe logs, with information such as the date of the log.

- As a user, I can search for recipes/logs.

- As a user, I can add new brew logs to the database.

- As a user, I can edit existing recipes/logs.

- As a user, I can add new ingredients not available in the database.

- As a user, I can delete recipes.

- As a user, I can create an account.

- As a user, I can log in to my account.

- As a user, I can log out.

- As a brewer, I would like to update a recipe/log by uploading a photo of the final result of my beer at the end of the process.



### Strategy
My goal in the design was to make it as easy as possible for users to log their brew day process and log the recipes, to have a clean look with no clutter or information overload by having a user-friendly and minimalistic design.

### Scope
For the users, I wanted to provide them with a functional platform to keep their brew records, lessen the burden of log keeping on physical notebooks and eventually serve as recipe storage. 

The scope has full CRUD functionality for logs.

* A landing page that acts as a brewing diary, showing all logs recorded by the user.
* A 'Log' page that displays the recipe and process of the beer they made.
* A 'Add log' page that allows the user to add new log into their brewing diary/database.
* An 'Edit log' page that allows the user to update and then saves to the database.
* Ability to Create an account and store account in database
* Functionality to login and log out of user dashboard/profile

### Structure


### Skeleton

Initial wireframes were done on paper and pen, I'll probably at a later stage add a design made in Balsamic, it was a bit challenging to figure out how I wanted the UX to be, although my idea was to maintain a clean and minimalistic look, and easy to use. The look and feel are intentionally planned for mobile and desktop.

### Wireframes

[Home Page](https://github.com/Honey20103/BrewMaster/blob/master/wireframes/homepage.png)

[Login Page](https://github.com/Honey20103/BrewMaster/blob/master/wireframes/loginpage.png)

[Brew Log Page](https://github.com/Honey20103/BrewMaster/blob/master/wireframes/logpage.png)

### Database Schema

Choose to work with both relational and non-relational databases namely SQLite3 and MongoDB. I used MongoBD for the brew data forms as its schema-less and  presents a clean document option JSON style documents. It seemed suitable for this use case of a diary log. As for the SQLite DB i chose to use it to test out working with a relational and the benefits of it being lightweight in terms of setup and database administration(no actual server or configurations required) and it fit my needs to be able to create to a database to store user info and fetch altogether, which would be advantageous when it comes to mobile devices considering the database is integrated with the app, meaning less lag(mobile first approach).

<img src="https://github.com/Honey20103/BrewMaster/blob/master/homebrew_app/project/static/images/database_schema.png" style="margin: 0;" >


### Surface
My idea for the design is to have colour relating to beer such as brown, gold, orange or essentially brown theme colour palette, this will help users associate with the act of beer brewing.

<img src="https://github.com/Honey20103/BrewMaster/blob/master/wireframes/themecolor1.png" style="margin: 0;" width="600" height="250" >




***

## Features

### Existing Features

* **User Accounts** - Signup for an account, log-in and log-out.
* **Log/Recipe page** - When a recipe or brew log is selected the user will be presented with the page for that recipe. 
* **Add Log/Recipe** - The user can go to the menu and open the add log brew day page, providing the user with a diary or digital like a notebook to log their brew day content and add them to the database.
* **Add Ingredient** - Ingredient options will be available however if an option is not found, the user can add a new ingredient to the database.
* **Edit & Delete ingredients** - Ability for the user to edit and delete ingredients.
* **Multiple users login** - Ability to have more profiles for multiple beer brewers to log their recipes.

### Future Features

- **Social sharing buttons**: Users will be able to share beer recipes to their social media channels via the social sharing buttons provided. 
- **Brew Images** Ability to add/update a log by adding an image or images of the final brew result.
- **Log order arrangement**List logs in dashboard according to date of brew and not when entered.
- **Rating system** - The ability to star rate favourite brew day recipe
- **View ther brewers logs** - Ability for brewers to unhide or unlock certain logs to be publicly visible to other brewers on the app.

***

## Technologies Used

### Frontend

* [HTML](https://en.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [Bootstrap](https://getbootstrap.com/)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Materialize](https://materializecss.com/)
* [Bulma](https://bulma.io/)


### Backend

* [MongoDB](https://www.mongodb.com/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Python](https://www.python.org/)
* [Flask-PyMongo](https://pypi.org/project/Flask-PyMongo/)

### Deployed

* [Heroku](https://www.heroku.com/)

***

## Testing

#### Code Validation

#### Devices used to Test

The BrewMaster App was test with the following devices:

MacBook Pro Laptop
HP Pavilion Laptop
Samsung Galaxy S9 Mobile
iPhone XS Max

Google Chrome
Microsoft Edge
Mozilla Firefox


#### User Story Testing

The full user story testing can be found [here]().

#### Chrome Developer Tools
Constantly used to ensure the app is mobile-first, and works well with all kinds of devices and provide real-time ability to identify errors in my HTML code, and helped me troubleshoot my HTML/CSS.

#### Random User Testing
Sent the app to boyfriend and colleagues to use, collecting their feedback for bug fixes and adjustments.

#### Python Testing
PEP8online

#### MongoDB Testing

#### SQLite Testing
Two ways to test that when a user signed up they were stored in the database or it worked;
  - Used a sqlite database viewer to look at the row that was added to the table
  - I also tried signing up with the same email address again, and when I got an error, I knew the first email was saved properly, also it   redirected me ssuccessfuly to the login page.

#### Known Bugs


#### Expected Behavior
* Burger menu in mobile view immediately displays nav menu without clicking the burger.(FIXED)

* Logo Image and favicon image will not load. (FIXED)

* JS for datepicker functionality will not initiate from static/js/script.js file, it only ssuccessfuly initiates js code is directly in base.html file


***

## Deployment / Project Setup 

Download
```bash
git clone https://github.com/Honey20103/BrewMaster.git
cd homebrew_app
```

Install python3
```bash
#use brew
brew install python3
```

Install pip3
```bash
#use apt-get
sudo apt install python3-pip
```

Deploy virtual environment.
```bash
#use pip3
pip3 install virtualenv
virtualenv venv
source ./venv/bin/activiate
```

Install requirements
```bash 
# install python requirements
python3 -m pip install -r requirements.txt
```
Deploy SQLite database
```python
# python3
from app import db, create_app
db.create_all(app=create_app())
```
Deploy Mongo database
```bash 
#Setup Mongo DB account [here](https://www.mongodb.com/)
Create a mongoDB database.
Create two collections in it: recipes, ingredients
```
In a terminal, you can set the FLASK_APP and FLASK_DEBUG values:
```bash
# these gives instrcution to flask on how to load the app, it should point to the folder that holds the __init__.py.
# or create .flaskenv file and add the below without 'export'cmd
export FLASK_APP=project
export FLASK_DEBUG=1
```
Run app
```bash
flask run
```

### App Link
Find the app deployed at [this link]()


***

## Credits

### Content
The content on the site is derived from my boyfriend's self-made beer brewing log manuscript book. 

### Code
[Hover CSS effect on homepage: ](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_image_overlay_fade) This package of CSS was used to render the behaviour of the homepage front image when hovering the image, to show the about of the app.

[Blueprints and configurations in application:](https://www.youtube.com/watch?v=Wfx4YBzg16s) This tutorial helped me use Application Factory, which allows to easily create multiple instances of the app with different configurations. The Blueprints restructuring split up my app into more manageable sections i.e Auth.py, main.py and _init_.py. 

[Authentication to App:](https://www.digitalocean.com/community/tutorials) Tutorial helped with setting up authentication to webapp.

### Media 

- The logo for the project was taken from the [pngtree](https://pngtree.com/) site. 

### Acknowledgements
- I was inspired to create this website from observing the struggles I watched my boyfriends encounter by trying to keep and maintain a manual notebook to store his brew day info or records, especially thankful for the help with testing functionality of the app. Thank you Robert Flink.

- I'd like to thank tutor Tim Nelson at CodeInstitute who helped unblock me when i was completely stuck and providing extra helpful resources.






