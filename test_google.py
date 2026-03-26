from selenium import webdriver

def test_google():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    print("Title:", driver.title)
    driver.quit()
