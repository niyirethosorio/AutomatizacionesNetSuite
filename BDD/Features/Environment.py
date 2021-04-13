import os

from selenium import webdriver


def before_scenario (context, scenario):
    context.browser = webdriver.Firefox('../lib/MozillaDriver/geckodriver.exe')
    context.browser.maximize_window()
