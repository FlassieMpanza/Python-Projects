#Student no.: MPNFLA001
#Assignment 1

#Question 1
import math
#Coordinates of variable A
X = 1000.0 
Y = 2000.0 
#The Distance and Bearing of point B from point A
dist = 5136.64             #in metres
deg = 45.67                #in degrees
d_ra= deg *(math.pi/180)   #converting the bearing from degrees to radians

#Calculating coordinates of B
B_x = dist*math.cos(d_ra) + X
print('The X coordinates of B:',B_x)
B_y = dist*math.sin(d_ra) + Y
print('The Y coordinates of B:', B_y)

#Displaying results in a text file
resultsfile = 'C:/Users/FLASSIE S MPANZA/OneDrive - University of Cape Town/APG40097/Assignment 01/MPNFLA001.txt'
results = open(resultsfile,'r+')
results.write('Bx coordinate:' + str(B_x))
results.write('\n')
results.write('By coordinates:' + str(B_y))
results.close()

#Question 2
#Creating a paragraph
Sunika = 'I love animals beacause they are loyal and friendly, and I also love reading'

#Saving the paragraph as a text file
with open('Sunika.txt', 'w') as file:
    file.write(Sunika)

    
    

