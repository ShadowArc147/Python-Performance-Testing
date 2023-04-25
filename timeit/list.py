import timeit



#Since the list comprehension is a single line, we can pass it directly to timeit. This doesn’t affect the performance; it just illustrates two ways to pass code for testing. So, it seems like the list comprehension is faster.

if __name__ == "__main__":
    timings = timeit.timeit('[(a, b) for a in (1, 3, 5, 7, 9, 11) for b in (2, 4, 6, 8, 10, 12)]')
    print(timings)

    