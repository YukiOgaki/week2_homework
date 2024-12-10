from db_config import Message


# 全データを確認する関数
def display_all_message():
    messages = Message.select()
    for message in messages:
        print(f"Name: {message.user} Age: {message.age}")


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
            name = input("New user name > ")
            age = int(input("New user age > "))
            print(f"Add new user: {name}")
            Message.create(user=name, age=age)
            continue

        if message == "Q":
            print("Bye!")
            break

        if message not in ("S", "A", "Q"):
            print(f"{message}: command not found")
            continue


if __name__ == "__main__":
    main()
