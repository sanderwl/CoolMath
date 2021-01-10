import numpy as np
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

rows = 16
columns = 30
points = rows*columns

driver = webdriver.Chrome()
driver.get("http://minesweeperonline.com/#200")

startClick = driver.find_element_by_xpath('//*[@id="9_14"]')
actions = ActionChains(driver)
actions.click(startClick).perform()

squareType = print(startClick.get_attribute("class")[:11])
squareDigit = print(startClick.get_attribute("class")[-1])
squareID = print(startClick.get_attribute("id"))

gridMat = np.zeros((rows, columns))
print(gridMat.shape)

def grid():
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            xpath = "//*[@id='" + str(i) + "_" + str(j) + "']"
            current = driver.find_element_by_xpath(xpath)
            if (isinstance(current.get_attribute("class")[-1], int) == True):
                gridMat[i-1, j-1] = current.get_attribute("class")[-1]
            else:
                gridMat[i-1, j-1] = 99
    return gridMat

gridMat = grid()
print(gridMat)

#//*[@id="1_1"]