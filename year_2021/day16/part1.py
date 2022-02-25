from collections import deque
input = '38006F45291200'


def hex_to_bin(input: str) -> str:
    """Convert from hex string to binary string"""
    return '{0:b}'.format(int(input, 16))


def take_from_queue(bin_queue: deque, times: int) -> list:
    response = []
    for _ in range(times):
        response.append(bin_queue.popleft())
    return response


def take_package_size(bin_queue: deque, size_bit: str) -> list:
    if size_bit == '1':
        return take_from_queue(bin_queue, 11)
    return take_from_queue(bin_queue, 15)


def take_literal_value(bin_queue: deque) -> list:
    response = []
    while(True):
        five_bits = take_from_queue(bin_queue, 5)

        response += five_bits[1:]
        if(five_bits[0] == '0'):
            break
    return response


def run():
    bin_string = hex_to_bin(input)

    print(bin_string)

    bin_queue = deque(list(bin_string))

    total_version_id = 0
    while bin_queue:
        version_id = ''.join(take_from_queue(bin_queue, 3))
        total_version_id += int(version_id, 2)
        print('{:<20} {:<10}'.format('version_id', int(version_id, 2)))
        print('{:<20} {:<10}'.format('total_version_id', total_version_id))
        type_id = ''.join(take_from_queue(bin_queue, 3))
        print('{:<20} {:<10}'.format('type_id', int(type_id, 2)))
        if int(type_id, 2) == 4:
            literal = take_literal_value(bin_queue)
            print(literal)
            print(int(''.join(literal), 2))
        while bin_queue and bin_queue[-1] == '0':
            bin_queue.popleft()


if __name__ == "__main__":
    run()
