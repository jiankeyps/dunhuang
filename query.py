# coding: utf-8
from flask import Flask,render_template,request,g,current_app

#点击查询后返回的选择列表



def query_func():

    click = g.click
    #全部选择点与HTML对应的字典
    dict_node = {'quanbuchaodai':'全部朝代','beiliang':'北凉','beiwei':'北魏','xiwei':'西魏','beizhou':'北周','chutang':'初唐',
        'shengtang':'盛唐','zhongtang':'中唐','wantang':'晚唐','wudai':'五代','songdai':'宋代','xixia':'西夏',
        'yuandai':'元代','quanbudongku':'全部洞窟','mo276':'莫276','mo301':'莫301','mo442':'莫442',
        'quanbuxingzhi':'全部形制','tazhu':'中心塔柱窟','fudou':'覆斗顶形窟','diantang':'殿堂窟','daxiang':'大像窟',
        'niepan':'涅槃窟','chanku':'禅窟','yingku':'影窟','quanbuzhuti':'全部主题','bensheng':'本生故事画',
        'fochuan':'佛传故事画','jingbian':'经变故事画','quanbubuju':'全部布局','danti':'单体','jianzhuqun':'建筑群',
        'quanbuleixing':'全部类型','fosi':'佛寺','ta':'塔','que':'阙','diantang':'殿堂','chengyuan':'城垣',
        'wubi':'坞壁','yuanluo':'院落','guanshu':'官署','zhaidi':'宅邸','qiaoliang':'桥梁','jianyu':'监狱','lang':'廊',
        'shigong':'施工','quanbuwuding':'全部屋顶','wudianding':'庑殿顶','xieshanding':'歇山顶',
        'cuanjianding':'攒尖顶','xuanshanding':'悬山顶','luding':'盝顶','huiding':'盔顶',
        'quanbuwudingjiegoufujian':'全部屋顶结构附件','yanchuan':'檐椽','dougong':'斗拱','lane':'阑额',
        'quanbuwashi':'全部瓦饰','chiwei':'鸱尾','xieji':'斜脊','chuiji':'垂脊','qiaoqi':'翘起',
        'quanbuwushen':'全部屋身','muzhu':'木柱','qiangti':'墙体','cejiao':'侧脚',
        'quanbuwushenjiegoufujian':'全部屋身结构附件','efang':'额枋','bidai':'壁带','menliang':'门梁',
        'men':'门','chuang':'窗','quanbuqiangshi':'全部墙饰','zhelian':'遮帘','weiman':'帷幔',
        'zhangriban':'障日板','quanbujizuo':'全部基座','zhuanshiji':'砖石基','xumizuo':'须弥座',
        'quanbujizuofujian':'全部基座附件','taijie':'台阶','langan':'栏杆'}


    #将选择列表对应到字典
    dict_result = {'chaodai':dict_node[click[0]],'dongku':dict_node[click[1]],'xingzhi':dict_node[click[2]],
               'zhuti':dict_node[click[3]],'buju':dict_node[click[4]],'leixing':dict_node[click[5]],
               'wuding':dict_node[click[6]],'wudingjiegoufujian':dict_node[click[7]],'washi':dict_node[click[8]],
               'wushen':dict_node[click[9]],'wushenjiegoufujian':dict_node[click[10]],'qiangshi':dict_node[click[11]],
               'jizuo':dict_node[click[12]],'jizuofujian':dict_node[click[13]]}

    #print(dict_result)
    #输入dict_result,生成Cypher问句



    if dict_result['chaodai'] != '全部朝代':
        query1 = '(n:壁画) -[*1..3]->({name:"%s"})'%(dict_result['chaodai']) + 'and'
    else:
        query1 = ''
    
    if dict_result['dongku'] != '全部洞窟':
        query2 = '(n:壁画) -[:cave]->({name:"%s"})'%(dict_result['dongku']) + 'and'
    else:
        query2 = ''  
    
    if dict_result['xingzhi'] != '全部形制':
        query3 = '(n:壁画) -[:cave]->({形制:"%s"})'%(dict_result['xingzhi']) + 'and'
    else:
        query3 = ''    
        
    if dict_result['zhuti'] != '全部主题':
        query4 = '(n:壁画) -[:theme]->({name:"%s"})'%(dict_result['zhuti']) + 'and'
    else:
        query4 = ''       

    if dict_result['buju'] != '全部布局':
        query5 = '(n:壁画) -[:layout]->({name:"%s"})'%(dict_result['buju']) + 'and'
    else:
        query5 = ''

    if dict_result['leixing'] != '全部类型':
        query6 = '(n:壁画) -[:type]->({name:"%s"})'%(dict_result['leixing']) + 'and'
    else:
        query6 = ''

    if dict_result['wuding'] != '全部屋顶':
        query7 = ' n.屋顶="%s"'%(dict_result['wuding']) + 'and'
    else:
        query7 = ''

    if dict_result['wudingjiegoufujian'] != '全部屋顶结构附件':
        if dict_result['wudingjiegoufujian'] == '檐椽':
            query8 = ' n.屋顶结构附件1="%s"'%(dict_result['wudingjiegoufujian']) + 'and'
        if dict_result['wudingjiegoufujian'] == '斗拱':
            query8 = ' n.屋顶结构附件2="%s"'%(dict_result['wudingjiegoufujian']) + 'and'
        if dict_result['wudingjiegoufujian'] == '阑额':
            query8 = ' n.屋顶结构附件3="%s"'%(dict_result['wudingjiegoufujian']) + 'and'
    else:
        query8 = ''

    if dict_result['washi'] != '全部瓦饰':
        if dict_result['washi'] == '鸱尾':
            query9 = ' n. 瓦饰1="%s"'%(dict_result['washi']) + 'and'
        if dict_result['washi'] == '斜脊':
            query9 = ' n. 瓦饰2="%s"'%(dict_result['washi']) + 'and'
        if dict_result['washi'] == '垂脊':
            query9 = ' n. 瓦饰3="%s"'%(dict_result['washi']) + 'and'
        if dict_result['washi'] == '翘起':
            query9 = ' n. 瓦饰4="%s"'%(dict_result['washi']) + 'and'
    else:
        query9 = ''

    if dict_result['wushen'] != '全部屋身':
        if dict_result['wushen'] == '木柱':
            query10 = ' n. 屋身1="%s"'%(dict_result['wushen']) + 'and'
        if dict_result['wushen'] == '墙体':
            query10 = ' n. 屋身2="%s"'%(dict_result['wushen']) + 'and'
        if dict_result['wushen'] == '侧脚':
            query10 = ' n. 屋身3="%s"'%(dict_result['wushen']) + 'and'
    else:
        query10 = ''

    if dict_result['wushenjiegoufujian'] != '全部屋身结构附件':
        if dict_result['wushenjiegoufujian'] == '额枋':
            query11 = ' n. 屋身结构附件1="%s"'%(dict_result['wushenjiegoufujian']) + 'and'
        if dict_result['wushenjiegoufujian'] == '壁带':
            query11 = ' n. 屋身结构附件2="%s"'%(dict_result['wushenjiegoufujian']) + 'and'
        if dict_result['wushenjiegoufujian'] == '门梁':
            query11 = ' n. 屋身结构附件3="%s"'%(dict_result['wushenjiegoufujian']) + 'and'
        if dict_result['wushenjiegoufujian'] == '门':
            query11 = ' n. 屋身结构附件4="%s"'%(dict_result['wushenjiegoufujian']) + 'and'
        if dict_result['wushenjiegoufujian'] == '窗':
            query11 = ' n. 屋身结构附件5="%s"'%(dict_result['wushenjiegoufujian']) + 'and'
    else:
        query11 = ''

    if dict_result['qiangshi'] != '全部墙饰':
        if dict_result['qiangshi'] == '遮帘':
            query12 = ' n. 墙饰1="%s"'%(dict_result['qiangshi']) + 'and'
        if dict_result['qiangshi'] == '帷幔':
            query12 = ' n. 墙饰2="%s"'%(dict_result['qiangshi']) + 'and'
        if dict_result['qiangshi'] == '障日板':
            query12 = ' n. 墙饰3="%s"'%(dict_result['qiangshi']) + 'and'
    else:
        query12 = ''

    if dict_result['jizuo'] != '全部基座':
        if dict_result['jizuo'] == '砖石基':
            query13 = ' n. 基座1="%s"'%(dict_result['jizuo']) + 'and'
        if dict_result['jizuo'] == '须弥座':
            query13 = ' n. 基座2="%s"'%(dict_result['jizuo']) + 'and'
    else:
        query13 = ''

    if dict_result['jizuofujian'] != '全部基座附件':
        if dict_result['jizuofujian'] == '台阶':
            query14 = ' n. 基座1="%s"'%(dict_result['jizuofujian']) + 'and'
        if dict_result['jizuofujian'] == '栏杆':
            query14 = ' n. 基座2="%s"'%(dict_result['jizuofujian']) + 'and'
    else:
        query14 = ''

        
        
        
    #获取Cypher查询语句       
    query = 'match (n:壁画) where' + query1 + query2 + query3 + query4  + query5 + query6 + query7 + query8 + query9  + query10  + query11 + query12 + query13 + query14 

    query = query.rstrip('and') + 'return n.name'   #删除尾字符and     + 'return n.name'
    
    if query == 'match (n:壁画) wherereturn n.name':      #全部选择全部的情况，去掉中间where
        query = 'match (n:壁画) return n.name'
        

    #print(query)
    return(query)






