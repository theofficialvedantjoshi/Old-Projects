from selenium import webdriver
import xlsxwriter
from datetime import date
from nltk.tokenize import word_tokenize
import textwrap
workbook = xlsxwriter.Workbook('C:/Users/vedant/Desktop/Programs/Python/Raytheon.xlsx')
worksheet1 = workbook.add_worksheet('Sheet1')
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://investor.raytheon.com/news-releases")
print(driver.title)
table = driver.find_element_by_tag_name("tbody")
rows = table.find_element_by_tag_name("tr")
#separating date from headline
txt = []
date = []
txt = word_tokenize(rows.text)
date = word_tokenize(rows.text)
length = len(date)
for i in range(length-1):
    date.pop()
del txt[0]
#joining into sentence
head = ' '.join(txt)
f_date = ''.join(date)
print(head,f_date)
#editing puncuations 
f_head = head.replace(" ," , ",")
nf_head = f_head.replace("$ ","$")
link = driver.find_element_by_link_text(nf_head)
link.click()
url = driver.current_url
#content
driver.get(url)
li = []
li = driver.find_elements_by_tag_name('p')
l = len(li)
content  = []
for i in range(0,l):
    content.append(li[i].text)
f_content =  ''.join(content)    
#writing to excel file    
worksheet1.write(0,0,"DATE")
worksheet1.write(0,1,"Headline")
worksheet1.write(0,2,"Content")
worksheet1.write(1,0,f_date)
worksheet1.write(1,1,f_head)
worksheet1.write(1,2,textwrap.fill(f_content,50))
workbook.close()
