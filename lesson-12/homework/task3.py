from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import json
import time

def scrape_laptops():
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    service = Service("chromedriver")  # Ensure you have chromedriver installed
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.demoblaze.com/")
    time.sleep(3)
    
    # Navigate to Laptops section
    laptops_section = driver.find_element(By.LINK_TEXT, "Laptops")
    laptops_section.click()
    time.sleep(3)
    
    laptops = []
    
    while True:
        laptop_cards = driver.find_elements(By.CLASS_NAME, "card.block")
        
        for card in laptop_cards:
            name = card.find_element(By.CLASS_NAME, "card-title").text.strip()
            price = card.find_element(By.CLASS_NAME, "price-container").text.strip()
            description = card.find_element(By.CLASS_NAME, "card-text").text.strip()
            
            laptops.append({
                "name": name,
                "price": price,
                "description": description
            })
        
        try:
            next_button = driver.find_element(By.ID, "next2")
            if not next_button.is_enabled():
                break
            next_button.click()
            time.sleep(3)
        except:
            break
    
    driver.quit()
    return laptops

if __name__ == "__main__":
    laptops_data = scrape_laptops()
    with open("laptops.json", "w", encoding="utf-8") as f:
        json.dump(laptops_data, f, indent=4, ensure_ascii=False)
    print("Laptop data saved to laptops.json")
