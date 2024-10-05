#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT, VERTICAL_SPEED
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.moving_up = False

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

        if self.name == 'Enemy3':
            if self.moving_up:
                self.rect.centery -= VERTICAL_SPEED
                if self.rect.top <= 0:
                    self.rect.top = 0
                    self.moving_up = False
            else:
                self.rect.centery += VERTICAL_SPEED * 2
                if self.rect.bottom >= WIN_HEIGHT:
                    self.rect.bottom = WIN_HEIGHT
                    self.moving_up = True
        else:
            self.rect.centery = self.rect.centery

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
