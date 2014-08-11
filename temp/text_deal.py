# -*- coding: utf-8 -*-
import sys
import os
import shutil
import re

'''def deal_weihui(path):
    list_dirs = os.walk(path)
    r1 = re.compile(r'[0-9]')
    for root, dirs, files in list_dirs:
        for f in dirs:
            print f
            if(r1.match(f)):
               print "++++++++++"
               temp_path=os.path.join(root,f)
               print os.path.join(root,f)
               shutil.rmtree(temp_path)'''
def list_num(path):
    dic={}
    m=1
    error_file="%s/error.txt"%(path)
    ou_file="%s/%s.txt"%(path,path.split('/')[-1])
    print ou_file
    ou=file(ou_file,"w")
    er=file(error_file,"a")
    list_dirs = os.walk(path)
    r1 = re.compile(r'[0-9]')
    for root, dirs, files in list_dirs:
        for f in dirs:
            #print root+"\t"+f
            tag1=root.split('/')[-1]
            tag2=f
            #print tag1+"+++"+tag2
            dic[tag1,tag2]=m
            m=m+1
    list_dirs = os.walk(path)
    for root, dirs, files in list_dirs:
        for f1 in files:
            #print f1
            if(f1=="weihui.txt"):
                #print f1
                f_path=os.path.join(root,f1)
                #print f_path
                lines=open(f_path,"r").readlines() 
                for line in lines:
                    #print line
                    line=line.rstrip()
                    try:
                      li0=line.split('\t')[0]
                      li1=line.split('\t')[1]
                    except:
                      er.write(line+"\n")
                      pass
                    if(r1.match(li1)):
                       continue
                    else:
                       tag1=li0.split('/')[-1]
                       tag2=li1
                       dic[tag1,tag2]=m
                       m=m+1
                       #print tag1+"---"+tag2

    for k,v in dic.items():
       tag_str=""
       for i in k:
           #print i
           tag_str+=i+"\t"
       print tag_str+"%s"%v+"\n"
       ou.write(tag_str+"%s"%v+"\n")
       ou.flush()
    ou.close()
    er.close()
 

__main__ = "main"
if __main__ == "main":
    #*******************************
    path ="../temp/src/四川省"
    #deal_weihui(path)
    list_num(path)
                 
