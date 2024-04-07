class SuperStr(str):
    def __init__(self, string):
        self.string = string

    def is_repeatanse(self, s):
        if not s:
            return False
        repeat = len(self.string)// len(s)
        return self.string == repeat * s

    def is_palindrom(self):
        return self.string.lower() == self.string[::-1].lower()


check_string = SuperStr("abaaba")
print(check_string.is_repeatanse("asjcsa"))
print(check_string.is_repeatanse("aba"))
print(check_string.is_palindrom())
