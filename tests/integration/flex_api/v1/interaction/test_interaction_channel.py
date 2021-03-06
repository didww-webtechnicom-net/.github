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


class InteractionChannelTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.flex_api.v1.interaction("KDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                   .channels("UOXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://flex-api.twilio.com/v1/Interactions/KDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Channels/UOXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "UOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1",
                "type": "chat",
                "interaction_sid": "KDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://flex-api.twilio.com/v1/Interactions/KDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/UOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1",
                "links": {
                    "participants": "https://flex-api.twilio.com/v1/Interactions/KDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/UOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1/Participants",
                    "invites": "https://flex-api.twilio.com/v1/Interactions/KDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/UOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1/Invites"
                }
            }
            '''
        ))

        actual = self.client.flex_api.v1.interaction("KDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .channels("UOXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.flex_api.v1.interaction("KDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                   .channels.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://flex-api.twilio.com/v1/Interactions/KDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Channels',
        ))

    def test_read_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "channels": [
                    {
                        "sid": "UOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1",
                        "type": "chat",
                        "interaction_sid": "KDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "url": "https://flex-api.twilio.com/v1/Interactions/KDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/UOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1",
                        "links": {
                            "participants": "https://flex-api.twilio.com/v1/Interactions/KDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/UOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1/Participants",
                            "invites": "https://flex-api.twilio.com/v1/Interactions/KDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/UOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1/Invites"
                        }
                    },
                    {
                        "sid": "UOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa2",
                        "type": "sms",
                        "interaction_sid": "KDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "url": "https://flex-api.twilio.com/v1/Interactions/KDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/UOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa2",
                        "links": {
                            "participants": "https://flex-api.twilio.com/v1/Interactions/KDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/UOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa2/Participants",
                            "invites": "https://flex-api.twilio.com/v1/Interactions/KDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/UOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa2/Invites"
                        }
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://flex-api.twilio.com/v1/Interactions/KDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://flex-api.twilio.com/v1/Interactions/KDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "channels"
                }
            }
            '''
        ))

        actual = self.client.flex_api.v1.interaction("KDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .channels.list()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.flex_api.v1.interaction("KDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                   .channels("UOXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update(status="close")

        values = {'Status': "close", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://flex-api.twilio.com/v1/Interactions/KDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Channels/UOXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
            data=values,
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "UOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1",
                "interaction_sid": "KDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "type": "chat",
                "url": "https://flex-api.twilio.com/v1/Interactions/KDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/UOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1",
                "links": {
                    "participants": "https://flex-api.twilio.com/v1/Interactions/KDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/UOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1/Participants",
                    "invites": "https://flex-api.twilio.com/v1/Interactions/KDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/UOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1/Invites"
                }
            }
            '''
        ))

        actual = self.client.flex_api.v1.interaction("KDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .channels("UOXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update(status="close")

        self.assertIsNotNone(actual)

    def test_update_status_closed_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "UOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1",
                "interaction_sid": "KDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "type": "chat",
                "url": "https://flex-api.twilio.com/v1/Interactions/KDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/UOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1",
                "links": {
                    "participants": "https://flex-api.twilio.com/v1/Interactions/KDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/UOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1/Participants",
                    "invites": "https://flex-api.twilio.com/v1/Interactions/KDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/UOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1/Invites"
                }
            }
            '''
        ))

        actual = self.client.flex_api.v1.interaction("KDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .channels("UOXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update(status="close")

        self.assertIsNotNone(actual)
