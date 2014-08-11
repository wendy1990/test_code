# -*- coding: utf-8 -*-
'''
Created on 2013-3-26

@author: ywt
'''
import sys
sys.path.append(r"beautifulsoup")
sys.path.append(r"selenium")

#coding=gbk
'''from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0'''
import time
import time
from bs4 import BeautifulSoup
import  urllib2
import os
import chardet
'''def pro_crawler(url,path):
    print url
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)
    try:
        pro_txt="%s/pro.txt"%(path)
        wr_pro=file(pro_txt,"w")
        pro_tag=soup.findAll('tr',attrs={"class":"provincetr"})
        for i in pro_tag:
            td_tag = i.findAll('td')
            print td_tag
            for a_tag in td_tag:
                a_name=a_tag.find('a').text
                aa_html=a_tag.find('a')['href']
                print a_name
                print aa_html
                try:
                   pro_name=a_name.encode('utf8')
                except:
                    pro_name=a_name
                try:
                    if not os.path.exists(pro_name):
                        os.mkdir(pro_name)
                except:
                    pass
                dest_html="http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2013/%s"%(aa_html)
                print a_name.encode('utf8')
                wr_pro.write(a_name.encode('utf8')+"\t"+dest_html.encode('utf8')+"\n")
    except:
        pass
    wr_pro.close()

def city_crawler(path):
    html_file=open("pro.txt","r")
    htlines=html_file.readlines()
    html_file.close()
    for line in htlines:
        line=line.strip()
        aa_name=line.split('\t')[0]
        aa_html=line.split('\t')[1]
        #print aa_name
        #print aa_html
        try:
            aa_name=aa_name.encode('utf8')
        except:
            pass
        a_path="%s/%s"%(path,aa_name)
        print a_path
        city_txt="%s/city.txt"%(a_path)
        ci_pro=file(city_txt,"w")
        try:
            response = urllib2.urlopen(aa_html)
            html = response.read()
            soup = BeautifulSoup(html)
            try:
                pro_tag=soup.findAll('tr',attrs={"class":"citytr"})
                for i in pro_tag:
                    #print i
                    td_tag = i.findAll('td')       
                    #print td_tag
                    for a_tag in td_tag:
                        a_name=a_tag.find('a').text
                        a_html=a_tag.find('a')['href']
                        dest_html="http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2013/%s"%(a_html)
                        try:
                           a_name=a_name.encode('utf8')
                        except:
                           pass
                        aa_path="%s/%s"%(a_path,a_name)
                        print aa_path
                        try:
                            if not os.path.exists(aa_path):
                                os.mkdir(aa_path)
                        except:
                            pass 
                        print a_name
                        ci_pro.write(a_name+"\t"+dest_html.encode('utf8')+"\n")
                        #print "+++"
            except:
                pass
        except:
            pass
        ci_pro.close()

def qu_crawler(path):
    list_dirs = os.walk(path)
    for root, dirs, files in list_dirs:  
        for f in files:
          if(f=="city.txt"):
            file_tag= os.path.join(root, f)
            html_file=open(file_tag,"r")
            #print file_tag
            htlines=html_file.readlines()
            html_file.close()
            for line in htlines:
                line=line.strip()
                aa_name=line.split('\t')[0]
                aa_html=line.split('\t')[1]
                #print chardet.detect(aa_name)
                try:
                  aa_name=aa_name.encode('utf8')
                except:
                  pass
                pre_file=file_tag.split('city.txt')[0]
                try:
                  pre_file=pre_file.encode('utf8')
                except:
                  pass
                a_path="%s/%s"%(pre_file,aa_name)
                print a_path
                qu_txt="%s/qu.txt"%(a_path)
                qu_pro=file(qu_txt,"w")
                try:
                    response = urllib2.urlopen(aa_html)
                    html = response.read()
                    soup = BeautifulSoup(html)
                    try:
                        #print soup
                        pro_tag=soup.findAll('tr',attrs={"class":"countytr"})
                        for i in pro_tag:
                            #print i
                            td_tag = i.findAll('td')
                            for a_tag in td_tag:
                               try:
                                   a_html=a_tag.find('a')['href']
                                   a_name=a_tag.find('a').text
                                   #print a_html
                                   try:
                                      a_name=a_name.encode('utf8')
                                   except:
                                      pass
                                   pre_html= aa_html.split(aa_html.split('/')[-1])[0]
                                   dest_html="%s/%s"%(pre_html,a_html)
                                   aa_path="%s/%s"%(a_path,a_name)
                                   try:
                                       if not os.path.exists(aa_path):
                                           os.mkdir(aa_path)
                                   except:
                                        pass
                                   #print "-------"
                                   #print dest_html
                                   print a_name
                                   qu_pro.write(a_name+"\t"+dest_html.encode('utf8')+"\n")
                                   #print "+++++++"
                               except:
                                   try:
                                       a_name=a_tag.find('a').text
                                       qu_pro.write(a_name+"\n")
                                       print "+++++++"
                                   except:
                                        pass
                                    
                               
                    except:
                        pass
                    qu_pro.close()
                except:
                    pass
def jiedao_crawler(path):
    list_dirs = os.walk(path)
    error_file="error.txt"
    error_pro=file(error_file,"a")
    for root, dirs, files in list_dirs:  
        for f in files:
          if(f=="qu.txt"):
            file_tag= os.path.join(root, f)
            html_file=open(file_tag,"r")
            #print file_tag
            htlines=html_file.readlines()
            html_file.close()
            for line in htlines:
              try:
                line=line.strip()
                aa_name=line.split('\t')[0]
                aa_html=line.split('\t')[1]
                #print chardet.detect(aa_name)
                try:
                  aa_name=aa_name.encode('utf8')
                except:
                  pass
                pre_file=file_tag.split('qu.txt')[0]
                try:
                  pre_file=pre_file.encode('utf8')
                except:
                  pass
                a_path="%s/%s"%(pre_file,aa_name)
                print a_path
                jiedao_txt="%s/jiedao.txt"%(a_path)
                jiedao_pro=file(jiedao_txt,"w")
                try:
                    response = urllib2.urlopen(aa_html)
                    html = response.read()
                    soup = BeautifulSoup(html)
                    try:
                        #print soup
                        pro_tag=soup.findAll('tr',attrs={"class":"towntr"})
                        for i in pro_tag:
                            #print i
                            td_tag = i.findAll('td')
                            for a_tag in td_tag:
                               try:
                                   a_html=a_tag.find('a')['href']
                                   a_name=a_tag.find('a').text
                                   #print a_html
                                   try:
                                      a_name=a_name.encode('utf8')
                                   except:
                                      pass
                                   pre_html= aa_html.split(aa_html.split('/')[-1])[0]
                                   dest_html="%s/%s"%(pre_html,a_html)
                                   aa_path="%s/%s"%(a_path,a_name)
                                   try:
                                       if not os.path.exists(aa_path):
                                           os.mkdir(aa_path)
                                   except:
                                        pass
                                   #print "-------"
                                   #print dest_html
                                   print a_name
                                   jiedao_pro.write(a_name+"\t"+dest_html.encode('utf8')+"\n")
                                   print "+++++++"
                               except:
                                   try:
                                       a_name=a_tag.find('a').text
                                       jiedao_pro.write(a_name+"\n")
                                       #print "+++++++"
                                   except:
                                        pass
                                    
                               
                    except:
                        pass
                    qu_pro.close()
                except:
                    pass
              except:
                error_pro.write(line+"\n")
                pass'''
