class Info():

    def __init__(self, session):
        self.session = session

    def get(self, site_id):
        uri = "/api/v1/sites/%s" % site_id
        resp = self.session.mist_get(uri)
        return resp
