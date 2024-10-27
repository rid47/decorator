from decorator  import debug


# @do_twice
# def say_whee():
#     print("Whee!")

# @do_twice
# def greet(name):
#     print(f"Hello {name}")

# say_whee()


# @do_twice
# def return_greeting(name):
#     print("Creating greeting")
#     return f"Hi {name}"

# # return_greeting("Ridwan")

# x = return_greeting("Ridwan")
# print(x)


### timer decorator test

# @timer
# def waste_some_time(num_times):
#     for _ in range(num_times):
#         sum([number**2 for number in range(10_000)])
#         # print()


# waste_some_time(1)
# waste_some_time(100)

# for data in range (10_000):
#     print(data)


### debug decorator test
@debug
def make_greeting(name,age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you're growing up!"
    


make_greeting("Ridwan")
make_greeting("Ridwan",33)