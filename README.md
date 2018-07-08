
# Signing with a Private Key


```python
# Signing Example
from random import randint

from ecc import G, N
from helper import double_sha256

secret = 1800555555518005555555
z = int.from_bytes(double_sha256(b'ECDSA is awesome!'), 'big')
k = randint(0, 2**256)
r = (k*G).x.num
s = (z+r*secret) * pow(k, N-2, N) % N
print(hex(z), hex(r), hex(s))
print(secret*G)
```

## Test Driven Exercise


```python
from ecc import PrivateKey, Signature, G, N
from random import randint
        
class PrivateKey(PrivateKey):
    
    def sign(self, z):
        # we need a random number k: randint(0, 2**256)
        # r is the x coordinate of the resulting point k*G
        # remember 1/k = pow(k, N-2, N)
        # s = (z+r*secret) / k
        # return an instance of Signature:
        # Signature(r, s)
        pass
```
