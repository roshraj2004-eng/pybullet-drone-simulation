while True:
    cmd = input("Command (w/a/s/d/q/e/x): ").lower()

    with open("cmd.txt", "w") as f:
        f.write(cmd)
