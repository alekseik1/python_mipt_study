class SmileChecker:
    def __init__(self):
        self.stack = []

    def append_smile(self, a):
        self.stack.append(a)

    def check_correct(self):
        left = [':-(', ':-[', ':-{', ':-<']
        right = [':-)', ':-]', ':-}', ':->']
        pair = dict(zip(right, left))
        res = []
        for bracket in self.stack:
            if bracket in left:
                res.append(bracket)
            elif bracket in right:
                if len(res) == 0:
                    return False
                if res[-1] != pair[bracket]:
                    return False
                else:
                    res.pop()
        if len(res) == 0:
            return True
        else:
            return False
