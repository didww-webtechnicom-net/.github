# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class PhoneNumberTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.messaging.v1.services("MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .phone_numbers.create(phone_number_sid="PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        values = {'PhoneNumberSid': "PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://messaging.twilio.com/v1/Services/MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/PhoneNumbers',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:12:31Z",
                "date_updated": "2015-07-30T20:12:33Z",
                "phone_number": "+987654321",
                "country_code": "US",
                "capabilities": [],
                "url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.messaging.v1.services("MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .phone_numbers.create(phone_number_sid="PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        self.assertIsNotNone(actual)

    def test_create_with_capabilities_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:12:31Z",
                "date_updated": "2015-07-30T20:12:33Z",
                "phone_number": "+987654321",
                "country_code": "US",
                "capabilities": [
                    "MMS",
                    "SMS",
                    "Voice"
                ],
                "url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.messaging.v1.services("MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .phone_numbers.create(phone_number_sid="PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.messaging.v1.services("MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .phone_numbers("PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://messaging.twilio.com/v1/Services/MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/PhoneNumbers/PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.messaging.v1.services("MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .phone_numbers("PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.messaging.v1.services("MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .phone_numbers.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://messaging.twilio.com/v1/Services/MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/PhoneNumbers',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PhoneNumbers?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "next_page_url": null,
                    "key": "phone_numbers",
                    "url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PhoneNumbers?PageSize=50&Page=0"
                },
                "phone_numbers": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2015-07-30T20:12:31Z",
                        "date_updated": "2015-07-30T20:12:33Z",
                        "phone_number": "+987654321",
                        "country_code": "US",
                        "capabilities": [],
                        "url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ]
            }
            '''
        ))

        actual = self.client.messaging.v1.services("MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .phone_numbers.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.messaging.v1.services("MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .phone_numbers("PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://messaging.twilio.com/v1/Services/MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/PhoneNumbers/PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:12:31Z",
                "date_updated": "2015-07-30T20:12:33Z",
                "phone_number": "12345",
                "country_code": "US",
                "capabilities": [],
                "url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.messaging.v1.services("MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .phone_numbers("PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)
