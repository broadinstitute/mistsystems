# Mist System Python Library
**Unofficial Juniper-Mist library**

## How to use this library
#### Install
```
pip install mistsystems
```
#### With API Token
```
>>> from mistsystems import api

>>> mist = api.MistSystems(host="api.mist.com", apitoken="mysecretapitoken")
```
#### With Login/password
```
>>> from mistsystems import api

>>> mist = api.MistSystems(host="api.mist.com", email="user@mycorp.com", password="mysecretpassword")
```
#### Display account privileges
```
>>> print(mist.privileges)
scope    role    name                   site_id    org_name    org_id                                msp_name       msp_id
-------  ------  ---------------------  ---------  ----------  ------------------------------------  -------------  ------------------------------------
org      admin   Demo Test                                     39ce2088-xxxx-xxxx-xxxx-1a5a88bab5ee
org      admin   Demo 1                                        e338cdf2-xxxx-xxxx-xxxx-2996d983d8bc  MSP Demo  1e7002ba-xxxx-xxxx-xxxx-eb6a8151b731
org      write   Demo 2                                        995f5d60-xxxx-xxxx-xxxx-4313da26e1c3
org      read    Demo 3                                        3440ed64-xxxx-xxxx-xxxx-d62ac4586fd1
```
#### Find an organization 
```
>>> mist.privileges.find_org(name="test")
[{'scope': 'org', 'org_id': '9ce2088-xxxx-xxxx-xxxx-1a5a88bab5ee', 'org_name': '', 'msp_id': '', 'msp_name': '', 'orggroup_ids': '', 'name': 'Demo Test', 'role': 'admin', 'site_id': '', 'sitegroup_ids': ''}, ]
```
#### Request the Mist Cloud
````
>>> mist.orgs.sites.get(org_id="ca7e9350-xxxx-xxxx-xxxx-db350863a910")
{'result': [{'timezone': 'Europe/Paris', 'country_code': 'FR', 'latlng': {'lat': 48.889036, 'lng': 2.280529}, 'address': '41 Rue de Villiers, 92200 Neuilly-sur-Seine, France', 'lat': 48.889036, 'lng': 2.280529, 'id': '42ee034a-xxxx-xxxx-xxxx-8499d934eff1', 'name': 'Primary Site', 'org_id': 'ca7e9350-xxxx-xxxx-xxxx-db350863a910', 'created_time': 1591344677, 'modified_time': 1598866388, 'rftemplate_id': None, 'secpolicy_id': None, 'alarmtemplate_id': None, 'networktemplate_id': None, 'tzoffset': 60}], 'status_code': 200, 'error': '', 'uri': '/api/v1/orgs/ca7e9350-xxxx-xxxx-xxxx-db350863a910/sites'}

>>> mist.sites.wlans.get(site_id="42ee034a-xxxx-xxxx-xxxx-8499d934eff1")
{'result': [{'ssid': 'test', 'enabled': False, 'hide_ssid': False, 'no_static_ip': False, 'no_static_dns': False, 'band': 'both', 'band_steer': False, 'airwatch': {'enabled': False, 'console_url': '', 'api_key': '', 'username': '', 'password': ''}, 'disable_wmm': False, 'disable_uapsd': False, 'use_eapol_v1': False, 'roam_mode': 'NONE', 'auth_servers_nas_id': '', 'auth_servers_nas_ip': '', 'auth_server_selection': 'ordered', 'disable_11ax': False, 'vlan_enabled': False, 'apply_to': 'site', 'id': '8b65474b-xxxx-xxxx-xxxx-b2e2456650fe', 'for_site': True, 'template_id': None, 'site_id': '42ee034a-xxxx-xxxx-xxxx-8499d934eff1', 'org_id': 'ca7e9350-xxxx-xxxx-xxxx-db350863a910', 'created_time': 1599767311, 'modified_time': 1599767311, 'mxtunnel_id': None, 'wxtunnel_id': None, 'interface': 'all'}], 'status_code': 200, 'error': '', 'uri': '/api/v1/sites/42ee034a-xxxx-xxxx-xxxx-8499d934eff1/wlans'}
```