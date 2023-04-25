import cProfile

test_code = '''
for a in range(3000000):
    output = []
    for a in (1, 3, 5, 7, 9, 11):
        for b in (2, 4, 6, 8, 10, 12):
            output.append((a, b))
'''



#cProfile’s output has six columns:

#ncalls - the number of times this function was called tottime - the total time spent in this function, excluding sub-functions. percall - tottime / ncalls cumtime - the total tie spent in this function including sub-functions. percall - cumtime / primitive calls filename:lineno(function) - function name and location

#Note that cProfile lists the functions by name, not by time or the order that the test code called them. So, our test ran for about 12 seconds, and it spent 9.4 creating strings and 2.8 in list’s append function.



if __name__ == "__main__":
    cProfile.run(test_code)