# -*- coding: utf-8 -*-
import os
import re
import scrapy
from tot_history.items import TianyaPostsItem

def clean_content(content):
    return re.sub('\u3000' ,' ', re.sub('<.*?>', '\n', content))


class TotSpider(scrapy.Spider):
    name = 'tot'
    allowed_domains = ['tianya.cn']
    # start_urls = ['http://www.tianya.cn/12310752/bbs?t=post']
    start_urls = open(os.path.dirname(os.path.abspath(__file__))+'/tot_urls.txt').read().split()

    # def parse(self, response):
    #     post_urls = response.xpath('//table[@class="posts"]//td/a/@href')
    #     for url in post_urls:
    #         yield scrapy.Request(url, callback=self.parse_post)
    #     # for next_page in next_pages:
    #     #     yield scrapy.Request(next_page, callback=self.parse_userpage)

    def parse(self, response):
        # response.meta={'title': title, 'posts': list()}
        title = response.meta.get('title', None)
        if not title:
            title = response.xpath('//head/title/text()').extract()[0]
        # see if there is host post
        host = response.meta.get('host', None)
        if not host:
            xhost = response.xpath('//div[@class="atl-main"]/div[@class="atl-item host-item"]')
            host = xhost.attrib.copy()
            content = xhost.xpath('.//div[@class="bbs-content clearfix"]').extract()
            if content:
                content = clean_content(content[0])
            else:
                content = ''
            host.update({'content' : content})
        posts = response.meta.get('posts', list())
        posts.append(self.parse_posts(response))
        # parse next page
        next_pages = response.xpath('//div[@class="atl-pages"]//a[@class="js-keyboard-next"]/@href')
        if next_pages:
            yield scrapy.Request('http://bbs.tianya.cn/'+next_pages[0].extract(), callback=self.parse,
                meta={'title' : title, 'host' : host, 'posts' : posts})
        else:
            item = TianyaPostsItem()
            item['title'] = title
            item['host'] = host
            item['posts'] = posts
            yield item


    def parse_posts(self, response):
        posts = list()
        page_posts = response.xpath('//div[@class="atl-main"]/div[@class="atl-item"]')
        for post in page_posts:
            attrib = post.attrib.copy()
            content = post.xpath('.//div[@class="bbs-content"]').extract()
            if content:
                content = clean_content(content[0])
            else:
                content = ''
            comments = self.parse_comments(post)
            attrib.update({'content' : content, 'comments' : comments})
            posts.append(attrib)
        return posts

    def parse_comments(self, post):
        comments = list()
        for _cmt in post.xpath('.//div[@class="item-reply-view"]//li'):
            attrib = _cmt.attrib.copy()
            content = _cmt.xpath('.//span[@class="ir-content"]/text()').extract()
            if content:
                content = clean_content(content[0])
            else:
                content = ''
            attrib.update({'content' : content})
            comments.append(attrib)
        return comments

