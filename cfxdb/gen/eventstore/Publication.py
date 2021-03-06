# automatically generated by the FlatBuffers compiler, do not modify

# namespace: eventstore

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

# This table stores WAMP publications with configurable amount of details, optionally including application payload.
class Publication(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsPublication(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Publication()
        x.Init(buf, n + offset)
        return x

    # Publication
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Timestamp when the publication was accepted by the broker. Epoch time in ns.
    # Publication
    def Timestamp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # WAMP publication ID that was assigned by the broker.
    # Publication
    def Publication(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # WAMP session ID of the publisher.
    # Publication
    def Publisher(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # The WAMP or application URI of the PubSub topic the event was published to.
    # Publication
    def Topic(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Positional values for application-defined event payload.
    # Publication
    def Args(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Publication
    def ArgsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Publication
    def ArgsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Publication
    def ArgsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

    # Keyword values for application-defined event payload.
    # Publication
    def Kwargs(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Publication
    def KwargsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Publication
    def KwargsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Publication
    def KwargsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

    # Alternative, transparent payload. If given, ``args`` and ``kwargs`` must be left unset.
    # Publication
    def Payload(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Publication
    def PayloadAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Publication
    def PayloadLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Publication
    def PayloadIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0

    # If ``True``, the broker was asked to acknowledge the publication with a success or error response.
    # Publication
    def Acknowledge(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # If ``True``, the broker was requested to retain this event.
    # Publication
    def Retain(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # If ``True``, the broker was asked to exclude the publisher from receiving the event.
    # Publication
    def ExcludeMe(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # List of WAMP session IDs to exclude from receiving this event.
    # Publication
    def Exclude(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # Publication
    def ExcludeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint64Flags, o)
        return 0

    # Publication
    def ExcludeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Publication
    def ExcludeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        return o == 0

    # List of WAMP authids to exclude from receiving this event.
    # Publication
    def ExcludeAuthid(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # Publication
    def ExcludeAuthidLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Publication
    def ExcludeAuthidIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        return o == 0

    # List of WAMP authroles to exclude from receiving this event.
    # Publication
    def ExcludeAuthrole(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # Publication
    def ExcludeAuthroleLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Publication
    def ExcludeAuthroleIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        return o == 0

    # List of WAMP session IDs eligible to receive this event.
    # Publication
    def Eligible(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # Publication
    def EligibleAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint64Flags, o)
        return 0

    # Publication
    def EligibleLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Publication
    def EligibleIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        return o == 0

    # List of WAMP authids eligible to receive this event.
    # Publication
    def EligibleAuthid(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # Publication
    def EligibleAuthidLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Publication
    def EligibleAuthidIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        return o == 0

    # List of WAMP authroles eligible to receive this event.
    # Publication
    def EligibleAuthrole(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # Publication
    def EligibleAuthroleLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Publication
    def EligibleAuthroleIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        return o == 0

    # When using payload transparency, the encoding algorithm that was used to encode the payload.
    # Publication
    def EncAlgo(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # When using payload transparency with an encryption algorithm, the payload encryption key.
    # Publication
    def EncKey(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Publication
    def EncKeyAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Publication
    def EncKeyLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Publication
    def EncKeyIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        return o == 0

    # When using payload transparency, the payload object serializer that was used encoding the payload.
    # Publication
    def EncSerializer(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

def PublicationStart(builder): builder.StartObject(19)
def PublicationAddTimestamp(builder, timestamp): builder.PrependUint64Slot(0, timestamp, 0)
def PublicationAddPublication(builder, publication): builder.PrependUint64Slot(1, publication, 0)
def PublicationAddPublisher(builder, publisher): builder.PrependUint64Slot(2, publisher, 0)
def PublicationAddTopic(builder, topic): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(topic), 0)
def PublicationAddArgs(builder, args): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(args), 0)
def PublicationStartArgsVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def PublicationAddKwargs(builder, kwargs): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(kwargs), 0)
def PublicationStartKwargsVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def PublicationAddPayload(builder, payload): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(payload), 0)
def PublicationStartPayloadVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def PublicationAddAcknowledge(builder, acknowledge): builder.PrependBoolSlot(7, acknowledge, 0)
def PublicationAddRetain(builder, retain): builder.PrependBoolSlot(8, retain, 0)
def PublicationAddExcludeMe(builder, excludeMe): builder.PrependBoolSlot(9, excludeMe, 0)
def PublicationAddExclude(builder, exclude): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(exclude), 0)
def PublicationStartExcludeVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def PublicationAddExcludeAuthid(builder, excludeAuthid): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(excludeAuthid), 0)
def PublicationStartExcludeAuthidVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def PublicationAddExcludeAuthrole(builder, excludeAuthrole): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(excludeAuthrole), 0)
def PublicationStartExcludeAuthroleVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def PublicationAddEligible(builder, eligible): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(eligible), 0)
def PublicationStartEligibleVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def PublicationAddEligibleAuthid(builder, eligibleAuthid): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(eligibleAuthid), 0)
def PublicationStartEligibleAuthidVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def PublicationAddEligibleAuthrole(builder, eligibleAuthrole): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(eligibleAuthrole), 0)
def PublicationStartEligibleAuthroleVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def PublicationAddEncAlgo(builder, encAlgo): builder.PrependUint8Slot(16, encAlgo, 0)
def PublicationAddEncKey(builder, encKey): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(encKey), 0)
def PublicationStartEncKeyVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def PublicationAddEncSerializer(builder, encSerializer): builder.PrependUint8Slot(18, encSerializer, 0)
def PublicationEnd(builder): return builder.EndObject()
