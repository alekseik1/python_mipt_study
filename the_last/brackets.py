class SmileChecker:

    s = ''

    def append_smile(self, smile):
        self.s += smile

    def __get_rid_of_these_fucking_smiles(self):
        ready = ''
        for i in self.s:
            if i == '[' or i == ']' or i == '{' or i == '}' or i == '(' or i == ')':
                ready += i
        #print(ready)
        return ready

    def brackets_check(self, s):
        m1 = 0
        m2 = 0
        m3 = 0
        for c in s:
            if c == '(':
                m1 += 1
            elif c == ')':
                m1 -= 1
                if m1 < 0:
                    return False
            elif c == '[':
                m2 += 1
            elif c == ']':
                m2 -= 1
                if m2 < 0:
                    return False
            elif c == '{':
                m3 += 1
            elif c == '}':
                m3 -= 1
                if m3 < 0:
                    return False
        return m1 == 0 and m2 == 0 and m3 == 0

    def check_correct(self):
        return self.brackets_check(self.__get_rid_of_these_fucking_smiles())
