from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get(
    "https://www.bukalapak.com/products?from=omnisearch&from_keyword_history=false&search%5Bkeywords%5D=panda&search_source=omnisearch_keyword&source=navbar"
)

try:
    product_data = []

    for _ in range(5):
        names = driver.find_elements(
            By.CSS_SELECTOR,
            ".bl-text.bl-text--body-14.bl-text--secondary.bl-text--ellipsis__2",
        )
        prices = driver.find_elements(
            By.CSS_SELECTOR,
            ".bl-text.bl-text--semi-bold.bl-text--ellipsis__1.bl-product-card-new__price",
        )

        for name, price in zip(names, prices):
            product_data.append({"Names": name.text, "Prices": price.text})

        driver.execute_script("window.scrollBy(0, 250)")

        time.sleep(2)

finally:
    driver.quit()

excel = pd.DataFrame(product_data).to_excel("./results/bukalapak.xlsx", index=False)

print("Success for Scraping")
