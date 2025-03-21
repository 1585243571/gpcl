'''
@Author: your name
@Date: 2020-05-23 23:41:50
@LastEditTime: 2020-05-24 00:31:27
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /y/股票策略/tools/gupiao_fenlei.py
'''
import baostock as bs
import pandas as pd
from pathlib import Path
import os

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
    rs = bs.query_stock_industry()
    
    #rs = bs.query_stock_basic(code_name="浦发银行")
    print('query_stock_industry error_code:'+rs.error_code)
    print('query_stock_industry respond  error_msg:'+rs.error_msg)
    print(type(rs.get_row_data()))
    #打印结果集
    industry_list = []
    type_ = set()
    while (rs.error_code == '0') & rs.next():
        val = rs.get_row_data()
        type_.add(val[3])
    #     # 获取一条记录，将记录合并在一起
        industry_list.append(rs.get_row_data())
    # result = pd.DataFrame(industry_list, columns=rs.fields)
    # # 结果集输出到csv文件
    # result.to_csv("./stock_industry.csv", encoding="gbk", index=False)
    # print(result)
    print("股票数目:%d\n",len(industry_list))
    for data in industry_list:
    # print("--------------")
        #print(data)
        for val in type_:
            if (len(val) == 0) | (len(data) == 0):
                continue
            
            if val == data[3]:
                name = "file/" + val + ".txt"
                # print(name)
                fo = open(name, "a+",encoding='utf-8')
                # print(data[2])
                #打印股息=
                data_=bs.query_dividend_data(data[1],'2024').data
                # bs.query_history_k_data_plus
                if len(data_) !=0:
                    # print(data_)
                    # print(data[2]," ",data_[0][9],data_[0][10],data_[0][12])
                    #data[0][8]股息日
                    k_=bs.query_history_k_data_plus(data[1],
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


                    print(guxilu)
                    
                    fo.writelines(" 当日股价 "+k_[0][5]+" 股息 "+data_[0][9]+" 股息率 "+str(guxilu)+" "+data[1] + " " + data[2] +" "+data_[0][10]+" "+data_[0][12]+'\n')
                    continue
                fo.writelines(data[1] + " " + data[2]+'\n')
                
        
    #登出系统
    # rs2 = bs.query_stock_basic(code_name="宁的时代")
    # print(rs2.get_row_data())
    # rs2 = bs.query_all_stock(day="2020-05-22")
    # while rs2.next():

    #     print(rs2.get_row_data())

    bs.logout()


if __name__ == "__main__":
    jj_fl()

    
