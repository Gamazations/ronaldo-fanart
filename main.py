# Name: Abdullah Zahir
# An animation of world renowned and famous soccer player, Cristiano Ronaldo doing his famous "SIUUU!" celebration.
# Background
Rect(0, 0, 400, 400, fill='black')

#BallonDor
#Creates an image of the trophy, "Ballon D'or".
#This image appears twice. The trophy is similar to a golden soccer ball, and appears to the right and left of Cristiano Ronaldo. 
#It also lists how many times he has won this prestigious award, which has been 5 seperate times
def BallonDor(x, y):
    Circle(x, y, 30, fill=gradient(rgb(224, 175, 38), rgb(168, 132, 32), start='top'))
    Polygon(x-30, y+40, x-20, y+30, x+20, y+30, x+30, y+40, fill=gradient(rgb(224, 175, 38), rgb(168, 132, 32), start='top'))
    Label("5x Ballon d'or", x, y+50, size=20, fill=gradient(rgb(224, 175, 38), rgb(168, 132, 32), start='top'))

# Body parts (Head & Neck)
Rect(175, 105, 40, 40, fill=rgb(199, 175, 154), rotateAngle=-5)
Rect(155, 70, 15, 45, fill=rgb(199, 175, 154))

# Shorts
Rect(150, 325, 100, 40, fill='white')
Rect(125, 325, 60, 100, fill='white', rotateAngle=25)
Rect(215, 332, 60, 100, fill='white', rotateAngle=-25)

# Lines on shorts
Line(150, 325, 115, 400, fill='black')
Line(155, 325, 120, 400, fill='black')
Line(240, 325, 275, 400, fill='black')
Line(245, 325, 280, 400, fill='black')
Line(125, 325, 275, 325, fill='black')

# Jersey
Rect(125, 150, 150, 175, fill=gradient('red', rgb(194, 14, 27), start='top'))

# Defining physique
Oval(110, 260, 50, 120, fill='black')
Oval(120, 300, 50, 120, fill='black')
Oval(290, 260, 50, 120, fill='black')
Oval(280, 300, 50, 120, fill='black')

#Stars
#Stars on the side of him
Star1 = Star(60, 270, 30, 5, fill='gold')
Star2 = Star(340, 270, 30, 5, fill='gold')

#arms
#Used for the resting position prior to Mouse Click and upon Mouse Release
Forearm1 = Rect(10, 200, 50, 35, fill=rgb(199, 175, 154), rotateAngle=-25)
Arm1 = Rect(-15, 190, 60, 35, fill=rgb(199, 175, 154), rotateAngle=50)
Arm2 = Rect(340, 200, 50, 35, fill=rgb(199, 175, 154), rotateAngle=25)
Forearm2 = Rect(360, 190, 60, 35, fill=rgb(199, 175, 154), rotateAngle=-50)

#Used for the "SIUUU!" celebration upon Mouse Click
Forearm3 = Rect(60, 260, 75, 31, fill=rgb(199, 175, 154), rotateAngle=-75, visible=False)
Forearm4 = Rect(270, 260, 75, 31, fill=rgb(199, 175, 154), rotateAngle=75, visible=False)

# Shoulders
#Used for the resting position prior to Mouse Click and upon Mouse Release
Shoulder1 = Rect(50, 160, 125, 50, fill=gradient('red', rgb(194, 14, 27), start='top'), rotateAngle=-25)
Shoulder2 = Rect(225, 160, 125, 50, fill=gradient('red', rgb(194, 14, 27), start='top'), rotateAngle=25)
Polygon(125, 150, 150, 135,  250, 135, 275, 150, fill='red')

#Used for the "SIUUU!" celebration upon Mouse Click
Shoulder3 = Rect(95, 145, 40, 105, fill=gradient('red', rgb(194, 14, 27), start='left'), rotateAngle=15, visible=False)
Shoulder4 = Rect(270, 145, 40, 105, fill=gradient('red', rgb(194, 14, 27), start='right'), rotateAngle=-15, visible=False)

