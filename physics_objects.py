#Bishal Khadka
#Apr 20, 2022
#CS152 B

#import required modules
import random
import graphicsPlus as gr
import time

class Thing:
    #this is the parent class for simulated objects

    def __init__(self, win, the_type):
        self.type = the_type
        self.mass = 1
        self.position = [0,0]  #initial value representing x and y location
        self.velocity = [0,0]   #initial value representing x and y velocities
        self.acceleration = [0,0]  #Initial acceleration representing x and y acceleration
        self.elasticity = 1  #energy retained after collision
        self.win = win   #GraphWin object
        self.scale = 10   #scale value
        self.vis = []
        self.color = (0,0,0)
        self.drawn = False

    #get methods
    def getType(self):
        '''Return the type of the object as a scalar value'''
        return self.type
    
    def getMass(self):
        '''Return the mass of the object as a scalar value'''
        return self.mass ################          #####senior multiploed by scal factor here why
    
    def getPosition(self):
        '''Returns a 2 element tuple with the x,y position'''
        return self.position[:]
    
    def getVelocity(self):
        '''returns a 2 element tuple with x and y velocities'''
        return self.velocity[:]   #returning copy of the list from self.velocity coordinates

    def getAcceleration(self):
        '''returns a 2-element tuple with x and y acceleration values'''
        return self.acceleration[:]   #returning copy of the list from self.acceleration coordinates

    def getElasticity(self):
        '''Returns elasticity'''
        return self.elasticity
    
    def getScale(self):
        '''Returns scale'''
        return self.scale
    
    def getColor(self):
        '''Returns color'''
        return self.color
    
    def draw(self):
        '''Takes each items in self.vis and draws them in the window'''
        for item in self.vis:
            item.draw(self.win)
        self.drawn = True
      
    def undraw(self):
        '''Takes each items in self.vis and undraws them in the window'''
        for item in self.vis:
            item.undraw()
        self.drawn = False      

    #set methods
    def setMass(self, m):
        '''sets the new mass m'''
        self.mass = m  #setting equal to new mass m
    
    def setVelocity(self, vx, vy):
        '''returns new vx,vy velocities'''
        self.velocity[0]=vx   #x velocity is vx
        self.velocity[1]=vy    #y velocity is vy
    
    def setAcceleration(self, ax, ay):
        '''returns a new ax, ay accelerationv values'''
        self.acceleration[0]=ax  #x acceleration in ax
        self.acceleration[1]=ay   #y acceleration is ay

    def setElasticity(self, E):
        '''returns a new ax, ay accelerationv values'''
        self.elasticity = E

    def setPosition(self,px,py):
        '''sets the position to new coordinates and moves the circles to that coordinates'''
        x_old = self.getPosition()[0]  #getting current x coordinate of position
        y_old = self.getPosition()[1]   #getting current y coordinate of position
        self.position[0]=px   #setting the x coordinate to px
        self.position[1]=py    #setting the y coordinate to py

        dx = (px - x_old)*self.scale   #change in x position
        dy = (py - y_old)*(-self.scale)   #change in y position

        for item in self.vis:
            item.move(dx,dy)   #moving the circle by dx,dy 

    def setColor(self, c):
        '''updates color'''
        self.color = c
        if c != None:
            for item in self.vis:
                item.setFill(gr.color_rgb(c[0],c[1],c[2])) 

    def update(self, dt):
        '''adjusts the internal position and velocity values based on current acceleration and forces'''
        x_old = self.position[0]
        y_old = self.position[1]
        self.position[0] = x_old+self.velocity[0]*dt + 0.5*self.acceleration[0]*dt*dt   #updating the x position using equation of kinematics
        self.position[1] = y_old+self.velocity[1]*dt+0.5*self.acceleration[1]*dt*dt    #updating the y position using equation of kinematics

        dx = self.scale *self.velocity[0]*dt   #change in x position
        dy = - self.scale *self.velocity[1]*dt #change in y position
        
        for item in self.vis:
            item.move(dx,dy)   #moving each circle in self.vis by dx and dy
        self.velocity[0]+=self.acceleration[0]*dt  
        self.velocity[1]+= self.acceleration[1]*dt  

