import time

from fastapi import FastAPI
from pydantic import BaseModel
import numpy

app = FastAPI()
np = numpy

@app.get('/')
async def root():
    return {"message": "Hello World"}

@app.post('/quicksort')
async def quicksort(a: list):
    start = time.perf_counter()
    array = sort_array(np.array(a))
    stop = time.perf_counter()
    return {
        "sorted_array": str(array),
        "time": stop - start
    }

@app.post('/mergesort')
async def mergesort(a: list):
    start = time.perf_counter()
    array = sort_array(np.array(a), 'mergesort')
    stop = time.perf_counter()
    return {
        "sorted_array": str(array),
        "time": stop - start
    }

@app.post('/heapsort')
async def heapsort(a: list):
    start = time.perf_counter()
    array = sort_array(np.array(a), 'heapsort')
    stop = time.perf_counter()
    return {
        "sorted_array": str(array),
        "time": stop - start
    }

@app.post('/stablesort')
async def stablesort(a: list):
    start = time.perf_counter()
    array = sort_array(np.array(a), 'stable')
    stop = time.perf_counter()
    return {
        "sorted_array": str(array),
        "time": stop - start
    }

def sort_array(array, sort_type = None):
    print(array)
    return np.sort(array, kind=sort_type)