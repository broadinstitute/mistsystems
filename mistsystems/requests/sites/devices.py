class Devices():

    def __init__(self, session):
        self.session = session

    def get(self, site_id, name=None, device_type=None, page=1, limit=100):
        uri = "/api/v1/sites/%s/devices" % site_id
        query = {}
        if name:
            query[name] = name
        if device_type:
            query["type"] = device_type
        resp = self.session.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def get_details(self, site_id, device_id):
        uri = "/api/v1/sites/%s/devices/%s" % (site_id, device_id)
        resp = self.session.mist_get(uri)
        return resp

    def get_stats_devices(self, site_id, device_id=None, device_type=None, page=1, limit=100):
        uri = "/api/v1/sites/%s/stats/devices" % site_id
        query = {}
        if device_id:
            uri += "/%s" % device_id
        if device_type:
            query["type"] = device_type
        resp = self.session.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def create(self, site_id, devices):
        uri = "/api/v1/sites/%s/devices" % site_id
        resp = self.session.mist_post(uri, body=devices)
        return resp

    def update(self, site_id, device_id, device_settings):
        uri = "/api/v1/sites/%s/devices/%s" % (site_id, device_id)
        resp = self.session.mist_put(uri, body=device_settings)
        return resp

    def delete(self, site_id, device_id):
        uri = "/api/v1/sites/%s/devices/%s" % (site_id, device_id)
        resp = self.session.mist_delete(uri)
        return resp

    def add_image(self, site_id, device_id, image_num, image_path):
        uri = "/api/v1/sites/%s/devices/%s/image%s" % (
            site_id, device_id, image_num)
        files = {'file': open(image_path, 'rb').read()}
        resp = self.session.mist_post_file(uri, files=files)
        return resp

    def set_device_conf(self, site_id, device_id, conf):
        uri = "/api/v1/sites/%s/devices/%s" % (site_id, device_id)
        body = conf
        resp = self.session.mist_put(uri, body=body)
        return resp
