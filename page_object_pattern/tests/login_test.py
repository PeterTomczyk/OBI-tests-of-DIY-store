from page_object_pattern.pages.login_data_page import LoginDataPage
import pytest
import allure
from page_object_pattern.utils.excel_reader_log_in_data_page_failed import ExcelReaderLogInDataPageFailed
from page_object_pattern.utils.excel_reader_log_in_data_page_passed import ExcelReaderLogInDataPagePassed


@pytest.mark.usefixtures("setup")
class TestLogIn:

    @allure.title("Test login passed")
    @allure.description("This is a successful login in test")
    @pytest.mark.parametrize("data", ExcelReaderLogInDataPagePassed.get_data())
    def test_log_in_passed(self, data):
        login_data_page = LoginDataPage(self.driver)
        login_data_page.open_page()
        login_data_page.log_in(data.username, data.password)

        assert login_data_page.is_logout_link_displayed()

    @allure.title("Test login failed")
    @allure.description("This is a failed login in test")
    @pytest.mark.parametrize("data", ExcelReaderLogInDataPageFailed.get_data())
    def test_log_in_failed(self, data):
        login_data_page = LoginDataPage(self.driver)
        login_data_page.open_page()
        login_data_page.log_in(data.username, data.password)

        assert "Zaloguj się do Twojego Konta" in login_data_page.log_in_message()
