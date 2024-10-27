from decorator  import do_twice


# @do_twice
# def say_whee():
#     print("Whee!")

# @do_twice
# def greet(name):
#     print(f"Hello {name}")

# say_whee()


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

# return_greeting("Ridwan")

x = return_greeting("Ridwan")
print(x)