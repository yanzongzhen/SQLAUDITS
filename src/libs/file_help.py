"""
    保存数据到本地
"""
from random import randint

import xlwt
import datetime
import os


def save_file(params, path):
    workbook = xlwt.Workbook(encoding="utf-8")
    booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)

    for i in range(len(params["title"])):
        booksheet.write(0, i, params["title"][i]["title"])

        for j in range(len(params["data"])):
            booksheet.write(j + 1, i, params["data"][j][params["title"][i]["title"]])

    try:
        time_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + str(randint(1111, 9999))
        save_path = os.path.join(path, time_str+'.xls')
        save_name = time_str+'.xls'
        workbook.save(save_path)
        return save_name, True
    except Exception as e:
        print(e)
        return None, False
