from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, Union, List
from enum import Enum
from random import randint
from coord import Coord
from item import Potion



@abstractmethod
class Character:
    def __init__(self, player, health, temp_health, attack, defense, move: int, range: int):
        if move and range < 1:
            raise ValueError
        if attack and defense < 0:
            raise ValueError
        self.__player = player
        self.__health = health
        self.__temp_health = temp_health
        self.__attack = attack
        self.__defense = defense
        self.__move = move
        self.__range = range

    @property
    def get_player(self):
        return self.__player
    
    @property.setter
    def set_player(self, player):
        self.__player = player

    @property
    def set_health(self):
        return self.__health
    
    @property.setter
    def get_health(self, health):
        self.__health = health

    @property
    def get_temp_health(self):
        return self.__temp_health
    
    @property.setter
    def set_temp_health(self, temp_health):
        self.__temp_health = temp_health

    @property.setter
    def set_combat(self):
        if not isinstance (self.__attack, int) and not isinstance(self.__defense, int):
            if self.__attack and self.__defense < 0:
                raise ValueError
            else:
                raise TypeError
        lst = []
        lst.extend(self.__attack, self.__defense)
        return lst

    @property
    def get_combat(self):
        return self.set_combat()
    

    @property
    def get_range(self):
        return self.__range
    
    @property.setter
    def set_range(self, range):
        self.__range = range
    
    @property
    def get_move(self):
        if not isinstance (self.__move, int):
            if self.__move < 1:
                raise ValueError
            else:
                raise TypeError
        return self.__move
    
    @property.setter
    def set_move(self, move):
        if not isinstance(move, int):
            if move < 1:
                raise ValueError
            else:
                raise TypeError
        self.__move = move






class CharacterDeath(Exception):

    def __init__(self, msg, char: Character):
        self.message = msg


class InvalidAttack(Exception):
    pass


class Player(Enum):
    VILLAIN = 0
    HERO = 1