# Design on the Jersey
Rect(185, 135, 20, 30, fill='white')
Polygon(195, 135, 190, 150, 200, 150, fill='black')
Rect(185, 295, 20, 30, fill='white')
Line(195, 295, 195, 325, fill='black', lineWidth=2)
Line(195, 150, 195, 165, fill='black', lineWidth=2)

# Armpatches on Jersey
#Used for the resting position prior to Mouse Click and upon Mouse Release
Patch1 = Polygon(73, 185, 73, 160, 103, 160, 103, 185, fill='white', rotateAngle=-25)
Patch3 = Polygon(93, 195, 93, 165, 113, 165, 113, 195, fill='white', rotateAngle=15, visible=False)

TriPatch1 = Polygon(93, 184, 74, 173, 93, 163, border='blue', fill='white')
TriPatch3 = Polygon(93, 184, 93, 163, 112, 173, border='blue', fill='white', visible=False)

Circle1 = Circle(84, 180, 5, fill='white', border='blue')
Circle3 = Circle(100, 186, 5, fill='white', border='blue', visible=False)

#Used for the "SIUUU!" celebration upon Mouse Click
Patch2 = Rect(308, 169, 30, 20, fill='white', rotateAngle=25)
Patch4 = Rect(284, 169, 24, 30, fill='white', rotateAngle=-15, visible=False)

TriPatch2 = Polygon(323, 184, 314, 169, 330, 169, fill='white', border='blue')
TriPatch4 = Polygon(288, 170, 304, 175, 288, 190, fill='white', border='blue', visible=False)

Circle2 = Circle(323, 180, 5, fill='white', border='blue')
Circle4 = Circle(296, 190, 5, fill='white', border='blue', visible=False)



# Hair 
Star(195, 115, 10, 7, fill=rgb(46, 42, 41))
Star(185, 115, 15, 7, fill=rgb(46, 42, 41))
Star(180, 115, 15, 7, fill=rgb(46, 42, 41))
Star(190, 115, 15, 7, fill=rgb(46, 42, 41))
Star(195, 113, 15, 7, fill=rgb(46, 42, 41))
Star(200, 114, 15, 7, fill=rgb(46, 42, 41))
Star(205, 110, 15, 7, fill=rgb(46, 42, 41))
Star(210, 110, 15, 7, fill=rgb(46, 42, 41))
Oval(193, 85, 60, 70, fill=rgb(46, 42, 41))
Oval(175, 60, 60, 30, fill=rgb(46, 42, 41))
Star(210, 105, 15, 7, fill=rgb(46, 42, 41))
Star(210, 100, 15, 7, fill=rgb(46, 42, 41))
Star(212, 95, 15, 7, fill=rgb(46, 42, 41))
Star(213, 90, 15, 7, fill=rgb(46, 42, 41))
Star(215, 85, 15, 7, fill=rgb(46, 42, 41))
Star(215, 80, 15, 7, fill=rgb(46, 42, 41))
Star(210, 75, 15, 7, fill=rgb(46, 42, 41))
Star(177, 105, 15, 7, fill=rgb(46, 42, 41))
Star(177, 100, 15, 7, fill=rgb(46, 42, 41))
Star(175, 95, 15, 7, fill=rgb(46, 42, 41))
Star(174, 90, 15, 7, fill=rgb(46, 42, 41))
Star(172, 85, 15, 7, fill=rgb(46, 42, 41))
Star(172, 80, 15, 7, fill=rgb(46, 42, 41))

