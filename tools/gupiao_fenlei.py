'''
@Author: your name
@Date: 2020-05-23 23:41:50
@LastEditTime: 2020-05-24 00:31:27
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /y/股票策略/tools/gupiao_fenlei.py
import'''



import jie_jia_ri_pan_duan
import baostock as bs
import pandas as pd
from pathlib import Path
import os
from datetime import datetime, timedelta
import holidays
def guxi(bs,name,date_start,date_end,shuju):
    #  rs=bs.query_stock_basic(code_name="海王生物")
    rs=bs.query_stock_basic(code_name=name)
    list_=[]
    while (rs.error_code == '0') & rs.next():
        # print(rs.get_row_data())

        # type_.add(val[3])
    #     # 获取一条记录，将记录合并在一起
        list_.append(rs.get_row_data())
    print(list_)
    code=list_[0][0]
    # 显示登陆返回信息
    offset=date_end-date_start
    for i in range(offset):
        date_=date_start+i 
        data_=bs.query_dividend_data(code,str(date_)).data
        # print(data_)
        if len(data_) !=0:
             k_=bs.query_history_k_data_plus(code,
        "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST",
        data_[0][7],data_[0][7]).data
             guxilu=0.00
             guxi=0.00
             for i in range(len(data_)):
                 ggg=0.0
                 try:
                    ggg=float(data_[i][9])
                 except ValueError as e:
                    ggg=0.0
                 guxi=guxi+ggg

             try:
                  guxilu= guxi/float(k_[0][5])*100    
             except ValueError as e:
                print(f"ValueError异常 {e}")
                guxilu=0.00
                print(guxilu)

             shuju.append([name,str(date_),k_[0][5],str(guxi),data_[0][9],str(guxilu),data_[0][10],data_[0][12]]) 
             if date_ == 2024:
                 # 获取当前日期和时间
                 now = datetime.now()
                 #yesterday = now - timedelta(days=1)
                 yesterday = now - timedelta(days=6) 
                 if jie_jia_ri_pan_duan.is_a_share_open(yesterday) == False:
                     print("大a修盘")
                     return
                 formatted_date = yesterday.strftime('%Y-%m-%d')
                # cn_holidays = holidays.China()
                

                 print(formatted_date)
                 k_25=bs.query_history_k_data_plus(code,
        "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST",str(formatted_date),
                 str(formatted_date)).data
                 shuju.append([name,str(formatted_date),k_25[0][5],str(guxi),data_[0][9],str(guxi/float(k_25[0][5])*100),data_[0][10],data_[0][12]])
                 
            #  print(str(date_)+" 当日股价 "+k_[0][5]+"总股息 "+str(guxi)+" 股息 "+data_[0][9]+" 股息率 "+str(guxilu) +" "+data_[0][10]+" "+data_[0][12]+'\n')
             


def jj_fl():
    '''
    该函数作用将股票按照行业分剋并保存到file文件目录下
    '''
    file_name = "file"
    my_file = Path(file_name)
    if my_file.exists():
        print("----flie---exists---")
    else:
        os.mkdir(file_name)
    # 登陆系统
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)
    # 获取行业分类数据
    # rs = bs.query_stock_industry()
    rs=bs.query_all_stock(day="2017-06-30")
    #rs = bs.query_stock_basic(code_name="浦发银行")
    print('query_stock_industry error_code:'+rs.error_code)
    print('query_stock_industry respond  error_msg:'+rs.error_msg)
    print(type(rs.get_row_data()))
    #打印结果集
    industry_list = []
    type_ = set()
    while (rs.error_code == '0') & rs.next():
        val = rs.get_row_data()
        # type_.add(val[3])
    #     # 获取一条记录，将记录合并在一起
        industry_list.append(rs.get_row_data())
    # result = pd.DataFrame(industry_list, columns=rs.fields)
    # # 结果集输出到csv文件
    # result.to_csv("./stock_industry.csv", encoding="gbk", index=False)
    # print(result)
    print("股票数目:%d\n",len(industry_list))
    for data in industry_list:
                print(data)
                name = "file/" + "gupiao" + ".txt"
                # print(name)
                fo = open(name, "a+",encoding='utf-8')
                # print(data[2])
                #打印股息=
                # print(data)
                if len(data) == 0:
                     continue
                data_=bs.query_dividend_data(data[0],'2021').data
                # bs.query_history_k_data_plus
                # print(data_)
                if len(data_) !=0:
                    # print(data_)
                    # print(data[2]," ",data_[0][9],data_[0][10],data_[0][12])
                    #data[0][8]股息日
                    k_=bs.query_history_k_data_plus(data[0],
        "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST",
        data_[0][7],data_[0][7]).data
                    #k_[0][5]收盘价 data_[0][9]股息
                    # print("k_:",k_,"k[0-5]",k_[0][5])
                    # print(data_[0][9],k_[0][5])
                    guxilu=0.00
                    #如果是派发股份情况用会存在异常 分红为null非数字 需要继续查下一个元素是否有分红这里简单支招第一个
                    try:
                        guxilu= float(data_[0][9])/float(k_[0][5])*100

                    except ValueError as e:
                        print(f"ValueError异常 {e}")
                        guxilu=0.00
                        print(guxilu)

                    if guxilu > 7:
                         print(" 当日股价 "+k_[0][5]+" 股息 "+data_[0][9]+" 股息率 "+str(guxilu)+" "+data[1] + " " + data[2] +" "+data_[0][10]+" "+data_[0][12]+'\n')
                    
                    fo.writelines(" 当日股价 "+k_[0][5]+" 股息 "+data_[0][9]+" 股息率 "+str(guxilu)+" "+data[1] + " " + data[2] +" "+data_[0][10]+" "+data_[0][12]+'\n')
                    continue
                # fo.writelines(data[1] + " " + data[2]+'\n')
                
        
    #登出系统
    # rs2 = bs.query_stock_basic(code_name="宁的时代")
    # print(rs2.get_row_data())
    # rs2 = bs.query_all_stock(day="2020-05-22")
    # while rs2.next():

    #     print(rs2.get_row_data())

    bs.logout()


if __name__ == "__main__":
    jj_fl()

    
