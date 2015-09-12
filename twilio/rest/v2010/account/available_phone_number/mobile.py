# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio.rest.resources.base import InstanceResource
from twilio.rest.resources.base import ListResource


class Mobile(InstanceResource):
    """
    .. attribute:: friendly_name
    
        The friendly_name
    
    .. attribute:: phone_number
    
        The phone_number
    
    .. attribute:: lata
    
        The lata
    
    .. attribute:: rate_center
    
        The rate_center
    
    .. attribute:: latitude
    
        The latitude
    
    .. attribute:: longitude
    
        The longitude
    
    .. attribute:: region
    
        The region
    
    .. attribute:: postal_code
    
        The postal_code
    
    .. attribute:: iso_country
    
        The iso_country
    
    .. attribute:: address_requirements
    
        The address_requirements
    
    .. attribute:: beta
    
        The beta
    
    .. attribute:: capabilities
    
        The capabilities
    """
    id_key = "sid"

    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        super(Mobile, self).__init__(parent, None)


class Mobiles(ListResource):
    name = "Mobile"
    mount_name = "mobile"
    key = "available_phone_numbers"
    instance = Mobile

    def __init__(self, *args, **kwargs):
        super(Mobiles, self).__init__(*args, **kwargs)

    def list(self, **kwargs):
        """
        Retrieve a collection of :class:`Mobile`
        
        :param bool beta: The beta
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`Mobile`
        """
        return self.get_instances(kwargs)

    def iter(self, **kwargs):
        """
        Return all instances of :class:`Mobile` using an iterator
        
        :param bool beta: The beta
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`Mobile`
        """
        return super(Mobiles, self).iter(**kwargs)

    def load_instance(self, data):
        """ Override because Mobile does not have a sid """
        instance = self.instance(self)
        instance.load(data)
        instance.load_subresources()
        return instance
