import os

import openpyxl

from config import datas_path


class ReadExcelUtil:
    @staticmethod
    def read_excle(file_path,sheet_name):

        wk = openpyxl.load_workbook(file_path)
        sheet = wk[sheet_name]

        datas = []
        for row in sheet.iter_rows(min_row=2):
            data = [cell.value for cell in row]
            for i in range(len(data)) :
                if data[i] is None:
                    data[i] = ''
            data = tuple(data)
            datas.append(data)
        print(datas)
        return datas

if __name__ == '__main__':
    file_path = os.path.join(datas_path, 'ecshop_datas.xlsx')
    sheet_name = 'login_data'

    ReadExcelUtil.read_excle(file_path, sheet_name)

