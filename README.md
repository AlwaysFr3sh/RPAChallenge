# RPA Challenge

Hello, this is my attempt at the Robotic Process Automation challenge found here:

http://www.rpachallenge.com

I am using python and selenium

### RUN
```
python3 main.py driverpath.txt -close
```

driverpath.txt is the path to your chromedriver, you need to add this to the directory.

the -close argument closes the chrome window 3 seconds after the challenge is completed.

# FYI

You need to have a chromedriver on your machine, google should tell you how.

The challenge file, that can be downloaded from the site needs to be .xls instead of .xlsx for this to work

also, downloading the file (and in this case converting it to xls) could be automated, but won't be in this case

### TODO

- Implement in python-rpa 

### Helpful links

I referenced these forums while doing this challenge (probably some others too but these ones are really helpful!)
https://stackoverflow.com/questions/31792301/locating-an-element-using-ng-model-using-selenium-in-python
https://stackoverflow.com/questions/48365252/how-to-find-element-using-type-in-selenium-and-python
