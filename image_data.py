#!/usr/bin/env python
#coding:utf-8
from flask import Flask,render_template,request,g


def image_func():
    result = g.result
    
    n = len(result)     #统计壁画列表个数
    i = 0

    image_list = []
    image_record = []

    for i in range(n):
        if i <= n:
            record = (result[i]['n.name'])      #分别取出壁画线描名称
            image_name = '/static/images/' + record +'.jpg'            #壁画线描路径
            image_yuantu = '/static/images/' + record +'-y.jpg'   #壁画原图路径
            record_yuantu = record + '原图'       #壁画原图名称 
            i += 1
            #print(i,image_name)
            image_list.append(image_name)      #添加线描图本地路径
            image_list.append(image_yuantu)    #添加原图本地路径
            image_record.append(record)        #生成线描图名称
            image_record.append(record_yuantu) #生成原图名称
        else:
            break

        
        
    #print(image_list)
    #print(image_record)

    data = dict(zip(image_list,image_record))   #为了在一个html的for循环中将路径与名称两个参数都传进去，生成一个字典
    #print(data)
    
    return(image_list,image_record,data)






