minecraft-quiz
==============

Minecraft Quiz on a Raspberry Pi

These files are designed for teachers to use with a raspberry pi in the classroom as a fun way of getting a whole class (or more)
of students competing against each other by answering questions in order to build blocks in a shared minecraft world.

![Example](https://cloud.githubusercontent.com/assets/760604/5298811/1f21e84e-7bb8-11e4-95df-3c773aacc7ac.jpg)

You can add your own questions. The quiz also tests students on being able to convert to/from binary / decimal and hexadecimal (although you can get them to use a converter if you've not taught them how yet!)

Credits
=======

The code in this project has been developed by Pete Dring from Manor CE Academy in York. It's free for anyone to use, adapt and share. See the licence document for more details.

This project works alongside Minecraft: Pi Edition which is available for free from: http://pi.minecraft.net/
The following files included in this project have been copied from the Minecraft: Pi Edition python api
* block.py
* connection.py
* event.py
* util.py
* vec3.py

These files have been created and shared by Mojang but I can't find any copyright info or restrictions relating to them. If you think they shouldn't be included here, let me know and I'll remove them. You can download them from: http://pi.minecraft.net/

Instructions
============

Getting started:
---------------
* First, you need to have have a raspberry pi with Minecraft installed and running. Follow instructions on http://pi.minecraft.net/
* The quiz uses figlet to display messages. To install it, open a terminal and type: `sudo apt-get install figlet`
* Download all of the source files from this project to your raspberry pi by typing `wget https://github.com/pddring/minecraft-quiz/archive/master.zip`
* Extract the zip archive by typing `unzip master.zip`


Setting up the quiz:
--------------------
* Go into the minecraft-quiz-master folder by typing `cd minecraft-quiz-master`
* Change the questions you want in your quiz by typing `nano questions.txt`
* The questions work as a list of keywords followed by definitions on the next line. Feel free to keep, edit or replace the existing questions. You can add new questions.
* Exit the editor by pressing Ctrl + X (save if you've made any changes)
* Generate a list of coordinates for a message that you want displayed in minecraft by typing `python mcquiz.py`
* - Enter the message you want to display in minecraft (e.g. Welcome to Code Club)
* - Enter the x coordinate of where you'd like the text to appear in minecraft(or 0 if you're unsure)
* - Enter the y coordinate of where you'd like the text to appear in minecraft (40 is usually fine for 4 words, 50 for 5 words etc...)
* - Enter the z coordinate of where you'd like the text to appear in minecraft (0 if you're unsure)
* The coordinates will then be saved to message.csv ready to be used in the quiz
![Setting up the quiz](https://cloud.githubusercontent.com/assets/760604/5298477/4b411142-7bb4-11e4-8a33-2311ed162c57.png)

Running the quiz:
-----------------
* Find out the ip address of your raspbery pi by running `ifconfig` and ask the students to connect to that ip address
![Finding the ip address](https://cloud.githubusercontent.com/assets/760604/5298526/e30123be-7bb4-11e4-8692-d504b77989c2.png)
* Get each student to log in to their own computer / laptop and open putty (you can download it from here: http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)
![Connecting via putty](https://cloud.githubusercontent.com/assets/760604/5298557/23a1b460-7bb5-11e4-8438-3429460385c6.png)
* Start minecraft on the raspberry pi by following the instructions on http://pi.minecraft.net/
* Get students to log in and run the quiz by going to the right folder and typing `python playquiz.py`

How the quiz works:
-------------------
* Students will be asked to enter their name and choose a team
![Joining the quiz](https://cloud.githubusercontent.com/assets/760604/5298479/4b44f0aa-7bb4-11e4-9f38-9f7fff7acad0.png)
* They'll get given a question at random with 4 random possible answers, one of which is the right answer.
![Attempting a question](https://cloud.githubusercontent.com/assets/760604/5298478/4b416e08-7bb4-11e4-83a5-fe9e23efd3a4.png)
* If they get the answer right, they'll get given the coordinates for a block in minecraft
* They have to convert the coordinates to/from binary/decimal/hexadecimal 
* If they convert both coordinates correctly, they get a point and the block will appear in the minecraft world on the raspberry pi
![Converting coordinates](https://cloud.githubusercontent.com/assets/760604/5298476/4b40d754-7bb4-11e4-852c-bc9947b47eff.png)

Useful cheats:
==============
Here are some commands that you can use to control the minecraft quiz. You can type them in at the start of the quiz at the welcome screen:
![cheats](https://cloud.githubusercontent.com/assets/760604/5298631/318265ce-7bb6-11e4-8615-fc7802638489.png)
* `o:test` displays the whole message in minecraft in randomly chosen wood, tnt and leaves blocks
* `o:clear` clears an area in minecraft from (0, 0, 1) to (90, 80, 1) which is normally the area where text is displayed
* `o:board` displays a glass grid in minecraft showing where the text is likely to appear
* `o:test WOOD` shows the whole message in minecraft in wood
* `o:test TNT` shows the whole message in minecraft in TNT
* `o:test LEAVES` shows the whole message in minecraft in leaves
* `o:clues` shows 10 randomly chosen blocks in either wood, tnt or leaves (useful if a class can't guess the word in minecraft and they're running out of time)
