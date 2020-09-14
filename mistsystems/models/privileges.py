
from tabulate import tabulate


class Privileges():
    def __init__(self, privileges):
        self.privileges = []
        for privilege in privileges:
            self.privileges.append(_Privilege(privilege))

    def __str__(self):
        columns_headers = ["scope", "role", "name", "site_id",
                           "org_name", "org_id", 'msp_name', "msp_id"]
        table = []
        for entry in self.privileges:
            temp = []
            for field in columns_headers:
                if hasattr(entry, field):
                    temp.append(str(getattr(entry, field)))
                else:
                    temp.append("")
            table.append(temp)
        return tabulate(table, columns_headers)

    def find_org(self, name=None, msp_name=None):
        result = []
        for priv in self.privileges:
            if priv.scope == "org":
                if (not name.lower or name.lower() in priv.name.lower()) and (not msp_name or msp_name.lower() in priv.msp_name.lower()):
                    result.append(priv.__dict__)
        return result

    def find_msp(self, name):
        result = []
        for priv in self.privileges:
            if priv.scope == "msp" and name.lower() in priv.name.lower():
                result.append(priv.__dict__)
        return result

    def find_by_role(self, role="admin"):
        """
        Find orgs by admin role
        Parameters:
            role: String (admin, write, read, Default is admin)
        """
        result = []
        for priv in self.privileges:
            if priv.role.lower() == role.lower():
                result.append(priv.__dict__)
        return result


class _Privilege:
    def __init__(self, privilege):
        self.scope = ""
        self.org_id = ""
        self.org_name = ""
        self.msp_id = ""
        self.msp_name = ""
        self.orggroup_ids = ""
        self.name = ""
        self.role = ""
        self.site_id = ""
        self.sitegroup_ids = ""
        for key, val in privilege.items():
            setattr(self, key, val)

    def __str__(self):
        fields = ["scope", "org_id", "org_name", "msp_id", "msp_name",
                  "orggroup_ids", "name", "role", "site_id", "sitegroup_ids"]
        string = ""
        for field in fields:
            if getattr(self, field) != "":
                string += "%s: %s \r\n" % (field, getattr(self, field))
        return string
