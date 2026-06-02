"""Hints for ex_02

    class Range:
        def __init__(self, *args):
            if len(args) == 1:
                self.start = 0
                self.stop = args[0]
                self.step = 1
            elif len(args) == 2:
                self.start = args[0]
                self.stop = args[1]
                self.step = 1
            elif len(args) == 3:
                self.start = args[0]
                self.stop = args[1]
                self.step = args[2]

        def __iter__(self):
            self.current = self.start
            return self

        def __next__(self):
            if self.step > 0 and self.current >= self.stop:
                raise StopIteration
            if self.step < 0 and self.current <= self.stop:
                raise StopIteration
            result = self.current
            self.current += self.step
            return result
"""
