import time
#Create a game map:  
legnth = 30
height = 20
# .----------.
# |  .       |
# |          |
# |      x   |
# |          |
# |          |
# |          |
# |          |
# |   .      |
# |          |
# |          |
# .----------.

# Set map
myMap = []

def createMap(start_x, start_y):
   print(f".{'-'*legnth}")
   #print(".{length}.".format(length="-"*legnth))
   for i in range(height):
      newLine = "|"
      for e in range(legnth):
         if start_x==i+1 and start_y==e+1:   
            newLine += "x"
         else:
            newLine += " "
      newLine += "|"
      print(newLine)
   print(f".{'-'*legnth}")
         

def loadMap(start_x, start_y):
   for i in range(height):
      newLine = []
      for e in range(legnth):
         if start_x==i+1 and start_y==e+1:
            newLine.append("x")
         else:
            newLine.append(".")
      myMap.append(newLine)



direction = "E"
myCord = {
   "x":0,
   "y":0
}
# move Snake in direction, 

def gameFlow():
   for i,line in enumerate(myMap):
      for e,element in enumerate(line):
         if element == "x":
            myMap[i][e] = "."
            if direction == "N":
               myMap[i-1][e] = "x"
               #print("North")
            elif direction == "E":
               myCord["x"] = i+1
               myCord["y"] = e+1+1
               #print(myMap[i][e+1])
               myMap[i][(e+1)%legnth] = "x"
               #print("East")
            elif direction == "S":
               myMap[i+1][e] = "x"
               #print("South")
            elif direction == "W":
               myMap[i][e+1] = "x"
               #print("West")

createMap(1, 1)
loadMap(1, 1)
def main():
   gameFlow()
   #print(myCord["x"], myCord["y"])
   createMap(myCord["x"], myCord["y"])
   time.sleep(1)

while True:
   main()



