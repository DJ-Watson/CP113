#!/usr/bin/env python3

# Created by: DJ
# Created on: november 2019
# constants for code.py

PLT = (b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'
       b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')


SCREEN_X = 160
SCREEN_Y = 120
SCREEN_GRID_X = 16
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
TOTAL_NUMBER_OF_ALIENS = 7
TOTAL_NUMBER_OF_LASERS = 5
FPS = 60
SPRITE_MOVEMENT_SPEED = 1
OFF_SCREEN_X = -100
OFF_SCREEN_Y = -100
LASER_SPEED = 2
ALIEN_SPEED = 1

OFF_TOP_SCREEN = -1 * SPRITE_SIZE
OFF_BOTTOM_SCREEN = SCREEN_Y + SPRITE_SIZE

button_state = {
  "button_up": "up",
  "button_just_pressed": "just pressed",
  "button_still_pressed": "still pressed",
  "button_released": "released"
}