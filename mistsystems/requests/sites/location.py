class Location():
    def __init__(self, session):
        self.session = session

    def get_sdk_stats(self, site_id, map_id):
        uri = "/api/v1/sites/{0}/stats/maps/{1}/sdkclients".format(
            site_id, map_id)
        resp = self.session.mist_get(uri)
        return resp

    def get_sdk_stats_details(self, site_id, map_id, sdkclient_uuid):
        uri = "/api/v1/sites/{0}/stats/maps/{1}/sdkclients/{2}".format(
            site_id, map_id, sdkclient_uuid)
        resp = self.session.mist_get(uri)
        return resp
