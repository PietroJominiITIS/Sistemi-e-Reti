from functools import reduce

class ipv4:

    # --------------- Wrappers --------------- #
    @staticmethod                              #
    def ones(): return ipv4('255.255.255.255') #
                                               #
    @staticmethod                              #
    def zeros(): return ipv4('0.0.0.0')        #
                                               #
    @staticmethod                              #
    def mask(mask): return ipv4_mask(mask)     #
    # ---------------------------------------- #

    # Validate int ip, 0 <= ip < (MAXIP :: 4294967296)
    @staticmethod
    def _validateint(ip):
        assert type(ip) is int, f'Only {int} ip allowed'
        return 0 <= ip < 2**32

    # Validate str ip
    # in form a.b.c.d | 0 <= a, b, c, d <= 255
    @staticmethod
    def _validatestr(ip):
        assert type(ip) is str, f'Only {str} ip allowed'
        chunks = ip.split('.')
        if len(chunks) != 4: return False
        try: return all(0 <= int(chunk) <= 255 for chunk in chunks)
        except ValueError: return False

    # ip str 2 int trasposition
    # ip: 192.168.1.1
    # 1) 0 << 8 | 192 -> 11000000
    # 2) 11000000 << 8 | 168 -> 11000000 10101000
    # 3) 11000000 10101000 << 8 | 1 -> 11000000 10101000 00000001
    # 4) 11000000 10101000 00000001 << 8 | 1 -> 11000000 10101000 00000001 00000001
    @staticmethod
    def _str2int(ip):
        assert ipv4._validatestr(ip), f'Invalid {str} ip'
        return reduce(lambda a, b: a << 8 | b, (int(chunk) for chunk in ip.split('.')))

    # ip str 2 int trasposition
    # ip: 11000000 10101000 00000001 00000001
    # 1) ip >> 24 & 11111111 -> 11000000 -> 192
    # 2) ip >> 16 & 11111111 -> 10101000 -> 168
    # 3) ip >> 8  & 11111111 -> 00000001 -> 1
    # 3) ip >> 0  & 11111111 -> 00000001 -> 1
    @staticmethod
    def _int2str(ip):
        assert ipv4._validateint(ip), f'Invalid {int} ip'
        return '.'.join(str(ip >> n & 0xFF) for n in [24, 16, 8, 0])

    # Input type matching, store data
    def __init__(self, ip):
        if type(ip) is int:
            assert ipv4._validateint(ip), f'Invalid {int} ip'
            self.ip = ip
        elif type(ip) is str: self.ip = ipv4._str2int(ip)
        else: raise Exception(f'Only {int} and {str} allowed')

    # ------------------- Op overloader ------------------- #
    def __str__(self): return ipv4._int2str(self.ip)        #
    def __int__(self): return self.ip                       #
                                                            #
    def __invert__(self): return ~self.ip                   #
                                                            #
    def __and__(self, other): return self.ip & other        #   
    def __rand__(self, other): return self.ip & other       #
                                                            #
    def __or__(self, other): return self.ip | other         #
    def __ror__(self, other): return self.ip | other        #
                                                            #
    def __xor__(self, other): return self.ip ^ other        #
    def __rxor__(self, other): return self.ip ^ other       #
                                                            #
    def __lshift__(self, other): return self.ip << other    #
    def __rlshift__(self, other): return self.ip << other   #
                                                            #
    def __rshift__(self, other): return self.ip >> other    #
    def __rrshift__(self, other): return self.ip >> other   #
    # ----------------------------------------------------- #

class ipv4_mask(ipv4):

    # Masks must pass bin regex \1+0+\
    # TODO refactor, ugly
    @staticmethod
    def _validateipv4mask(mask):
        bmask = bin(mask)[2:]
        bmask_ones = bin(mask >> (bmask.count('0')))[2:]
        return len(bmask_ones) == bmask_ones.count('1')

    # Validate ip inn both:
    # a) a.b.c.d | 0 <= a, b, c, d <= 255
    # b) n | 0 <= n <= 32
    @staticmethod
    def _validatestr(mask):
        assert type(mask) is str, f'Only {str} mask allowed'
        chunks = mask.split('.')
        if len(chunks) == 4:
            try: return all(0 <= int(chunk) <= 255 for chunk in chunks)
            except ValueError: return False
        elif len(chunks) == 1:
            try: return 0 <= int(chunks[0]) <= 32
            except ValueError: return False
        else: return False

    # mask str 2 int transposing overload
    # works both for a.b.c.d and n forms
    # a.b.c.d -> as ipv4
    # n -> '1'*n + '0'*(32 - n)
    # ex n = 24 -> '1' * 24 + '0' * 8 -> 11111111111111111111111100000000
    @staticmethod
    def _str2int(mask):
        assert ipv4_mask._validatestr(mask), f'Invalid {str} mask'
        if mask.count('.') == 0: return int('1' * int(mask) + '0' * (32 - int(mask)), 2)    # TODO refactor, ugly
        else: return reduce(lambda a, b: a << 8 | b, (int(chunk) for chunk in mask.split('.')))

    # Input tye matching, store data, ipv4 bacward compatibility
    def __init__(self, mask):
        if type(mask) is int:
            assert ipv4._validateint(mask), f'Invalid {int} ip'
            self.mask = mask
        elif type(mask) is str: self.mask = ipv4_mask._str2int(mask)
        else: raise Exception(f'Only {int} and {str} allowed')
        assert ipv4_mask._validateipv4mask(self.mask), f'Invalid mask {self.mask}'

        # Backward compatibility with ipv4
        self.ip = self.mask

    # :OwO:
    def __str__(self): return '\\' + str(bin(self.ip).count('1'))
