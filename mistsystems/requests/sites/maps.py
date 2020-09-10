class Maps():

    def __init__(self, session):
        self.session = session

    def get(self, site_id, page=1, limit=100):
        uri = "/api/v1/sites/%s/maps" % site_id
        resp = self.session.mist_get(uri, page=page, limit=limit)
        return resp

    def delete(self, site_id, map_id):
        uri = "/api/v1/sites/%s/maps/%s" % (site_id, map_id)
        resp = self.session.mist_delete(uri)
        return resp

    def create(self, site_id, map_settings):
        uri = "/api/v1/sites/%s/maps" % site_id
        body = map_settings
        resp = self.session.mist_post(uri, body=body)
        return resp

    def add_image(self, site_id, map_id, image_path):
        uri = "/api/v1/sites/%s/maps/%s/image" % (site_id, map_id)
        files = {'file': open(image_path, 'rb').read()}
        resp = self.session.mist_post_file(uri, files=files)
        return resp

    def delete_image(self, site_id, map_id):
        uri = "/api/v1/sites/%s/maps/%s/image" % (site_id, map_id)
        resp = self.session.mist_delete(uri)
        return resp
