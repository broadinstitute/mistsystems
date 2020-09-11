class Juniper():
    def __init__(self, session):
        self.session = session

    def get_devices_command(self, org_id):
        uri = "/api/v1/orgs/{0}/ocdevices/outbound_ssh_cmd".format(org_id)
        resp = self.session.mist_get(uri)
        return resp