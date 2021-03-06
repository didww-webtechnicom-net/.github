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


class AccessTokenTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .access_tokens.create(identity="identity", factor_type="push")

        values = {'Identity': "identity", 'FactorType': "push", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/AccessTokens',
            data=values,
        ))

    def test_create_with_ttl_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "YKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "entity_identity": "ff483d1ff591898a9942916050d2ca3f",
                "factor_type": "push",
                "factor_friendly_name": "John Doe iPhone",
                "ttl": 300,
                "date_created": "2015-07-30T20:00:00Z",
                "token": "eyJ6aXAiOiJERUYiLCJraWQiOiJTQVNfUzNfX19LTVNfdjEiLCJjdHkiOiJ0d2lsaW8tZnBhO3Y9MSIsImVuYyI6IkEyNTZHQ00iLCJhbGciOiJkaXIifQ..qjltWfIgQaTwp2De.81Z_6W4kR-hdlAUvJQCbwS8CQ7QAoFRkOvNMoySEj8zEB4BAY3MXhPARfaK4Lnr4YceA2cXEmrzPKQ7bPm0XZMGYm1fqLYzAR8YAqUetI9WEdQLFytg1h4XnJnXhgd99eNXsLkpKHhsCnFkchV9eGpRrdrfB0STR5Xq0fdakomb98iuIFt1XtP0_iqxvxQZKe1O4035XhK_ELVwQBz_qdI77XRZBFM0REAzlnEOe61nOcQxkaIM9Qel9L7RPhcndcCPFAyYjxo6Ri5c4vOnszLDiHmeK9Ep9fRE5-Oz0px0ZEg_FgTUEPFPo2OHQj076H1plJnFr-qPINDJkUL_i7loqG1IlapOi1JSlflPH-Ebj4hhpBdMIcs-OX7jhqzmVqkIKWkpPyPEmfvY2-eA5Zpoo08YpqAJ3G1l_xEcHl28Ijkefj1mdb6E8POx41skAwXCpdfIbzWzV_VjFpmwhacS3JZNt9C4hVG4Yp-RGPEl1C7aJHRIUavAmoRHaXbfG20zzv5Zu0P5PcopDszzoqVfZpzc.GCt35DWTurtP-QaIL5aBSQ",
                "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AccessTokens/YKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .access_tokens.create(identity="identity", factor_type="push")

        self.assertIsNotNone(actual)

    def test_create_without_ttl_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "YKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "entity_identity": "ff483d1ff591898a9942916050d2ca3f",
                "factor_type": "push",
                "factor_friendly_name": "John Doe iPhone",
                "ttl": 60,
                "date_created": "2015-07-30T20:00:00Z",
                "token": "eyJ6aXAiOiJERUYiLCJraWQiOiJTQVNfUzNfX19LTVNfdjEiLCJjdHkiOiJ0d2lsaW8tZnBhO3Y9MSIsImVuYyI6IkEyNTZHQ00iLCJhbGciOiJkaXIifQ..qjltWfIgQaTwp2De.81Z_6W4kR-hdlAUvJQCbwS8CQ7QAoFRkOvNMoySEj8zEB4BAY3MXhPARfaK4Lnr4YceA2cXEmrzPKQ7bPm0XZMGYm1fqLYzAR8YAqUetI9WEdQLFytg1h4XnJnXhgd99eNXsLkpKHhsCnFkchV9eGpRrdrfB0STR5Xq0fdakomb98iuIFt1XtP0_iqxvxQZKe1O4035XhK_ELVwQBz_qdI77XRZBFM0REAzlnEOe61nOcQxkaIM9Qel9L7RPhcndcCPFAyYjxo6Ri5c4vOnszLDiHmeK9Ep9fRE5-Oz0px0ZEg_FgTUEPFPo2OHQj076H1plJnFr-qPINDJkUL_i7loqG1IlapOi1JSlflPH-Ebj4hhpBdMIcs-OX7jhqzmVqkIKWkpPyPEmfvY2-eA5Zpoo08YpqAJ3G1l_xEcHl28Ijkefj1mdb6E8POx41skAwXCpdfIbzWzV_VjFpmwhacS3JZNt9C4hVG4Yp-RGPEl1C7aJHRIUavAmoRHaXbfG20zzv5Zu0P5PcopDszzoqVfZpzc.GCt35DWTurtP-QaIL5aBSQ",
                "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AccessTokens/YKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .access_tokens.create(identity="identity", factor_type="push")

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .access_tokens("YKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/AccessTokens/YKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "YKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "entity_identity": "ff483d1ff591898a9942916050d2ca3f",
                "factor_type": "push",
                "factor_friendly_name": "John Doe iPhone",
                "ttl": 60,
                "date_created": "2015-07-30T20:00:00Z",
                "token": "eyJ6aXAiOiJERUYiLCJraWQiOiJTQVNfUzNfX19LTVNfdjEiLCJjdHkiOiJ0d2lsaW8tZnBhO3Y9MSIsImVuYyI6IkEyNTZHQ00iLCJhbGciOiJkaXIifQ..qjltWfIgQaTwp2De.81Z_6W4kR-hdlAUvJQCbwS8CQ7QAoFRkOvNMoySEj8zEB4BAY3MXhPARfaK4Lnr4YceA2cXEmrzPKQ7bPm0XZMGYm1fqLYzAR8YAqUetI9WEdQLFytg1h4XnJnXhgd99eNXsLkpKHhsCnFkchV9eGpRrdrfB0STR5Xq0fdakomb98iuIFt1XtP0_iqxvxQZKe1O4035XhK_ELVwQBz_qdI77XRZBFM0REAzlnEOe61nOcQxkaIM9Qel9L7RPhcndcCPFAyYjxo6Ri5c4vOnszLDiHmeK9Ep9fRE5-Oz0px0ZEg_FgTUEPFPo2OHQj076H1plJnFr-qPINDJkUL_i7loqG1IlapOi1JSlflPH-Ebj4hhpBdMIcs-OX7jhqzmVqkIKWkpPyPEmfvY2-eA5Zpoo08YpqAJ3G1l_xEcHl28Ijkefj1mdb6E8POx41skAwXCpdfIbzWzV_VjFpmwhacS3JZNt9C4hVG4Yp-RGPEl1C7aJHRIUavAmoRHaXbfG20zzv5Zu0P5PcopDszzoqVfZpzc.GCt35DWTurtP-QaIL5aBSQ",
                "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AccessTokens/YKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .access_tokens("YKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)
