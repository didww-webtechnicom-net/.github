# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio.rest.resources.util import UNSET_TIMEOUT
from twilio.rest.v2010.account.usage.record import (
    Record,
    Records,
)
from twilio.rest.v2010.account.usage.trigger import (
    Trigger,
    Triggers,
)


class Usage(object):
    """ Holds all specific Usage list resources """
    key = "usage"

    def __init__(self, client, base_uri, auth, timeout=UNSET_TIMEOUT):
        self.timeout = timeout
        self.client = client
        self.records = Records(client, base_uri, auth, timeout)
        self.triggers = Triggers(client, base_uri, auth, timeout)
