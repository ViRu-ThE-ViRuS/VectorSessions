# Numpy Arrays
The default `list` data structure/data type in python lacks functionality and efficiency. Thus, the few remaining people of the world came up with solutions to this with libraries like `numpy` which provide a much more efficient, high level and useful interface to deal with the array data structure.


Numpy is one of the most widely used library for matrix math in the world with high level frameworks like Tensorflow and NLTK using it (just to mention a few). 


### Installation
- run `pip install numpy` in your console/command prompt/terminal after install python and pip.

### Useful functionality
- `numpy.arange` -> function which generates and returns a numpy array containing integers from 0 till the number passed a parameter.

- `numpy.empty` -> function which generates and returns a new numpy array without initializing entries.

- `numpy.zeros` -> function which generates and returns a new numpy array filled with zeros.

- `numpy.array` -> function which converts and returns the passed list, into a numpy array.

- `numpy.linspace` -> function which generates and returns a new numpy array filled with linearly spaced `n` values between the start and end point passed as parameters. `n` is also passed as a parameter.

- `numpy.append(<array appending to>, <object that you're appending>` -> function that populates an array. Just like the .append function like in python. 

#### functions over an existing numpy array:
 - ndarray`.reshape` -> change the dimentionality/shape of the array
 - ndarray`.ndim` -> get the dimensions of the array
 - ndarray`.shape` -> get the shape of the array
 - ndarray`.size` -> get the number of elements in the array
 - ndarray`.dtype` -> get the datatype of the elements of the array
 - ndarray`.data` -> get the buffer containing the acutal elements of the array

### Useful Resources and Links:
- [Quick Tutorial](https://www.youtube.com/watch?v=8JfDAm9y_7s)
- [Official Documentation](https://docs.scipy.org/doc/numpy-1.13.0/reference/index.html)
- [Quick Start](https://docs.scipy.org/doc/numpy-1.13.0/user/quickstart.html)   
- Make sure you're checking the documentation when you can't remember the exact syntax for the above. 
