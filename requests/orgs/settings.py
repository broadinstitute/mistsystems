class Settings():

    def __init__(self, session):
        self.session = session

    def get(mist_session, org_id):
        uri = "/api/v1/orgs/%s/setting" % org_id
        resp = mist_session.mist_get(uri)
        return resp

    def update(mist_session, org_id, settings):
        uri = "/api/v1/orgs/%s/setting" % org_id
        body = settings
        resp = mist_session.mist_put(uri, body=body)
        return resp
