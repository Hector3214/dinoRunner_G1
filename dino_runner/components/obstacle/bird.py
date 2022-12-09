import random
from dino_runner.components.obstacle.obstacle import Obstacle


class Bird(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,1)
        super().__init__(image, self.type)
        self.step_index = 0
        if random.randint(0,1) ==0:
            self.rect.y = 250
        else:
            self.rect.y = 300

    def draw(self, SCREEN):
        if self.step_index >=10:
            self.step_index = 0

        SCREEN.blit(self.image[self.step_index//5], self.rect)
        self.step_index += 1
    