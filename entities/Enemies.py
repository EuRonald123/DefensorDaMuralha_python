import random
from entities.Entity import Entity


class Enemy(Entity):
    def __init__(self, enemy_type, time_seconds):
        configs = {
            1: {
                'animation_frames': [
                    'assets/soldados/inimigo1/1.png',
                    'assets/soldados/inimigo1/2.png'
                ],
                'hp': 2, 'w': 40, 'h': 60, 'y': -160, 'speed_div': 19, 'damage': 1, 'animation_speed':26
            },
            
            2: {
                'animation_frames': [
                    'assets/soldados/inimigo2/1.png',
                    'assets/soldados/inimigo2/2.png',
                    'assets/soldados/inimigo2/3.png'
                ],
                'hp': 5, 'w': 80, 'h': 100, 'y': -400, 'speed_div': 28, 'damage': 3, 'animation_speed':26
            },
            
            3: {
                'animation_frames': [
                    'assets/soldados/inimigo3/1.png',
                    'assets/soldados/inimigo3/3.png'
                ],
                'hp': 8, 'w': 65, 'h': 80, 'y': -650, 'speed_div': 60, 'damage': 7, 'animation_speed':55
            }
        }
        cfg = configs[enemy_type]
        x = random.randint(1, 540)
        super().__init__(None, x, cfg['y'], cfg['hp'], cfg['w'], cfg['h'], animation_frames=cfg['animation_frames'], animation_speed = cfg['animation_speed'])
        self.enemy_type = enemy_type
        self.hp_max = cfg['hp']
        self.divider_speed = cfg['speed_div']
        self.wall_damage = cfg['damage']
        self.time_seconds = time_seconds
        self.base_animation_speed = cfg['animation_speed']
    
    def update(self, time_seconds):
        self.time_seconds = time_seconds
        self.y += time_seconds / self.divider_speed
        
        self.animation_speed = max(3, self.base_animation_speed - (time_seconds // 6))
        self.update_animation()
        self.update_rect()
    
    def wall_arrived(self):
        limit = {1: 540, 2: 500, 3: 480}
        return self.y >= limit[self.enemy_type]
    
    def respawn(self):
        self.x = random.randint(1, 540)
        ys = {1: -160, 2: -400, 3: -650}
        self.y = ys[self.enemy_type]
        self.hp = self.hp_max
        self.update_rect()