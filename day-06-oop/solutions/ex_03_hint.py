"""Hints for ex_03

    class Person:
        def __init__(self, name):
            self.name = name
            self.friends = set()

        def add_friend(self, other):
            self.friends.add(other)
            other.friends.add(self)

        def friends_of_friends(self):
            result = set()
            for f in self.friends:
                for fof in f.friends:
                    if fof is not self and fof not in self.friends:
                        result.add(fof)
            return result

        def __str__(self):
            friends_names = [f.name for f in self.friends]
            return f"{self.name}: {', '.join(friends_names) if friends_names else 'no friends'}"

        def __repr__(self):
            return self.name
"""
