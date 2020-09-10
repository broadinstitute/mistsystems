class VBeacons():

    def __init__(self, session):
        self.session = session

    def create(self, site_id, vbeacon_settings):
        uri = "/api/v1/sites/%s/vbeacons" % site_id
        body = vbeacon_settings
        resp = self.session.mist_post(uri, body=body)
        return resp

    def update(self, site_id, vbeacon_id, body={}):
        uri = "/api/v1/sites/%s/vbeacons/%s" % (site_id, vbeacon_id)
        resp = self.session.mist_put(uri, body=body)
        return resp

    def delete(self, site_id, vbeacon_id):
        uri = "/api/v1/sites/%s/vbeacons/%s" % (site_id, vbeacon_id)
        resp = self.session.mist_delete(uri)
        return resp

    def get(self, site_id, page=1, limit=100):
        uri = "/api/v1/sites/%s/vbeacons" % site_id
        resp = self.session.mist_get(uri, page=page, limit=limit)
        return resp
