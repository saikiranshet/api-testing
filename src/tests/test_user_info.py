import pytest
from ..utils.routes import USER_INFO
from ..utils import DATA


class TestUserInfo:
    def test_fetch_user_info(self, get_api_obj):
        """
        This
        """
        url_offset = USER_INFO.GET_USER_INFO
        data = get_api_obj.get(url_offset)
        contacts = data["contacts"]
        assert isinstance(contacts, list)
        for contact in contacts:
            assert "emails" in contact
            assert "phone_numbers" in contact

    def test_fetch_user_info_by_phone_number(self, get_api_obj):
        """
        This
        """
        url_offset = f"{USER_INFO.GET_USER_INFO}?phone_number={DATA.PHONE_NUMBER}"
        data = get_api_obj.get(url_offset)
        contacts = data["contacts"]
        assert isinstance(contacts, list)
        for contact in contacts:
            phone_numbers = [contact["value"] for contact in contact["phone_numbers"]]
            assert DATA.PHONE_NUMBER in phone_numbers

    def test_fetch_user_info_by_email(self, get_api_obj):
        """
        This
        """
        url_offset = f"{USER_INFO.GET_USER_INFO}?email={DATA.EMAIL}"
        data = get_api_obj.get(url_offset)
        contacts = data["contacts"]
        assert isinstance(contacts, list)
        for contact in contacts:
            emails = [contact["value"] for contact in contact["emails"]]
            assert DATA.EMAIL in emails

    def test_fetch_user_info_desc(self, get_api_obj):
        """
        This
        """
        url_offset = f"{USER_INFO.GET_USER_INFO}?order=asc"
        data = get_api_obj.get(url_offset)
        contacts = data["contacts"]
        assert isinstance(contacts, list)

    def test_fetch_user_info_asc(self, get_api_obj):
        """
        This
        """
        url_offset = f"{USER_INFO.GET_USER_INFO}?order=desc"
        data = get_api_obj.get(url_offset)
        contacts = data["contacts"]
        assert isinstance(contacts, list)

    def test_fetch_user_info_created_at(self, get_api_obj):
        """
        This
        """
        url_offset = f"{USER_INFO.GET_USER_INFO}?order_by=created_at"
        data = get_api_obj.get(url_offset)
        contacts = data["contacts"]
        assert isinstance(contacts, list)

    def test_fetch_user_info_updated_at(self, get_api_obj):
        """
        This
        """
        url_offset = f"{USER_INFO.GET_USER_INFO}?order_by=updated_at"
        data = get_api_obj.get(url_offset)
        contacts = data["contacts"]
        assert isinstance(contacts, list)

    def test_fetch_user_info_all_parms(self, get_api_obj):
        """
        This
        """
        url_offset = f"{USER_INFO.GET_USER_INFO}?order=asc&order_by=created_at&phone_number={DATA.PHONE_NUMBER}"
        data = get_api_obj.get(url_offset)
        contacts = data["contacts"]
        assert isinstance(contacts, list)
        for contact in contacts:
            phone_numbers = [contact["value"] for contact in contact["phone_numbers"]]
            assert DATA.PHONE_NUMBER in phone_numbers