# Ronaldo Name and Number on Jersey
Label('R', 150, 190, fill='white', size=25, rotateAngle=-20, font='arial', bold=True, border='black')
Label('O', 165, 185, fill='white', size=25, rotateAngle=-15, font='arial', bold=True, border='black')
Label('N', 180, 180, fill='white', size=25, rotateAngle=-10, font='arial', bold=True, border='black')
Label('A', 195, 177, fill='white', size=25, font='arial', bold=True, border='black')
Label('L', 210, 180, fill='white', size=25, rotateAngle=10, font='arial', bold=True, border='black')
Label('D', 225, 185, fill='white', size=25, rotateAngle=15, font='arial', bold=True, border='black')
Label('O', 240, 190, fill='white', size=25, rotateAngle=20, font='arial', bold=True, border='black')
Label('7', 200, 240, fill='white', size=100, bold=True, font='cinzel', border='black')

# Cool Quote
Quote = Label('Wreathed in Red', 90, 15, fill='red', size=30, font='sacramento')

#Using "BallonDor" Functions as Defined Above
BallonDor(60, 60)
BallonDor(340, 60)

#Label for "SIUUU!" that appears upon Mouse Click
Siu = Label('SIUUU!', -100, -100, size=40, fill='white', font='arial')

#SiuCelebration
#This function puts Cristiano Ronaldo in his famous celebration, which is called the "SIUUUU!". This celebration is world famous and a
#very popular celebration in which Cristiano Ronaldo puts both his hands to the side of his hips and screams "SIUUUU!"
#My code moves his hands from their current position to their "SIUUUU!" position, which immitates him doing the celebration.
#This code also spawns the "SIUUUU!" upon mouse click wherever the user clicks it. This also moves the quote "Wreathed in Red" to the right.
#Additionally, this also moves the two stars on both sides of Cristiano Ronaldo up by 10 pixels, and makes the color "gold"
def onMousePress(mouseX, mouseY):
    #This part moves the different objects on the screen
    Quote.centerX+=5
    Star1.centerY-=10
    Star1.fill='gold'
    Star2.centerY-=10
    Star2.fill='gold'
    #This makes the "SIUUU!" visible and wherever the person clicks
    Siu.visible=True
    Siu.centerX = mouseX
    Siu.centerY = mouseY
    #This changes the individual components to make Ronaldo seem as if he is doing the "SIUUU!" celebration
    Shoulder1.visible=False
    Shoulder2.visible=False
    Forearm1.visible=False
    Forearm2.visible=False
    Arm1.visible=False
    Arm2.visible=False
    Patch1.visible=False
    TriPatch1.visible=False
    Circle1.visible=False
    TriPatch2.visible=False
    Circle2.visible=False
    Patch2.visible=False
    Shoulder3.visible=True
    Patch3.visible=True
    Circle3.visible=True
    TriPatch3.visible=True
    Shoulder4.visible=True
    Patch4.visible=True
    TriPatch4.visible=True
    Circle4.visible=True
    Forearm3.visible=True
    Forearm4.visible=True
  
#Release  
#This function puts Cristiano Ronaldo back into his position prior to how he was before the "SIUUUU!" celebration and resets his position.
#It also removes the "SIUUUU!" text so that it is reset fully and able to be reused. Upon Mouse Release the Star's colors get changed to 
#rgb(168, 132, 32), which is a brownish-goldish kind of color.
def onMouseRelease(mouseX, mouseY):
    #This changes the Star Color
    Star1.fill=rgb(168, 132, 32)
    Star2.fill=rgb(168, 132, 32)
    #Makes the "SIUUU!" invisible so it is reset
    Siu.visible=False
    #Resets the entire code back to how it was before hitting the "SIUUU!", in it's original position
    Shoulder1.visible=True
    Shoulder2.visible=True
    Forearm1.visible=True
    Forearm2.visible=True
    Arm1.visible=True
    Arm2.visible=True
    Patch1.visible=True
    TriPatch1.visible=True
    Circle1.visible=True
    TriPatch2.visible=True
    Circle2.visible=True
    Patch2.visible=True
    Shoulder3.visible=False
    Patch3.visible=False
    Circle3.visible=False
    TriPatch3.visible=False
    Shoulder4.visible=False
    Patch4.visible=False
    TriPatch4.visible=False
    Circle4.visible=False
    Forearm3.visible=False
    Forearm4.visible=False
    
