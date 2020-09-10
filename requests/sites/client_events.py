class ClientEvents():

    def __init__(self, session):
        self.session = session

    def get_definition(self):
        uri = "/api/v1/const/client_events"
        resp = self.session.mist_get(uri)
        return resp
