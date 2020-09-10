class Stats():

    def __init__(self, session):
        self.session = session

    def clients(self, site_id):
        uri = "/api/v1/sites/%s/stats/clients" % (site_id)
        resp = self.session.mist_get(uri)
        return resp
