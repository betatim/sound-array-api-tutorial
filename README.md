# Tutorial: learning array API with sound

This is a tutorial in which you will learn about the [array API](https://data-apis.org/array-api/latest/).
It uses sound and sound effects as examples to illustrate how to write code
that works with array inputs from array API compatible libraries such as
Numpy, CuPy, PyTorch, etc.

The target audience are people who want to write libraries or code that is agnostic
to the type of the input arrays.

The tutorial will not make you a master sound effects engineer. Sorry.


## Preliminaries

We will use [Google colab](https://colab.research.google.com/). This gives
you an environment with a GPU and minimal setup. To use it you will need a
Google account (create one if you don't already have one).


## Notebooks

You should be able to run the notebooks for this tutorial on Google's Colab.
We recommend using it because it has (almost all) the required libraries and
it gives you access to a CUDA GPU.

Click the links below to open each of the notebooks:

1. [Array API](https://colab.research.google.com/github/betatim/sound-array-api-tutorial/blob/main/01%20-%20array%20api.ipynb) - introduction to why we need the array API
1. [Sound](https://colab.research.google.com/github/betatim/sound-array-api-tutorial/blob/main/02%20-%20sound.ipynb) - introduction to sound
1. [Sound effects](https://colab.research.google.com/github/betatim/sound-array-api-tutorial/blob/main/03%20-%20sound%20effects.ipynb) - creating a simple sound effect
1. [Testing](https://colab.research.google.com/github/betatim/sound-array-api-tutorial/blob/main/04%20-%20simple%20testing.ipynb) - testing array API compatible code