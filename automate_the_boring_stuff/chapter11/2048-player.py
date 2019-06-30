#! python3
# 2048-player.py - Opens the 2048 game on Firefox and attempts to play the game by constantly inputting down and right into the game

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random

keys = [Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT]

browser = webdriver.Firefox()
browser.get('https://play2048.co/')

html_elem = browser.find_element_by_tag_name('html')
game_check = browser.find_element_by_css_selector('.game-container p')

while game_check.text != 'Game over!':
    html_elem.send_keys(keys[random.randint(0, 3)])
    game_check = browser.find_element_by_css_selector('.game-container p')

score_elem = browser.find_element_by_class_name('score-container')
print(f'You scored {score_elem.text}')