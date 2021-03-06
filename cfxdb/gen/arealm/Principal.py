# automatically generated by the FlatBuffers compiler, do not modify

# namespace: arealm

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

# Application realm client principals.
class Principal(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsPrincipal(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Principal()
        x.Init(buf, n + offset)
        return x

    # Principal
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ID of this principal.
    # Principal
    def Oid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = o + self._tab.Pos
            from ..oid_t import oid_t
            obj = oid_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ID of the application realm the authenticated principal will be joined to.
    # Principal
    def ArealmOid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = o + self._tab.Pos
            from ..oid_t import oid_t
            obj = oid_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # WAMP authid of the principal, must be unique within the application realm at any moment in time.
    # Principal
    def Authid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ID of the role the authenticated principal will be joined to the application realm.
    # Principal
    def RoleOid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = o + self._tab.Pos
            from ..oid_t import oid_t
            obj = oid_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Optional authextra information returned to the authenticating principal (CBOR serialized).
    # Principal
    def Authextra(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Principal
    def AuthextraAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Principal
    def AuthextraLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Principal
    def AuthextraIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

def PrincipalStart(builder): builder.StartObject(5)
def PrincipalAddOid(builder, oid): builder.PrependStructSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(oid), 0)
def PrincipalAddArealmOid(builder, arealmOid): builder.PrependStructSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(arealmOid), 0)
def PrincipalAddAuthid(builder, authid): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(authid), 0)
def PrincipalAddRoleOid(builder, roleOid): builder.PrependStructSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(roleOid), 0)
def PrincipalAddAuthextra(builder, authextra): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(authextra), 0)
def PrincipalStartAuthextraVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def PrincipalEnd(builder): return builder.EndObject()
