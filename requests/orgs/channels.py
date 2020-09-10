class Channels():

    def __init__(self, session):
        self.session = session

    def country_codes_get(self):
        uri = "/api/v1/const/countries"
        resp = self.session.mist_get(uri)
        return resp

    def ap_channels_get(self, country_code):
        uri = "/api/v1/const/ap_channels"
        query = {"country_code":country_code}
        resp = self.session.mist_get(uri=uri, query=query)
        return resp


