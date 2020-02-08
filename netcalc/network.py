from ipv4 import ipv4, ipv4_mask

class network:

    # ip:       11000000.10101000.00000001.00000001
    # mask:     11111111.11111111.11111111.00000000
    # &:        ++++++++.++++++++.++++++++.--------
    #           11000000.10101000.00000001.00000000
    @staticmethod
    def _address(ip, mask): return ip & mask

    # mask:     11111111.11111111.11111111.00000000
    # ~:        00000000.00000000.00000000.11111111
    # ones:     11111111.11111111.11111111.11111111
    # &:        --------.--------.--------.11111111
    # -1:       --------.--------.--------.11111110
    @staticmethod
    def _nhost(mask): return -1 + ~mask & ipv4.ones()

    # ip:       11000000.10101000.00000001.00000001
    # mask:     11111111.11111111.11111111.00000000
    # add:      11000000.10101000.00000001.00000000
    # nhost:    --------.--------.--------.11111110
    # broad:    11000000.10101000.00000001.11111110
    # +1:       11000000.10101000.00000001.11111111
    @staticmethod
    def _broadcast(ip, mask): return network._address(ip, mask) + network._nhost(mask) + 1

    # ip:       11000000.10101000.00000001.00000001
    # mask:     11111111.11111111.11111111.00000000
    # nhost:    --------.--------.--------.11111110
    # add:      11000000.10101000.00000001.00000000
    # for i in 0.0.0.0 -> 0.0.0.11111110:
    #     add + i + 1
    #     ex i = 101: 11000000.10101000.00000001.00000110
    @staticmethod
    def _hosts(ip, mask):
        net = network._address(ip, mask)
        for i in range(network._nhost(mask)):
            yield net + i + 1

    # ip:       11000000.10101000.00000001.00000001
    # mask:     11111111.11111111.11111111.00000000
    # mask_der: 11111111.11111111.11111111.11100000
    # diff:     00000000.00000000.00000000.11100000 -> 3
    # for i in 0 -> [2**3] 8
    #     ex i = 2: 
    #         net: 11000000.10101000.00000001.00000000
    #         0's in mask_der: 5
    #         -> 11000000.10101000.00000001.01000000
    @staticmethod
    def _mask(ip, mask_ori, mask_der):
        diff = bin(mask_der ^ mask_ori).count('1')  # TODO ugly, refactor
        for i in range(2**diff):
            yield network._address(ip, mask_ori) + (i << bin(int(mask_der))[2:].count('0'))

    # Assert basic knowledge, store data
    def __init__(self, ip, mask):
        assert type(ip) is ipv4 and type(mask) is ipv4_mask, f'{type(ip)} should be {ipv4} and {type(mask)} should be {ipv4_mask}'
        self._ip = ip
        self._mask = mask

    # :OwO:
    def __str__(self): return f'{str(self._ip)} {str(self._mask)}'

    # --------------------- Wrapers around @staticmethods --------------------- #
    def simple(self): return self._ip                                           #
    def mask(self): return self._mask                                           #
    def address(self): return ipv4(network._address(self._ip, self._mask))      #
    def nhost(self): return network._nhost(self._mask)                          #
    def broadcast(self): return ipv4(network._broadcast(self._ip, self._mask))  #
    def hosts(self):                                                            #
        for host in network._hosts(self._ip, self._mask):                       #
            yield network(ipv4(host), self._mask)                               #
    def mask(self, amask):                                                      #
        assert type(amask) is ipv4_mask, f'{amask} should be {ipv4_mask}'       #
        for subnet in network._mask(self._ip, self._mask, amask):               #
            yield network(ipv4(subnet), amask)                                  #
    # ------------------------------------------------------------------------- #

if __name__ == "__main__":

    net = network(ipv4('192.168.10.23'), ipv4.mask('255.255.255.0'))
    
    print(f'net: {net}')
    print(f'address: {net.address()}')
    print(f'broadcast: {net.broadcast()}')
    
    print(f'\nApplied mask {ipv4.mask("255.255.255.248")}:')
    for subnet in net.mask(ipv4.mask('29')):
        print(subnet)

    print(f'\nFirst subnet hosts:')
    subnet = list(net.mask(ipv4.mask('29')))[0]
    for host in subnet.hosts():
        print(host.simple())
    print(f'Broadcast: {subnet.broadcast()}')