def weihui_crawler(path):
    list_dirs = os.walk(path)
    error_file="error.txt"
    error_pro=file(error_file,"a")
    for root, dirs, files in list_dirs:  
        for f in files:
          if(f=="jiedao.txt"):
            file_tag= os.path.join(root, f)
            html_file=open(file_tag,"r")
            #print file_tag
            htlines=html_file.readlines()
            html_file.close()
            for line in htlines:
              try:
                line=line.strip()
                aa_name=line.split('\t')[0]
                aa_html=line.split('\t')[1]
                #print chardet.detect(aa_name)
                try:
                  aa_name=aa_name.encode('utf8')
                except:
                  pass
                pre_file=file_tag.split('jiedao.txt')[0]
                try:
                  pre_file=pre_file.encode('utf8')
                except:
                  pass
                a_path="%s/%s"%(pre_file,aa_name)
                #print a_path
                weihui_txt="%s/weihui.txt"%(a_path)
                weihui_pro=file(weihui_txt,"w")
                #print weihui_pro
                try:
                    response = urllib2.urlopen(aa_html)
                    html = response.read()
                    soup = BeautifulSoup(html)
                    try:
                        #print soup
                        pro_tag=soup.findAll('tr',attrs={"class":"villagetr"})
                        for i in pro_tag:
                            #print i
                            td_tag = i.findAll('td')
                            for a_tag in td_tag:
                               try:
                                   a_name=a_tag.text
                                   try:
                                      a_name=a_name.encode('utf8')
                                   except:
                                      pass
                                   #print "----"
                                   #print pre_file
                                   dest_path=a_path.split('src/')[1]
                                   #print dest_path
                                   print dest_path+"\t"+a_name                                                  
                                   weihui_pro.write(dest_path+"\t"+a_name+"\n")
                                   #print "+++++++"
                               except:
                                   pass
                    except:
                        pass
                    weihui_pro.close()
                except:
                    pass
              except:
                error_pro.write(line+"\n")
                pass
                    
    
    
__main__ = "main"
if __main__ == "main":
    #*******************************
    path ="../src/四川省"
    #url="http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2013/index.html"
    #pro_crawler(url,path)
    #city_crawler(path)
    #qu_crawler(path)
    #jiedao_crawler(path)
    weihui_crawler(path)
    
    



