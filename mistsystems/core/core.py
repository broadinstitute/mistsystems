from mistsystems.core import sites


class Sites():

    def __init__(self, api_session):
        self.api_session = api_session
        self.sites = sites.sites.Sites(self.api_session)

class Orgs():
    def __init__(self, api_session):
        self.api_session = api_session