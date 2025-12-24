import pygame, random
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH
        )
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # This asteroid is always destroyed
        self.kill()

        # If it's already the smallest size, stop here
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Log the split event
        log_event("asteroid_split")

        # Generate a random angle between 20 and 50 degrees
        angle = random.uniform(20, 50)

        # Create two new velocity vectors by rotating the original
        velocity1 = self.velocity.rotate(angle)
        velocity2 = self.velocity.rotate(-angle)

        # Compute the new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create the two new asteroids at the same position
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Make them move faster
        asteroid1.velocity = velocity1 * 1.2
        asteroid2.velocity = velocity2 * 1.2

