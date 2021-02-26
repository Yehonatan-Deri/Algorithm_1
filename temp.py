from typing import NewType

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
