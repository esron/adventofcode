from collections import deque
input  = 'D2FE28'

def hex_to_bin(input: str) -> str:
    """Convert from hex string to binary string"""
    return '{0:b}'.format(int(input, 16))

def take_from_queue(bin_queue: deque, times: int) -> list:
    version_id = []
    for _ in range(times):
        version_id.append(bin_queue.popleft())
    return version_id

bin_string = hex_to_bin(input)

print(bin_string)
bin_queue = deque(list(bin_string))

version_id = ''.join(take_from_queue(bin_queue, 3))
print('{:<12} {:<3}'.format('version_id', int(version_id, 2)))
type_id = ''.join(take_from_queue(bin_queue, 3))
print('{:<12} {:<3}'.format('type_id', int(type_id, 2)))
