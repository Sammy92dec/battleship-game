# Battleship Game

A strategic board game played by one player. In this case, this game will be played by guessing randomly hidden ships. The program allows you to guess by row and column.The aim is to find 3 ships using your 20 chances.This game is made with simple python language.

Here is a live link to the game :- https://thebattleshipgame-86288aeb3d78.herokuapp.com/

<img src="assets/images/maindisplay.png">

# Table of contents
1. [Battleship Game](#battleship-game)
2. [How to play](#how-to-play)
3. [User Stories](#user-stories)
4. [Features](#features)
    * [Existing Features](#existing-features)
    * [Future Features](#future-features)
    * [Language used](#languages-used)
5. [Testing](#testing)
    * [Solved Bugs](#solved-bugs)
    * [Validator testing](#validator-testing)
    * [Unfixed bugs](#unfixed-bugs)
5. [Deployment](#deployment)
6. [Credits](#credits)
    * [Content](#content)
    * [Acknowledgements](#acknowledgements)

# How to play

The rules of the game are fairly simple. It begins by asking the player to choose a username and their board is created. The user will select a row and column from 0 - 9. After both a valid row and column are entered by the user, a sign is displayed on the board depending on whether or not their guess was correct. If the user managed to hit a ship successfully, they are told their guess was correct by seeing "X" displayed on the board which corresponds with the row and column selected by the user. If their guess was incorrect, however "O" is displayed on the board. If the user happens to select a row or column outside of that range or enter an unrecognized key, they will be given an error message and asked to type in a valid row.

The player has a total of 3 ships to sink on the board. Once they run out of rounds and not total of 3 ships are hit, they are presented with a game-over message and the game ends. If the user successfully manages to guess the correct position of all ships, however, then they are presented with an congratulatory message and told they have sunk all ships.


## User stories
A simple and fun game to play.
Easy to understand the structure of the webpage. 


#### User goals
To play a fun game.
To  play a game that is easy to navigate and understand.

## Future Implementations

- To set a break for best out of five.
- To be able to start over without pressing run program.
- To have players board. 

## Languages Used

- Python

### Testing

- Used PEP8 to test the code.All it gave me back was white space and spaces between the funtion.

## Solved bugs
 
- Fixed invalid name that it won't accept signs or numbers.
Added a def 

# Deploying to Heroku
Go to Heroku, create account if you don't have and log in.
Head to your dashboard and click "New", then "Create new app"
New/CreateNewApp
Next step is to give your app a name and to choose region. After that click on "Create app".
Name/Region/Create
After that head to "Settings" tab which you can find on top of your Heroku page.

Then in the "Buildpacks" section you will need to add buildpacks. Pay attention to the order in which you add buildpacks you need. In my case I had to add Python first and nodejs second.

First add "Python", by clicking on Python icon and then click on "Add Buildpack".

Then add "nodejs", by clicking on nodejs icon and then click on "Add Buildpack".

Then head to "Deployment" tab which you can also find on top of your Heroku page and under "Deployment method" click on "GitHub"(in my case that's where my repository is).

After that, just under the "Deployment method" section is "Connect to GitHub" section where you need to find your repository and then click on "Connect".

Just under "Connect to GitHub" section is "Automatic deploys" section where you can click on "Enable Automatic Deploys" if that's what you want and just under is "Manual Deploy" section, where you need to click on "Deploy Manually".