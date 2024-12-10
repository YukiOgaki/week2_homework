from db_config import User


# 全データを確認する関数
def display_all_message():
    for user in User.select():
        print(f"Name: {user.user} Age: {user.age}")


# 新規データを登録する関数
def create():
    name = input("New user name > ")
    age = int(input("New user age > "))
    print(f"Add new user: {name}")
    User.create(user=name, age=age)


print(
    """
===== Welcome to CRM Application =====
[S]how: Show all users info
[A]dd: Add new user
[Q]uit: Quit The Application
======================================
"""
)


def main():
    message = ""
    while True:
        message = input("\nYour command > ")

        if message == "S":
            display_all_message()
            continue

        if message == "A":
            create()
            continue

        if message == "Q":
            print("Bye!")
            break

        if message not in ("S", "A", "Q"):
            print(f"{message}: command not found")
            continue


if __name__ == "__main__":
    main()
