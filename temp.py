from typing import NewType
import numpy as np

UserId = NewType('UserId', int)
some_id = UserId(524313)
ProUserId = NewType('ProUserId', UserId)
some_ProUserId = ProUserId(some_id)


def get_user_name(user_id: UserId):
    print(user_id)
    print(type(user_id))


get_user_name(some_id)
get_user_name(7)
get_user_name(some_ProUserId)
# w: list = []

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(np.array(a)[])
from Algorithm_1.graph.distance import *

# _init([],9)
d = {"a": 1, "b": 2, 'c': 3, 'd': 4}
d1 = {'e': 6}
d2 = {**d, **d1}
print(d2)
for x in d2:
    print(type(x))
a = np.array([6, 7, 8, 9, 0, 0])

print(a[a > 0])
a = [6, 7, 8, 9, 0, 0]
print(a[4 == 9])
