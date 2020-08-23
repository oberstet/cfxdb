##############################################################################
#
#                        Crossbar.io FX
#     Copyright (C) Crossbar.io Technologies GmbH. All rights reserved.
#
##############################################################################
import pprint
import uuid

import flatbuffers
import numpy as np
from cfxdb import pack_uint256, unpack_uint256
from cfxdb.gen.xbr import Market as MarketGen
from zlmdb import table, MapUuidFlatBuffers, MapBytes20TimestampUuid, MapBytes20Uuid


class _MarketGen(MarketGen.Market):
    """
    Expand methods on the class code generated by flatc.

    FIXME: come up with a PR for flatc to generated this stuff automatically.
    """
    @classmethod
    def GetRootAsMarket(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = _MarketGen()
        x.Init(buf, n + offset)
        return x

    def MarketAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def CreatedAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def OwnerAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def CoinAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def MakerAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def ProviderSecurityAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def ConsumerSecurityAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def MarketFeeAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def TidAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def SignatureAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None


class Market(object):
    """
    ``XBRNetwork.Market`` database object.
    """
    def __init__(self, from_fbs=None):
        self._from_fbs = from_fbs

        # [uint8] (uuid)
        self._market = None

        # uint64 (timestamp)
        self._timestamp = None

        # uint256
        self._created = None

        # uint32
        self._seq = None

        # [uint8] (address)
        self._owner = None

        # [uint8] (address)
        self._coin = None

        # string (multihash)
        self._terms = None

        # string (multihash)
        self._meta = None

        # [uint8] (address)
        self._maker = None

        # [uint8] (uint256)
        self._provider_security = None

        # [uint8] (uint256)
        self._consumer_security = None

        # [uint8] (uint256)
        self._market_fee = None

        # [uint8] (ethhash)
        self._tid = None

        # [uint8] (ethsig)
        self._signature = None

    def marshal(self) -> dict:
        obj = {
            'market': self.market.bytes if self.market else None,
            'timestamp': int(self.timestamp) if self.timestamp else None,
            'created': pack_uint256(self.created) if self.created else None,
            'seq': self.seq,
            'owner': bytes(self.owner) if self.owner else None,
            'coin': bytes(self.coin) if self.coin else None,
            'terms': self.terms,
            'meta': self.meta,
            'maker': bytes(self.maker) if self.maker else None,
            'provider_security': pack_uint256(self.provider_security) if self.provider_security else None,
            'consumer_security': pack_uint256(self.consumer_security) if self.consumer_security else None,
            'market_fee': pack_uint256(self.market_fee) if self.market_fee else None,
            'tid': bytes(self.tid) if self.tid else None,
            'signature': bytes(self.signature) if self.signature else None,
        }
        return obj

    def __str__(self):
        return '\n{}\n'.format(pprint.pformat(self.marshal()))

    @property
    def market(self) -> uuid.UUID:
        """
        The unique ID of the market.
        """
        if self._market is None and self._from_fbs:
            if self._from_fbs.MarketLength():
                _market = self._from_fbs.MarketAsBytes()
                self._market = uuid.UUID(bytes=bytes(_market))
        return self._market

    @market.setter
    def market(self, value: uuid.UUID):
        assert value is None or isinstance(value, uuid.UUID)
        self._market = value

    @property
    def timestamp(self) -> np.datetime64:
        """
        Database transaction time (epoch time in ns) of insert or last update.
        """
        if self._timestamp is None and self._from_fbs:
            self._timestamp = np.datetime64(self._from_fbs.Timestamp(), 'ns')
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value: np.datetime64):
        assert value is None or isinstance(value, np.datetime64)
        self._timestamp = value

    @property
    def created(self) -> int:
        """
        Block number (on the blockchain) when the actor (originally) joined the market.
        """
        if self._created is None and self._from_fbs:
            if self._from_fbs.CreatedLength():
                _created = self._from_fbs.CreatedAsBytes()
                self._created = unpack_uint256(bytes(_created))
            else:
                self._created = 0
        return self._created

    @created.setter
    def created(self, value: int):
        assert value is None or type(value) == int
        self._created = value

    @property
    def seq(self) -> int:
        """
        Global market sequence number.
        """
        if self._seq is None and self._from_fbs:
            self._seq = self._from_fbs.Seq()
        return self._seq or 0

    @seq.setter
    def seq(self, value: int):
        assert value is None or type(value) == int
        self._seq = value

    @property
    def owner(self) -> bytes:
        """
        Market owner.
        """
        if self._owner is None and self._from_fbs:
            if self._from_fbs.OwnerLength():
                self._owner = self._from_fbs.OwnerAsBytes()
        return self._owner

    @owner.setter
    def owner(self, value: bytes):
        assert value is None or (type(value) == bytes and len(value) == 20)
        self._owner = value

    @property
    def coin(self) -> bytes:
        """
        Market coin.
        """
        if self._coin is None and self._from_fbs:
            if self._from_fbs.CoinLength():
                self._coin = self._from_fbs.CoinAsBytes()
        return self._coin

    @coin.setter
    def coin(self, value: bytes):
        assert value is None or (type(value) == bytes and len(value) == 20)
        self._coin = value

    @property
    def terms(self) -> str:
        """
        The XBR market terms set by the market owner. IPFS Multihash pointing to a ZIP archive file with market documents.
        """
        if self._terms is None and self._from_fbs:
            terms = self._from_fbs.Terms()
            if terms:
                self._terms = terms.decode('utf8')
        return self._terms

    @terms.setter
    def terms(self, value: str):
        assert value is None or type(value) == str
        self._terms = value

    @property
    def meta(self) -> str:
        """
        The XBR market metadata published by the market owner. IPFS Multihash pointing to a RDF/Turtle file with market metadata.
        """
        if self._meta is None and self._from_fbs:
            meta = self._from_fbs.Meta()
            if meta:
                self._meta = meta.decode('utf8')
        return self._meta

    @meta.setter
    def meta(self, value):
        assert value is None or type(value) == str
        self._meta = value

    @property
    def maker(self) -> bytes:
        """
        The address of the XBR market maker that will run this market. The delegate of the market owner.
        """
        if self._maker is None and self._from_fbs:
            if self._from_fbs.MakerLength():
                self._maker = self._from_fbs.MakerAsBytes()
        return self._maker

    @maker.setter
    def maker(self, value: bytes):
        assert value is None or (type(value) == bytes and len(value) == 20)
        self._maker = value

    @property
    def provider_security(self) -> int:
        """
        The amount of XBR tokens a XBR provider joining the market must deposit.
        """
        if self._provider_security is None and self._from_fbs:
            if self._from_fbs.ProviderSecurityLength():
                _provider_security = self._from_fbs.ProviderSecurityAsBytes()
                self._provider_security = unpack_uint256(bytes(_provider_security))
            else:
                self._provider_security = 0
        return self._provider_security

    @provider_security.setter
    def provider_security(self, value: int):
        assert value is None or type(value) == int
        self._provider_security = value

    @property
    def consumer_security(self) -> int:
        """
        The amount of XBR tokens a XBR consumer joining the market must deposit.
        """
        if self._consumer_security is None and self._from_fbs:
            if self._from_fbs.ConsumerSecurityLength():
                _consumer_security = self._from_fbs.ConsumerSecurityAsBytes()
                self._consumer_security = unpack_uint256(bytes(_consumer_security))
            else:
                self._consumer_security = 0
        return self._consumer_security

    @consumer_security.setter
    def consumer_security(self, value: int):
        assert value is None or type(value) == int
        self._consumer_security = value

    @property
    def market_fee(self) -> int:
        """
        The fee taken by the market (beneficiary is the market owner). The fee is a percentage of the revenue of the XBR Provider that receives XBR Token paid for transactions. The fee must be between 0% (inclusive) and 99% (inclusive), and is expressed as a fraction of the total supply of XBR tokens.
        """
        if self._market_fee is None and self._from_fbs:
            if self._from_fbs.MarketFeeLength():
                _market_fee = self._from_fbs.MarketFeeAsBytes()
                self._market_fee = unpack_uint256(bytes(_market_fee))
            else:
                self._market_fee = 0
        return self._market_fee

    @market_fee.setter
    def market_fee(self, value):
        assert value is None or type(value) == int
        self._market_fee = value

    @property
    def tid(self) -> bytes:
        """
        Transaction hash of the transaction this change was committed to the blockchain under.
        """
        if self._tid is None and self._from_fbs:
            if self._from_fbs.TidLength():
                self._tid = self._from_fbs.TidAsBytes()
        return self._tid

    @tid.setter
    def tid(self, value: bytes):
        assert value is None or (type(value) == bytes and len(value) == 32)
        self._tid = value

    @property
    def signature(self) -> bytes:
        """
        When signed off-chain and submitted via ``XBRMarket.createMarketFor``.
        """
        if self._signature is None and self._from_fbs:
            if self._from_fbs.SignatureLength():
                self._signature = self._from_fbs.SignatureAsBytes()
        return self._signature

    @signature.setter
    def signature(self, value: bytes):
        assert value is None or (type(value) == bytes and len(value) == 65)
        self._signature = value

    @staticmethod
    def cast(buf):
        return Market(_MarketGen.GetRootAsMarket(buf, 0))

    def build(self, builder):

        market = self.market.bytes if self.market else None
        if market:
            market = builder.CreateString(market)

        created = self.created
        if created:
            created = builder.CreateString(pack_uint256(created))

        owner = self.owner
        if owner:
            owner = builder.CreateString(owner)

        coin = self.coin
        if coin:
            coin = builder.CreateString(coin)

        terms = self.terms
        if terms:
            terms = builder.CreateString(terms)

        meta = self.meta
        if meta:
            meta = builder.CreateString(meta)

        maker = self.maker
        if maker:
            maker = builder.CreateString(maker)

        provider_security = self.provider_security
        if provider_security:
            provider_security = builder.CreateString(pack_uint256(provider_security))

        consumer_security = self.consumer_security
        if consumer_security:
            consumer_security = builder.CreateString(pack_uint256(consumer_security))

        market_fee = self.market_fee
        if market_fee:
            market_fee = builder.CreateString(pack_uint256(market_fee))

        tid = self.tid
        if tid:
            tid = builder.CreateString(tid)

        signature = self.signature
        if signature:
            signature = builder.CreateString(signature)

        MarketGen.MarketStart(builder)

        if market:
            MarketGen.MarketAddMarket(builder, market)

        if self.timestamp:
            MarketGen.MarketAddTimestamp(builder, int(self.timestamp))

        if created:
            MarketGen.MarketAddProviderSecurity(builder, created)

        if self.seq:
            MarketGen.MarketAddSeq(builder, self.seq)

        if owner:
            MarketGen.MarketAddOwner(builder, owner)

        if coin:
            MarketGen.MarketAddCoin(builder, coin)

        if terms:
            MarketGen.MarketAddTerms(builder, terms)

        if meta:
            MarketGen.MarketAddMeta(builder, meta)

        if maker:
            MarketGen.MarketAddMaker(builder, maker)

        if provider_security:
            MarketGen.MarketAddProviderSecurity(builder, provider_security)

        if consumer_security:
            MarketGen.MarketAddConsumerSecurity(builder, consumer_security)

        if market_fee:
            MarketGen.MarketAddMarketFee(builder, market_fee)

        if tid:
            MarketGen.MarketAddTid(builder, tid)

        if signature:
            MarketGen.MarketAddSignature(builder, signature)

        final = MarketGen.MarketEnd(builder)

        return final


@table('861b0942-0c3f-4d41-bc35-d8c86af0b2c9', build=Market.build, cast=Market.cast)
class Markets(MapUuidFlatBuffers):
    """
    Markets table, mapping from ``market_id|UUID`` to :class:`cfxdb.xbr.Market`
    """


@table('7c3d67b4-35a3-449f-85a6-2695636fc63e')
class IndexMarketsByOwner(MapBytes20TimestampUuid):
    """
    Markets-by-owner index with ``(owner_adr|bytes[20], created|int) -> market_id|UUID`` mapping.
    """


@table('4f50a97a-4531-4eab-a91b-45cc42b3dd21')
class IndexMarketsByActor(MapBytes20TimestampUuid):
    """
    Markets-by-actor index with ``(actor_adr|bytes[20], joined|int) -> market_id|UUID`` mapping.
    """


@table('d511774c-0c7b-4d3f-a2de-6748c072a56f')
class IndexMarketsByMaker(MapBytes20Uuid):
    """
    Markets-by-maker index with ``maker_adr|bytes[20] -> market_id|UUID`` mapping.
    """
