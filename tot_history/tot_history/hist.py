browser.get('http://www.tianya.cn/12310752/bbs?t=post')
browser.find_element_by_class_name('closeBtn').click()
browser.find_elements_by_xpath('//td[@class="p-title"]')
browser.find_elements_by_xpath('//td[@class="p-title"]/@href').extract()
browser.find_elements_by_xpath('//td[@class="p-title"]/@href')
browser.find_elements_by_xpath('//td[@class="p-title"]/a/@href')
browser.find_elements_by_xpath('//td[@class="p-title"]/a')
browser.find_elements_by_xpath('//td[@class="p-title"]/a')[0].get('href'
)
x = browser.find_elements_by_xpath('//td[@class="p-title"]/a')[0]
x.get_attribute('href')
post_lists = []
post_lists = set()
post_set = set()
browser.find_elements_by_xpath('//td[@class="p-title"]/a')
[post_set.add(href) for href in browser.find_elements_by_xpath('//td[@class="p-title"]/a').get_attribute('href')]
[post_set.add(href.get_attribute('href')) for href in browser.find_elements_by_xpath('//td[@class="p-title"]/a')]
post_set
for href in browser.find_elements_by_xpath('//td[@class="p-title"]/a'):
    print(href)
href.text
href.get_property
href.get_property()
href.__dict__
post_set = set()
for href in browser.find_elements_by_xpath('//div[@id="post"]//td[@class="p-title"]/a'):
    post_set.add(href.get_attribute('href'))
post_set
post_set = set()
while True:
    for href in browser.find_elements_by_xpath('//div[@id="post"]//td[@class="p-title"]/a'):
        post_set.add(href.get_attribute('href'))
    try:
        browser.find_element_by_link_text('下一页').click()
    except:
        break
_set
post_set
while True:
    for href in browser.find_elements_by_xpath('//div[@id="post"]//td[@class="p-title"]/a'):
        post_set.add(href.get_attribute('href'))
    try:
        browser.find_element_by_link_text('下一页').click()
    except:
        break
with open('tot_urls.txt', 'w') as fd:
    [print(url, file=fd) for url in post_set]
%hist -f hist.py
