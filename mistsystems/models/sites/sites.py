import logging


class SiteModel():
    def __init__(self, site_id=None):
        self.site_id = site_id
        self.name = None
        self.timezone = None
        self.country_code = None
        self.latlng = None
        self.address = None
        self.sitegroupo_ids = None
        self.lat = None
        self.lng = None
        self.org_id = None
        self.created_time = None
        self.modified_time = None
        self.rftempalte_id = None
        self.secpolicy_id = None
        self.alarmtemplate_id = None
        self.networktemplate_id = None
        self.tzoffset = None

    def _set_id(self, site_id):
        self.site_id = site_id

    def _set_org_id(self, org_id):
        self.org_id = org_id

    def _set_created_time(self, created_time):
        self.created_time = created_time

    def _set_modified_time(self, modified_time):
        self.modified_time = modified_time

    def set_name(self, name):
        self.name = name

    def set_timezone(self, timezone):
        self.timezone = timezone

    def set_country_code(self, country_code):
        self.country_code = country_code

    def set_latlng(self, latlng):
        self.latlng = latlng

    def set_address(self, address):
        self.address = address

    def set_sitegroupo_ids(self, sitegroupo_ids):
        self.sitegroupo_ids = sitegroupo_ids

    def set_lat(self, lat):
        self.lat = lat

    def set_lng(self, lng):
        self.lng = lng

    def set_rftempalte_id(self, rftempalte_id):
        self.rftempalte_id = rftempalte_id

    def set_secpolicy_id(self, secpolicy_id):
        self.secpolicy_id = secpolicy_id

    def set_alarmtemplate_id(self, alarmtemplate_id):
        self.alarmtemplate_id = alarmtemplate_id

    def set_networktemplate_id(self, networktemplate_id):
        self.networktemplate_id = networktemplate_id

    def set_tzoffset(self, tzoffset):
        self.tzoffset = tzoffset

    def set_site(self, data):
        self._set_id(data["id"])
        self._set_org_id(data["org_id"])
        self._set_created_time(data["created_time"])
        self._set_modified_time(data["modified_time"])
        self.set_name(data["name"])
        self.set_timezone(data["timezone"])
        self.set_country_code(data["country_code"])
        self.set_latlng(data["latlng"])
        self.set_address(data["address"])
        self.set_sitegroupo_ids(data["sitegroupo_ids"])
        self.set_lat(data["lat"])
        self.set_lng(data["lng"])
        self.set_rftempalte_id(data["rftempalte_id"])
        self.set_secpolicy_id(data["secpolicy_id"])
        self.set_alarmtemplate_id(data["alarmtemplate_id"])
        self.set_networktemplate_id(data["networktemplate_id"])
        self.set_tzoffset(data["tzoffset"])
        

    def get_id(self):
        return self.site_id

    def get_org_id(self):
        return self.org_id 

    def get_created_time(self):
        return self.created_time

    def get_modified_time(self):
        return self.modified_time

    def get_name(self):
        return self.name 

    def get_timezone(self):
        return self.timezone 

    def get_country_code(self):
        return self.country_code

    def get_latlng(self):
        return self.latlng

    def get_address(self):
        return self.address 

    def get_sitegroupo_ids(self):
        return self.sitegroupo_ids 

    def get_lat(self):
        return self.lat

    def get_lng(self):
        return self.lng 

    def get_rftempalte_id(self):
        return self.rftempalte_id

    def get_secpolicy_id(self):
        return self.secpolicy_id 

    def get_alarmtemplate_id(self):
        return self.alarmtemplate_id

    def get_networktemplate_id(self):
        return self.networktemplate_id

    def get_tzoffset(self):
        return self.tzoffset 
