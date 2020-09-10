class RfTemplates():

    def __init__(self, session):
        self.session = session

    def get(mist_session, org_id):
        uri = "/api/v1/orgs/%s/rftemplates" % org_id
        resp = mist_session.mist_get(uri)
        return resp

    def create(mist_session, org_id, settings):
        uri = "/api/v1/orgs/%s/rftemplates" % org_id
        body = settings
        resp = mist_session.mist_post(uri, body=body)
        return resp

    def get_by_id(mist_session, org_id, rftemplate_id):
        uri = "/api/v1/orgs/%s/rftemplates/%s" % (org_id, rftemplate_id)
        resp = mist_session.mist_get(uri)
        return resp

    def update(mist_session, org_id, rftemplate_id, settings):
        uri = "/api/v1/orgs/%s/rftemplates/%s" % (org_id, rftemplate_id)
        body = settings
        resp = mist_session.mist_put(uri, body=body)
        return resp

    def delete(mist_session, org_id, rftemplate_id):
        uri = "/api/v1/orgs/%s/rftemplates/%s" % (org_id, rftemplate_id)
        resp = mist_session.mist_delete(uri)
        return resp
