#Author: zlldt
#Date: 2018/3/22
import os
import time
from selenium import webdriver
import xlwt

username = "用户名"
password = "密码"
batchno = "批次号"

browser = webdriver.Chrome()
browser.maximize_window()

browser.get("http://10.128.8.73:7001/hbcard/login.jsp")

#输入用户姓名、密码
browser.find_element_by_xpath('/html/body/form/table/tbody/tr/td/center/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[2]/input').send_keys(username)
browser.find_element_by_xpath('/html/body/form/table/tbody/tr/td/center/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/input').send_keys(password)

#模拟点击事件
browser.find_element_by_xpath('/html/body/form/table/tbody/tr/td/center/table/tbody/tr[2]/td[2]/p/input[1]').click()

#暂停等待网页载入
time.sleep(5)

    # #点击统计查询
    # # browser.find_element_by_xpath('//*[@id="T6090M"]').click()
    # # browser.find_element_by_id('T6090A').click()
    # browser.find_element_by_xpath('//*[@id="T6090"]/tbody/tr/td[2]/a').click()
    #
    # #暂停等待网页载入
    # time.sleep(5)
    #
    # #点击综合查询
    # browser.find_element_by_xpath('//*[@id="T6090A"]/tbody/tr[1]/td[2]/a').click()
    #
    # #暂停等待网页载入
    # time.sleep(5)
    #
    # #批次号输入
    # browser.find_element_by_xpath('/html/body/form/table[3]/tbody/tr[1]/td[8]/input').send_keys(batchno)
    #
    # #点击开始查找
    # browser.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td[2]/input').click()
#打开综合查询
browser.get('http://10.128.8.73:7001/hbcard/tjbb/sbkcx.jsp')
#批次号输入
browser.find_element_by_xpath('/html/body/form/table[3]/tbody/tr[1]/td[8]/input').send_keys(batchno)

#点击开始查找
browser.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td[2]/input').click()

#暂停等待网页载入
time.sleep(5)

#进入第一页，需保存网页内容到本地

wbk = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = wbk.add_sheet('sheet 1', cell_overwrite_ok=True)

# 表的内容
#将表的每一行存在table_tr_list中
table_tr_list = browser.find_element_by_xpath("//*[@id='主表']/table[1]/tbody").find_elements_by_tag_name('tr')

# print(table_tr_list)

#每行输出到row_list中,将所有的row_list输入到table_list中
linenumber = 1
for r,tr in enumerate(table_tr_list,1):
    #将表的每一行的每一列内容存在table_td_list中
    table_td_list = tr.find_elements_by_tag_name('td')
    #将行列的内容加入到table_list中
    for c,td in enumerate(table_td_list):
        #row_list.append(td.text)
        # print(td.text)
        sheet.write(linenumber, c, td.text)
    linenumber += 1
    #table_list.append(row_list)

#翻页，
while True:
    browser.find_element_by_xpath('/html/body/form/table[4]/tbody/tr/td[2]/a[3]').click()
    time.sleep(5)
    #复制保存表格内容部分
    table_tr_list = browser.find_element_by_xpath("//*[@id='主表']/table[1]/tbody").find_elements_by_tag_name('tr')

    # 每行输出到row_list中,将所有的row_list输入到table_list中
    for r, tr in enumerate(table_tr_list, 1):
        # 将表的每一行的每一列内容存在table_td_list中
        table_td_list = tr.find_elements_by_tag_name('td')
        # 将行列的内容加入到table_list中
        for c, td in enumerate(table_td_list):
            # row_list.append(td.text)
            # print(td.text)
            sheet.write(linenumber, c, td.text)
        linenumber += 1
    #如果结果条数小于99，说明没有下一页，结束翻页
    if len(table_tr_list)<99:
        break

wbk.save('d:\\20180322.xls')
print('Done')

#最后返回table_list
#return table_list

#后页
'/html/body/form/table[4]/tbody/tr/td[2]/a[3]'

os.system("pause")
