import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
Products_list=[]
Price_list = []
Specifications_list = []
ID_list = []
driver = webdriver.Chrome(ChromeDriverManager().install())
website = "https://www.hp.com/es-es/shop/list.aspx?sel=MTO&ctrl=f"
driver.implicitly_wait(10)
driver.get(website)
driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()
driver.find_element_by_class_name('Link-module_wrapper__RyrSK').click()
names = driver.find_elements_by_class_name('ProductTitle-module_title__2JK08')
prices = driver.find_elements_by_class_name('PriceBlock-module_salePrice___Hf7T')
Specifications = driver.find_elements_by_class_name('SpecFirstGlance-module_specFirstGlance__mQCoQ')
ids = driver.find_elements_by_class_name('ProductTile-module_sku__O-ADv')
for name in names:
    Products_list.append(name.text)
for price in prices:
    Price_list.append(price.text)
for Specification in Specifications:
    Specifications_list.append(Specification.text)
for id in ids:
    ID_list.append(id.text)
df = pd.DataFrame({'Product Name':Products_list,'Price':Price_list,'Specifications':Specifications_list,'ID':ID_list}) 
df.to_excel('monitores.xlsx', index=False, encoding='utf-8')