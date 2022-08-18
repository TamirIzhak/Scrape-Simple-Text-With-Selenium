from selenium import webdriver

def get_driver():
  # Set options to make browsing easier
  options = webdriver.ChromeOption()
  options.add_arguments("disable-infobars")
  options.add_arguments("start-maximized")
  options.add_arguments("disable-dev-shm-usage")
  options.add_arguments("no-sandbox")
  options.add_experimental_option("excludeSwitches",["enable-automation"])
  options.add_arguments("disabled-blink-features=AutomationControlled")
  
  driver = webdriver.Chrome(options)
  driver.get("http://automated.pythonanywhere.com")
  return driver

def main ():
  driver=get_driver()
  element = driver.find_element_by_xpath("/html/body/div[1]/div/h1[1]/text()")
  return element

  print(main())
  


