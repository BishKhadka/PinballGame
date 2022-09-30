#Bishal Khadka
#Apr 20, 2022
#CS152 B

'''As I added more features to the pinball scence as a part of extension, there are some changes from just what is required in the project. 
To get the results excluding extension, uncomment down line 29, add triangle1 in line 32 list, follow instruction on line 45, comment line 52-61, line 68-74, 
line 97-98 and line 103-125)'''
'''Use left and right arrow key when you run this script to control the block at the bottom'''
#importing required moduels
import physics_objects as pho
import graphicsPlus as gr
import collision
import random

def buildObstacles(win):
    '''bulds obstacles with different shapes'''

    ball1 = pho.Ball(win, radius=2, x0=13, y0=30)  #creating ball
    ball2 = pho.Ball(win, radius=1.5, x0=20, y0=20)
    ball3 = pho.Ball(win, radius=2, x0=37, y0=30)
    ball4 = pho.Ball(win, radius=1.5, x0=30, y0=20)   
    block1 = pho.Block(win, width = 15, height = 5, color = [0,100,200], x0=5, y0=43)  #creating block
    block2 = pho.Block(win, width = 15, height = 5, color = [0,100,200], x0=45, y0=43)
    block3 = pho.Block(win, width = 10, height = 5, color = [0,100,200], x0=5, y0=20)
    block4 = pho.Block(win, width = 10, height = 5, color = [0,100,200], x0=45, y0=20)
    block5 = pho.Block(win, width = 2, height = 50, color = [150,100,0], x0=0, y0=25)
    block6 = pho.Block(win, width = 2, height = 50, color = [150,100,0], x0=50, y0=25)
    block7 = pho.Block(win, width = 50, height = 2, color = [150,100,0], x0=25, y0=50)
    #triangle1= pho.Triangle(win, width=7, height=3, color = [0,0,0], x0 = 25, y0=10)  #this triangle was created before the extension
    triangle2= pho.Triangle(win, width=10, height=3, color = [0,0,0], x0 = 10, y0=10)    
    triangle3= pho.Triangle(win, width=10, height=3, color = [0,0,0], x0 = 40, y0=10)   #creating a triangle
    object_list = [ball1, ball2, ball3, ball4, block1, block2, block3, block4, block5, block6, block7, triangle2, triangle3]  #add triangle 1 in the list for the same result as in video
    return object_list

def  main():
    '''creates the pinball game scene and a block controller at the button'''

    win = gr.GraphWin("Pinball", 500, 500, False)
    win.setBackground("gold")   
    shapes = buildObstacles(win)
    for shape in shapes:
        shape.draw()
    dt = 0.02
    frame = 10
    ball1 = pho.Unique_Ball(win, radius = 1)   #(change to ball1 = pho.New_Shape(win, radius = 1, height = 2, width = 2)) to get results excluding extensions)
    ball1.setPosition(25,40)  #set  position
    ball1.setAcceleration(0,-20)   # set acceleration
    ball1.setVelocity(random.randint(-20,20), random.randint(-10,10))  #set velocity
    ball1.setColor([50,200,100])  #set color
    ball1.draw()

    #creating another ball same as above
    ball2 = pho.Unique_Ball(win, radius = 1)
    ball2.setPosition(20,45)
    ball2.setAcceleration(0,-20)
    ball2.setVelocity(random.randint(-20,20), random.randint(-10,10))
    ball2.setColor([50,200,100])
    ball2.draw()

    block = pho.Block(win, width = 15, height = 1, color = [150,100,0], x0=25, y0=1)   #create block to be used as a flapper
    block.draw()

    while True:
        if frame%10 ==0:
            win.update()
        key = win.checkKey()

        if key== "Left":
            position = block.getPosition()
            block.setPosition(position[0]-10, position[1])  #shifting block position to left with left key

        if key == "Right":
            position = block.getPosition()
            block.setPosition(position[0]+10, position[1])   #shifting block position to right with right key

        if key == "q":
            break
        
        if win.checkMouse():
            break
        
        pos1 = ball1.getPosition()
        if (pos1[0]*(ball1.scale) <= 0) or (pos1[0]*ball1.scale >=win.getWidth()):  #condition for the ball to get out of window
            ball1.setPosition(25,45)   #position to the center
            ball1.setVelocity(random.randint(-10,10), random.randint(-10,10))   #give random velocity

        elif (pos1[1]*ball1.scale >= win.getHeight()) or (pos1[1]*ball1.scale <=0):  #condition for the ball to get out of window
            ball1.setPosition(25, 45)   #position to the center
            ball1.setVelocity(random.randint(-10,10), random.randint(-10,10))    #give random velocity

        collided = False

        for shape in shapes:   #loop through the shapes
            if collision.collision(ball1, shape, dt)==True:  
                collided = True

        if collision.collision(ball1, block, dt)==True:
            collided = True

        if collided == False:
            ball1.update(dt)   #update if collided is not true

        #same for ball2
        pos2 = ball2.getPosition()
        if (pos2[0]*(ball2.scale) <= 0) or (pos2[0]*ball2.scale >=win.getWidth()):  #condition for the ball to get out of window
            ball2.setPosition(20,40)   #position to the center
            ball2.setVelocity(random.randint(-10,10), random.randint(-10,10))   #give random velocity

        elif (pos2[1]*ball1.scale >= win.getHeight()) or (pos2[1]*ball1.scale <=0):  #condition for the ball to get out of window
            ball2.setPosition(20, 40)   #position to the center
            ball2.setVelocity(random.randint(-10,10), random.randint(-10,10))    #give random velocity

        collided = False
        for shape in shapes:
            if collision.collision(ball2, shape, dt)==True:
                collided = True

        if collision.collision(ball2, block, dt)==True:
            collided = True

        if collision.collision(ball1,ball2, dt)==True:
            collided = True

        if collided == False:
            ball2.update(dt)

        win.update()
        frame += 1
    win.close()

if __name__ == "__main__":
    '''execute main'''
    
    main()
    