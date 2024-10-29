from datetime import datetime

from pydantic import BaseModel

class Delivery(BaseModel):
    timestamp: datetime
    dimensions: tuple[int, int]


m = Delivery(timestamp='2020-01-02T03:04:05Z', dimensions=['10', '20'])
print(repr(m.timestamp))
print(m.timestamp)
print(type(m.timestamp))

print(m.dimensions)

Delivery(timestamp='2020-01-02T03:04:05Z', dimensions=['10'])