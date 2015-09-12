# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio.rest.resources.util import (
    parse_date,
    parse_iso_date,
)
from twilio.rest.resources.base import InstanceResource
from twilio.rest.resources.base import ListResource


class Transcription(InstanceResource):
    """
    .. attribute:: account_sid
    
        The unique id of the Account responsible for this transcription.
    
    .. attribute:: api_version
    
        The api_version
    
    .. attribute:: date_created
    
        The date that this resource was created, given in RFC 2822 format.
    
    .. attribute:: date_updated
    
        The date that this resource was last updated, given in RFC 2822 format.
    
    .. attribute:: duration
    
        The duration of the transcribed audio, in seconds.
    
    .. attribute:: owner_account_sid
    
        The owner_account_sid
    
    .. attribute:: price
    
        The charge for this transcript in the currency associated with the
        account. Populated after the transcript is completed. Note, this value
        may not be immediately available.
    
    .. attribute:: price_unit
    
        The currency in which `Price` is measured, in ISO 4127 format (e.g.
        `usd`, `eur`, `jpy`).
    
    .. attribute:: recording_sid
    
        The unique id of the Recording this Transcription was made of.
    
    .. attribute:: sid
    
        A 34 character string that uniquely identifies this resource.
    
    .. attribute:: status
    
        A string representing the status of the transcription: `in-progress`,
        `completed` or `failed`.
    
    .. attribute:: transcription_text
    
        The text content of the transcription.
    
    .. attribute:: type
    
        The type
    
    .. attribute:: uri
    
        he URI for this resource, relative to `https://api.twilio.com`
    """
    id_key = "sid"
    COMPLETED = "completed"
    FAILED = "failed"
    IN_PROGRESS = "in-progress"

    def load(self, *args, **kwargs):
        super(Transcription, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)

    def delete(self):
        """
        Delete a transcription from the account used to make the request
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance()


class Transcriptions(ListResource):
    name = "Transcriptions"
    mount_name = "transcriptions"
    key = "transcriptions"
    instance = Transcription

    def __init__(self, *args, **kwargs):
        super(Transcriptions, self).__init__(*args, **kwargs)

    def get(self, sid):
        """
        Fetch and instance of a Transcription
        
        :param str sid: The transcription Sid that uniquely identifies this resource
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`Transcription`
        :returns: A placeholder for a :class:`Transcription` resource
        """
        return self.get_instance(sid)

    def delete(self, sid):
        """
        Delete a transcription from the account used to make the request
        
        :param str sid: The transcription Sid that uniquely identifies this resource
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance(sid)

    def list(self, **kwargs):
        """
        Retrieve a list of transcriptions belonging to the account used to make the request
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`Transcription`
        """
        return self.get_instances(kwargs)

    def iter(self, **kwargs):
        """
        Retrieve a list of transcriptions belonging to the account used to make the request
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`Transcription`
        """
        return super(Transcriptions, self).iter(**kwargs)
