class Zones():

    def __init__(self, session):
        self.session = session

    def create(self, site_id, zone_settings):
        uri = "/api/v1/sites/%s/zones" % site_id
        body = zone_settings
        resp = self.session.mist_post(uri, body=body)
        return resp

    def update(self, site_id, zone_id, body={}):
        uri = "/api/v1/sites/%s/zones/%s" % (site_id, zone_id)
        resp = self.session.mist_put(uri, body=body)
        return resp

    def delete(self, site_id, zone_id):
        uri = "/api/v1/sites/%s/zones/%s" % (site_id, zone_id)
        resp = self.session.mist_delete(uri)
        return resp

    def get(self, site_id, page=1, limit=100):
        uri = "/api/v1/sites/%s/zones" % site_id
        resp = self.session.mist_get(uri, page=page, limit=limit)
        return resp
