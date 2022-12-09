import random
import pygame
from dino_runner.components.obstacle.cactus import Cactus
from dino_runner.components.obstacle.large_cactus import LargeCactus
from dino_runner.components.obstacle.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
from dino_runner.components.obstacle.obstacle import Obstacle


class ObstacleManager():
    def __init__(self):
        self.obstacles = []
        self.index=0
        
        
        #self.cactus_option = self.cactus_option.random()
        
    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0,2) ==0:
                self.obstacles.append( Cactus(SMALL_CACTUS))
            elif random.randint(0,2) ==1:
                self.obstacles.append( LargeCactus(LARGE_CACTUS))
            elif random.randint(0,2) ==2:
                self.obstacles.append( Bird(BIRD))
                #self.obstacles.append(BIRD[0] if self.index <=5 else BIRD[1]) -> intentos para que el ave vuele :(        

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle):
                pygame.time.delay(500)
                #game.playing= False
                #break
                #game.death_count += 1
                #pygame.time.delay(100)
                #self.obstacles = []
                if not game.player.shield:
                    game.player_heart_manager.reduce_heart()
                    if game.player_heart_manager.heart_count >0:
                        game.player.show_text = False
                        game.player.shield = True
                        start_time = pygame.time.get_ticks()
                        game.player.shield_time_up = start_time +1000

                    else:
                        pygame.time.delay(500)
                        game.playing = False
                        game.death_count +=1
                        break
                else:
                    self.obstacles.remove(obstacle) 
                       
                

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacle(self, self1):
        self.obstacles = []                           