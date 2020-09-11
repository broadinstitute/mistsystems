class Const():

    def __init__(self, session):
        self.session = session

    def getApplications(self):
        uri = "/api/v1/const/applications"
        resp = self.session.mist_get(uri)
        return resp

    def getApLedStatus(self):
        uri = "/api/v1/const/ap_led_status"
        resp = self.session.mist_get(uri)
        return resp

    def getApModels(self):
        uri = "/api/v1/const/device_models"
        resp = self.session.mist_get(uri)
        return resp

    def getClientEvents(self):
        uri = "/api/v1/const/client_events"
        resp = self.session.mist_get(uri)
        return resp

    def getCountryCodes(self):
        uri = "/api/v1/const/countries"
        resp = self.session.mist_get(uri)
        return resp
    def getSystemEvents(self):
        uri = "/api/v1/const/system_events"
        resp = self.session.mist_get(uri)
        return resp
