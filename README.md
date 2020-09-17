<p align="center">
  <img src="https://github.com/Honey20103/BrewMaster/blob/master/assets/images/brewmaster1.png" style="margin: 0;" width="150" height="150" >
</p>

# Brew Master 
> Home beer brewing logs and recipes. 
This repo hosts the assets used to build the Brew Master website / web application. A web application focused on offering passionate home beer brewers a platform they could utilise to log the entire process and steps taken during brew day. 

>The Brew Master app will help home brewers improve on their brewing process and end result of the beer batches, by having a log/diary of each recipe they will be able to defer to for future brew days.

***

### Background
The idea of this application was birthed from my boyfriend who does homebrewing as a hobby. During a normal brew day he would have a notebook logging and taking notes on the entire process of the specific recipe on the day, these would include temperatures etc. Notes would be taken for each process such as the mashing, lautering, boiling, cooling, fermentating, maturing(carbonation) and packaging steps.
When he needed to repeat the same brew, or after tasting the batch he would go back to his notebook to review notes and look at ways to improve or change some of the parameters in the brew such as temperatures for boiling and cooling and ingredient amounts. 

Hence, this is where the app idea stemed from. And thus away with the notebook, and hello 21st century logging or technology. He will now be able to write done his brew day notes in the application, easily return to recipes to edit and make changes, and have his recipe logs available on a database online. No fear for loss of the notebook and easy access.

The application will be available to the public in the future as a beer brewing recipe site and ability to review the recipes.


***

### Website
A live demo can be found here [here](xxx)

[Home iPhone](xxx)

[Home iPad](xxx)

[Recipe iPhone](xxx)

[Recipe iPad](xxx)

[Form iPhone](xxx)



***

## UX

### User stories
- As an amateur home brewer, it is important to take record of the entire process of brew day,
inorder to learn from my previous mistakes and help improve my future batches.

- I often record my brew day notes or logs on a physical notebook, or sometimes the closest paper I
can find, and in some cases I lose it and there goes my brew record, no recollection of what was done.

- As a faily confident home brewer, I need an application to store my recipes and eventually start a microbrewery or make a profit from my home made recipes.

- I am quite new to brewing, and I often make mistakes and need to change things in my notes, my notebook ends up looking like a childs scrapbook. Having digital notebook will help with keeping my notes neat and easily editable.

- As a user I would like to be able to see other brewer's processes, mistakes and results to improve my own brewing techniques.

- Beer brewing is quite an expensive hobby, having to view other brewers recipes saves me the need buy brew recipes from companies.

- I'd like the ability to rate the different brew recipes I make, inorder to know which ones to repeat.

- As a user I can view all brew recipe logs, with information such like date of log.

- As a user I can search for recipes/logs.

- As a user I am able to add new brew logs to the database.

- As a user I am able to edit existing recipes/logs.

- As a user I am able to add new ingredients not available in the database.

- As a user I am able to delete recipes.

- As a user I am able to create an account.

- As a user I am able to log into my account.

- As a user I am able to log out.

- As a brewer i would like to update a recipe/log by uploading a photo of the final result of my beer at the end of the process.



### Strategy
My goal in the design was to make it as easy as possible for users to log their brew day process and log the  recipes, to have a clean look with no clutter or information over load by having a user-friendly and minimalistic design.

### Scope
For the users I wanted to provide them with a functional platform to keep their brew records, lessen the burden of log keeping on physical notebooks and eventually serve as a recipe storage. 

Scope has full CRUD functionality for logs.

* A landing page that acts as a brewing diary , showing all logs recorded by the user.
* A 'Log' page that displays the recipe and process of the beer they made.
* A 'Create log' page that allows the user to add new log into their brewing diary/database.
* An 'Edit recipe' page that allows the user to update and then saves to database.
* A 'Create ingredient' allows the user the ability to add new ingredients as they create a new log.

### Structure


### Skeleton

Initial wireframes were done on paper and pen, I'll probably at a later stage add a design made in Balsamic, it was abit challlenging to figure out how I wanted the UX to be, although my idea was to maintain a clean and minimalistic look, and easy to use. The look and feel is intentionally planned for mobile and desktop.

### Wireframes

