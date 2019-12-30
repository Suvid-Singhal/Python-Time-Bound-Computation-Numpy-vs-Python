# Numpy vs Python for Matrix Multiplication
The code in this repository demonstrates that Numpy is way fater than Normal Python for mathematical computation (especially Matrix Multiplication)
## Running the code produces the following graph
This graph is a comparision between time taken by Numpy and Nowmal Python code in multiplying 2 matrices. X axis shows Value of n (no. of rows and colums of a randomly generated matrix) whereas the Y axis shows time taken in seconds.

![alt Plot](https://github.com/Suvid-Singhal/Python-Time-Bound-Computation-Numpy-vs-Python/blob/master/plot.png)
## Instructions to Run
Run the following commands in order to run the code
```bash
git clone https://github.com/Suvid-Singhal/Python-Time-Bound-Computation-Numpy-vs-Python.git
cd Python-Time-Bound-Computation-Numpy-vs-Python
python3 run.py
```

## Conclusion

After seeing the result, we can conclude that Numpy is way faster than Normal Python for complex mathematical calculations. But let us now see why Numpy is faster than Normal Python.

## Why Numpy is faster?

NumPy is written (mostly) in C which is a low-level language, makes it very fast. It hides all this complexity under an easy to use module of Python.

Looping over lists in Python is slow because the language itself is dynamically typed. This means that you do not have to specify a variables data type but every time Python uses a variable it has to check data type. Even though Python is also written in C, this bookkeeping makes it much slower than other low-level languages.

Operations in Numpy are much faster because they take advantage of parallelism (which is the case of Single Instruction Multiple Data (SIMD)), while traditional for loop can't make use of it.


Credits: https://www.datadiscuss.com/proof-that-numpy-is-much-faster-than-normal-python-array/
