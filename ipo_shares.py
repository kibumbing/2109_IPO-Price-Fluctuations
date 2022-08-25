from selenium import webdriver
import time
import pandas as pd

chromedriver = 'C:/Users/asdf/finance/chromedriver.exe'

driver = webdriver.Chrome(chromedriver)


myDictionaryList = []
for i in range(1, 54):
    driver.get(f'http://www.38.co.kr/html/fund/index.htm?o=k&page={i}')
    try:
        for j in range(1, 26):
            mydictionary ={}
            mydictionary["name"] = driver.find_element_by_xpath(
                f'/html/body/table[3]/tbody/tr/td/table[1]/tbody/tr/td[1]/table[4]/tbody/tr[2]/td/table/tbody/tr[{j}]/td[1]/a/font[1]').text
            mydictionary["cost"] = driver.find_element_by_xpath(
                f'/html/body/table[3]/tbody/tr/td/table[1]/tbody/tr/td[1]/table[4]/tbody/tr[2]/td/table/tbody/tr[{j}]/td[3]').text
            mydictionary["competitive rate"] = driver.find_element_by_xpath(
                f'/html/body/table[3]/tbody/tr/td/table[1]/tbody/tr/td[1]/table[4]/tbody/tr[2]/td/table/tbody/tr[{j}]/td[5]').text
            driver.find_element_by_xpath(f'/html/body/table[3]/tbody/tr/td/table[1]/tbody/tr/td[1]/table[4]/tbody/tr[2]/td/table/tbody/tr[{j}]/td[1]/a/font[1]').click()
            mydictionary["code"] = driver.find_element_by_xpath(
                f'/html/body/table[3]/tbody/tr/td/table[1]/tbody/tr/td[1]/table[2]/tbody/tr[2]/td[4]').text
            try:
                mydictionary["date"] = driver.find_element_by_xpath(f'/html/body/table[3]/tbody/tr/td/table[1]/tbody/tr/td[1]/table[7]/tbody/tr[6]/td[2]').text
            except:
                mydictionary["date"] = driver.find_element_by_xpath(
                    f'/html/body/table[3]/tbody/tr/td/table[1]/tbody/tr/td[1]/table[6]/tbody/tr[6]/td[2]').text
            driver.back()

            myDictionaryList.append(mydictionary)
    except Exception as ex:
        print(ex)
        pass
print(myDictionaryList)
df = pd.DataFrame().from_dict(myDictionaryList)
df.to_csv("./data.csv",encoding="utf-8-sig")
