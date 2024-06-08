connection = True
paid = False
internet = False
online = True

def go_online():
    if not connection:
        print("No connection...")
        return

    elif not paid:
        print("User has not paid...")
        return

    elif not internet:
        print("No internet...")
        return

    elif not online:
        print("You are offline...")
        return

    print("You are online!")

go_online()