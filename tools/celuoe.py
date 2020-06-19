'''
@Author: your name
@Date: 2020-05-24 08:55:16
@LastEditTime: 2020-05-25 23:29:19
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /y/股票策略/tools/celuoe.py
'''
import baostock as bs
import pandas as pd
import os

def test1(bs):
    rs = bs.query_stock_industry()
    print(rs.get_row_data())
    
class Interface:
    def __init__(self,bs,start_date='2020-06-15',end_date='2020-06-16'):
        #### 登陆系统 ####
        self.bs_ = bs 
        self.tatol_=0
        lg = self.bs_.login()
        # 显示登陆返回信息
        print('login respond error_code:'+lg.error_code)
        print('login respond  error_msg:'+lg.error_msg)
        self.industry_list_ = self.get_industry_list()
        self.hsitory_k_data_ = []
        for val in self.industry_list_:
            data = self.get_history_k_data(val[1],start_date,end_date)
#            print(data)
            if len(data) == 2:
                self.hsitory_k_data_.append(data) 
 #               print(data[1])
                self.strategy(data[0],data[1])
            elif len(data) == 3:
                self.strategy_3(data[0],data[1],data[2])
            elif len(data) == 1:
                self.strategy_4(data[0])
        print("hstory_k_data_size:%d",len(self.hsitory_k_data_))
        print("----------------:%d",self.tatol_) 
        self.stop()
    def stop(self):
        ### 关闭系统 ###
        self.bs_.logout()
    def strategy_er_zhu(self,data1,data2):
        pass 

    def strategy(self,data1,data2):
        #策略一  open 2 ，high 3 , low 4,close 5 找锤子线看涨
            bz = 10
            if float(data1[2]) > float(data1[5]):
                if float(data2[5]) < float(data1[2]):
                    if float(data2[2]) < float(data2[5]):
                        v = (float(data2[5]) - float(data2[2]))
                        if v == 0:
                            v = 0.001
                        if  ((float(data2[2]) - float(data2[4])) / v ) > bz:
                            if (float(data2[3]) - float(data2[5])) / v < 10:
                                print(data2)
                                cmd = "grep -r  " + data2[1] + " /home/zn/y/股票策略/file "
                                os.system(cmd)

    def strategy_3(self,data,data1,data2):
        if float(data[2]) < float(data[5]):
            if float(data1[2]) < float(data[5]):
                if float(data2[2]) < float(data1[5]):
                    print(data2)
                     

    def strategy_4(self,data2):
        bz =10
        v = (float(data2[5]) - float(data2[2]))
        if v == 0:
            v = 0.001
        if  ((float(data2[2]) - float(data2[4])) / v ) > bz:
            if (float(data2[3]) - float(data2[5])) / v < 10:
                print(data2)
                cmd = "grep -r  " + data2[1] + " /home/zn/y/股票策略/file "
                os.system(cmd)

        
    def get_industry_list(self):
        rs_ = self.bs_.query_stock_industry()
        industry_list = []
        while (rs_.error_code == '0') & rs_.next():
            # 获取一条记录，将记录合并在一起
            industry_list.append(rs_.get_row_data())
        return industry_list
    def get_history_k_data(self,code,start_date,end_date):
        rs_ = self.bs_.query_history_k_data_plus(code,
        "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST",
        start_date=start_date, end_date=end_date,
        frequency="d", adjustflag="3")
        data = []
        while (rs_.error_code == '0') & rs_.next():
            data.append(rs_.get_row_data())
        #print("siee:%d",len(data))
        return data







    

if __name__ == "__main__":
    test = Interface(bs=bs)
    '''for i in range(10):
        if i == 0:
            continue
        a = '2020-05-'+ str(i+5);
        print(a)
        test = Interface(bs,a,a)
        
    '''
