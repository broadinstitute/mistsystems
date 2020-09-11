class Maps():

    def __init__(self, session):
        self.session = session

    #TODO
    def import_org_maps(self, org_id, site_name, json, file, csv):
        uri = "/api/v1/orgs/{0}/sites/{1}/maps/import".format(org_id, site_name)
        resp = self.session.mist_post(uri, files=file, body=json)
        return resp