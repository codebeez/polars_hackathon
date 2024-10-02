# Codebeez Polars Hackathon

This time we dive into Polars, a powerful DataFrame Python library with a highly efficient, multi-threaded implementation in Rust in using Apache Arrow.
It has support for SQL syntax as well as native Python syntax and, while very efficient and complete on its own, plays well together with Pandas and DuckDB for nearly seamless conversion between data structures from and to the other libraries.
Not only are we excited about the benchmarks that show significant performance improvements with respect to Pandas, and to a lesser extent DuckDB, but we also love the intuitive Python syntax in comparison.

That is not all, as we will also cover a basic machine learning (or, more specifically, deep learning) use case
Namely, after our exploration of the Polars library, we will put it to the test in a fun practical use case for preprocessing our data efficiently in order to train a neural network.

## Install environment

If poetry is installed on your system, you can simply install the project through the command `poetry install --no-root`.
Otherwise, you can set up your environment using the `requirements.txt` file.