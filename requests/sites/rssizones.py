class RssiZones():

    def __init__(self, session):
        self.session = session

    def create(self, site_id, rssizone_settings):
        uri = "/api/v1/sites/%s/rssizones" % site_id
        body = rssizone_settings
        resp = self.session.mist_post(uri, body=body)
        return resp

    def update(self, site_id, rssizone_id, body={}):
        uri = "/api/v1/sites/%s/rssizones/%s" % (site_id, rssizone_id)
        resp = self.session.mist_put(uri, body=body)
        return resp

    def delete(self, site_id, rssizone_id):
        uri = "/api/v1/rsites/%s/ssizones/%s" % (site_id, rssizone_id)
        resp = self.session.mist_delete(uri)
        return resp

    def get(self, site_id, page=1, limit=100):
        uri = "/api/v1/sites/%s/rssizones" % site_id
        resp = self.session.mist_get(uri, page=page, limit=limit)
        return resp
