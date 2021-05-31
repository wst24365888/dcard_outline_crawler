from selenium import webdriver
import time

def printArticleOutline(driver, index):
    title = driver.find_element_by_xpath(f"/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div[{index}]/article/h2/a/span")
    print(title.text)

    link = driver.find_element_by_xpath(f"/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div[{index}]/article/h2/a")
    print(link.get_attribute("href"))

    emoji_amount = driver.find_element_by_xpath(f"/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div[{index}]/article/div[3]/div[1]/div/div[2]")
    print("emoji_amount:", emoji_amount.text)

    reply_amount = driver.find_element_by_xpath(f"/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div[{index}]/article/div[3]/div[2]/div/span")
    print("reply_amount:", reply_amount.text)

def crawl():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])   # disable some hardware logs

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.dcard.tw/f")

    for i in range(2, 10):
        printArticleOutline(driver, i)

    driver.quit()

if __name__ == "__main__":
    crawl()