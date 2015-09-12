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
from twilio.rest.v2010.account.sip.credential_list.credential import (
    Credential,
    Credentials,
)
from twilio.rest.resources.base import ListResource


class CredentialList(InstanceResource):
    """
    .. attribute:: account_sid
    
        The unique id of the Account that responsible for this resource.
    
    .. attribute:: date_created
    
        The date that this resource was created, given as GMT in RFC 2822
        format.
    
    .. attribute:: date_updated
    
        The date that this resource was last updated, given as GMT in RFC 2822
        format.
    
    .. attribute:: friendly_name
    
        The friendly_name
    
    .. attribute:: sid
    
        A 34 character string that uniquely identifies this resource.
    
    .. attribute:: subresource_uris
    
        The subresource_uris
    
    .. attribute:: uri
    
        The URI for this resource, relative to `https://api.twilio.com`
    """
    id_key = "sid"
    subresources = [
        Credentials
    ]

    def load(self, *args, **kwargs):
        super(CredentialList, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)

    def update(self, **kwargs):
        """
        Change the password of a Credential record
        
        :param str friendly_name: The friendly_name
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns a new instance of the updated :class:`CredentialList`
        """
        return self.update_instance(kwargs)

    def delete(self):
        """
        Remove a credential from a CredentialList
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance()


class CredentialLists(ListResource):
    name = "SIP/CredentialLists"
    mount_name = "credential_lists"
    key = "credential_lists"
    instance = CredentialList

    def __init__(self, *args, **kwargs):
        super(CredentialLists, self).__init__(*args, **kwargs)

    def list(self, **kwargs):
        """
        Retrieve a list of Credentials belonging to the account used to make the request
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`CredentialList`
        """
        return self.get_instances(kwargs)

    def create(self, friendly_name, **kwargs):
        """
        Add a Credential to the list
        
        :param str friendly_name: The friendly_name
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`CreateQuery`
        :returns: A CreateQuery when executed returns an instance of the created :class:`CredentialList`
        """
        kwargs["FriendlyName"] = friendly_name
        return self.create_instance(kwargs)

    def get(self, sid):
        """
        Retrieve a specific Credential in a list
        
        :param str sid: The credential Sid that uniquely identifies this resource
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`CredentialList`
        :returns: A placeholder for a :class:`CredentialList` resource
        """
        return self.get_instance(sid)

    def update(self, sid, friendly_name, **kwargs):
        """
        Change the password of a Credential record
        
        :param str friendly_name: The friendly_name
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns an instance of the updated :class:`CredentialList`
        """
        kwargs["FriendlyName"] = friendly_name
        return self.update_instance(sid, kwargs)

    def delete(self, sid):
        """
        Remove a credential from a CredentialList
        
        :param str sid: The credential Sid that uniquely identifies this resource
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance(sid)

    def iter(self, **kwargs):
        """
        Retrieve a list of Credentials belonging to the account used to make the request
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`CredentialList`
        """
        return super(CredentialLists, self).iter(**kwargs)
