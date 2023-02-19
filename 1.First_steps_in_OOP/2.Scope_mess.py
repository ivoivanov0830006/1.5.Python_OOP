x = "global"


def outer():
    x = "local"

    def inner():
        nonlocal x          # added
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x            # added
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()


print(x)
outer()
print(x)

"""
------------------------------------ Problem to resolve --------------------------------

Fix the code below, so it returns the expected output:

x = "global"


def outer():
    x = "local"

    def inner():
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()


print(x)
outer()
print(x)
-------------------------------------- Example inputs ----------------------------------
Current Output	
global
outer: local
inner: nonlocal
outer: local
global	
Expected Output
global
outer: local
inner: nonlocal
outer: nonlocal
global: changed!

"""
