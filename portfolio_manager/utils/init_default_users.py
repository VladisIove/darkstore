from routers.user.models import User


async def init_default_users() -> None:
    default_users = ["admin", "John Doe"]
    usernames = await User.filter(name__in=default_users).values_list("name", flat=True)
    not_exists_usernames = set(default_users) - set(usernames)

    users = []
    for username in not_exists_usernames:
        users.append(User(name=username))

    if users:
        await User.bulk_create(users)
