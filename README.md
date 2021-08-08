# The-Chain-Game
The Atom Chain reaction game using PyGame - Python, Inspired and based on the popular game Chain Reaction on Play Store.

## Acknowledgements:
Inspired and based on the popular game Chain Reaction on Play Store.

## Using:
Pygame, sys, math Libraries - Python

# Description
A strategy game for 2 to 8 players.
The objective of Chain Reaction is to take control of the board by eliminating your opponents' orbs.
Players take it in turns to place their orbs in a cell. Once a cell has reached critical mass the orbs explode into the surrounding cells adding an extra orb and claiming the cell for the player. A player may only place their orbs in a blank cell or a cell that contains orbs of their own colour. As soon as a player looses all their orbs they are out of the game.

Default: 4 PLayers. 
You can change no. of players from Line 30.
```
noPlayers = 4
```
You can change the color for each Player from line 24.
```
#--Customize player-color here  --1,2,3,4 --#
playerColor = [red, green, violet, yellow, white]
```
for colors other than listed in code (red,white,blue,green,violet) you can add the color and its rgb value on line 21-22 onwards.
Example-
```
orange = (244, 128, 0)
grey = (160,160,160)
```
## Contribution:
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.  
