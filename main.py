'''
@Author: your name
@Date: 2020-05-23 23:54:22
@LastEditTime: 2020-05-24 09:30:05
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /y/股票策略/main.py
'''
import sys


sys.path.append("./tools")

import baostock as bs
import pandas as pd
from pathlib import Path
import os
import gupiao_fenlei
import celuoe


if __name__ == "__main__":
    gupiao_fenlei.jj_fl()
    lg = bs.login()
    celuoe.test1(bs)