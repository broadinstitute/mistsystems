from mistsystems.models.sites.sites import SiteModel


class Sites():
    def __init__(self, session):
        self.session = session


    def get_by_id(self, site_id):
        site_json = self.session.sites.site.get(site_id=site_id)
        site = SiteModel()
        site.set_site(site_json)
        return site

    def save(self, site):
        print(type(site))