class Ball(Thing):
    #create a child class Ball

    def __init__(self, win, radius=1, x0=0, y0=0, color=[50,200,250]):   #initialize the ball
        Thing.__init__(self, win, "ball")  #inherit the attributes of Thing class
        self.radius = radius
        self.position = [x0,y0]  
        self.refresh()  
        self.setColor(color) 

    def refresh(self):
        '''draws the ball'''
        drawn = self.drawn
        if drawn:
            self.undraw()
    
        self.vis = [gr.Circle(gr.Point(self.position[0]*self.scale,
                                        self.win.getHeight()-self.position[1]*self.scale), 
                                        self.radius*self.scale)]
        if drawn:
            self.draw(self.win)
    
    def getRadius(self):
        '''returns the radius of the object as a scalar value'''
        return self.radius
    
    def setRadius(self, R):
        '''returns the radius of the object as a scalar value'''
        self.radius = R
        self.refresh()

class Block(Thing):
    #create Block class
    def __init__(self, win, x0=0, y0=0, width=4, height=2, color = None):  #Initialize Block
        Thing.__init__(self, win, "block")  #inherit the attributes of Thing class
        self.width = width 
        self.height = height
        self.position = [x0,y0]
        self.reshape()
        self.setColor(color)

    def reshape(self):
        '''draw the block'''
        if self.drawn:
            self.undraw()
        self.vis = [gr.Rectangle(gr.Point((self.position[0]-0.5*self.width)*self.scale, (self.win.getHeight()-(self.position[1]-0.5*self.height)*self.scale)),
                    gr.Point((self.position[0]+0.5*self.width)*self.scale,(self.win.getHeight()-(self.position[1]+0.5*self.height)*self.scale)))]
        if self.drawn:
            self.drawn(self.win)
            
    def getWidth(self):
        '''get width of block'''
        return self.width
        
    def getHeight(self):
        '''get height of block'''
        return self.height
        
    def setWidth(self,dx):
        '''set width of block '''
        self.width = dx
        self.reshape()
        
    def setHeight(self, dy):
        '''set height of block'''
        self.height = dy
        self.reshape()
        
        
class Triangle(Thing):
    '''create a Triangle child class'''
    def __init__(self, win, x0=0, y0=0, width=5, height=5, color = [0,0,0]): #initialize the class
        Thing.__init__(self, win, "triangle")  #inherit the attributes of Thing class
        self.width = width
        self.height = height
        self.position = [x0, y0]
        self.reshape()
        self.setColor(color)

    def reshape(self):
        '''draw the triangle'''
        if self.drawn:
            self.undraw()
        
        x = self.position[0]*self.scale
        y = self.position[0]*self.scale
        h = self.height*self.scale
        w = self.width * self.scale

        self.vis = [gr.Polygon(gr.Point(self.position[0]*self.scale, self.win.getHeight()-(self.position[1]+ self.height/2)*self.scale),
                gr.Point((self.position[0]+self.width/2)*self.scale,self.win.getHeight()-(self.position[1]-self.height/2)*self.scale),
                gr.Point((self.position[0]-self.width/2)*self.scale, self.win.getHeight()-(self.position[1]-self.height/2)*self.scale))]

        for item in self.vis:
            item.setFill(self.color)   #color  the triangle
        
        if self.drawn:
            self.drawn(self.win)  #draw int he window
    
    def getHeight(self):
        '''get height of triangle'''
        return self.height
    
    def getWidth(self):
        '''get width of triangle'''
        return self.width
    
    def setHeight(self,dy):
        '''set height of triangle'''
        self.height = dy
        self.redraw()
    
    def setWidth(self,dx):
        '''set width of triangle'''
        self.width = dx
        self.redraw()


