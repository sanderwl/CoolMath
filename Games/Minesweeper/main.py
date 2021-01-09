import numpy as np
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

num1 = 30
num2 = 16
points = num1*num2

driver = webdriver.Chrome()
driver.get("http://minesweeperonline.com/#200")

startClick = driver.find_element_by_xpath('//*[@id="9_14"]')
actions = ActionChains(driver)
actions.click(startClick).perform()

#squareType = print(startClick.get_attribute("class")[:11])
#squareDigit = print(startClick.get_attribute("class")[-1])
#squareID = print(startClick.get_attribute("id"))

gridMat = np.zeros((num2,num1))
print(str(7) + "_" + str(8))

def grid():
    for i in range(1, num1+1):
        for j in range(1, num2+1):
            xpath = "//*[@id='" + str(j) + "_" + str(i) + "')]"
            gridMat[j, i] = driver.find_element_by_xpath(xpath)
    return gridMat
gridMat = grid()
print(gridMat)