import xlrd
from page_object_pattern.utils.entering_log_in_data_page_pased import EnteringLogInDataPagePassed


class ExcelReaderLogInDataPagePassed:

    @staticmethod
    def get_data():
        wb = xlrd.open_workbook("../utils/test_log_in_passed.xlsx")
        sheet = wb.sheet_by_index(0)
        data = []
        for i in range(1, sheet.nrows):
            account_data = {
                "username": sheet.cell(i, 0).value,
                "password": sheet.cell(i, 1).value,
            }
            entering_log_in_data_page_passed = EnteringLogInDataPagePassed(**account_data)
            data.append(entering_log_in_data_page_passed)
        return data

