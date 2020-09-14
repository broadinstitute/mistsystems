from mistsystems.models.sites.sites import SiteModel
import logging
import json


class Sites(SiteModel):
    def __init__(self, session):
        self._session = session

    def get_by_id(self, site_id):
        site_json = self._session.sites.site.get(site_id=site_id)["result"]
        self.from_json(site_json)
        return self

    def save(self):
        obj = self.to_json()
        obj_id = self.id

        if obj_id: 
            print("updating {0} at {1}".format(obj, obj_id))     
        else: 
            print("creating {0}".format(obj))

