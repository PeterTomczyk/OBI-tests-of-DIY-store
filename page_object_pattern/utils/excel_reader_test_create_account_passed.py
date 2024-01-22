import xlrd

from page_object_pattern.utils.entering_test_create_acccount_passed import EnteringTestCreateAccountPassed


class ExcelReaderTestCreateAccountPassed:

    @staticmethod
    def get_data():
        wb = xlrd.open_workbook("../utils/test_create_account_passed.xlsx")
        sheet = wb.sheet_by_index(0)
        data = []
        for i in range(1, sheet.nrows):
            account_data = {
                "name": sheet.cell(i, 0).value,
                "last_name": sheet.cell(i, 1).value,
                "street_name": sheet.cell(i, 2).value,
                "street_number": sheet.cell(i, 3).value,
                "postal_code": sheet.cell(i, 4).value,
                "town": sheet.cell(i, 5).value,
                "password": sheet.cell(i, 6).value,
                "repeat_password": sheet.cell(i, 7).value,
                "phone": sheet.cell(i, 8).value,
            }
            entering_test_create_account_passed = EnteringTestCreateAccountPassed(**account_data)
            data.append(entering_test_create_account_passed)
        return data
