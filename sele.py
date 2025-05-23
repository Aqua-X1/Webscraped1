from selenium  import webdriver
from selenium.webdriver.edge.service import Service
import pandas as pd
#manual;
website = 'https://quotes.toscrape.com/'
path = 'msedgedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Edge(service=service)
driver.get(website)
containers = driver.find_elements(by='xpath',value='//div[@class="quote"]')#//div[@class="quote"]//span/text()
#Manual:

quotes =[]
for container in containers:
    quote = container.find_element(by='xpath',value='.//span[@class="text"]').text
    quotes.append(quote)


dict_i =pd.DataFrame({'quotes':quotes})
dict_i.to_csv('quoest.csv')
print(f'Scrapes: {len(quotes)}')
driver.quit()