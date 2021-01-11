import numpy as np
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

columns = 30
rows = 16
points = columns * rows
startrow = 9
startColumn = 14
startID = str(startrow) + "_" + str(startColumn)

driver = webdriver.Chrome()
driver.get("http://minesweeperonline.com/#200")

startClick = driver.find_element_by_xpath('//*[@id="' + startID + '"]')
actions = ActionChains(driver)
actions.click(startClick).perform()

board = np.zeros((rows, columns))
grid = board
for i in range(1, rows+1):
    for j in range(1, columns+1):
        IDS = str(i) + "_" + str(j)
        currentID = driver.find_element_by_xpath('//*[@id="' + IDS + '"]')
        if (currentID.get_attribute("class")[:12] == "square blank"):
            board[i - 1][j - 1] = float("NaN")
        else:
            board[i - 1][j - 1] = int(currentID.get_attribute("class")[-1])







#squareType = print(startClick.get_attribute("class")[:11])
#squareDigit = print(startClick.get_attribute("class")[-1])
#squareID = print(startClick.get_attribute("id"))

