class Stats():

    def __init__(self, session):
        self.session = session

    def get(self, org_id):
        uri = "/api/v1/orgs/%s/stats" % org_id
        resp = self.session.mist_get(uri)
        return resp
