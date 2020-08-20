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
    array, time = sort_array(np.array(a))
    return {
        "sorted_array": str(array),
        "time": time
    }

@app.post('/mergesort')
async def mergesort(a: list):
    array, time = sort_array(np.array(a), 'mergesort')
    return {
        "sorted_array": str(array),
        "time": time
    }

@app.post('/heapsort')
async def heapsort(a: list):
    array, time = sort_array(np.array(a), 'heapsort')
    return {
        "sorted_array": str(array),
        "time": time
    }

@app.post('/stablesort')
async def stablesort(a: list):
    array, time = sort_array(np.array(a), 'stable')
    return {
        "sorted_array": str(array),
        "time": time
    }

def sort_array(array, sort_type = None):
    start = time.perf_counter()
    a = np.sort(array, kind=sort_type)
    stop = time.perf_counter()
    return a, stop - start