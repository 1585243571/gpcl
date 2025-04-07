# 安装必要库

from datetime import datetime
import chinese_calendar as calendar

def is_a_share_open(date):
    """判断A股当日是否开盘"""
    # 规则1：排除所有周末
    if date.weekday() >= 5:
        return False
    
    # 规则2：排除法定节假日及调休的休息日
    return not calendar.is_holiday(date)


