##############################################################################
#
#                        Crossbar.io FX
#     Copyright (C) Crossbar.io Technologies GmbH. All rights reserved.
#
##############################################################################

import pprint
import uuid

from cfxdb.common import ConfigurationElement


class Permission(ConfigurationElement):
    """
    Role permission database object.
    """
    def __init__(self,
                 oid=None,
                 label=None,
                 description=None,
                 tags=None,
                 role_oid=None,
                 uri=None,
                 created=None,
                 owner=None,
                 _unknown=None):
        """

        :param oid: Object ID of this permission object
        :type oid: uuid.UUID

        :param label: Optional user label of permission
        :type label: str

        :param description: Optional user description of permission
        :type description: str

        :param tags: Optional list of user tags on permission
        :type tags: list[str]

        :param role_oid: Object ID of role this permission applies to.
        :type role_oid: uuid.UUID

        :param uri: URI matched for permission.
        :type uri: str

        :param created: Timestamp when the permission was created
        :type created: datetime.datetime

        :param owner: Owning user (object ID)
        :type owner: uuid.UUID

       :param _unknown: Any unparsed/unprocessed data attributes
        :type _unknown: None or dict
        """
        ConfigurationElement.__init__(self, oid=oid, label=label, description=description, tags=tags)
        self.role_oid = role_oid
        self.uri = uri
        self.created = created
        self.owner = owner

        # private member with unknown/untouched data passing through
        self._unknown = _unknown

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if not ConfigurationElement.__eq__(self, other):
            return False
        if other.role_oid != self.role_oid:
            return False
        if other.uri != self.uri:
            return False
        if other.created != self.created:
            return False
        if other.owner != self.owner:
            return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return pprint.pformat(self.marshal())

    def copy(self, other, overwrite=False):
        """
        Copy over other object.

        :param other: Other permission to copy data from.
        :type other: instance of :class:`ManagementRealm`
        :return:
        """
        ConfigurationElement.copy(self, other, overwrite=overwrite)

        if (not self.role_oid and other.role_oid) or overwrite:
            self.role_oid = other.role_oid
        if (not self.uri and other.uri) or overwrite:
            self.uri = other.uri
        if (not self.created and other.created) or overwrite:
            self.created = other.created
        if (not self.owner and other.owner) or overwrite:
            self.owner = other.owner

        # _unknown is not copied!

    def marshal(self):
        """
        Marshal this object to a generic host language object.

        :return: dict
        """
        assert isinstance(self.oid, uuid.UUID)
        assert isinstance(self.role_oid, uuid.UUID)
        assert type(self.uri) == str
        assert self.created is None or type(self.created) == int
        assert self.owner is None or isinstance(self.owner, uuid.UUID)

        obj = ConfigurationElement.marshal(self)

        obj.update({
            'oid': str(self.oid) if self.oid else None,
            'role_oid': str(self.role_oid) if self.role_oid else None,
            'uri': self.uri,
            'created': self.created,
            'owner': str(self.owner) if self.owner else None,
        })

        if self._unknown:
            # pass through all attributes unknown
            obj.update(self._unknown)

        return obj

    @staticmethod
    def parse(data):
        """
        Parse generic host language object into an object of this class.

        :param data: Generic host language object
        :type data: dict

        :return: instance of :class:`ManagementRealm`
        """
        assert type(data) == dict

        obj = ConfigurationElement.parse(data)
        data = obj._unknown

        # future attributes (yet unknown) are not only ignored, but passed through!
        _unknown = {}
        for k in data:
            if k not in ['oid', 'role_oid', 'uri', 'owner', 'created']:
                _unknown[k] = data[k]

        role_oid = data.get('role_oid', None)
        assert role_oid is None or type(role_oid) == str
        if role_oid:
            role_oid = uuid.UUID(role_oid)

        uri = data.get('uri', None)
        assert uri is None or type(uri) == str

        owner = data.get('owner', None)
        assert owner is None or type(owner) == str
        if owner:
            owner = uuid.UUID(owner)

        created = data.get('created', None)
        assert created is None or type(created) == int

        obj = Permission(oid=obj.oid,
                         label=obj.label,
                         description=obj.description,
                         tags=obj.tags,
                         role_oid=role_oid,
                         uri=uri,
                         owner=owner,
                         created=created,
                         _unknown=_unknown)

        return obj
