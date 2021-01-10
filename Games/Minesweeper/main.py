import numpy as np
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

num1 = 30
num2 = 16
points = num1*num2
startID = "9_14"

driver = webdriver.Chrome()
driver.get("http://minesweeperonline.com/#200")

startClick = driver.find_element_by_xpath('//*[@id="' + startID + '"]')
actions = ActionChains(driver)
actions.click(startClick).perform()

startNum = startID.find("_")
currentID = startID
currentColumn = int(currentID[startNum + 1:])
currentRow = int(currentID[:startNum])
currentClick = driver.find_element_by_xpath('//*[@id="' + currentID + '"]')
currentNum = 0

while (int(currentClick.get_attribute("class")[-1]) < 1):
    currentRow -= 1
    currentID = str(currentRow) + "_" + str(currentColumn)
    currentClick = driver.find_element_by_xpath('//*[@id="' + currentID + '"]')
    currentNum = currentClick.get_attribute("class")[-1]
    print(currentClick.get_attribute("class")[-1])
    print(currentID)

squareGrid = np.zeros((3,3))

def surrounding(currentNum):

    count = 0
    upID = str(currentRow-1) + "_" + str(currentColumn)
    surroundClickUp = driver.find_element_by_xpath('//*[@id="' + upID + '"]')
    if (surroundClickUp.get_attribute("class")[:12] == "square blank"):
        count += 1

    upLeftId = str(currentRow-1) + "_" + str(currentColumn-1)
    surroundClickUpLeft = driver.find_element_by_xpath('//*[@id="' + upLeftId + '"]')
    if (surroundClickUpLeft.get_attribute("class")[:12] == "square blank"):
        count += 1

    leftID = str(currentRow) + "_" + str(currentColumn-1)
    surroundClickLeft = driver.find_element_by_xpath('//*[@id="' + leftID + '"]')
    if (surroundClickLeft.get_attribute("class")[:12] == "square blank"):
        count += 1

    downLeftID = str(currentRow+1) + "_" + str(currentColumn-1)
    surroundClickDownLeft = driver.find_element_by_xpath('//*[@id="' + downLeftID + '"]')
    if (surroundClickDownLeft.get_attribute("class")[:12] == "square blank"):
        count += 1

    downID = str(currentRow+1) + "_" + str(currentColumn)
    surroundClickDown = driver.find_element_by_xpath('//*[@id="' + downID + '"]')
    if (surroundClickDown.get_attribute("class")[:12] == "square blank"):
        count += 1

    downRightID = str(currentRow+1) + "_" + str(currentColumn+1)
    surroundClickDownRight = driver.find_element_by_xpath('//*[@id="' + downRightID + '"]')
    if (surroundClickDownRight.get_attribute("class")[:12] == "square blank"):
        count += 1

    rightID = str(currentRow) + "_" + str(currentColumn+1)
    surroundClickRight = driver.find_element_by_xpath('//*[@id="' + rightID + '"]')
    if (surroundClickRight.get_attribute("class")[:12] == "square blank"):
        count += 1

    upRightID = str(currentRow-1) + "_" + str(currentColumn+1)
    surroundClickUpRight = driver.find_element_by_xpath('//*[@id="' + upRightID + '"]')
    if (surroundClickUpRight.get_attribute("class")[:12] == "square blank"):
        count += 1

    if (currentNum == count):
        actions.context_click(surroundClick).perform()
    return count



#squareType = print(startClick.get_attribute("class")[:11])
#squareDigit = print(startClick.get_attribute("class")[-1])
#squareID = print(startClick.get_attribute("id"))

