# Now... with functions!
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg: {arg1}")

def print_none():
    print(f"I got nothin'")

# Now, run thru the functions...
print_two("Ray", "Hightower")
print_two_again("Ray", "Hightower")
print_one("First!")
print_none()
