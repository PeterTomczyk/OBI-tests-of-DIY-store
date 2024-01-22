import random
import allure
import pytest
from page_object_pattern.pages.account_registration_page import AccountRegistrationPage
from page_object_pattern.utils.excel_reader_test_create_account_failed import ExcelReaderTestCreateAccountFailed
from page_object_pattern.utils.excel_reader_test_create_account_passed import ExcelReaderTestCreateAccountPassed


@pytest.mark.usefixtures("setup")
class TestOfCreatingAccount:

    @allure.title("Test create account passed")
    @allure.description("This is test of correct account creation")
    @pytest.mark.parametrize("data", ExcelReaderTestCreateAccountPassed.get_data())
    def test_create_account_passed(self, data):
        email = str(random.randint(0, 1000)) + "pythondeveloper@o2.pl"
        account_registration_page = AccountRegistrationPage(self.driver)
        account_registration_page.open_page()
        account_registration_page.set_personal_data(data.name, data.last_name)
        account_registration_page.set_address_part_1(data.street_name, data.street_number)
        account_registration_page.set_address_part_2(data.postal_code, data.town)
        account_registration_page.set_email(email)
        account_registration_page.set_password(data.password, data.repeat_password)
        account_registration_page.set_phone(data.phone)
        account_registration_page.newsletter_subscription()
        account_registration_page.consent_to_the_conditions()
        account_registration_page.save_data()

        assert "Witaj nowy użytkowniku OBI.pl!" in account_registration_page.correct_msg_created()

    @allure.title("Test create account failed")
    @allure.description("This is test of incorrect account creation")
    @pytest.mark.parametrize("data", ExcelReaderTestCreateAccountFailed.get_data())
    def test_create_account_failed(self, data):
        account_registration_page = AccountRegistrationPage(self.driver)
        account_registration_page.open_page()
        account_registration_page.set_personal_data(data.name, data.last_name)
        account_registration_page.set_address_part_1(data.street_name, data.street_number)
        account_registration_page.set_address_part_2(data.postal_code, data.town)
        account_registration_page.set_email(data.email)
        account_registration_page.set_password(data.password, data.repeat_password)
        account_registration_page.set_phone(data.phone)
        account_registration_page.newsletter_subscription()
        account_registration_page.consent_to_the_conditions()
        account_registration_page.save_data()

        assert "Pod tym adresem mailowym zostało już zarejestrowane konto Klienta na OBI.pl." in account_registration_page.error_msg_created()

