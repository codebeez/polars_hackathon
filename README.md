# Codebeez Polars Hackathon

This time we dive into Polars, a powerful DataFrame Python library with a highly efficient, multi-threaded implementation in Rust in using Apache Arrow.
It has support for SQL syntax as well as native Python syntax and, while very efficient and complete on its own, plays well together with Pandas and DuckDB for nearly seamless conversion between data structures from and to the other libraries.
Not only are we excited about the benchmarks that show significant performance improvements with respect to Pandas, and to a lesser extent DuckDB, but we also love the intuitive Python syntax in comparison.

That is not all, as we will also cover a basic machine learning (or, more specifically, deep learning) use case
Namely, after our exploration of the Polars library, we will put it to the test in a fun practical use case for preprocessing our data efficiently in order to train a neural network.

## Set up environment
In order to set up the environment, you can simply use the Docker image that facilitates the setup.
For VSCode, there is also a Dev container that you can use through the "Dev Containers" extension.
If you are using PyCharm or another IDE, you will have to configure the Docker interpreter in some other way.
Pay attention that in that case you will also have to run "poetry install" within the Docker container as soon as it's running.

## Exercises
There are five logical parts to this workshop, each defined in its own Jupyter notebook and with its own exercises:

1 - Exploring Polars
2 - Data Analysis
3 - Pandas to Polars
4 - Lazy Loading Evaluation
5 - Sentiment Prediction

The parts are sort of set up from easy to harder, with a case of training a neural network at the end.
If you are already familiar with Polars, you might want to skip through the first part very quickly, which is meant to introduce you to the very basics.
