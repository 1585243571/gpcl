import sys
sys.path.append("./tools")
import baostock as bs
import pandas as pd
from pathlib import Path
import os
from prettytable import PrettyTable
import gupiao_fenlei
import celuoe



import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_email(message):
    # 发件人邮箱及授权码（授权码需要在QQ邮箱中开启SMTP服务并获取）
    sender_email = '1585243571@qq.com'
    smtp_auth_code = '推送吗需要自己获取'

    # 收件人邮箱地址
    recipient_email = '1585243571@qq.com'

    # 邮件内容
    subject = 'Test Message'
    body = message

    # 创建MIMEText对象
    message = MIMEText(body, 'plain', 'utf-8')
    message['From'] = Header(sender_email)
    message['To'] = Header(recipient_email)
    message['Subject'] = Header(subject)

    try:
        # 连接到SMTP服务器
        smtp_server = 'smtp.qq.com'
        smtp_port = 465
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(sender_email, smtp_auth_code)
        server.sendmail(sender_email, [recipient_email], message.as_string())
        print('Message sent successfully!')
    except Exception as e:
        print(f'Failed to send message. Error: {e}')
    finally:
        server.quit()


def init_code_list(file_name,list_):
    with open('example.txt', 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            print(line.strip())

def tab(shuju):
    data = [
    ["code","date", "当日股价", "总股息","股息","股息率","税前税后股息","派发信息"]]
    for iterm in shuju:
        if len(iterm) == 0:
            continue
        data.append(iterm)
    table = PrettyTable()
    table.field_names = data[0]
    for row in data[1:]:
        table.add_row(row)
    print(str(table))
    send_email(str(table))



if __name__ == "__main__":


    # data = [
    # ["code","date", "当日股价", "总股息","股息","股息率","税前税后股息","派发信息"]]
    
    #  gupiao_fenlei.jj_fl()

    lg = bs.login()
    # celuoe.test1(bs)
#输入股票名称即可查找2000-20025年之间的股息
    name=["冀中能源","南京银行","民生银行"
          ,"江苏银行","中国神华","浙商银行","上海银行","山西焦煤"]
    for i in name:
        shuju=[[]]
        gupiao_fenlei.guxi(bs,i,2000,2026,shuju)
        tab(shuju)
        # for iterm in shuju:
        #     if len(iterm) == 0:
        #         continue
        #     print(iterm)
        #     data.append(iterm)

    
    # table = PrettyTable()
    # table.field_names = data[0]
    # for row in data[1:]:
    #     print(row)
    #     table.add_row(row)
    # print(table)
