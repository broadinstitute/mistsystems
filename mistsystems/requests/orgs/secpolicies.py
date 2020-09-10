class SecPolicies():

    def __init__(self, session):
        self.session = session

    def create(mist_session, org_id, secpolicy_settings):
        uri = "/api/v1/orgs/%s/secpolicies" % org_id
        body = secpolicy_settings
        resp = mist_session.mist_post(uri, body=body)
        return resp

    def update(mist_session, org_id, secpolicy_settings, body={}):
        uri = "/api/v1/orgs/%s/secpolicies/%s" % (org_id, secpolicy_settings)
        resp = mist_session.mist_put(uri, body=body)
        return resp

    def delete(mist_session, org_id, secpolicy_settings):
        uri = "/api/v1/orgs/%s/secpolicies/%s" % (org_id, secpolicy_settings)
        resp = mist_session.mist_delete(uri)
        return resp

    def get(mist_session, org_id, page=1, limit=100):
        uri = "/api/v1/orgs/%s/secpolicies" % org_id
        resp = mist_session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_by_id(mist_session, org_id, secpolicy_id):
        uri = "/api/v1/orgs/%s/secpolicies/%s" % (org_id, secpolicy_id)
        resp = mist_session.mist_get(uri)
        return resp
