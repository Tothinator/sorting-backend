import time

from fastapi import FastAPI
import numpy

app = FastAPI()
np = numpy

a = np.array([4, 5, 2, 1, 3])

@app.get('/')
async def root():
    return {"message": "Hello World"}

@app.get('/quicksort')
async def sort():
    start = time.perf_counter()
    array = sort_array(a)
    stop = time.perf_counter()
    return {
        "sorted_array": str(array),
        "time": stop - start
    }

@app.get('/mergesort')
async def sort():
    start = time.perf_counter()
    array = sort_array(a, 'mergesort')
    stop = time.perf_counter()
    return {
        "sorted_array": str(array),
        "time": stop - start
    }

@app.get('/heapsort')
async def sort():
    start = time.perf_counter()
    array = sort_array(a, 'heapsort')
    stop = time.perf_counter()
    return {
        "sorted_array": str(array),
        "time": stop - start
    }

@app.get('/stablesort')
async def sort():
    start = time.perf_counter()
    array = sort_array(a, 'stable')
    stop = time.perf_counter()
    return {
        "sorted_array": str(array),
        "time": stop - start
    }

def sort_array(array, sort_type = None):
    return np.sort(array, kind=sort_type)