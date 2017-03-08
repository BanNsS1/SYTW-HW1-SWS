#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Get daily free book name of packtpub.com
@author: BanNsS1
'''

import urllib2
import bs4

class FreeBookClient(object):
	
	def __init__(self):
		super(FreeBookClient, self).__init__()

	def get_webpage(self,url):
		f = urllib2.urlopen(url)
		content = f.read()
		f.close()
		return content

	def parse_webpage(self, content):
		soup = bs4.BeautifulSoup(content, 'html.parser')
		return soup.find(id="deal-of-the-day").h2.string.strip();
		
	def print_data(self,book):
		print "Today's free book at packtpub.com is: " + book;
		print "Access https://www.packtpub.com/packt/offers/free-learning/ to download it!"

	def run(self):
		content = self.get_webpage("https://www.packtpub.com/packt/offers/free-learning/");
		book = self.parse_webpage(content)
		self.print_data(book)
	

if __name__ == "__main__":
	client = FreeBookClient()
	client.run()