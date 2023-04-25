import timeit

test_code = '''
output = []
for a in (1, 3, 5, 7, 9, 11):
    for b in (2, 4, 6, 8, 10, 12):
        output.append((a, b))
'''

#We start by importing the module. Then we need to save the code under test in a string so we can pass it to timeit. Using a heredoc instead of formatting it on one line makes it easier to read the code.

#Then we pass it to the timeit method.

#Timeit executed the code one million times and returned the time, in seconds, it took to execute them.


if __name__ == "__main__":
    timings = timeit.timeit(test_code)
    print(timings)