#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def Test(driver):
  driver.get("https://google.com")
  searchBar = driver.find_element_by_name("q")
  searchBar.send_keys("time in melbourne")
  searchBar.send_keys(Keys.RETURN)

def PressStartButton(driver):
  submitButton = driver.find_element_by_xpath("/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button") 
  print("pressed submit button")
  submitButton.send_keys(Keys.RETURN)

def PressSubmitButton(driver):
  submitButton = driver.find_element_by_xpath("/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input")
  submitButton.send_keys(Keys.RETURN)

def FillForm(driver):
  # gather elements
  firstName = driver.find_element_by_xpath("/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/div/div[1]/rpa1-field/div/input")
  lastName = driver.find_element_by_xpath("/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/div/div[2]/rpa1-field/div/input")
  role = driver.find_element_by_xpath("/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/div/div[3]/rpa1-field/div/input")
  company = driver.find_element_by_xpath("/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/div/div[4]/rpa1-field/div/input")
  phoneNumber = driver.find_element_by_xpath("/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/div/div[5]/rpa1-field/div/input")
  email = driver.find_element_by_xpath("/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/div/div[6]/rpa1-field/div/input")
  address = driver.find_element_by_xpath("/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/div/div[7]/rpa1-field/div/input")

  # send input
  firstName.send_keys("hello")
  lastName.send_keys("test")
  role.send_keys("test")
  company.send_keys("test")
  phoneNumber.send_keys("test")
  email.send_keys("test")
  address.send_keys("test")

def main(driver):
  driver.get("http://rpachallenge.com")
  PressSubmitButton(driver)
  for i in range(5):
    PressSubmitButton(driver)
    FillForm(driver)
  


if __name__ == "__main__":
  path = "/Users/tomhollo/Documents/personal projects/RPAChallenge/chromedriver"
  driver = webdriver.Chrome(path)
  main(driver)
