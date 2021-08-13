#!/usr/bin/env python3
# main.py

import sys
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import pandas as pd

# press a button!
def PressButton(driver, xpath):
  button = driver.find_element_by_xpath(xpath)
  button.send_keys(Keys.RETURN)

def GetDriverPath(fileName):
  f = open(fileName, "r")
  ret = f.readline().rstrip()
  f.close()
  return ret

# gets data from excel file and returns it in a 2d list
def GetData(path):
  data = pd.read_excel(r''.join(path))
  ret = []
  for i, row in data.iterrows():
    ret.append([row["First Name"],
      row["Last Name "],
      row["Company Name"],
      row["Role in Company"],
      row["Address"],
      row["Email"],
      row["Phone Number"]])

  return ret

# returns the form elements we need to fill 
def GetElements(driver):
  # gather elements
  # spaghetti, but easy to read
  elements = [driver.find_element_by_xpath("//input[@ng-reflect-name='labelFirstName']"),  
  driver.find_element_by_xpath("//input[@ng-reflect-name='labelLastName']"), 
  driver.find_element_by_xpath("//input[@ng-reflect-name='labelCompanyName']"), 
  driver.find_element_by_xpath("//input[@ng-reflect-name='labelRole']"), 
  driver.find_element_by_xpath("//input[@ng-reflect-name='labelAddress']"), 
  driver.find_element_by_xpath("//input[@ng-reflect-name='labelEmail']"), 
  driver.find_element_by_xpath("//input[@ng-reflect-name='labelPhone']")]
  
  return elements

# fills form, inputs is array of First name, last name etc
def FillForm(driver, row):
  elements = GetElements(driver)

  # send data 
  for element, data in zip(elements, row):
    element.send_keys(data)

  # Hit Submit
  PressButton(driver, "//input[@type='submit']")

# main
def main(driver, dataPath):
  # Load website
  driver.get("http://rpachallenge.com")
  # Hit start
  PressButton(driver, "//*[text()='Start']")
  # Get the input data from the excel file
  inputData = GetData(dataPath)
  # Input each row into the form
  for row in inputData:
    FillForm(driver, row)

# need to init driver here for some reason
if __name__ == "__main__":
  path = GetDriverPath(sys.argv[1]) 
  print(path)
  driver = webdriver.Chrome(path)
  main(driver, "challenge2.xls")
  if len(sys.argv) > 2 and sys.argv[2] == "-close":
    # so we can see the time we got
    time.sleep(3)
    # closes browser 'gracefully'
    driver.quit()

