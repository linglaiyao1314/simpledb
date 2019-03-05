class Type:
    STRING_LEN = 128

    @classmethod
    def get_len(cls):
        """"""


class IntType(Type):
    @classmethod
    def get_len(cls):
        return 4


class StringType(Type):
    @classmethod
    def get_len(cls):
        return cls.STRING_LEN + 4

