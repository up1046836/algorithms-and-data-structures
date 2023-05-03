class Pair():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, other):
        return (self.a == other.a and self.b == other.b) or (self.a == other.b and self.b == other.a)

    def __str__(self):
        red = "\033[1;31;40m"
        normal = "\033[0;37;40m"

        code1 = self.a
        code2 = self.b
        code1_str = ""
        code2_str = ""

        for char1, char2 in zip(code1.code, code2.code):
            if char1 == char2:
                code1_str += normal + char1
                code2_str += normal + char2
            else:
                code1_str += red + char1
                code2_str += red + char2

        code1_str += normal
        code2_str += normal
        return f"({code1.id}) {code1_str} ({code2.id}) {code2_str}"

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        if self.a.code < self.b.code:
            return hash(self.a.code + self.b.code)
        else:
            return hash(self.b.code + self.a.code)