class New_Shape(Thing):
    #create a new class
    def __init__(self, win, radius=1, x0=0, y0=0, width = 1, height = 1, color=[50,200,250]):  #initialize the class
        Thing.__init__(self, win, "ball")  #inherit the properties of Thing
        self.radius = radius
        self.position = [x0,y0]
        self.width = width
        self.height = height
        self.refresh()  
        self.setColor(color) 

        #create 1 circle and 1 block and add to self_vis
        self.circle = gr.Circle(gr.Point(self.position[0]*self.scale+17,
                                        self.win.getHeight()-self.position[1]*self.scale +17), 
                                        self.radius*self.scale)  
        self.block = gr.Rectangle(gr.Point((self.position[0]-0.5*self.width)*self.scale, (self.win.getHeight()-(self.position[1]-0.5*self.height)*self.scale)),
                    gr.Point((self.position[0]+0.5*self.width)*self.scale,(self.win.getHeight()-(self.position[1]+0.5*self.height)*self.scale)))
    
        self.vis += self.circle, self.block

    def refresh(self):
        '''draws the ball'''
        drawn = self.drawn
        if drawn:
            self.undraw()
    
        self.vis = [gr.Circle(gr.Point(self.position[0]*self.scale,
                                        self.win.getHeight()-self.position[1]*self.scale), 
                                        self.radius*self.scale)] 
        if drawn:
            self.draw(self.win)

    def update(self, dt):
        '''adjusts the internal position and velocity values based on current acceleration and forces'''
        x_old = self.position[0]
        y_old = self.position[1]
        self.position[0] = x_old+self.velocity[0]*dt + 0.5*self.acceleration[0]*dt*dt   #updating the x position using equation of kinematics
        self.position[1] = y_old+self.velocity[1]*dt+0.5*self.acceleration[1]*dt*dt    #updating the y position using equation of kinematics

        dx = self.scale *self.velocity[0]*dt   #change in x position
        dy = - self.scale *self.velocity[1]*dt #change in y position
        
        for circle in self.vis:
            circle.move(dx,dy)   #moving each circle in self.vis by dx and dy
        self.velocity[0]+=self.acceleration[0]*dt
        self.velocity[1]+= self.acceleration[1]*dt
    
    def getRadius(self):
        '''returns the radius of the object as a scalar value'''
        return self.radius
    
    def setRadius(self, R):
        '''returns the radius of the object as a scalar value'''
        self.radius = R
        self.refresh()




#Extension Class Starts Here
'''New Class Used for Extension'''
'''I should have changes many attributes of the Ball class to get the colorful balls with concentric radii, so I created a new class'''

class Unique_Ball(Thing):
    #create a new child class Unique_Ball
    
    def __init__(self, win, radius=1, x0=0, y0=0, color=[50,200,250]):  #initialize the class
        Thing.__init__(self, win, "ball")   #inherit attributes of the Thing class
        self.radius = radius
        self.position = [x0,y0]
        self.refresh()  
        self.setColor(color) 

        #creates three circles and add to self.vis
        self.circle1 = gr.Circle(gr.Point(self.position[0]*self.scale,
                                        self.win.getHeight()-self.position[1]*self.scale), 
                                        self.radius*self.scale)
        self.circle2 = gr.Circle(gr.Point(self.position[0]*self.scale,
                                        self.win.getHeight()-self.position[1]*self.scale), 
                                        0.75*self.scale)
        self.circle3 = gr.Circle(gr.Point(self.position[0]*self.scale,
                                        self.win.getHeight()-self.position[1]*self.scale), 
                                        0.5*self.scale)
        self.vis += self.circle1, self.circle2, self.circle3

    def refresh(self):
        '''draws the concentric circles'''
        drawn = self.drawn
        if drawn:
            self.undraw()
    
        self.vis = [gr.Circle(gr.Point(self.position[0]*self.scale,
                                        self.win.getHeight()-self.position[1]*self.scale), 
                                        self.radius*self.scale)]
        if drawn:
            self.draw(self.win)

    def update(self, dt):
        '''adjusts the internal position and velocity values based on current acceleration and forces'''
        x_old = self.position[0]
        y_old = self.position[1]
        self.position[0] = x_old+self.velocity[0]*dt + 0.5*self.acceleration[0]*dt*dt   #updating the x position using equation of kinematics
        self.position[1] = y_old+self.velocity[1]*dt+0.5*self.acceleration[1]*dt*dt    #updating the y position using equation of kinematics

        dx = self.scale *self.velocity[0]*dt   #change in x position
        dy = - self.scale *self.velocity[1]*dt #change in y position
        
        for circle in self.vis:
            circle.move(dx,dy)   #moving each circle in self.vis by dx and dy
            circle.setFill(random.choice(["red", "blue", "green", "brown", "pink"]))
        self.velocity[0]+=self.acceleration[0]*dt
        self.velocity[1]+= self.acceleration[1]*dt
    
    def getRadius(self):
        '''returns the radius of the object as a scalar value'''
        return self.radius
    
    def setRadius(self, R):
        '''returns the radius of the object as a scalar value'''
        self.radius = R
        self.refresh()