class SiteGroups():

    def __init__(self, session):
        self.session = session

    def get(mist_session, org_id, page=1, limit=100):
        uri = "/api/v1/orgs/%s/sitegroups" % org_id
        resp = mist_session.mist_get(uri, page=page, limit=limit)
        return resp

    def get_by_id(mist_session, org_id, sitegroup_id):
        uri = "/api/v1/orgs/%s/sitegroups/%s" % (org_id, sitegroup_id)
        resp = mist_session.mist_get(uri)
        return resp

    def create(mist_session, org_id, group_name):
        uri = "/api/v1/orgs/%s/sitegroups" % org_id
        body = group_name
        resp = mist_session.mist_post(uri, body=body)
        return resp

    def update(mist_session, org_id, sitegroup_id, body):
        uri = "/api/v1/orgs/%s/sitegroups/%s" % (org_id, sitegroup_id)
        resp = mist_session.mist_put(uri, body=body)
        return resp

    def delete(mist_session, org_id, sitegroup_id):
        uri = "/api/v1/orgs/%s/sitegroups/%s" % (org_id, sitegroup_id)
        resp = mist_session.mist_delete(uri)
        return resp
