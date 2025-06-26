from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def get_driver():
    driver = webdriver.Chrome()
    return driver