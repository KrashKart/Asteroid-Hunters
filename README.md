# Asteroid Hunters
## Video Demo:  https://youtu.be/PrBYKTbEQ9I
### Description:
A simple space shooter game

Using the W, A, S, D keys, move your spaceship around and avoid the asteroids. Use the spacebar to fire a missile
to destroy the rockets, but beware; the missiles have a limited rate of fire so use them wisely.

You have 3 lives, and every asteroid destroyed gives 100 points. Every few seconds of survival adds 100 points.

Asteroids spawn as time elapsed increases.

### Structure
The player, asteroid and missile sprites have their separate classes stores in entities.py, loaded in from
the respective image files. Each sprite class (player, asteroid, missile) have their own movement patterns
encapsulated within themselves. The player moves with keyboard inputs (in the __main__ game loop), the
asteroids have random x and y coordinate spawns and move down with constant y speed and missiles spawn at the
player position and move up with constant y speed. All sprites are redrawn and updated every game loop on the screen (in __main__).

The screens and visuals exist in visuals.py. visuals.py firstly initiates the engine, window and game background.
visuals.py is also runs the "pause", "game over" and title game state screens and contain most of the visual
assets.

### Challenges

#### Learning Pygame
I had to pick up a completely new module and its syntax. Having learnt Machine Learning before this,
I found the switch to Game Development (if you could call it that for such a small project) difficult.
In addition, I did not want to spend too much time on this project so I decided to keep the features minimal.

Due to my limited knowledge in Game Dev and pygame, the code might be inefficient and long, but I feel like I
tried my best and am decently proud of it


#### Title, Pause and Game Over screens
This was by far the hardest challenge. Coding separate sceens and transitioning between the "start game",
"quit" and "pause" game states was the most confusing. I opted to think of it in terms of game loops to
avoid confusion, which worked out decently

Adding the responsive buttons was also a challenge, but with the help of the blog mentioned in credits.txt,
I managed to make it work OK

#### OOP
A minor challenge was understanding how object-oriented programming integrated into game development. I had
studied this concept in courses but have not implemented it myself. Understanding that game objects can
encapsulate properties and functions in a game context enabled me to control game variables much more easily.

### Takeaways
This project was quite painful for me since I was a slow learner, and although the final product seems
very shoddily-made, I was still quite proud of it since this was done over the course of 9 hours in a
single day.

This project also forced me out of my comfort zone to try new things like game development. Besides
expanding my portfolio of projects, I had gained new insight into what game design looks like at the
basic level.

Screen design and Object-Oriented Programming featured heavily in this project, and I have gained
newfound appreciation for the ease of access and readability that classes and encapsulation provides.
In addition, I now have better knowledge on how to create responsive buttons and windows in Python with
Pygame.

Overall, I would like to thank CS50P for reinforcing my Python knowledge and even introducing new concepts
to me like unit testing, and reaffirming my understanding of Python. Hopefully, I have improved in my Python
coding skills and have emerged an overall better programmer.
