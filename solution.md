
# Signing


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
from ecc import PrivateKey, Signature, S256Point, G, N
from random import randint
        
class PrivateKey(PrivateKey):
    
    def sign(self, z):
        # we need a random number k: randint(0, 2**256)
        k = randint(0, 2**256)
        # r is the x coordinate of the resulting point k*G
        r = (k*G).x.num
        # remember 1/k = pow(k, N-2, N)
        k_inv = pow(k, N-2, N)
        # s = (z+r*secret) / k
        s = (z + r*self.secret) * k_inv % N
        if s > N/2:
            s = N - s
        # return an instance of Signature:
        # Signature(r, s)
        return Signature(r, s)
```
