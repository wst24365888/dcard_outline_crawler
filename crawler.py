from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


def printArticleOutline(driver, index):
    title = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
        (By.XPATH, f"/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div[{index}]/article/h2/a/span")))
    print(title.text)

    link = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
        (By.XPATH, f"/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div[{index}]/article/h2/a")))
    print(link.get_attribute("href"))

    emoji_amount = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
        (By.XPATH, f"/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div[{index}]/article/div[3]/div[1]/div/div[2]")))
    print("emoji_amount:", emoji_amount.text)

    reply_amount = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
        (By.XPATH, f"/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div[{index}]/article/div[3]/div[2]/div/span")))
    print("reply_amount:", reply_amount.text)


def crawl():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option(
        "excludeSwitches", ["enable-logging"])   # disable some hardware logs

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.dcard.tw/f")

    for i in range(2, 10):
        printArticleOutline(driver, i)

    driver.quit()


if __name__ == "__main__":
    crawl()
