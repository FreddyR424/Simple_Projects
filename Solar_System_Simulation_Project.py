#!/usr/bin/env python
# coding: utf-8

# # Solar System Simulation
# 
# 
# ### This project is to show the inner planets (Mars, Earth, Venus, and Mercury) orbits around the sun.

# In[3]:


import pygame
import math
pygame.init()

# Display Window
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")

# RGB Color Codes
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 150, 237)
RED = (188, 39, 50)
Gray = (80, 78, 81)

class Planet:
    AU = 149.6e6 * 1000 # Astronomical Unit = Distance from Earth to sun
    G = 6.67428e-11 # Gravitational constant
    SCALE = 225 / AU # Scales Planets relative to where they are in Space
    TIMESTEP = 3600 * 24 # One day
    
    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        
        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0
        
        self.x_vel = 0 # horizontal
        self.y_vel = 0 # vertical
        
    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        
        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))
                
            pygame.draw.lines(win, self.color, False, updated_points, 2)
            
        pygame.draw.circle(win, self.color, (x, y), self.radius)
        
    # Math for Planet Movement
    # Distance from Planets to sun
    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
        
        if other.sun:
            self.distance_to_sun = distance
        
        # Force of Attraction
        force = self.G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y
    
    # Update planet positions for movement 
    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue
                
            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy
        
        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP
        
        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))
        
# Program / Main Function 
def main():
    run = True
    clock = pygame.time.Clock()
    
    sun = Planet(0, 0, 35, YELLOW, 1.98892 * 10**30)
    sun.sun = True
    
    earth = Planet(-1 * Planet.AU, 0, 18, BLUE, 5.9742 * 10**24)
    earth.y_vel = 29.783 * 1000 # M/s
    
    mars = Planet(-1.524 * Planet.AU, 0, 14, RED, 6.39 * 10**23)
    mars.y_vel = 24.077 * 1000 # M/s
    
    mercury = Planet(0.387 * Planet.AU, 0, 10, Gray, 3.30 * 10**23)
    mercury.y_vel = -47.4 * 1000 # M/s
    
    venus = Planet(0.723 * Planet.AU, 0, 16, WHITE, 4.8685 * 10**24)
    venus.y_vel = -35.02 * 1000 # M/s
    
    planets = [sun, earth, mars, mercury, venus]

    while run:
        clock.tick(60) # Update rate per second
        WIN.fill((0, 0, 0)) 
        # pygame.display.update() - test background update
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)
            
        pygame.display.update()

    pygame.quit()

main()


# In[ ]:





# In[ ]:




