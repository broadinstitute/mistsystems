# Mist System Python Library
**This is an Unofficial Juniper-Mist library**

## How to use this library
```
>>>from mistsystems import api

>>> mist = api.MistSystems(host="api.mist.com", email="user@mycorp.com", password="mysecretpassword")

>>> mist.orgs.sites.get(org_id="ca7e9350-xxxx-xxxx-xxxx-db350863a910")
{'result': [{'timezone': 'Europe/Paris', 'country_code': 'FR', 'latlng': {'lat': 48.889036, 'lng': 2.280529}, 'address': '41 Rue de Villiers, 92200 Neuilly-sur-Seine, France', 'lat': 48.889036, 'lng': 2.280529, 'id': '42ee034a-xxxx-xxxx-xxxx-8499d934eff1', 'name': 'Primary Site', 'org_id': 'ca7e9350-xxxx-xxxx-xxxx-db350863a910', 'created_time': 1591344677, 'modified_time': 1598866388, 'rftemplate_id': None, 'secpolicy_id': None, 'alarmtemplate_id': None, 'networktemplate_id': None, 'tzoffset': 60}], 'status_code': 200, 'error': '', 'uri': '/api/v1/orgs/ca7e9350-xxxx-xxxx-xxxx-db350863a910/sites'}

>>> mist.sites.wlans.get(site_id="42ee034a-xxxx-xxxx-xxxx-8499d934eff1")
{'result': [{'ssid': 'test', 'enabled': False, 'hide_ssid': False, 'no_static_ip': False, 'no_static_dns': False, 'band': 'both', 'band_steer': False, 'airwatch': {'enabled': False, 'console_url': '', 'api_key': '', 'username': '', 'password': ''}, 'disable_wmm': False, 'disable_uapsd': False, 'use_eapol_v1': False, 'roam_mode': 'NONE', 'auth_servers_nas_id': '', 'auth_servers_nas_ip': '', 'auth_server_selection': 'ordered', 'disable_11ax': False, 'vlan_enabled': False, 'apply_to': 'site', 'id': '8b65474b-xxxx-xxxx-xxxx-b2e2456650fe', 'for_site': True, 'template_id': None, 'site_id': '42ee034a-xxxx-xxxx-xxxx-8499d934eff1', 'org_id': 'ca7e9350-xxxx-xxxx-xxxx-db350863a910', 'created_time': 1599767311, 'modified_time': 1599767311, 'mxtunnel_id': None, 'wxtunnel_id': None, 'interface': 'all'}], 'status_code': 200, 'error': '', 'uri': '/api/v1/sites/42ee034a-xxxx-xxxx-xxxx-8499d934eff1/wlans'}
```