[Home Page](https://github.com/Honey20103/BrewMaster/blob/master/wireframes/homepage.png)

[Login Page](https://github.com/Honey20103/BrewMaster/blob/master/wireframes/loginpage.png)

[Brew Log Page](https://github.com/Honey20103/BrewMaster/blob/master/wireframes/logpage.png)

### Database Schema

- [MongoDB database scheme]

### Surface
My idea for design is to have colour relating to beer such like brown, gold, or essentially brown theme color palette, this will help users associate with the act of beer brewing.

![Colour Scheme]<img src="https://github.com/Honey20103/BrewMaster/blob/master/wireframes/themecolor1.png" style="margin: 0;" width="400" height="400" >


![Colour Scheme](https://github.com/Honey20103/BrewMaster/blob/master/wireframes/themecolor2.png "colour scheme2")


***

## Features

### Existing Features

* **User Accounts** - Signup for an account, log-in and log-out.
* **Rating system** - The ability to star rate favorite brew day recipe.
* **Log/Recipe page** - When a recipe or brew log is selected the user will be presented with the page for that recipe. 
* **Add Log/Recipe** - The user can go to the menu and open the add log brew day page, providing the user a diary or digital like notebook to log their brew day content and add them to the database.
* **Add Ingredient** - Ingredient options will be available however if an option is not found, the user is abale to add a new ingredient to the database.
* **Edit & Delete ingredients** - Ability for the user to edit and delete ingredients.

### Future Features

- Ability to have more profiles for multiple beer brewers to log their recipes.
- Ability to update a log by adding an image or images of the final brew result.

***

## Technologies Used

### Frontend

* [HTML](https://en.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [Bootstrap](https://getbootstrap.com/)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Materialize](https://materializecss.com/)


### Backend

* [MongoDB](https://www.mongodb.com/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Python](https://www.python.org/)

### Deployed

* [Heroku](https://www.heroku.com/)

***

## Testing

#### Code Validation

#### User Story Testing

Read the full user story testing 

#### Chrome Developer Tools
Constantly used to ensure the app is mobile first, and works well with all kinds of devices and provide real time ability to identify errors in my html code, and helped me troubleshoot my html/css.

#### Random User Testing
Sending the app to friends & colleges to use, collecting their feedback for bug fixes and adjustments.

#### Python Testing

#### MongoDB Testing



#### Known Bugs


#### Expected Behavior
* 

*

*


***

## Deployment / Project Setup 

### Setting up a MongoDB Database
- Set up a mongoDB database.
- Create the following collections: `log`, `ingredients`.

### Backend -Locally
- Clone this directory to your local computer.
- Create a virtual enviroment
`virtualenv venv`.
- Activate the virtual environment `source venv/bin/activate`.
- Change to the backend folder `cd backend`.
- Do a pip install for all dependancies & dev dependancies `pip install -e .[dev]`.
- Create a `.env` file with the following content
  ```
  MONGO_URI="$MONGO_URI"
  ```
  where `$MONGO_URI` is the URI to your database.
- Run the backend `flask run --reload`.
- Leave this terminal window open and running.

### Frontend -Locally
- Open a second terminal window.
- Change to your front end directory `cd frontend`.
- Install all dependancies `npm install`.
- Start the frontend `npm start`.


### Deploy to Heroku
These instructions assume you have a github account and a Heroku account, and have set up the Heroku CLI on your computer.
- Clone this git repository to your own github account
- Run the following commands
  ```bash
  heroku apps:create $APP_NAME --region eu
  heroku stack:set container -a $APP_NAME
  heroku config:set -a $APP_NAME MONGO_URI="$MONGO_DB_URI"
  ```
  where `$APP_NAME` is the name of your Heroku app, and `$MONGO_DB_URI` is
  your MongoDB
- On the Heroku website, in your new app, connect to your github
- Select the repo you have cloned
- On the deploy tab manually deploy

### App Link
Find the app deployed at [this link]()


***

## Credits

### Content
The content on the site is derived from my boyfriend's self-made beer brewing log manuscript book. 

### Media 

- The logo for the project were taken from the [pngtree](https://pngtree.com/) site. 

### Acknowledgements
- I was inspired to create this website from observing the struggles i watched my boyfriends encounter by trying to keep and maintain a manual notebook to store his brew day info or records.






