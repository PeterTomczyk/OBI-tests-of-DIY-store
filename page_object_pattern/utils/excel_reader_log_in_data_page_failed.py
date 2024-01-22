import xlrd
from page_object_pattern.utils.entering_log_in_data_page_failed import EnteringLogInDataPageFailed


class ExcelReaderLogInDataPageFailed:

    @staticmethod
    def get_data():
        wb = xlrd.open_workbook("../utils/test_log_in_failed.xlsx")
        sheet = wb.sheet_by_index(0)
        data = []
        for i in range(1, sheet.nrows):
            account_data = {
                "username": sheet.cell(i, 0).value,
                "password": sheet.cell(i, 1).value,
            }
            entering_log_in_data_page_failed = EnteringLogInDataPageFailed(**account_data)
            data.append(entering_log_in_data_page_failed)
        return data
