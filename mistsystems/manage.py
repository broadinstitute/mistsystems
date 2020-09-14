'''
Written by: Thomas Munzer (tmunzer@juniper.net)
Github repository: https://github.com/tmunzer/mistsystems/
'''
import logging
import json

from mistsystems.manage.core import Orgs, Sites
from mistsystems import api
from mistsystems.models.privileges import Privileges

class MistSystems():
    def __init__(self, host=None, email="", password="", apitoken=None, session_file=None, settings_file=None, auto_login=True):   
        self.api = api.MistSystems(host=host, email=email, password=password, apitoken=apitoken, session_file=session_file, settings_file=settings_file, auto_login=auto_login)
        self.sites = Sites(self.api)