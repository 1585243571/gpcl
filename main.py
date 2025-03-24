import sys
sys.path.append("./tools")
import baostock as bs
import pandas as pd
from pathlib import Path
import os
import gupiao_fenlei
import celuoe
if __name__ == "__main__":
    #  gupiao_fenlei.jj_fl()

    # lg = bs.login()
    # celuoe.test1(bs)
#输入股票名称即可查找2000-20025年之间的股息
    gupiao_fenlei.guxi('中国神华',2000,2025)
    
