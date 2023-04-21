class Code():
    count = 1

    def __init__(self, code):
        self.id = Code.count
        self.code = code
        Code.count += 1

    def __str__(self):
        return f"({self.id}) {self.code}"

    def __repr__(self):
        return self.__str__();
    
    def __eq__(self, other):
        return self.code == other.code
