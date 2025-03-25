import sys
sys.path.append("./tools")
import baostock as bs
import pandas as pd
from pathlib import Path
import os
from prettytable import PrettyTable
import gupiao_fenlei
import celuoe
if __name__ == "__main__":


    data = [
    ["code","date", "当日股价", "总股息","股息","股息率","税前税后股息","派发信息"]]
    
    #  gupiao_fenlei.jj_fl()

    lg = bs.login()
    # celuoe.test1(bs)
#输入股票名称即可查找2000-20025年之间的股息
    name=["冀中能源","南京银行","民生银行","江苏银行"]
    for i in name:
        shuju=[[]]
        gupiao_fenlei.guxi(bs,i,2000,2025,shuju)
        for iterm in shuju:
            if len(iterm) == 0:
                continue
            print(iterm)
            data.append(iterm)

    
    table = PrettyTable()
    table.field_names = data[0]
    for row in data[1:]:
        print(row)
        table.add_row(row)
    print(table)
