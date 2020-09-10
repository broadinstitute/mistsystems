class Psks():

    def __init__(self, session):
        self.session = session

    def create(self, org_id, psk):
        uri = "/api/v1/orgs/%s/psks" % org_id
        resp = self.session.mist_post(uri, body=psk)
        return resp

    def get(self, org_id, psk_id="", name="", ssid="", page=1, limit=100):
        uri = "/api/v1/orgs/%s/psks" % org_id
        query = {}
        if psk_id != "":
            uri += "/%s" % psk_id
        if name != "":
            query["name"] = name
        if ssid != "":
            query["ssid"] = ssid
        resp = self.session.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def delete(self, org_id, psk_id="", name="", ssid=""):
        uri = "/api/v1/orgs/%s/psks" % org_id
        if psk_id != "":
            uri += "/%s" % psk_id
        if org_id != "" and ssid != "":
            uri += "?name=%s&ssid=%s" % (name, ssid)
        elif name != "":
            uri += "?name=%s" % name
        elif ssid != "":
            uri += "?ssid=%s" % ssid
        resp = self.session.mist_delete(uri)
        return resp
