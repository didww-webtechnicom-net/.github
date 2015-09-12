# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

import unittest
from datetime import datetime
from twilio.ext.holodeck import Holodeck
from twilio.rest.v2010.client import V2010Client
from twilio.rest.http import Response
from twilio.rest.resources.util import parse_iso_date


class NotificationIntegrationTest(unittest.TestCase):

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "api_version": "2008-08-01",
            "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "Tue, 18 Aug 2015 08:46:56 +0000",
            "date_updated": "Tue, 18 Aug 2015 08:46:57 +0000",
            "error_code": "15003",
            "log": "1",
            "message_date": "Tue, 18 Aug 2015 08:46:56 +0000",
            "message_text": "statusCallback=http%3A%2F%2Fexample.com%2Ffoo.xml&ErrorCode=15003&LogLevel=WARN&Msg=Got+HTTP+404+response+to+http%3A%2F%2Fexample.com%2Ffoo.xml",
            "more_info": "https://www.twilio.com/docs/errors/15003",
            "request_method": null,
            "request_url": "",
            "request_variables": "",
            "response_body": "",
            "response_headers": "",
            "sid": "NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications/NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .calls.get("CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .notifications.get("NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications/NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            query_params={},
            form_params={},
        )

    def test_fetch_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "api_version": "2008-08-01",
            "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "Tue, 18 Aug 2015 08:46:56 +0000",
            "date_updated": "Tue, 18 Aug 2015 08:46:57 +0000",
            "error_code": "15003",
            "log": "1",
            "message_date": "Tue, 18 Aug 2015 08:46:56 +0000",
            "message_text": "statusCallback=http%3A%2F%2Fexample.com%2Ffoo.xml&ErrorCode=15003&LogLevel=WARN&Msg=Got+HTTP+404+response+to+http%3A%2F%2Fexample.com%2Ffoo.xml",
            "more_info": "https://www.twilio.com/docs/errors/15003",
            "request_method": null,
            "request_url": "",
            "request_variables": "",
            "response_body": "",
            "response_headers": "",
            "sid": "NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications/NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .calls.get("CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .notifications.get("NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.api_version)
        self.assertEqual(u"2008-08-01", instance.api_version)
        self.assertIsNotNone(instance.call_sid)
        self.assertEqual(u"CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.call_sid)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Tue, 18 Aug 2015 08:46:56 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Tue, 18 Aug 2015 08:46:57 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.error_code)
        self.assertEqual(u"15003", instance.error_code)
        self.assertIsNotNone(instance.log)
        self.assertEqual(u"1", instance.log)
        self.assertIsNotNone(instance.message_date)
        self.assertEqual(parse_iso_date("Tue, 18 Aug 2015 08:46:56 +0000"), instance.message_date)
        self.assertIsNotNone(instance.message_text)
        self.assertEqual(u"statusCallback=http%3A%2F%2Fexample.com%2Ffoo.xml&ErrorCode=15003&LogLevel=WARN&Msg=Got+HTTP+404+response+to+http%3A%2F%2Fexample.com%2Ffoo.xml", instance.message_text)
        self.assertIsNotNone(instance.more_info)
        self.assertEqual(u"https://www.twilio.com/docs/errors/15003", instance.more_info)
        self.assertIsNone(instance.request_method)
        self.assertIsNotNone(instance.request_url)
        self.assertEqual(u"", instance.request_url)
        self.assertIsNotNone(instance.request_variables)
        self.assertEqual(u"", instance.request_variables)
        self.assertIsNotNone(instance.response_body)
        self.assertEqual(u"", instance.response_body)
        self.assertIsNotNone(instance.response_headers)
        self.assertEqual(u"", instance.response_headers)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)

    def test_delete_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(204, "{}"))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .calls.get("CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .notifications.delete("NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "DELETE",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications/NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            query_params={},
            form_params={},
        )

    def test_delete_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(204, "{}"))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .calls.get("CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .notifications.delete("NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        self.assertTrue(query.execute())

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json?PageSize=50&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json?PageSize=50&Page=0",
            "next_page_uri": null,
            "notifications": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "api_version": "2008-08-01",
                    "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "date_created": "Tue, 18 Aug 2015 08:46:56 +0000",
                    "date_updated": "Tue, 18 Aug 2015 08:46:57 +0000",
                    "error_code": "15003",
                    "log": "1",
                    "message_date": "Tue, 18 Aug 2015 08:46:56 +0000",
                    "message_text": "statusCallback=http%3A%2F%2Fexample.com%2Ffoo.xml&ErrorCode=15003&LogLevel=WARN&Msg=Got+HTTP+404+response+to+http%3A%2F%2Fexample.com%2Ffoo.xml",
                    "more_info": "https://www.twilio.com/docs/errors/15003",
                    "request_method": null,
                    "request_url": "",
                    "sid": "NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications/NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            ],
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .calls.get("CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .notifications.list(
                log=1,
                message_date=datetime(2008, 1, 2, 0, 0),
                message_date_before=datetime(2008, 1, 1, 0, 0),
                message_date_after=datetime(2008, 1, 3, 0, 0)
            )
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].account_sid)
        self.assertIsNotNone(instances[0].api_version)
        self.assertEqual(u"2008-08-01", instances[0].api_version)
        self.assertIsNotNone(instances[0].call_sid)
        self.assertEqual(u"CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].call_sid)
        self.assertIsNotNone(instances[0].date_created)
        self.assertEqual(parse_iso_date("Tue, 18 Aug 2015 08:46:56 +0000"), instances[0].date_created)
        self.assertIsNotNone(instances[0].date_updated)
        self.assertEqual(parse_iso_date("Tue, 18 Aug 2015 08:46:57 +0000"), instances[0].date_updated)
        self.assertIsNotNone(instances[0].error_code)
        self.assertEqual(u"15003", instances[0].error_code)
        self.assertIsNotNone(instances[0].log)
        self.assertEqual(u"1", instances[0].log)
        self.assertIsNotNone(instances[0].message_date)
        self.assertEqual(parse_iso_date("Tue, 18 Aug 2015 08:46:56 +0000"), instances[0].message_date)
        self.assertIsNotNone(instances[0].message_text)
        self.assertEqual(u"statusCallback=http%3A%2F%2Fexample.com%2Ffoo.xml&ErrorCode=15003&LogLevel=WARN&Msg=Got+HTTP+404+response+to+http%3A%2F%2Fexample.com%2Ffoo.xml", instances[0].message_text)
        self.assertIsNotNone(instances[0].more_info)
        self.assertEqual(u"https://www.twilio.com/docs/errors/15003", instances[0].more_info)
        self.assertIsNone(instances[0].request_method)
        self.assertIsNotNone(instances[0].request_url)
        self.assertEqual(u"", instances[0].request_url)
        self.assertIsNotNone(instances[0].sid)
        self.assertEqual(u"NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].sid)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json?PageSize=50&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json?PageSize=50&Page=0",
            "next_page_uri": null,
            "notifications": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "api_version": "2008-08-01",
                    "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "date_created": "Tue, 18 Aug 2015 08:46:56 +0000",
                    "date_updated": "Tue, 18 Aug 2015 08:46:57 +0000",
                    "error_code": "15003",
                    "log": "1",
                    "message_date": "Tue, 18 Aug 2015 08:46:56 +0000",
                    "message_text": "statusCallback=http%3A%2F%2Fexample.com%2Ffoo.xml&ErrorCode=15003&LogLevel=WARN&Msg=Got+HTTP+404+response+to+http%3A%2F%2Fexample.com%2Ffoo.xml",
                    "more_info": "https://www.twilio.com/docs/errors/15003",
                    "request_method": null,
                    "request_url": "",
                    "sid": "NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications/NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            ],
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .calls.get("CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .notifications.list(
                log=1,
                message_date=datetime(2008, 1, 2, 0, 0),
                message_date_before=datetime(2008, 1, 1, 0, 0),
                message_date_after=datetime(2008, 1, 3, 0, 0)
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            query_params={
                "Log": 1,
                "MessageDate": "2008-01-02",
                "MessageDate<": "2008-01-01",
                "MessageDate>": "2008-01-03"
            },
            form_params={},
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json?PageSize=50&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json?PageSize=50&Page=0",
            "next_page_uri": null,
            "notifications": [],
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .calls.get("CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .notifications.list(
                log=1,
                message_date=datetime(2008, 1, 2, 0, 0),
                message_date_before=datetime(2008, 1, 1, 0, 0),
                message_date_after=datetime(2008, 1, 3, 0, 0)
            )
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json?PageSize=50&Page=0",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json?PageSize=50&Page=0",
            "next_page_uri": null,
            "notifications": [],
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .calls.get("CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .notifications.list(
                log=1,
                message_date=datetime(2008, 1, 2, 0, 0),
                message_date_before=datetime(2008, 1, 1, 0, 0),
                message_date_after=datetime(2008, 1, 3, 0, 0)
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            query_params={
                "Log": 1,
                "MessageDate": "2008-01-02",
                "MessageDate<": "2008-01-01",
                "MessageDate>": "2008-01-03"
            },
            form_params={},
        )
