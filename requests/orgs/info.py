class Info():

    def __init__(self, session):
        self.session = session

    def get(self, org_id):
        uri = "/api/v1/orgs/%s" % org_id
        resp = self.session.mist_get(uri)
        return resp

    def create(self, org_id, org_settings):
        uri = "/api/v1/orgs/%s" % org_id
        body = org_settings
        resp = self.session.mist_post(uri, body=body)
        return resp

    def update(self, org_id, org_settings):
        uri = "/api/v1/orgs/%s" % org_id
        body = org_settings
        resp = self.session.mist_put(uri, body=body)
        return resp
