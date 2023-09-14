"""Implement a class called player that represents a cricket player. 
The player class have a method called play(), which prints "The player is playing" 
Derive two classes Batsman and Bowler from the player class. 
Override the play() method in each derived class to print "The Batsman is batting" and"The Bowler is bowling "
Write a program to create objects of both the bowler and batsman classes and call the play() method for each object """

#Define the base class player 
class player:
 def play(self):
   print("The Player is  playing cricket")
#Define the dreived class Batsman 
class Batsman(player):
  def play(self):
    print("The Batsman is batting")
    #Define the derived class bowler
class Bowler(player):
  def play(self):
   print("The Bowler is bowling ")
#Create objects of Batsman and Bowler
batsman=Batsman()
bowler=Bowler()
#Call the play()method for each object 
batsman.play()
bowler. play()