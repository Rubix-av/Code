import timeit

def traditional_loop():
    x = []
    for i in range(1_000_000):
        x.append(i**2)
    return x

def comprehension():
    return [i**2 for i in range(1_000_000)]

class Timer:
    def __init__(self):
        self.start = None
        self.end = None

    def __enter__(self):
        self.start = timeit.default_timer()
        return self

    def __exit__(self, *args):
        self.end = timeit.default_timer()
        self.interval = self.end - self.start

# Time the traditional loop
with Timer() as t:
    traditional_loop()
print(f'Traditional loop time: {t.interval:.5f} seconds')

# Time the list comprehension
with Timer() as t:
    comprehension()
print(f'Comprehension time: {t.interval:.5f} seconds')
