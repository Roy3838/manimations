from manim import *


width=1080
height=1920
config.frame_size = [width, height]





class Uncertainty(ZoomedScene):
    def construct(self):
        self.camera.background_color ="#E2E2E2" 


        # Updater that tells the particle where to go and to bounce off the walls
        def bounce(particle, dt):
            particle.shift(particle.velocity * dt)
            if particle.get_bottom()[1] <= -4 or particle.get_top()[1] >= 4:
                particle.velocity[1] = -particle.velocity[1]
            if particle.get_left()[0] <= -4 or particle.get_right()[0] >= 4:
                particle.velocity[0] = -particle.velocity[0]

            # Updater that creates a trail behind the particle
            if particle.photographed == True:
                trail = Dot(color = particle.get_color(), radius = particle.get_radius()).move_to(particle.get_center()).set_opacity(0.1)
                self.add(trail)
            

        #def flash():

        # Method that does the animation of taking a photograph for a certain number of frames
        def take_photograph(seconds):
            # Set the particle to be photographed
            particle.photographed = True
            # Wait n frames
            self.wait(seconds)
            # Set the particle to not be photographed
            particle.photographed = False

        



        # Box
        box = Rectangle(width=8, height=8, color=GREY_B, stroke_width=3)


        # Particle 
        particle = Dot(color=GREY_D, radius=0.5)
        particle.velocity = np.array([4.5, 2.5, 0])
        particle.photographed = False
        particle.add_updater(bounce)

        self.add(box, particle)
        self.wait(3)
        take_photograph(1/60)
        self.wait(3)



