def murmurhash3_16(key, seed=0):
    def rotl(x, r):
        return ((x << r) | (x >> (32 - r))) & 0xFFFFFFFF

    h1 = seed
    c1 = 0xcc9e2d51
    c2 = 0x1b873593

    data = key.encode('utf-8')
    length = len(data)
    nblocks = length // 4
    tail = length % 4

    for i in range(nblocks):
        k = int.from_bytes(data[i * 4:(i + 1) * 4], byteorder='little')
        k = (k * c1) & 0xFFFFFFFF
        k = rotl(k, 15)
        k = (k * c2) & 0xFFFFFFFF

        h1 ^= k
        h1 = rotl(h1, 13)
        h1 = (h1 * 5) & 0xFFFFFFFF
        h1 += 0xe6546b64

    k = 0
    if tail == 3:
        k = int.from_bytes(data[length - 3:length], byteorder='little')
        k = (k * c1) & 0xFFFFFFFF
        k = rotl(k, 15)
        k = (k * c2) & 0xFFFFFFFF
        h1 ^= k
    if tail >= 2:
        k = int.from_bytes(data[length - 2:length], byteorder='little')
        k = (k * c1) & 0xFFFFFFFF
        k = rotl(k, 15)
        k = (k * c2) & 0xFFFFFFFF
        h1 ^= k
    if tail >= 1:
        k = data[length - 1]
        k = (k * c1) & 0xFFFFFFFF
        k = rotl(k, 15)
        k = (k * c2) & 0xFFFFFFFF
        h1 ^= k

    h1 ^= length
    h1 ^= h1 >> 16
    h1 = (h1 * 0x85ebca6b) & 0xFFFFFFFF
    h1 ^= h1 >> 13
    h1 = (h1 * 0xc2b2ae35) & 0xFFFFFFFF
    h1 ^= h1 >> 16
    h1 = h1 & 0x1FFFFFF
    return h1