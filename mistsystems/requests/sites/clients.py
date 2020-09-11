class Wireless():
    def __init__(self, session): 
        self.session = session

    def disconnectClient(self, site_id, client_mac):
        """
        Disconnect a wireless client
        Parameters:
            site_id: String
            client_mac: String
        """
        uri = "/api/v1/sites/{0}/clients/{1}/disconnect".format(site_id, client_mac)
        resp = self.session.mist_post(uri)
        return resp

    def disconnectMultipleClients(self, site_id, client_macs):
        """
        Disconnect multiple wireless clients
        Parameters:
            site_id: String
            client_macs: Array
        """
        uri = "/api/v1/sites/{0}/clients/disconnect".format(site_id)        
        resp = self.session.mist_post(uri, body=client_macs)
        return resp

    def unauthorizeClient(self, site_id, client_mac):
        """
        Unauthorize a wireless client
        Parameters:
            site_id: String
            client_mac: String
        """
        uri = "/api/v1/sites/{0}/clients/{1}/unauthorize".format(site_id, client_mac)
        resp = self.session.mist_post(uri)
        return resp

    def unauthorizeMultipleClients(self, site_id, client_macs):
        """
        Unauthorize multiple wireless clients
        Parameters:
            site_id: String
            client_macs: Array
        """
        uri = "/api/v1/sites/{0}/clients/unauthorize".format(site_id)        
        resp = self.session.mist_post(uri, body=client_macs)
        return resp

    def search(self, site_id, search={}, page=1, limit=100):
        """
        Search wireless clients
        Parameters:
            site_id: String
            search: Dict
                mac: string: partial / full MAC address
                hostname: string: partial / full hostname
                device: string: device type, e.g. Mac, Nvidia, iPhone
                os: string: os, e.g. Sierra, Yosemite, Windows 10
                model: string: model, e.g. “MBP 15 late 2013”, 6, 6s, “8+ GSM”
                ap: string: AP mac where the client has connected to
                ssid: string: SSID
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri="/api/v1/sites/{0}/clients/search".format(site_id)
        resp = self.session.mist_get(uri, query=search, page=page, limit=limit)
        return resp


    def searchClientEvents(self, site_id, search={}, page=1, limit=100):
        """
        Search client events
        Parameters:
            site_id: String
            search: Dict
                type: string: event type, e.g. MARVIS_EVENT_CLIENT_FBT_FAILURE
                reason_code: int: for assoc/disassoc events
                ssid: string: SSID
                ap: string: AP MAC
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri="/api/v1/sites/{0}/clients/events".format(site_id)
        resp = self.session.mist_get(uri, query=search, page=page, limit=limit)
        return resp

    def searchClientSession(self, site_id, search={}, page=1, limit=100):
        """
        Search client sessions
        Parameters:
            site_id: String
            search: Dict
                ap: string: AP MAC
                band: string: 5 / 24
                client_family: string: E.g. “Mac”, “iPhone”, “Apple watch”
                client_manufacture: string: E.g. “Apple”
                client_model: string: E.g. “8+”, “XS”
                client_os: string: E.g. “Mojave”, “Windows 10”, “Linux”
                ssid: string: SSID
                wlan_id: string: wlan_id
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri="/api/v1/sites/{0}/clients/sessions/search".format(site_id)
        resp = self.session.mist_get(uri, query=search, page=page, limit=limit)
        return resp

    def countByDistinctAttributes(self, site_id, distinct, search={}, page=1, limit=100):
        """
        Count number of wireless client by distinct attribute
        Parameters:
            site_id: String
            distinct: String (ssid, ap, ip, vlan, hostname, os, model, device, default is device)
            search: Dict
                mac: string: partial / full MAC address
                hostname: string: partial / full hostname
                device: string: device type, e.g. Mac, Nvidia, iPhone
                os: string: os, e.g. Sierra, Yosemite, Windows 10
                model: string: model, e.g. “MBP 15 late 2013”, 6, 6s, “8+ GSM”
                ap: string: AP mac where the client has connected to
                ssid: string: SSID
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri="/api/v1/sites/{0}/clients/count".format(site_id)
        query = search
        query["distinct"] = distinct
        resp = self.session.mist_get(uri, query=query, page=page, limit=limit)
        return resp
    
    def countSessionsByDistinctAttributes(self, site_id, distinct, search={}, page=1, limit=100):
        """
        Count number of wireless client by distinct attribute
        Parameters:
            site_id: String
            distinct: String (ssid, ap, ip, vlan, hostname, os, model, device, default is device)
            search: Dict
                ap: string: AP MAC
                band: string: 5 / 24
                client_family: string: E.g. “Mac”, “iPhone”, “Apple watch”
                client_manufacture: string: E.g. “Apple”
                client_model: string: E.g. “8+”, “XS”
                client_os: string: E.g. “Mojave”, “Windows 10”, “Linux”
                ssid: string: SSID
                wlan_id: string: wlan_id
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri="/api/v1/sites/{0}/clients/sessions/count".format(site_id)
        query = search
        query["distinct"] = distinct
        resp = self.session.mist_get(uri, query=query, page=page, limit=limit)
        return resp

    def countEventsByDistinctAttributes(self, site_id, distinct, search={}, page=1, limit=100):
        """
        Count number of wireless client by distinct attribute
        Parameters:
            site_id: String
            distinct: String (ssid, ap, ip, vlan, hostname, os, model, device, default is device)
            search: Dict
                type: string: event type, e.g. MARVIS_EVENT_CLIENT_FBT_FAILURE
                reason_code: int: for assoc/disassoc events
                ssid: string: SSID
                ap: string: AP MAC
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri="/api/v1/sites/{0}/clients/events/count".format(site_id)
        query = search
        query["distinct"] = distinct
        resp = self.session.mist_get(uri, query=query, page=page, limit=limit)
        return resp


    def getClientEvents(self, site_id, client_mac, search={}, page=1, limit=100):
        """ 
        Get list of client events
        Parameters:
            site_id: String
            client_mac: String
            search: Dict
                type: string: event type, e.g. MARVIS_EVENT_CLIENT_FBT_FAILURE
                reason_code: int: for assoc/disassoc events
                ssid: string: SSID
                ap: string: AP MAC
            page: Int (pagination page)
            limit: Int (maximum number of entries per request)
        """
        uri="/api/v1/sites/{0}/clients/{1}/events".format(site_id, client_mac)
        resp = self.session.mist_get(uri, query=search, page=page, limit=limit)
        return resp