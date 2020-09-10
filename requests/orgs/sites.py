class Sites():

    def __init__(self, session):
        self.session = session

    def create(self, org_id, site_settings):
        uri = "/api/v1/orgs/%s/sites" % org_id
        body = site_settings
        resp = self.session.mist_post(uri, body=body)
        return resp

    def update(self, org_id, site_id, body={}):
        uri = "/api/v1/sites/%s" % site_id
        resp = self.session.mist_put(uri, body=body)
        return resp

    def delete(self, org_id, site_id):
        uri = "/api/v1/sites/%s" % site_id
        resp = self.session.mist_delete(uri)
        return resp

    def get(self, org_id, page=1, limit=100):
        uri = "/api/v1/orgs/%s/sites" % org_id
        resp = self.session.mist_get(uri, page=page, limit=limit)
        return resp

    def stats(self, site_id, page=1, limit=100):
        uri = "/api/v1/sites/%s/stats" % site_id
        resp = self.session.mist_get(uri, page=page, limit=limit)
        return resp
