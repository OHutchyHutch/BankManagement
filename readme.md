Hello! If I did this correctly, you should see this file on the right side of your screen. This file is my guide to the code and explanation of everything. You can open the other files and this will remain open on the right side of your browser.


Now, let's get started by opening user.py

# user.py 
User.py is quite simple, it's just a bunch of simple getter/setter functions (functions that do nothing but get a value or set a value). 

First we have ```def __init__```, 
* this is a common function across the classes as it's what the class is created with and requires. To create a user, you **NEED** a name, password, and $ amount. 

```getName```
* This just simply gets and returns the name of the currently accessed user

```checkPassword```
* Compare the string from the argument and the user's password. Return ```True``` if matched.

```getMoney```
* Return the user's money 

```addMoney```
* Add the value from the arguments to the user's local value

```removeMoney```
* Remove the value from the arguments from the user's local value

# Next, bankusers.py
At its core, bankusers is a manager for users. Think of it like a chest, where you store your toys (users) into and can access all of them from there. To do so, we need to import users

```__init__```
* Initialize the bankusers object with an array of users.

```accessUsers```
* Return the array of users

```addUsers```
* Add to the array a new user with the values from the arguments of username, password, and deposit

# Now, login.py
In case you haven't noticed by now, this program can be thought of as a ladder. Where each step (class) requires the last. As the name implies, login is used to check if a user exists and to create one if they do not and then to log them into their account. To do this, we'll need to import bankusers (which imports users aswell)

```__init__```
* Initialize the login object with the bankusers class.

```isRegistered```
* Ask if the user already has an account. If not, take a series of inputs and create an account with $0 in the account. Then proceed to login

```loggingIn```
* We use a while loop here incase an input is incorrect, we can quickly and easily restart the login process without having to restart the entire program. First, we ask for the username. We then go through the bankUsers to see if that username exists. If it does, then we promptand store the user to ```accessedUser```. If it does not, we restart. Then, if a username was correct and with accessedUser already stored for easy access, we prompt the user for a password. We then compare that password with accessedUser's password. If they match, return ```True``` and ```accessedUser``` (you'll see why soon)

# Finally, main.py
![Oh yeah, it's all coming together] (https://media1.tenor.com/images/b4a67ab17be1e0e1d1be76cecc2ca9cd/tenor.gif)
Main.py is the boss of the whole operation. We need to import every class for main.py (this is because we want to have full control of all functions here. If you play your cards right and move things around, you could only require a single class if you really wanted)


Next, we will create the bankUsersClass variable and make it the bankusers.py class with an empty array. Then, we will intialize login with the class we just created .

```isLoggedIn, accessedUser = login.isRegistered()``` is probably a confusing line to read at first, but as you know to initialize a variable it's just x = 2. Why couldn't we initialize 2 variables at the same time? Recall how in login.py's loggingIn we have it return ```True``` **AND** ```accessedUser```. That is exactly what this does. We will give the bool ```True``` to isLoggedIn and the ```accessedUser``` to the ```accessedUser``` in the main class.

At this point, we are officially considered to be logged in. Here we will prompt the user on what they want to do. Depending on their response, depends on what we will do. We will then run the function with the ```accessedUser``` we just assigned and bam. You got a working bank system!