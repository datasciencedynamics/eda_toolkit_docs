.. _getting_started:   

Welcome to the EDA Toolkit Python Library Documentation!
========================================================
.. note::
   This documentation is for ``eda_toolkit`` version ``0.0.24``.


The ``eda_toolkit`` is a comprehensive library designed to streamline and 
enhance the process of Exploratory Data Analysis (EDA) for data scientists, 
analysts, and researchers. This toolkit provides a suite of functions and 
utilities that facilitate the initial investigation of datasets, enabling users 
to quickly gain insights, identify patterns, and uncover underlying structures 
in their data.

Project Links
---------------

1. .. raw:: html

      <a href="https://pypi.org/project/eda_toolkit/" target="_blank" rel="noopener noreferrer">
        PyPI Page
      </a>

2. .. raw:: html

      <a href="https://github.com/lshpaner/eda_toolkit" target="_blank" rel="noopener noreferrer">
        GitHub Repository
      </a>

3. .. raw:: html

      <a href="https://colab.research.google.com/drive/1vg2mdR1aH60olgofjGXbWo2hOM3M_E1n" target="_blank" rel="noopener noreferrer">
        Comprehensive Google Colab Notebook (End-to-End Examples)
      </a>


.. tip::
   A comprehensive Google Colab notebook is linked below that walks through
   nearly everything discussed in this documentation, including data loading,
   cleaning, visualization, and reporting workflows using the ``eda_toolkit``.
   This notebook is designed as a practical, end-to-end companion to the documentation
   and can be run entirely in the browser without any local setup.

   .. raw:: html

      <a href="https://colab.research.google.com/drive/1vg2mdR1aH60olgofjGXbWo2hOM3M_E1n"
         target="_blank" rel="noopener noreferrer">
         Open the Google Colab notebook
      </a>



What is EDA?
-------------

Exploratory Data Analysis (EDA) is a crucial step in the data science workflow. 
It involves various techniques to summarize the main characteristics of the data, 
often with visual methods. EDA helps in understanding the data better, identifying 
anomalies, discovering patterns, and forming hypotheses. This process is essential 
before applying any machine learning models, as it ensures the quality and relevance 
of the data.


Purpose of EDA Toolkit
-----------------------
The ``eda_toolkit`` library is a comprehensive suite of tools designed to 
streamline and automate many of the tasks associated with Exploratory Data 
Analysis (EDA). It offers a broad range of functionalities, including:

- **Data Management:** Tools for managing directories, generating unique IDs, 
  standardizing dates, and handling common DataFrame manipulations.
- **Data Cleaning:** Functions to address missing values, remove outliers, and 
  correct formatting issues, ensuring data is ready for analysis.
- **Data Visualization:** A variety of plotting functions, including KDE 
  distribution plots, stacked bar plots, scatter plots with optional best fit 
  lines, and box/violin plots, to visually explore data distributions, 
  relationships, and trends.
- **Descriptive and Summary Statistics:** Methods to generate comprehensive 
  reports on data types, summary statistics (mean, median, standard deviation, 
  etc.), and to summarize all possible combinations of specified variables.
- **Reporting and Export:** Features to save DataFrames to Excel with 
  customizable formatting, create contingency tables, and export generated 
  plots in multiple formats.
 


Key Features
-------------

- **Ease of Use:** The toolkit is designed with simplicity in mind, offering intuitive and easy-to-use functions.  
- **Customizable:** Users can customize various aspects of the toolkit to fit their specific needs.  
- **Integration:** Seamlessly integrates with popular data science libraries such as ``Pandas``, ``NumPy``, ``Matplotlib``, and ``Seaborn``.  
- **Documentation and Examples:** Comprehensive documentation and examples to help users get started quickly and effectively.  


Prerequisites
--------------

Before you install ``eda_toolkit``, ensure your system meets the following requirements:

- ``Python``: Version ``3.8`` or higher.

Additionally, ``eda_toolkit`` depends on the following packages, which will be automatically installed when you install ``eda_toolkit``:

- ``jinja2``: version ``3.0.0`` or higher
- ``matplotlib``: version ``3.5.3`` or higher, but capped at ``3.9.2``
- ``nbformat``: version ``4.2.0`` or higher, but capped at ``5.10.4``
- ``numpy``: version ``1.21.6`` or higher, but capped at ``2.1.2``
- ``pandas``: version ``1.3.5`` or higher, but capped at ``2.2.3``
- ``plotly``: version ``5.18.0`` or higher, but capped at ``5.24.1``
- ``scikit-learn``: version ``1.0.2`` or higher
- ``scipy``: version ``1.7.3`` or higher
- ``seaborn``: version ``0.12.2`` or higher, but capped at ``0.13.2``
- ``tqdm``: version ``4.66.4`` or higher
- ``xlsxwriter``: version ``3.2.0`` (exact version required)

Installation
--------------

You can install ``eda_toolkit`` directly from PyPI:

.. code-block:: bash

    pip install eda_toolkit


Description
===============

This guide provides detailed instructions and examples for using the functions 
provided in the ``eda_toolkit`` library and how to use them effectively in your projects.

For most of the ensuing examples, we will leverage the Census Income Data (1994) from
the UCI Machine Learning Repository [#]_. This dataset provides a rich source of
information for demonstrating the functionalities of the ``eda_toolkit``.

.. [#] Kohavi, R. (1996). *Census Income*. UCI Machine Learning Repository. `https://doi.org/10.24432/C5GP7S <https://doi.org/10.24432/C5GP7S>`_.

