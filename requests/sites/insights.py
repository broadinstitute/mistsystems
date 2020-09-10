class Insights():

    def __init__(self, session):
        self.session = session

    def stats(self, site_id, start, end, metrics, page=1, limit=100):
        uri = "/api/v1/sites/%s/insights/stats" % site_id
        query = {"start": start, "end": end, "metrics": metrics}
        resp = self.session.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def client(self, site_id, client_mac, start, end, interval, metrics, page=1, limit=100):
        uri = "/api/v1/sites/%s/insights/client/%s/stats" % (
            site_id, client_mac)
        query = {"start": start, "end": end,
                 "interval": interval, "metrics": metrics}
        resp = self.session.mist_get(uri, query=query, page=page, limit=limit)
        return resp
