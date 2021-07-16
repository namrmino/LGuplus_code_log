##################################################################
##################################################################

import pandas as pd
import numpy as np
import datetime
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

##################################################################
##################################################################

def MakeDateCusum(df_num):
    re_dict = df_num['date_y'].value_counts().to_dict()

    df_num['date_y'] = df_num['date_y'].astype('str')
    daterange = pd.DataFrame(pd.date_range(df_num['date_y'][0], df_num['date_y'][len(df_num['date_y'])-1]), columns=['date_y'])
    daterange['date_y'] = daterange['date_y'].astype('str')

    result1 = pd.merge(daterange, df_num, on='date_y', how='left')
    result1 = result1.reset_index(drop=True)
    result1['apt_no'] = result1['apt_no'].fillna(result1['apt_no'][0])
    result1['cust_no_x'] = result1['cust_no_x'].fillna(result1['cust_no_x'][0])
    result1 = result1.drop_duplicates(['date_y','cust_no_y','apt_nm_y','apt_addr_y','sys_creation_date_y'], keep='first')
    result1 = result1.sort_values(by=['date_y'], axis=0)
    result1 = result1.reset_index(drop=True)
    result1['date_y'] = result1['date_y'].astype('str')
    df_num['date_y'] = df_num['date_y'].astype('str')
    result1['date_count'] = 0

    ddd = list(set(result1['date_y'].unique()))
    ddd.sort()

    dict_key_value = {}
    aaa = 0
    for temp in ddd:
        if temp in list(re_dict.keys()):
            aaa += re_dict[temp]
            dict_key_value[temp] = aaa
        else:
            dict_key_value[temp] = aaa

    result1['date_count'] = result['date_y'].apply(lambda x: dict_key_value[x])
    return result1

##################################################################
##################################################################

def MakeDFxls(DataFrame):
    df_xls = pd.DataFrame(columns=['','개요','유형(소)분류','예정일자','요청내용','대상구분코드','대상ID','처리팀','담당자','신고자','신고자전화번호'])

    outline_list = []
    sch_date_list = []
    task_team_list = []
    f_man_list = []

    for i in range(len(DataFrame)):
        outline = '[PILOT_신규아파트입주알림][건물군ID:{apt_no}][{apt_nm}][입주시작일:{date_y}][{apt_addr_new}]'
        outline = outline.format(apt_no = DataFrame.iloc[i][0],
                                apt_nm = DataFrame.iloc[i][3],
                                date_y = DataFrame.iloc[i][1],
                                apt_addr_new = DataFrame.iloc[i][4])
        outline_list.append(outline)

        sch_date = '{date_y}'
        sch_date = sch_date.format(date_y = (datetime.now() + relativedelta(days=5)).strftime("%Y-%m-%d").replace('-',''))
        sch_date_list.append(sch_date)

        task_team = '{task_team}'
        task_team = task_team.format(task_team = DataFrame.iloc[i][11])
        task_team_list.append(task_team)

        f_man = '{f_man}'
        f_man = f_man.format(f_man = DataFrame.iloc[i][12])
        f_man_list.append(f_man)

    df_xls['개요'] = outline_list
    df_xls['유형(소)분류'] = '000300'
    df_xls['유형(소)분류'] = df_xls['유형(소)분류'].astype('string')
    df_xls['예정일자'] = sch_date_list
    df_xls['요청내용'] = outline_list
    df_xls['처리팀'] = task_team_list
    df_xls['담장자'] = f_man_list

    for i in range(len(df_xls)):
        if df_xls['처리팀'][i] == 'nan':
            df_xls['처리팀'][i] = '1067571'
            df_xls['담당자'][i] = np.nan

    return df_xls

##################################################################
##################################################################

def MakeDFxls2(DataFrame):
    df_xls = pd.DataFrame(columns=['','개요','유형(소)분류','예정일자','요청내용','대상구분코드','대상ID','처리팀','담당자','신고자','신고자전화번호'])

    outline_list = []
    sch_date_list = []
    task_team_list = []
    f_man_list = []

    for i in range(len(DataFrame)):
        outline = '[PILOT_신규아파트입주알림][건물군ID:{apt_no}][{apt_nm}][입주시작일:{date_y}][{apt_addr_new}]'
        outline = outline.format(apt_no = DataFrame.iloc[i][0],
                                apt_nm = DataFrame.iloc[i][3],
                                date_y = DataFrame.iloc[i][1],
                                apt_addr_new = DataFrame.iloc[i][5])
        outline_list.append(outline)

        sch_date = '{date_y}'
        sch_date = sch_date.format(date_y = (datetime.now() + relativedelta(days=5)).strftime("%Y-%m-%d").replace('-',''))
        sch_date_list.append(sch_date)

        task_team = '{task_team}'
        task_team = task_team.format(task_team = DataFrame.iloc[i][9])
        task_team_list.append(task_team)

        f_man = '{f_man}'
        f_man = f_man.format(f_man = DataFrame.iloc[i][10])
        f_man_list.append(f_man)

    df_xls['개요'] = outline_list
    df_xls['유형(소)분류'] = '000300'
    df_xls['유형(소)분류'] = df_xls['유형(소)분류'].astype('string')
    df_xls['예정일자'] = sch_date_list
    df_xls['요청내용'] = outline_list
    df_xls['처리팀'] = task_team_list
    df_xls['담장자'] = f_man_list

    for i in range(len(df_xls)):
        if df_xls['처리팀'][i] == 'nan':
            df_xls['처리팀'][i] = '1067571'
            df_xls['담당자'][i] = np.nan

    return df_xls

##################################################################
##################################################################




