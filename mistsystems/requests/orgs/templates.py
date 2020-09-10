class Templates():

    def __init__(self, session):
        self.session = session

    def get(self, org_id, page=1, limit=100):
        uri = "/api/v1/orgs/%s/templates" % org_id
        resp = self.session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_details(self, org_id, template_id):
        uri = "/api/v1/orgs/%s/templates/%s" % (org_id, template_id)
        resp = self.session.mist_get(uri)
        return resp

    def create(self, org_id, template_settings):
        uri = "/api/v1/orgs/%s/templates" % org_id
        resp = self.session.mist_post(uri, body=template_settings)
        return resp

    def delete(self, org_id, template_id):
        uri = "/api/v1/orgs/%s/templates/%s" % (org_id, template_id)
        resp = self.session.mist_delete(uri)
        return resp
