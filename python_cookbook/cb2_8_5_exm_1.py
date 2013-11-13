def __testTrace():
    secretOfUniverse = 42
    watch(secretOfUniverse)
if __name__ == "__main__":
    a = "something else"
    watch(a)
    __testTrace()
    trace("This line was executed!")
    raw("Just some raw text...")
