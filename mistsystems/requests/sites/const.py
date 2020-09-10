class Const():

    def __init__(self, session):
        self.session = session

    def get_applications(self):
        uri = "/api/v1/const/applications"
        resp = self.session.mist_get(uri)
        return resp

    def get_ap_led_status(self):
        uri = "/api/v1/const/ap_led_status"
        resp = self.session.mist_get(uri)
        return resp

    def get_ap_models(self):
        uri = "/api/v1/const/device_models"
        resp = self.session.mist_get(uri)
        return resp
