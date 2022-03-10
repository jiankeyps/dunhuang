#!/usr/bin/env python
#coding:utf-8
from flask import Flask,render_template,request,g,jsonify
from py2neo import *
from functools import reduce

graph = Graph("http://localhost:7474",auth=("neo4j","123456"))

#获取查询结果
#input_result = g.result  #应放进函数内，否则报错

nodes = []       #空的全局变量
edges = []

def buildNodes(graph_record):     #读取节点数据    
    data_a ={"data":{"id":str(graph_record['id(a)']), "name": graph_record.get('q').start_node.get('name'),
              "label": ''.join(graph_record['labels(a)'])}}
    data_b = {"data":{"id":str(graph_record['id(b)']), "name": graph_record.get('q').end_node.get('name'),
              "label": ''.join(graph_record['labels(b)'])}}
    for p,q in zip(data_a,data_b):   # for循环中使用zip()便能够同时对多个对象进行迭代.
        nodes.append(data_a)
        nodes.append(data_b)        
    #print('nodes1:',nodes)
    return nodes

def buildEdges(graph_record):    #读取边数据    
    data = {"data":{"source": str(graph_record['id(a)']),
            "target": str(graph_record['id(b)']),
            "relationship": ''.join(graph_record['labels(b)'])}}
    edges.append(data)
    #print('edges1:',edges)
    return edges

#节点列表里的字典元素去重
def list_dict_duplicate_removal():
    run_function = lambda x, y: x if y in x else x + [y]
    return reduce(run_function, [[], ] + nodes)



def graph_func():
    global nodes    #在函数内部声明全局变量,才能更改该变量
    global edges
    nodes = []     #将调用函数的变量值清空，否则会在再次调用时append累积
    edges = []
         
    input_result = g.result     #先获取按钮查询结果各个壁画名称    
    
    m = len(input_result)
    n = 0
    
    for n in range(m):    #循环获取每个壁画的名称        
        if n <= m:            
            bihua = input_result[n]['n.name']
            graph_result = graph.run('match q =  (a) -[r*1..3]->(b) where a.name="%s" return q,id(a),id(b),labels(a),labels(b),r'% bihua).data()   #传入壁画名，读取节点、id、标签
    
            s = len(graph_result)
            i = 0
            
            for i in range(s):   #循环获取每个壁画的所有节点和关系的数据
                if i <= s:
                    graph_record = graph_result[i] 
                    buildNodes(graph_record)
                    buildEdges(graph_record)
                    i += 1               
                    
            n += 1     
    
    nodes = list_dict_duplicate_removal()   #去除节点中的重复，关系没有重复  
    
    return jsonify(elements={"nodes": nodes, "edges": edges})    # #用jsonify函数把elements转成JSON格式返回给前端
    #return nodes,edges







