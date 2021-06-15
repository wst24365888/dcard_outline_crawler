from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
import time
import configparser
from article_outline import ArticleOutline
from firebase_service import FirebaseService


def fetchArticleOutline(driver, index):
    global firebaseService

    data = None
    while type(data) is not WebElement:
        try:
            data = WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, f"div[data-index='{index-1}']")))
        except:
            html = driver.find_element_by_tag_name('html')
            html.send_keys(Keys.PAGE_DOWN)

    try:
        article = WebDriverWait(data, 1).until(
            EC.presence_of_element_located((By.XPATH, "./article")))
    except:
        return

    try:
        title = WebDriverWait(article, 1).until(
            EC.presence_of_element_located((By.XPATH, "./h2/a/span")))

        link = WebDriverWait(article, 1).until(
            EC.presence_of_element_located((By.XPATH, "./h2/a")))

        emoji_amount = WebDriverWait(article, 1).until(
            EC.presence_of_element_located((By.XPATH, "./div[3]/div[1]/div/div[2]")))

        reply_amount = WebDriverWait(article, 1).until(
            EC.presence_of_element_located((By.XPATH, "./div[3]/div[2]/div/span")))

        articleOutline = ArticleOutline(title.text, link.get_attribute(
            "href"), emoji_amount.text, reply_amount.text)

        # articleOutline.printJSON()

        firebaseService.addArticleOutline(articleOutline)
    except:
        return


def crawl():
    global config

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option(
        "excludeSwitches", ["enable-logging"])   # disable some hardware logs

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(config['domain']['url'])

    for i in range(2, int(config['data']['amount'])):
        fetchArticleOutline(driver, i)

    driver.quit()


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')

    firebaseService = FirebaseService()

    crawl()
