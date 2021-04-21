import os

from selenium import webdriver


def before_scenario (context, scenario):
    context.browser = webdriver.Firefox(executable_path='D:\Clases de Automatización\Repositories\AutomatizacionesNetSuite\BDD\Lib\MozilaDriver/geckodriver.exe')
    context.browser.maximize_window()