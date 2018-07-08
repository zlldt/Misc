from selenium import webdriver

option = webdriver.ChromeOptions()
# option.set_headless()
# browser = webdriver.Chrome(chrome_options=option)
browser = webdriver.Chrome()
browser.maximize_window()

keywordlist = ['上市', '上线', '上線', 'lists', '首发']

browser.get("https://www.feixiaohao.com/notice")
html = browser.page_source

table_li_list = browser.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/ul").find_elements_by_tag_name("li")

for r, li in enumerate(table_li_list, 1):
    table_a_list = li.find_elements_by_tag_name('a')
    for c, a in enumerate(table_a_list):
        if c == 1:
            for keyword in keywordlist:
                if keyword in a.text:
                    print(c, a.text)
browser.close()
