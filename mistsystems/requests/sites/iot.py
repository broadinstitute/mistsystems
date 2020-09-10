class Iot():

    def __init__(self, session):
        self.session = session

    def get(self, site_id, device_id):
        uri = "/api/v1/sites/%s/devices/%s/iot" % (site_id, device_id)
        resp = self.session.mist_get(uri)
        return resp

    def update(self, site_id, device_id):
        uri = "/api/v1/sites/%s/devices/%s/iot" % (site_id, device_id)
        resp = self.session.mist_put(uri)
        return resp
