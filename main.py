#!/usr/bin/env python3

import time

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import pandas as pd

# presses start button
def PressStartButton(driver):
  submitButton = driver.find_element_by_xpath("/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button") 
  print("pressed submit button")
  submitButton.send_keys(Keys.RETURN)

#presses submit button
def PressSubmitButton(driver):
  submitButton = driver.find_element_by_xpath("/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input")
  submitButton.send_keys(Keys.RETURN)

# returns the form elements we need to fill 
def GetElements(driver):
  # gather elements
  # TODO: this is terrible, put paths in a file and read into list with a loop (or list comprehension?)
  firstName = driver.find_element_by_xpath("/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/div/div[1]/rpa1-field/div/input")
  lastName = driver.find_element_by_xpath("/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/div/div[2]/rpa1-field/div/input")
  role = driver.find_element_by_xpath("/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/div/div[3]/rpa1-field/div/input")
  company = driver.find_element_by_xpath("/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/div/div[4]/rpa1-field/div/input")
  phoneNumber = driver.find_element_by_xpath("/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/div/div[5]/rpa1-field/div/input")
  email = driver.find_element_by_xpath("/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/div/div[6]/rpa1-field/div/input")
  address = driver.find_element_by_xpath("/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/div/div[7]/rpa1-field/div/input")

  elements = []
  elements.append(firstName)
  elements.append(lastName)
  elements.append(role)
  elements.append(company)
  elements.append(phoneNumber)
  elements.append(email)
  elements.append(address)

  return elements

# fills form, inputs is array of First name, last name etc
def FillForm(driver, row):
  elements = GetElements(driver)

  # send data 
  for element, data in zip(elements, row):
    element.send_keys(data)

# gets data from excel file and returns it in a 2d list
def GetData(path):
  data = pd.read_excel(r''.join(path))
  ret = []
  for i, row in data.iterrows():
    ret.append([row["First Name"], row["Last Name "], row["Company Name"], row["Role in Company"], row["Address"], row["Email"], row["Phone Number"]])

  return ret

# main
def main(driver, dataPath):
  driver.get("http://rpachallenge.com")
  PressStartButton(driver)

  inputData = GetData(dataPath)

  for row in inputData:
    FillForm(driver, row)
    PressSubmitButton(driver)
  

# need to init driver here to avoid it getting caught by the garbage collector
if __name__ == "__main__":
  path = "/Users/tomhollo/Documents/personal projects/RPAChallenge/chromedriver"
  driver = webdriver.Chrome(path)
  main(driver, "challenge2.xls")
  # so we can see the time we got
  time.sleep(3)
  # closes browser 'gracefully'
  driver.quit()
