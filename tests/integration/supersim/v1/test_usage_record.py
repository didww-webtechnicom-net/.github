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


class UsageRecordTestCase(IntegrationTestCase):

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.supersim.v1.usage_records.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://supersim.twilio.com/v1/UsageRecords',
        ))

    def test_read_all_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "usage_records": [
                    {
                        "period": {
                            "start_time": "2015-05-01T20:00:00Z",
                            "end_time": "2015-06-01T20:00:00Z"
                        },
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "data_upload": 150000,
                        "data_download": 150000,
                        "data_total": 300000,
                        "data_total_billed": "0.03",
                        "billed_unit": "USD",
                        "sim_sid": null,
                        "fleet_sid": null,
                        "network_sid": null,
                        "iso_country": null
                    }
                ],
                "meta": {
                    "first_page_url": "https://supersim.twilio.com/v1/UsageRecords?PageSize=50&Page=0",
                    "key": "usage_records",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://supersim.twilio.com/v1/UsageRecords?PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.supersim.v1.usage_records.list()

        self.assertIsNotNone(actual)

    def test_read_all_day_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "usage_records": [
                    {
                        "period": {
                            "start_time": "2019-05-03T00:00:00Z",
                            "end_time": "2019-05-04T00:00:00Z"
                        },
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "data_upload": 150000,
                        "data_download": 150000,
                        "data_total": 300000,
                        "data_total_billed": "0.03",
                        "billed_unit": "USD",
                        "sim_sid": null,
                        "fleet_sid": null,
                        "network_sid": null,
                        "iso_country": null
                    },
                    {
                        "period": {
                            "start_time": "2019-05-02T00:00:00Z",
                            "end_time": "2019-05-03T00:00:00Z"
                        },
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "data_upload": 150000,
                        "data_download": 150000,
                        "data_total": 300000,
                        "data_total_billed": "0.03",
                        "billed_unit": "USD",
                        "sim_sid": null,
                        "fleet_sid": null,
                        "network_sid": null,
                        "iso_country": null
                    }
                ],
                "meta": {
                    "first_page_url": "https://supersim.twilio.com/v1/UsageRecords?Granularity=day&PageSize=50&Page=0",
                    "key": "usage_records",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://supersim.twilio.com/v1/UsageRecords?Granularity=day&PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.supersim.v1.usage_records.list()

        self.assertIsNotNone(actual)

    def test_read_all_hour_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "usage_records": [
                    {
                        "period": {
                            "start_time": "2019-05-01T01:00:00Z",
                            "end_time": "2019-05-01T02:00:00Z"
                        },
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "data_upload": 150000,
                        "data_download": 150000,
                        "data_total": 300000,
                        "data_total_billed": "0.03",
                        "billed_unit": "USD",
                        "sim_sid": null,
                        "fleet_sid": null,
                        "network_sid": null,
                        "iso_country": null
                    },
                    {
                        "period": {
                            "start_time": "2019-05-01T00:00:00Z",
                            "end_time": "2019-05-01T01:00:00Z"
                        },
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "data_upload": 150000,
                        "data_download": 150000,
                        "data_total": 300000,
                        "data_total_billed": "0.03",
                        "billed_unit": "USD",
                        "sim_sid": null,
                        "fleet_sid": null,
                        "network_sid": null,
                        "iso_country": null
                    }
                ],
                "meta": {
                    "first_page_url": "https://supersim.twilio.com/v1/UsageRecords?Granularity=hour&PageSize=50&Page=0",
                    "key": "usage_records",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://supersim.twilio.com/v1/UsageRecords?Granularity=hour&PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.supersim.v1.usage_records.list()

        self.assertIsNotNone(actual)

    def test_read_day_sim_filter_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "usage_records": [
                    {
                        "period": {
                            "start_time": "2019-05-03T00:00:00Z",
                            "end_time": "2019-05-04T00:00:00Z"
                        },
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "sim_sid": "HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "data_upload": 150000,
                        "data_download": 150000,
                        "data_total": 300000,
                        "data_total_billed": "0.03",
                        "billed_unit": "USD",
                        "fleet_sid": null,
                        "network_sid": null,
                        "iso_country": null
                    },
                    {
                        "period": {
                            "start_time": "2019-05-02T00:00:00Z",
                            "end_time": "2019-05-03T00:00:00Z"
                        },
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "data_upload": 150000,
                        "data_download": 150000,
                        "data_total": 300000,
                        "data_total_billed": "0.03",
                        "billed_unit": "USD",
                        "sim_sid": "HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "fleet_sid": null,
                        "network_sid": null,
                        "iso_country": null
                    }
                ],
                "meta": {
                    "first_page_url": "https://supersim.twilio.com/v1/UsageRecords?Sim=HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&Granularity=day&PageSize=50&Page=0",
                    "key": "usage_records",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://supersim.twilio.com/v1/UsageRecords?Sim=HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&Granularity=day&PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.supersim.v1.usage_records.list()

        self.assertIsNotNone(actual)

    def test_read_day_network_filter_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "usage_records": [
                    {
                        "period": {
                            "start_time": "2019-05-03T00:00:00Z",
                            "end_time": "2019-05-04T00:00:00Z"
                        },
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "data_upload": 150000,
                        "data_download": 150000,
                        "data_total": 300000,
                        "data_total_billed": "0.03",
                        "billed_unit": "USD",
                        "sim_sid": null,
                        "fleet_sid": null,
                        "network_sid": "HWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "iso_country": null
                    },
                    {
                        "period": {
                            "start_time": "2019-05-02T00:00:00Z",
                            "end_time": "2019-05-03T00:00:00Z"
                        },
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "data_upload": 150000,
                        "data_download": 150000,
                        "data_total": 300000,
                        "data_total_billed": "0.03",
                        "billed_unit": "USD",
                        "sim_sid": null,
                        "fleet_sid": null,
                        "network_sid": "HWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "iso_country": null
                    }
                ],
                "meta": {
                    "first_page_url": "https://supersim.twilio.com/v1/UsageRecords?Network=HWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&Granularity=day&PageSize=50&Page=0",
                    "key": "usage_records",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://supersim.twilio.com/v1/UsageRecords?Network=HWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&Granularity=day&PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.supersim.v1.usage_records.list()

        self.assertIsNotNone(actual)

    def test_read_day_country_filter_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "usage_records": [
                    {
                        "period": {
                            "start_time": "2019-05-03T00:00:00Z",
                            "end_time": "2019-05-04T00:00:00Z"
                        },
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "data_upload": 150000,
                        "data_download": 150000,
                        "data_total": 300000,
                        "data_total_billed": "0.03",
                        "billed_unit": "USD",
                        "sim_sid": null,
                        "fleet_sid": null,
                        "network_sid": null,
                        "iso_country": "FR"
                    },
                    {
                        "period": {
                            "start_time": "2019-05-02T00:00:00Z",
                            "end_time": "2019-05-03T00:00:00Z"
                        },
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "data_upload": 150000,
                        "data_download": 150000,
                        "data_total": 300000,
                        "data_total_billed": "0.03",
                        "billed_unit": "USD",
                        "sim_sid": null,
                        "fleet_sid": null,
                        "network_sid": null,
                        "iso_country": "FR"
                    }
                ],
                "meta": {
                    "first_page_url": "https://supersim.twilio.com/v1/UsageRecords?IsoCountry=FR&Granularity=day&PageSize=50&Page=0",
                    "key": "usage_records",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://supersim.twilio.com/v1/UsageRecords?IsoCountry=FR&Granularity=day&PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.supersim.v1.usage_records.list()

        self.assertIsNotNone(actual)

    def test_read_day_fleet_filter_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "usage_records": [
                    {
                        "period": {
                            "start_time": "2019-05-03T00:00:00Z",
                            "end_time": "2019-05-04T00:00:00Z"
                        },
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "data_upload": 150000,
                        "data_download": 150000,
                        "data_total": 300000,
                        "data_total_billed": "0.03",
                        "billed_unit": "USD",
                        "sim_sid": null,
                        "fleet_sid": "HFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "network_sid": null,
                        "iso_country": null
                    },
                    {
                        "period": {
                            "start_time": "2019-05-02T00:00:00Z",
                            "end_time": "2019-05-03T00:00:00Z"
                        },
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "data_upload": 150000,
                        "data_download": 150000,
                        "data_total": 300000,
                        "data_total_billed": "0.03",
                        "billed_unit": "USD",
                        "sim_sid": null,
                        "fleet_sid": "HFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "network_sid": null,
                        "iso_country": null
                    }
                ],
                "meta": {
                    "first_page_url": "https://supersim.twilio.com/v1/UsageRecords?Fleet=HFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&Granularity=day&PageSize=50&Page=0",
                    "key": "usage_records",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://supersim.twilio.com/v1/UsageRecords?Fleet=HFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&Granularity=day&PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.supersim.v1.usage_records.list()

        self.assertIsNotNone(actual)

    def test_read_day_group_by_sim_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "usage_records": [
                    {
                        "period": {
                            "start_time": "2019-05-03T00:00:00Z",
                            "end_time": "2019-05-04T00:00:00Z"
                        },
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "data_upload": 150000,
                        "data_download": 150000,
                        "data_total": 300000,
                        "data_total_billed": "0.03",
                        "billed_unit": "USD",
                        "sim_sid": "HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "fleet_sid": null,
                        "network_sid": null,
                        "iso_country": null
                    },
                    {
                        "period": {
                            "start_time": "2019-05-03T00:00:00Z",
                            "end_time": "2019-05-04T00:00:00Z"
                        },
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "data_upload": 150000,
                        "data_download": 150000,
                        "data_total": 300000,
                        "data_total_billed": "0.03",
                        "billed_unit": "USD",
                        "sim_sid": "HSbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
                        "fleet_sid": null,
                        "network_sid": null,
                        "iso_country": null
                    }
                ],
                "meta": {
                    "first_page_url": "https://supersim.twilio.com/v1/UsageRecords?Group=sim&PageSize=50&Page=0",
                    "key": "usage_records",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://supersim.twilio.com/v1/UsageRecords?Group=sim&PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.supersim.v1.usage_records.list()

        self.assertIsNotNone(actual)

    def test_read_day_group_by_fleet_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "usage_records": [
                    {
                        "period": {
                            "start_time": "2019-05-03T00:00:00Z",
                            "end_time": "2019-05-04T00:00:00Z"
                        },
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "data_upload": 150000,
                        "data_download": 150000,
                        "data_total": 300000,
                        "data_total_billed": "0.03",
                        "billed_unit": "USD",
                        "sim_sid": null,
                        "fleet_sid": "HFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "network_sid": null,
                        "iso_country": null
                    },
                    {
                        "period": {
                            "start_time": "2019-05-03T00:00:00Z",
                            "end_time": "2019-05-04T00:00:00Z"
                        },
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "data_upload": 150000,
                        "data_download": 150000,
                        "data_total": 300000,
                        "data_total_billed": "0.03",
                        "billed_unit": "USD",
                        "sim_sid": null,
                        "fleet_sid": "HFbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
                        "network_sid": null,
                        "iso_country": null
                    }
                ],
                "meta": {
                    "first_page_url": "https://supersim.twilio.com/v1/UsageRecords?Group=fleet&PageSize=50&Page=0",
                    "key": "usage_records",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://supersim.twilio.com/v1/UsageRecords?Group=fleet&PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.supersim.v1.usage_records.list()

        self.assertIsNotNone(actual)

    def test_read_day_group_by_network_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "usage_records": [
                    {
                        "period": {
                            "start_time": "2019-05-03T00:00:00Z",
                            "end_time": "2019-05-04T00:00:00Z"
                        },
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "data_upload": 150000,
                        "data_download": 150000,
                        "data_total": 300000,
                        "data_total_billed": "0.03",
                        "billed_unit": "USD",
                        "sim_sid": null,
                        "fleet_sid": null,
                        "network_sid": "HWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "iso_country": null
                    },
                    {
                        "period": {
                            "start_time": "2019-05-03T00:00:00Z",
                            "end_time": "2019-05-04T00:00:00Z"
                        },
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "data_upload": 150000,
                        "data_download": 150000,
                        "data_total": 300000,
                        "data_total_billed": "0.03",
                        "billed_unit": "USD",
                        "sim_sid": null,
                        "fleet_sid": null,
                        "network_sid": "HWbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
                        "iso_country": null
                    }
                ],
                "meta": {
                    "first_page_url": "https://supersim.twilio.com/v1/UsageRecords?Group=network&PageSize=50&Page=0",
                    "key": "usage_records",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://supersim.twilio.com/v1/UsageRecords?Group=network&PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.supersim.v1.usage_records.list()

        self.assertIsNotNone(actual)

    def test_read_day_group_by_iso_country_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "usage_records": [
                    {
                        "period": {
                            "start_time": "2019-05-03T00:00:00Z",
                            "end_time": "2019-05-04T00:00:00Z"
                        },
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "data_upload": 150000,
                        "data_download": 150000,
                        "data_total": 300000,
                        "data_total_billed": "0.03",
                        "billed_unit": "USD",
                        "sim_sid": null,
                        "fleet_sid": null,
                        "network_sid": null,
                        "iso_country": "FR"
                    },
                    {
                        "period": {
                            "start_time": "2019-05-03T00:00:00Z",
                            "end_time": "2019-05-04T00:00:00Z"
                        },
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "data_upload": 150000,
                        "data_download": 150000,
                        "data_total": 300000,
                        "data_total_billed": "0.03",
                        "billed_unit": "USD",
                        "sim_sid": null,
                        "fleet_sid": null,
                        "network_sid": null,
                        "iso_country": "US"
                    }
                ],
                "meta": {
                    "first_page_url": "https://supersim.twilio.com/v1/UsageRecords?Group=isoCountry&PageSize=50&Page=0",
                    "key": "usage_records",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://supersim.twilio.com/v1/UsageRecords?Group=isoCountry&PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.supersim.v1.usage_records.list()

        self.assertIsNotNone(actual)

    def test_read_day_group_by_sim_and_filter_by_country_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "usage_records": [
                    {
                        "period": {
                            "start_time": "2019-05-03T00:00:00Z",
                            "end_time": "2019-05-04T00:00:00Z"
                        },
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "data_upload": 150000,
                        "data_download": 150000,
                        "data_total": 300000,
                        "data_total_billed": "0.03",
                        "billed_unit": "USD",
                        "sim_sid": "HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "fleet_sid": null,
                        "network_sid": null,
                        "iso_country": "FR"
                    },
                    {
                        "period": {
                            "start_time": "2019-05-03T00:00:00Z",
                            "end_time": "2019-05-04T00:00:00Z"
                        },
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "data_upload": 150000,
                        "data_download": 150000,
                        "data_total": 300000,
                        "data_total_billed": "0.03",
                        "billed_unit": "USD",
                        "sim_sid": "HSbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
                        "fleet_sid": null,
                        "network_sid": null,
                        "iso_country": "FR"
                    }
                ],
                "meta": {
                    "first_page_url": "https://supersim.twilio.com/v1/UsageRecords?IsoCountry=FR&Group=sim&PageSize=50&Page=0",
                    "key": "usage_records",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://supersim.twilio.com/v1/UsageRecords?IsoCountry=FR&Group=sim&PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.supersim.v1.usage_records.list()

        self.assertIsNotNone(actual)

    def test_read_all_no_billing_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "usage_records": [
                    {
                        "period": {
                            "start_time": "2015-05-01T20:00:00Z",
                            "end_time": "2015-06-01T20:00:00Z"
                        },
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "data_upload": 1000,
                        "data_download": 1000,
                        "data_total": 2000,
                        "data_total_billed": "0",
                        "billed_unit": null,
                        "sim_sid": null,
                        "fleet_sid": null,
                        "network_sid": null,
                        "iso_country": null
                    }
                ],
                "meta": {
                    "first_page_url": "https://supersim.twilio.com/v1/UsageRecords?PageSize=50&Page=0",
                    "key": "usage_records",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://supersim.twilio.com/v1/UsageRecords?PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.supersim.v1.usage_records.list()

        self.assertIsNotNone(actual)
