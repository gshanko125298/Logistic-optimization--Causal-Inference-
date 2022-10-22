## Datashader

    Datashader is a graphics pipeline system for creating meaningful representations of large datasets quickly and flexibly. Datashader breaks the creation of images into a series of explicit steps that allow computations to be done on intermediate representations. This approach allows accurate and effective visualizations to be produced automaticallywithout trial-and-error parameter tuning, and also makes it simple for data scientists to focus on particular data and relationships of interest in a principled way.

    The computation-intensive steps in this process are written in ordinary Python but transparently compiled to machine code using Numba and flexibly distributed across CPU cores and processors using Dask or GPUs using CUDA. This approach provides a highly optimized rendering pipeline that makes it practical to work with extremely large datasets even on standard hardware, while exploiting distributed and GPU systems when available.

Installation

Datashader supports Python 3.7, 3.8, 3.9 and 3.10 on Linux, Windows, or Mac and can be installed with conda:

    conda install datashader

or with pip:

    pip install datashader

For the best performance, we recommend using conda so that you are sure to get numerical libraries optimized for your platform. The latest releases are available on the pyviz channel conda install -c pyviz datashader and the latest pre-release versions are available on the dev-labeled channel conda install -c pyviz/label/dev datashader. Fetching Examples

Once you’ve installed datashader as above you can fetch the examples:

datashader examples
    cd datashader-examples

This will create a new directory called datashader-examples with all the data needed to run the examples.

To run all the examples you will need some extra dependencies. If you installed datashader within a conda environment, with that environment active run:

    conda env update --file environment.yml

Otherwise create a new environment:

conda env create --name datashader --file environment.yml

    conda activate datashader
## Usage

Detailed Datashader documentation is contained in the User Guide, and the Topics pages show examples of what you can do with Datashader. But to get started quickly, check out the introductory guide sections in order; it should take around 1 hour in total.

    1. Introduction Simple self-contained example to show how Datashader works.

    2. Pipeline Detailed step-by-step explanation how Datashader turns your data into an image.

    3. Interactivity Embedding images into rich, interactive plots in a web browser.

This web page was generated from a Jupyter notebook and not all interactivity will work on this website. Right click to download and run locally for full Python-backed interactivity.

    1 Introduction
    2 Pipeline
    3 Interactivity

