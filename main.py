import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

sun_radius = 60
earth_radius = 30
venus_radius = 30
mars_radius = 25
mercury_radius = 20
jupitur_radius = 45
saturn_radius = 40
neptune_radius = 40
uranus_radius = 40

sun_color = 'yellow'
earth_color = 'blue'
mercury_color = 'grey'
venus_color = 'orange'
mars_color = 'red'
jupitur_color = '#c99039'
saturn_color = '#ceb8b8'
neptune_color = '#7CB7BB'
uranus_color = '#d9ddf4'

orbit_color = 'grey'

lucy_radius = 5
vesta_radius = 4
eros_radius = 3
didymos_radius = 5

lucy_color = 'green'
vesta_color = 'brown'
eros_color = 'red'
didymos_color = 'grey'

class Planet():
    def __init__(self, name, distance, speed, radius, color):
        self.name = name
        self.distance = distance
        self.speed = speed
        self.angle = 0
        self.radius = radius
        self.color = color

    def update(self):
        self.angle += self.speed

    def get_position(self):
        x = self.distance * np.cos(self.angle)
        y = self.distance * np.sin(self.angle)
        z = 0
        return x, y, z
    
class Orrery:
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.planets = [
            Planet('Mercury', 50, 0.01 ,mercury_radius, mercury_color),
            Planet('Venus',80, 0.005, venus_radius, venus_color),
            Planet( 'Earth', 110, 0.003, earth_radius, earth_color),
            Planet('Mars',140, 0.002, mars_radius, mars_color),
            Planet('Jupiter',170, 0.001, jupitur_radius, jupitur_color),
            Planet('Saturn', 200, 0.0005, saturn_radius, saturn_color),
            Planet('Uranus',230, 0.0002, uranus_radius, uranus_color),
            Planet('Neptune',260, 0.0001, neptune_radius, neptune_color),
            Planet('Lucy', 120, 0.004, lucy_radius, lucy_color),  # new planet
            Planet('Vesta', 160, 0.0035, vesta_radius, vesta_color),  # new planet
            Planet('Eros', 140, 0.003, eros_radius, eros_color), 
            Planet('Didymos', 125, 0.00026, didymos_radius, didymos_color), # new planet
        ]

    def update(self, frame):
        self.ax.clear()
        self.ax.set_xlim(-180, 180)
        self.ax.set_ylim(-180, 180)
        self.ax.set_zlim(-180, 180)
        self.ax.scatter(0, 0, 0, c=sun_color, s=sun_radius*10)
        for planet in self.planets:
            planet.update()
            x, y, z = planet.get_position()
            self.ax.scatter(x, y, z, c=planet.color, s=planet.radius*10)
            self.ax.text(x, y, z, planet.name, ha='left', va='bottom', size=10)
            if planet.name not in ['Lucy', 'Vesta', 'Eros', 'Didymos']:
                theta = np.linspace(0, 2*np.pi, 100)
                x_orbit = planet.distance * np.cos(theta)
                y_orbit = planet.distance * np.sin(theta)
                z_orbit = np.zeros_like(theta)
                self.ax.plot(x_orbit, y_orbit, z_orbit, c=orbit_color, lw=1)

        self.ax.set_title(' Space Orrery - DevFreaks')

        

    def animate(self):
        ani = animation.FuncAnimation(self.fig, self.update, frames=200, interval=50)
        plt.show()

orrery = Orrery()
orrery.animate()
