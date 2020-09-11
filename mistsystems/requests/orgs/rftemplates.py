class RfTemplates():

    def __init__(self, session):
        self.session = session

    def get(self, org_id):
        uri = "/api/v1/orgs/%s/rftemplates" % org_id
        resp = self.session.mist_get(uri)
        return resp

    def create(self, org_id, settings):
        uri = "/api/v1/orgs/%s/rftemplates" % org_id
        body = settings
        resp = self.session.mist_post(uri, body=body)
        return resp

    def get_by_id(self, org_id, rftemplate_id):
        uri = "/api/v1/orgs/%s/rftemplates/%s" % (org_id, rftemplate_id)
        resp = self.session.mist_get(uri)
        return resp

    def update(self, org_id, rftemplate_id, settings):
        uri = "/api/v1/orgs/%s/rftemplates/%s" % (org_id, rftemplate_id)
        body = settings
        resp = self.session.mist_put(uri, body=body)
        return resp

    def delete(self, org_id, rftemplate_id):
        uri = "/api/v1/orgs/%s/rftemplates/%s" % (org_id, rftemplate_id)
        resp = self.session.mist_delete(uri)
        return resp
