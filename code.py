#!/usr/bin/env python3

# Created by: DJ Watson
# Created on: november 2019

import ugame
import stage
import constants
import time
import random

score = 0

def show_alien(aliens):
    for alien_number in range(len(aliens)):
        if aliens[alien_number].x < 0:
           aliens[alien_number].move(random.randint(0 + constants.SPRITE_SIZE, constants.SCREEN_X - constants.SPRITE_SIZE), constants.OFF_TOP_SCREEN)
           break

def splash_scene():
    # this function is the splash scene game loop

    # an image bank for CircuitPython
    image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 160, 120)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # Wait for 1 seconds
        time.sleep(1.0)
        menu_scene()

        # redraw sprite list

def menu_scene():
    # this function is a scene

    # an image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")


    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    # a list of sprites
    sprites = []

    # add text objects
    text = []

    text1 = stage.Text(width=29, height=14, font=None, palette=constants.PLT, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None, palette=constants.PLT, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + sprites + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic
        keys = ugame.buttons.get_pressed()
        # print(keys)

        if keys & ugame.K_START != 0:  # Start button
            game_scene()
            #break

        # redraw sprite list


def game_scene():
    # image bank
    image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")
    # setting button state
    a_button = constants.button_state["button_up"]
    # setting sound
    pew_sound = open("pew.wav", 'rb')
    boom_sound = open("boom.wav", 'rb')
    crash_sound = open("pew2.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    # set background
    background = stage.Grid(image_bank_1, constants.SCREEN_X,
                            constants.SCREEN_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1,3)
            background.tile(x_location, y_location, tile_picked)
    # sprite bank
    sprites = []
    # load ship sprite
    ship = stage.Sprite(image_bank_1, 4, int(constants.SCREEN_X / 2 -
                        constants.SPRITE_SIZE / 2),
                        int(constants.SCREEN_Y - constants.SPRITE_SIZE +
                        constants.SPRITE_SIZE / 2))
    sprites.append(ship)
    # load lasers
    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        single_laser = stage.Sprite(image_bank_1, 10, constants.OFF_SCREEN_X,
                                    constants.OFF_SCREEN_Y)
        lasers.append(single_laser)
    # load aliens
    aliens = []
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        single_alien = stage.Sprite(image_bank_1, 9, constants.OFF_SCREEN_X,
                                    constants.OFF_SCREEN_Y)
        aliens.append(single_alien)
    # number of aliens moving down
    alien_count = 1
    show_alien(aliens)

    # add score text
    global score
    scoretext = []
    score_text = stage.Text(width=29, height=14, font=None, palette=constants.PLT, buffer=None)
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("Score: {0}".format(score))
    scoretext.append(score_text)
    # set game configurations
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = scoretext + sprites + lasers + aliens + [background]
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()
        # print (keys)

        if keys & ugame.K_X != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        if keys & ugame.K_RIGHT != 0:
            if ship.x > constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
            else:
                ship.move(ship.x + 3, ship.y)

        if keys & ugame.K_LEFT != 0:
            if ship.x < 0:
                ship.move(0, ship.y)
            else:
                ship.move(ship.x - 3, ship.y)

        if a_button == constants.button_state["button_just_pressed"]:
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number] .move(ship.x, ship.y)
                    sound.stop()
                    sound.play(pew_sound)
                    break

        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(lasers[laser_number].x, lasers[laser_number].y - constants.LASER_SPEED)
                lasers[laser_number].move(lasers[laser_number].x, lasers[laser_number].y - constants.LASER_SPEED)
                if lasers[laser_number].y < constants.OFF_SCREEN_Y:
                    lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                aliens[alien_number].move(aliens[alien_number].x, aliens[alien_number].y + constants.ALIEN_SPEED)
                if aliens[alien_number].y > constants.SCREEN_Y:
                    aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    show_alien(aliens)

        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for alien_number in range(len(aliens)):
                    if aliens[alien_number].x > 0:
                        if stage.collide(lasers[laser_number].x, lasers[laser_number].y,
                                         lasers[laser_number].x + 16, lasers[laser_number].y + 16,
                                          aliens[alien_number].x, aliens[alien_number].y,
                                         aliens[alien_number].x + 16, aliens[alien_number].y + 16):
                            aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            score += 1
                            score_text.clear()
                            score_text.cursor(0, 0)
                            score_text.move(1, 1)
                            score_text.text("Score: {0}".format(score))
                            sound.stop()
                            sound.play(boom_sound)
                            show_alien(aliens)
                            show_alien(aliens)
                        if stage.collide(aliens[alien_number].x, aliens[alien_number].y,
                                         aliens[alien_number].x + 16, aliens[alien_number].y + 16
                                         ship.x, ship.y,
                                         ship.x + 15, ship.y + 15):
                            sound.stop()
                            sound.play(crash_sound)
                            time.sleep(4.0)
                            sounds.stop()
                            game_over_scene()
        game.render_sprites(sprites + lasers + aliens)
        game.tick()  # wait until refresh rate finishes


def game_over_scene():
    global score
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    text = []

    text0 = stage.Text(29, 14, None, constants.PLT, buffer=None)
    text0.move(22, 20)
    text0.text("Final Score: {:0>2d}".format(score))
    text.append(text0)

    text1 = stage.Text(29, 14, None, constants.PLT, buffer=None)
    text1.move(43, 60)
    text1.text("GAME OVER")
    text.append(text1)

    text2 = stage.Text(29, 14, None, constants.PLT, buffer=None)
    text2.move(32, 110)
    text2.text("PRESS START")
    text.append(text2)

    game = stage.Stage(ugame.display, 60)
    game.layers = text + [background]
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_SELECT != 0:
            keys = 0
            menu_scene()



if __name__ == "__main__":
    splash_scene()