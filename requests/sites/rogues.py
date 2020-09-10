class Rogues():

    def __init__(self, session):
        self.session = session

    def set_rogue(self, site_id, rogue_param):
        uri = "/api/v1/sites/%s/setting" % site_id
        resp = self.session.mist_post(uri, body=rogue_param)
        return resp

    def get(self, site_id, duration="1d", r_type="others", page=1, limit=100):
        uri = "/api/v1/sites/%s/insights/rogues" % site_id
        query = {"duration": duration, "type": r_type}
        resp = self.session.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def report(self, site_id, r_type, fields):
        rogues = get(self, site_id)
        result = []
        for rogue in rogues['result']["results"]:
            temp = []
            for field in fields:
                if field not in rogue:
                    temp.append("")
                else:
                    temp.append("%s" % rogue[field])
            result.append(temp)
        return result
