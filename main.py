#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main(driver):
  searchBar = driver.find_element_by_name("q")
  searchBar.send_keys("time in melbourne")
  searchBar.send_keys(Keys.RETURN)


if __name__ == "__main__":
  path = "/Users/tomhollo/Documents/personal projects/RPAChallenge/chromedriver"
  driver = webdriver.Chrome(path)
  driver.get("https://google.com")
  main(driver)
