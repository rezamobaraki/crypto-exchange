import dataclasses


@dataclasses.dataclass(frozen=True)
class RedisNameTemplates:
    AGGREGATE_ORDERS: str = "aggregate_orders:{crypto_name}"

    @classmethod
    def aggregate_orders(cls,*, crypto_name) -> str:
        return cls.AGGREGATE_ORDERS.format(crypto_name=crypto_name)
