from functools import lru_cache

from .schema import Customer, Order, Product

CustomerStorageType = dict[int, Customer]
OrdersStorageType = dict[int, Order]
ProductsStorageType = dict[int, Product]

CUSTOMERS: CustomerStorageType = {}
ORDERS: OrdersStorageType = {}
PRODUCTS: ProductsStorageType = {}


@lru_cache(maxsize=1)
def get_customers_storage() -> CustomerStorageType:
    return CUSTOMERS

@lru_cache(maxsize=1)
def get_orders_storage() -> OrdersStorageType:
    return ORDERS

@lru_cache(maxsize=1)
def get_products_storage() -> ProductsStorageType:
    return PRODUCTS