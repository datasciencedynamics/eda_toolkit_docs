.. _data_management:   

.. _target-link:

.. raw:: html

   <div class="no-click">

.. image:: ../assets/eda_toolkit_logo.svg
   :alt: EDA Toolkit Logo
   :align: left
   :width: 300px

.. raw:: html

   </div>

.. raw:: html
   
   <div style="height: 100px;"></div>

Data Management Overview
===========================

In any data-driven project, effective management of data is crucial. This 
section provides essential techniques for handling and preparing data to ensure 
consistency, accuracy, and ease of analysis. From directory setup and data 
cleaning to advanced data processing, these methods form the backbone of reliable 
data management. Dive into the following topics to enhance your data handling 
capabilities and streamline your workflow.

Data Management Techniques
===============================

Path directories
------------------

**Ensure that the directory exists. If not, create it.**

.. function:: ensure_directory(path)

    :param path: The path to the directory that needs to be ensured.
    :type path: str

    :returns: None


The ``ensure_directory`` function is a utility designed to facilitate the 
management of directory paths within your project. When working with data 
science projects, it is common to save and load data, images, and other 
artifacts from specific directories. This function helps in making sure that 
these directories exist before any read/write operations are performed. If 
the specified directory does not exist, the function creates it. If it 
already exists, it does nothing, thus preventing any errors related to 
missing directories.


**Implementation Example**

In the example below, we demonstrate how to use the ``ensure_directory`` function 
to verify and create directories as needed. This example sets up paths for data and 
image directories, ensuring they exist before performing any operations that depend on them.

First, we define the base path as the parent directory of the current directory. 
The ``os.pardir`` constant, equivalent to ``"..""``, is used to navigate up one 
directory level. Then, we define paths for the data directory and data output 
directory, both located one level up from the current directory. 


Next, we set paths for the PNG and SVG image directories, located within an 
``images`` folder in the parent directory. Using the ``ensure_directory`` 
function, we then verify that these directories exist. If any of the specified 
directories do not exist, the function creates them.

.. code-block:: python

    from eda_toolkit import ensure_directory 
    import os # import operating system for dir
    

    base_path = os.path.join(os.pardir)

    # Go up one level from 'notebooks' to parent directory, 
    # then into the 'data' folder
    data_path = os.path.join(os.pardir, "data")
    data_output = os.path.join(os.pardir, "data_output")

    # create image paths
    image_path_png = os.path.join(base_path, "images", "png_images")
    image_path_svg = os.path.join(base_path, "images", "svg_images")

    # Use the function to ensure'data' directory exists
    ensure_directory(data_path)
    ensure_directory(data_output)
    ensure_directory(image_path_png)
    ensure_directory(image_path_svg)

**Output**

.. code-block:: python

    Created directory: ../data
    Created directory: ../data_output
    Created directory: ../images/png_images
    Created directory: ../images/svg_images


.. _Adding_Unique_Identifiers:

Reading CSV Files with Progress Bar
------------------------------------

.. function:: read_csv_with_progress(file_path, nrows=None, chunksize=10000, low_memory=False, **kwargs)

   Read a CSV file in chunks with a ``tqdm`` progress bar. Optionally
   limit the number of rows read and pass any additional keyword arguments
   directly to ``pandas.read_csv``.

   :param file_path: Path to the CSV file.
   :type file_path: str

   :param nrows: If specified, limits the number of rows read.
   :type nrows: int, optional

   :param chunksize: Number of rows per chunk. Default is ``10,000``.
   :type chunksize: int, optional

   :param low_memory: If ``False``, disables mixed-type inference for
      better dtype consistency at the cost of higher memory usage.
      Default is ``False``.
   :type low_memory: bool, optional

   :param kwargs: Additional keyword arguments passed to
      ``pandas.read_csv`` (e.g. ``sep``, ``encoding``, ``usecols``,
      ``dtype``, ``skiprows``). Note that ``chunksize`` cannot be passed
      via ``kwargs``; use the explicit parameter instead.

   :returns: DataFrame containing the read data.
   :rtype: pandas.DataFrame

   :raises ValueError: If ``chunksize`` is passed via ``kwargs``.

Example
^^^^^^^

.. code-block:: python

   from eda_toolkit import read_csv_with_progress

   # Basic read
   df = read_csv_with_progress("data/adult_income.csv")

   # Limit rows and pass kwargs
   df = read_csv_with_progress(
       "data/adult_income.csv",
       nrows=10000,
       chunksize=2000,
       usecols=["age", "education", "income"],
       dtype={"age": float},
   )

**Output**

.. code-block:: text

    Reading ../data/adult_income.csv: 100%|██████████| 48842/48842 [00:00<00:00, 922518.72line/s]
    Reading ../data/adult_income.csv: 100%|██████████| 10000/10000 [00:00<00:00, 948594.17line/s]

.. note::

      This function is particularly useful when working with large CSV files
      where a standard ``pandas.read_csv`` call gives no feedback on progress.
      The ``tqdm`` progress bar updates in real time as each chunk is read,
      giving a clear indication of how much of the file has been processed
      and how long remains, especially valuable in notebook environments
      where long-running cells provide no visual feedback by default.
      
Adding Unique Identifiers
--------------------------

**Add a column of unique IDs with a specified number of digits to the DataFrame.**

.. function:: add_ids(df, id_colname="ID", num_digits=9, seed=None, set_as_index=False)

    :param df: The DataFrame to which IDs will be added.
    :type df: pd.DataFrame
    :param id_colname: The name of the new column for the unique IDs. Defaults to ``"ID"``.
    :type id_colname: str, optional
    :param num_digits: The number of digits for the unique IDs. Defaults to ``9``. The first digit will always be non-zero to ensure proper formatting.
    :type num_digits: int, optional
    :param seed: The seed for the random number generator to ensure reproducibility. Defaults to ``None``.
    :type seed: int, optional
    :param set_as_index: If ``True``, the generated ID column will replace the existing index of the DataFrame. Defaults to ``False``.
    :type set_as_index: bool, optional

    :returns: The updated DataFrame with a new column of unique IDs. If ``set_as_index`` is ``True``, the new ID column replaces the existing index.
    :rtype: pd.DataFrame

    :raises ValueError: If the number of rows in the DataFrame exceeds the pool of possible unique IDs for the specified ``num_digits``.

.. admonition:: Notes

    - The function ensures all IDs are unique by resolving potential collisions during generation, even for large datasets.
    - The total pool size of unique IDs is determined by :math:`9 \times 10^{(\text{num\_digits} - 1)}`, since the first digit must be non-zero.
    - Warnings are printed if the number of rows in the DataFrame approaches the pool size of possible unique IDs, recommending increasing ``num_digits``.
    - If ``set_as_index`` is ``False``, the ID column will be added as the first column in the DataFrame.
    - Setting a random seed ensures reproducibility of the generated IDs.

The ``add_ids`` function is used to append a column of unique identifiers with a 
specified number of digits to a given dataframe. This is particularly useful for 
creating unique patient or record IDs in datasets. The function allows you to 
specify a custom column name for the IDs, the number of digits for each ID, and 
optionally set a seed for the random number generator to ensure reproducibility. 
Additionally, you can choose whether to set the new ID column as the index of the 
dataframe.

**Implementation Example**

In the example below, we demonstrate how to use the ``add_ids`` function to add a 
column of unique IDs to a dataframe. We start by importing the necessary libraries 
and creating a sample dataframe. We then use the ``add_ids`` function to generate 
and append a column of unique IDs with a specified number of digits to the dataframe.

First, we import the pandas library and the ``add_ids`` function from the ``eda_toolkit``. 
Then, we create a sample dataframe with some data. We call the ``add_ids`` function, 
specifying the dataframe, the column name for the IDs, the number of digits for 
each ID, a seed for reproducibility, and whether to set the new ID column as the 
index. The function generates unique IDs for each row and adds them as the first 
column in the dataframe.

.. code-block:: python

    from eda_toolkit import add_ids

    # Add a column of unique IDs with 9 digits and call it "census_id"
    df = add_ids(
        df=df,
        id_colname="census_id",
        num_digits=9,
        seed=111,
        set_as_index=True, 
    )

**Output**

`First 5 Rows of Census Income Data (Adapted from Kohavi, 1996, UCI Machine Learning Repository)` [1]_

.. code-block:: bash

    DataFrame index is unique.

.. raw:: html

    <style type="text/css">
    .tg-wrap {
      width: 100%;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
    }
    .tg  {border-collapse:collapse;border-spacing:0;margin:0px auto;}
    .tg td{border-color:black;border-style:solid;border-width:1px;font-family:monospace, sans-serif;font-size:11px;
      overflow:hidden;padding:0px 5px;word-break:normal;}
    .tg th{border-color:black;border-style:solid;border-width:1px;font-family:monospace, sans-serif;font-size:11px;
      font-weight:normal;overflow:hidden;padding:0px 5px;word-break:normal;}
    .tg .tg-zv4m{border-color:#ffffff;text-align:left;vertical-align:top}
    .tg .tg-8jgo{border-color:#ffffff;text-align:center;vertical-align:top}
    .tg .tg-aw21{border-color:#ffffff;font-weight:bold;text-align:center;vertical-align:top}
    </style>
    <div class="tg-wrap">
    <table class="tg">
      <thead>
        <tr>
          <th class="tg-zv4m"></th>
          <th class="tg-aw21">age</th>
          <th class="tg-aw21">workclass</th>
          <th class="tg-aw21">fnlwgt</th>
          <th class="tg-aw21">education</th>
          <th class="tg-aw21">education-num</th>
          <th class="tg-aw21">marital-status</th>
          <th class="tg-aw21">occupation</th>
          <th class="tg-aw21">relationship</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="tg-aw21">census_id</td>
          <td class="tg-8jgo"></td>
          <td class="tg-8jgo"></td>
          <td class="tg-8jgo"></td>
          <td class="tg-8jgo"></td>
          <td class="tg-8jgo"></td>
          <td class="tg-8jgo"></td>
          <td class="tg-8jgo"></td>
          <td class="tg-8jgo"></td>
        </tr>
        <tr>
          <td class="tg-zv4m">582248222</td>
          <td class="tg-8jgo">39</td>
          <td class="tg-8jgo">State-gov</td>
          <td class="tg-8jgo">77516</td>
          <td class="tg-8jgo">Bachelors</td>
          <td class="tg-8jgo">13</td>
          <td class="tg-8jgo">Never-married</td>
          <td class="tg-8jgo">Adm-clerical</td>
          <td class="tg-8jgo">Not-in-family</td>
        </tr>
        <tr>
          <td class="tg-zv4m">561810758</td>
          <td class="tg-8jgo">50</td>
          <td class="tg-8jgo">Self-emp-not-inc</td>
          <td class="tg-8jgo">83311</td>
          <td class="tg-8jgo">Bachelors</td>
          <td class="tg-8jgo">13</td>
          <td class="tg-8jgo">Married-civ-spouse</td>
          <td class="tg-8jgo">Exec-managerial</td>
          <td class="tg-8jgo">Husband</td>
        </tr>
        <tr>
          <td class="tg-zv4m">598098459</td>
          <td class="tg-8jgo">38</td>
          <td class="tg-8jgo">Private</td>
          <td class="tg-8jgo">215646</td>
          <td class="tg-8jgo">HS-grad</td>
          <td class="tg-8jgo">9</td>
          <td class="tg-8jgo">Divorced</td>
          <td class="tg-8jgo">Handlers-cleaners</td>
          <td class="tg-8jgo">Not-in-family</td>
        </tr>
        <tr>
          <td class="tg-zv4m">776705221</td>
          <td class="tg-8jgo">53</td>
          <td class="tg-8jgo">Private</td>
          <td class="tg-8jgo">234721</td>
          <td class="tg-8jgo">11th</td>
          <td class="tg-8jgo">7</td>
          <td class="tg-8jgo">Married-civ-spouse</td>
          <td class="tg-8jgo">Handlers-cleaners</td>
          <td class="tg-8jgo">Husband</td>
        </tr>
        <tr>
          <td class="tg-zv4m">479262902</td>
          <td class="tg-8jgo">28</td>
          <td class="tg-8jgo">Private</td>
          <td class="tg-8jgo">338409</td>
          <td class="tg-8jgo">Bachelors</td>
          <td class="tg-8jgo">13</td>
          <td class="tg-8jgo">Married-civ-spouse</td>
          <td class="tg-8jgo">Prof-specialty</td>
          <td class="tg-8jgo">Wife</td>
        </tr>
      </tbody>
    </table>
    </div>


\


Trailing Period Removal
-------------------------

**Strip the trailing period from values in a specified column of a DataFrame, if present.**

.. function:: strip_trailing_period(df, column_name)

    :param df: The DataFrame containing the column to be processed.
    :type df: pd.DataFrame
    :param column_name: The name of the column containing values with potential trailing periods.
    :type column_name: str

    :returns: The updated DataFrame with trailing periods removed from the specified column.
    :rtype: pd.DataFrame

    :raises ValueError: If the specified ``column_name`` does not exist in the DataFrame, pandas will raise a ``ValueError``.

.. admonition:: Notes:

    - For string values, trailing periods are stripped directly.
    - For numeric values represented as strings (e.g., ``"1234."``), the trailing period is removed, and the value is converted back to a numeric type if possible.
    - ``NaN`` values are preserved and remain unprocessed.
    - Non-string and non-numeric types are returned as-is.


The ``strip_trailing_period`` function is designed to remove trailing periods 
from float values in a specified column of a DataFrame. This can be particularly 
useful when dealing with data that has been inconsistently formatted, ensuring 
that all float values are correctly represented.


**Implementation Example**

In the example below, we demonstrate how to use the ``strip_trailing_period`` function to clean a 
column in a DataFrame. We start by importing the necessary libraries and creating a sample DataFrame. 
We then use the ``strip_trailing_period`` function to remove any trailing periods from the specified column.

.. code-block:: python

    from eda_toolkit import strip_trailing_period

    # Create a sample dataframe with trailing periods in some values
    data = {
        "values": [1.0, 2.0, 3.0, 4.0, 5.0, 6.],
    }
    df = pd.DataFrame(data)

    # Remove trailing periods from the 'values' column
    df = strip_trailing_period(df=df, column_name="values")


**Output**

`First 6 Rows of Data Before and After Removing Trailing Periods (Adapted from Example)`

.. raw:: html

    <table>
        <tr>
            <td style="padding-right: 10px; font-family: Arial; font-size: 14px;">

                <strong>Before:</strong>

                <table border="1" style="width: 150px; text-align: center; font-family: Arial; font-size: 14px;">
                    <tr>
                        <th>Index</th>
                        <th>Value</th>
                    </tr>
                    <tr>
                        <td>0</td>
                        <td>1.0</td>
                    </tr>
                    <tr>
                        <td>1</td>
                        <td>2.0</td>
                    </tr>
                    <tr>
                        <td>2</td>
                        <td>3.0</td>
                    </tr>
                    <tr>
                        <td>3</td>
                        <td>4.0</td>
                    </tr>
                    <tr>
                        <td>4</td>
                        <td>5.0</td>
                    </tr>
                    <tr style="background-color: #FFCCCC;">
                        <td>5</td>
                        <td>6.</td>
                    </tr>
                </table>

            </td>
            <td style="padding-left: 10px; font-family: Arial; font-size: 14px;">

                <strong>After:</strong>

                <table border="1" style="width: 150px; text-align: center; font-family: Arial; font-size: 14px;">
                    <tr>
                        <th>Index</th>
                        <th>Value</th>
                    </tr>
                    <tr>
                        <td>0</td>
                        <td>1.0</td>
                    </tr>
                    <tr>
                        <td>1</td>
                        <td>2.0</td>
                    </tr>
                    <tr>
                        <td>2</td>
                        <td>3.0</td>
                    </tr>
                    <tr>
                        <td>3</td>
                        <td>4.0</td>
                    </tr>
                    <tr>
                        <td>4</td>
                        <td>5.0</td>
                    </tr>
                    <tr style="background-color: #FFCCCC;">
                        <td>5</td>
                        <td>6.0</td>
                    </tr>
                </table>

            </td>
        </tr>
    </table>


\

.. note:: 
    
    The last row shows 6 as an ``int`` with a trailing period with its conversion to ``float``.


\

Standardized Dates
-------------------

**Parse and standardize date strings based on the provided rule.**

.. function:: parse_date_with_rule(date_str)

    This function takes a date string and standardizes it to the ``ISO 8601`` format
    (``YYYY-MM-DD``). It assumes dates are provided in either **day/month/year** or
    **month/day/year** format. The function first checks if the first part of the
    date string (day or month) is greater than 12, which unambiguously indicates
    a **day/month/year** format. If the first part is 12 or less, the function
    attempts to parse the date as **month/day/year**, falling back to **day/month/year**
    if the former raises a ``ValueError`` due to an impossible date (e.g., month
    being greater than 12).

    :param date_str: A date string to be standardized.
    :type date_str: str

    :returns: A standardized date string in the format ``YYYY-MM-DD``.
    :rtype: str

    :raises ValueError: If ``date_str`` is in an unrecognized format or if the function
                        cannot parse the date.


**Implementation Example**

In the example below, we demonstrate how to use the ``parse_date_with_rule`` 
function to standardize date strings. We start by importing the necessary library 
and creating a sample list of date strings. We then use the ``parse_date_with_rule`` 
function to parse and standardize each date string to the ``ISO 8601`` format.

.. code-block:: python

    from eda_toolkit import parse_date_with_rule

    date_strings = ["15/04/2021", "04/15/2021", "01/12/2020", "12/01/2020"]

    standardized_dates = [parse_date_with_rule(date) for date in date_strings]

    print(standardized_dates)

**Output**

.. code-block:: python

    ['2021-04-15', '2021-04-15', '2020-12-01', '2020-01-12']



.. important:: 
    
    In the next example, we demonstrate how to apply the ``parse_date_with_rule`` 
    function to a DataFrame column containing date strings using the ``.apply()`` method. 
    This is particularly useful when you need to standardize date formats across an 
    entire column in a DataFrame.

.. code-block:: python

    # Creating the DataFrame
    data = {
        "date_column": [
            "31/12/2021",
            "01/01/2022",
            "12/31/2021",
            "13/02/2022",
            "07/04/2022",
        ],
        "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "amount": [100.0, 150.5, 200.75, 250.25, 300.0],
    }

    df = pd.DataFrame(data)

    # Apply the function to the DataFrame column
    df["standardized_date"] = df["date_column"].apply(parse_date_with_rule)

    print(df)

**Output**

.. code-block:: text

       date_column     name  amount standardized_date
    0   31/12/2021    Alice  100.00        2021-12-31
    1   01/01/2022      Bob  150.50        2022-01-01
    2   12/31/2021  Charlie  200.75        2021-12-31
    3   13/02/2022    David  250.25        2022-02-13
    4   07/04/2022      Eve  300.00        2022-04-07

Outlier Detection
-------------------

For a theoretical treatment of the Z-score, IQR, and Isolation Forest methods, 
including the underlying formulas and a side-by-side comparison see
:ref:`outlier_detection_theory`.
 
.. function:: detect_outliers(df, features=None, method="iqr", threshold=1.5, contamination=0.05, return_mask=False, return_bounds=False, flag_col=None, groupby=None, verbose=False)
 
   Detect outliers in numeric columns of a DataFrame using IQR, Z-score,
   or Isolation Forest methods. Returns a summary DataFrame with outlier
   counts, percentages, and bounds per feature.
 
   :param df: Input DataFrame to analyze for outliers.
   :type df: pandas.DataFrame
 
   :param features: List of numeric column names to check. If ``None``,
      all numeric columns are used.
   :type features: list of str, optional
 
   :param method: Outlier detection method. Options are ``"iqr"``,
      ``"zscore"``, or ``"isoforest"``.
   :type method: str, optional
 
   :param threshold: IQR multiplier (e.g. ``1.5`` for Tukey fences,
      ``3.0`` for extreme outliers) or absolute Z-score cutoff.
      Ignored when ``method="isoforest"``.
   :type threshold: float, optional
 
   :param contamination: Expected proportion of outliers. Only used when
      ``method="isoforest"``. Must be between 0 and 0.5.
   :type contamination: float, optional
 
   :param return_mask: If ``True``, also returns a boolean DataFrame
      aligned to the input where ``True`` indicates an outlier.
   :type return_mask: bool, optional
 
   :param return_bounds: If ``True``, also returns a dictionary mapping
      each feature to a ``(lower_bound, upper_bound)`` tuple. Bounds are
      ``"N/A"`` when ``method="isoforest"``. Values can be passed directly
      to :func:`data_doctor` as ``lower_cutoff`` / ``upper_cutoff``.
   :type return_bounds: bool, optional
 
   :param flag_col: If provided, adds a boolean column with this name to
      ``df`` (in place) that is ``True`` for any row where at least one
      feature is flagged as an outlier.
   :type flag_col: str, optional
 
   :param groupby: If provided, outlier detection is performed within each
      group of this column rather than across the full dataset.
   :type groupby: str, optional
 
   :param verbose: If ``True``, prints a formatted ASCII summary report
      to the console. When no structured returns are requested, the
      function returns ``None`` to suppress Jupyter auto-display.
   :type verbose: bool, optional
 
   :returns:
      - Default: summary ``DataFrame`` with columns ``Variable``,
        ``Outlier (n)``, ``Outlier (%)``, ``Lower Bound``, ``Upper Bound``
      - ``return_mask=True``: ``(summary, mask)``
      - ``return_bounds=True``: ``(summary, bounds)``
      - ``return_mask=True, return_bounds=True``: ``(summary, mask, bounds)``
      - ``verbose=True`` with no other return flags: ``None``
 
   :rtype: pandas.DataFrame or tuple or None
 
   :raises ValueError: If ``method`` is not one of ``"iqr"``,
      ``"zscore"``, or ``"isoforest"``.
   :raises ValueError: If ``threshold`` is not a positive number.
   :raises ValueError: If ``contamination`` is not between 0 and 0.5.
   :raises ValueError: If ``groupby`` column is not found in the DataFrame.
   :raises ValueError: If no numeric features are found.
 
   .. note::
 
      - Rows with ``NaN`` in a feature are excluded from detection and
        never flagged as outliers.
      - When ``groupby`` is specified, bounds are computed per group.
        This is particularly useful for clinical datasets where
        distributions differ meaningfully by cohort or age group.
      - Use ``Lower Bound`` and ``Upper Bound`` from the summary or the
        ``bounds`` dict directly as inputs to :func:`data_doctor` for
        feature-level transformation and treatment.

.. rubric:: Implementation Examples
    :class: rubric-large

Example 1: Basic IQR outlier detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
 
   from eda_toolkit import detect_outliers
 
   summary = detect_outliers(
       df,
       features=["age", "capital-gain", "hours-per-week"],
       method="iqr",
       threshold=1.5,
   )
   print(summary)
 

**Output**

.. code-block:: text

            Variable  Outlier (n)  Outlier (%)  Lower Bound  Upper Bound
    0  hours-per-week        13496        27.63         32.5         52.5
    1    capital-gain         4035         8.26          0.0          0.0
    2             age          216         0.44         -2.0         78.0

 
Example 2: Within-group detection using ``groupby``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
 
   summary = detect_outliers(
       df,
       features=["age", "hours-per-week"],
       method="iqr",
       groupby="education",
   )
   print(summary)

**Output**

.. code-block:: text

            Variable  Outlier (n)  Outlier (%)  Lower Bound  Upper Bound
    0  hours-per-week        11282        23.10        -10.0         77.5
    1             age          239         0.49        -23.0        101.0

Example 3: Z-Score Outlier Detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Z-score method flags observations that deviate from the mean by more
than a specified number of standard deviations. 

.. code-block:: python

    print("Z-score: threshold=3.0")
    summary_z = detect_outliers(
        df,
        features=numeric_features,
        method="zscore",
        threshold=3.0,
    )
    print(summary_z.to_string(index=False))


**Output**

.. code-block:: text

    Z-score: threshold=3.0
          Variable  Outlier (n)  Outlier (%)  Lower Bound  Upper Bound
      capital-loss         2216         4.54   -1121.5113    1296.5160
    hours-per-week          681         1.39       3.2481      77.5967
            fnlwgt          506         1.04 -127147.9417  506476.2109
      capital-gain          331         0.68  -21276.9895   23435.1248
     education-num          330         0.68       2.3652      17.7910
               age          186         0.38      -2.4879      79.7751


Example 4: Isolation Forest Outlier Detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    print("Isolation Forest: contamination=0.05")
    summary_iso = detect_outliers(
        df,
        features=numeric_features,
        method="isoforest",
        contamination=0.05,
    )
    print(summary_iso.to_string(index=False))

**Output**

.. code-block:: text   

    Isolation Forest: contamination=0.05
         Variable  Outlier (n)  Outlier (%) Lower Bound Upper Bound
              age         2443          5.0         N/A         N/A
           fnlwgt         2443          5.0         N/A         N/A
    education-num         2443          5.0         N/A         N/A
     capital-gain         2443          5.0         N/A         N/A
     capital-loss         2443          5.0         N/A         N/A
   hours-per-week         2443          5.0         N/A         N/A

Example 5: Verbose ASCII Summary Report
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setting ``verbose=True`` prints a formatted ASCII summary report directly
to the console, showing the detection method, total rows, and per-feature
outlier counts, percentages, and bounds. When no structured return flags
are set, the function returns ``None`` to suppress Jupyter auto-display —
the ASCII report is the sole output.

.. code-block:: python

   detect_outliers(
       df,
       features=numeric_features,
       method="iqr",
       threshold=1.5,
       verbose=True,
   )

**Output**

.. code-block:: text

                  OUTLIER DETECTION SUMMARY REPORT
   +------------------------+------------------------------------------+
   | Method                 | IQR (threshold=1.5)                      |
   | Total rows             | 48,842                                   |
   +------------------------+--------------+--------------+----------------+----------------+
   | Variable               |  Outlier (n) |  Outlier (%) |    Lower Bound |    Upper Bound |
   +------------------------+--------------+--------------+----------------+----------------+
   | hours-per-week         |       13,496 |        27.63 |        32.5000 |        52.5000 |
   | capital-gain           |        4,035 |         8.26 |         0.0000 |         0.0000 |
   | capital-loss           |        2,282 |         4.67 |         0.0000 |         0.0000 |
   | education-num          |        1,794 |         3.67 |         4.5000 |        16.5000 |
   | fnlwgt                 |        1,453 |         2.97 |   -62,586.7500 |   417,779.2500 |
   | age                    |          216 |         0.44 |        -2.0000 |        78.0000 |
   +------------------------+--------------+--------------+----------------+----------------+

   Total flagged rows (any feature): 20,284 (41.53%)


Example 6: Return Bounds for Downstream Use in ``data_doctor``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setting ``return_bounds=True`` returns a dictionary mapping each feature
to a ``(lower_bound, upper_bound)`` tuple alongside the summary DataFrame.
The bounds can be passed directly to :func:`data_doctor` as
``lower_cutoff`` and ``upper_cutoff``, creating a seamless workflow from
outlier detection to feature-level treatment.

.. code-block:: python

   summary_b, bounds = detect_outliers(
       df,
       features=numeric_features,
       method="iqr",
       return_bounds=True,
   )

   print("  Bounds per feature:")
   for feat, (lower, upper) in bounds.items():
       print(f"    {feat:<20} lower={lower:>10}  upper={upper:>10}")

   print("\n  Example: pass capital-gain bounds directly to data_doctor:")
   print(f"    lower_cutoff={bounds['capital-gain'][0]}")
   print(f"    upper_cutoff={bounds['capital-gain'][1]}")

**Output**

.. code-block:: text

   [12] return_bounds=True — bounds dict for downstream data_doctor use
     Bounds per feature:
       age                  lower=      -2.0  upper=      78.0
       fnlwgt               lower=  -62586.75  upper=  417779.25
       education-num        lower=       4.5  upper=      16.5
       capital-gain         lower=       0.0  upper=       0.0
       capital-loss         lower=       0.0  upper=       0.0
       hours-per-week       lower=      32.5  upper=      52.5

     Example: pass capital-gain bounds directly to data_doctor:
       lower_cutoff=0.0
       upper_cutoff=0.0



DataFrame Analysis
-------------------

**Analyze DataFrame columns, including data type, null values, and unique value counts.**

The ``dataframe_profiler`` function provides a comprehensive summary of a DataFrame's columns, including information on data types, null values, unique values, and the most frequent values. It can output either a plain DataFrame for further processing or a styled DataFrame for visual presentation in Jupyter environments.

.. function:: dataframe_profiler(df, background_color=None, return_df=False, sort_cols_alpha=False)

    :param df: The DataFrame to analyze.
    :type df: pandas.DataFrame
    :param background_color: Hex color code or color name for background styling in the output 
                             DataFrame. Applies to specific columns, such as unique value totals 
                             and percentages. Defaults to ``None``.
    :type background_color: str, optional
    :param return_df: If ``True``, returns the plain DataFrame with summary statistics. If ``False``, 
                      returns a styled DataFrame for visual presentation. Defaults to ``False``.
    :type return_df: bool, optional
    :param sort_cols_alpha: If ``True``, sorts the DataFrame columns alphabetically in the output. 
                            Defaults to ``False``.
    :type sort_cols_alpha: bool, optional

    :returns: 
        - If ``return_df`` is ``True`` or running in a terminal environment, returns the plain 
          DataFrame containing column summary statistics.
        - If ``return_df`` is ``False`` and running in a Jupyter Notebook, returns a styled 
          DataFrame with optional background styling.
    :rtype: pandas.DataFrame
    :raises ValueError: If the DataFrame is empty or contains no columns.

.. admonition:: Notes

    - Automatically detects whether the function is running in a Jupyter Notebook or terminal and adjusts the output accordingly.
    - In Jupyter environments, uses Pandas' Styler for visual presentation. If the installed Pandas version does not support ``hide``, falls back to ``hide_index``.
    - Utilizes a ``tqdm`` progress bar to show the status of column processing.
    - Preprocesses columns to handle NaN values and replaces empty strings with Pandas' ``pd.NA`` for consistency.


.. rubric:: Implementation Examples
    :class: rubric-large

Census Income Example
^^^^^^^^^^^^^^^^^^^^^^

In the example below, we demonstrate how to use the ``dataframe_profiler`` 
function to analyze a DataFrame's columns. 

.. code-block:: python

    from eda_toolkit import dataframe_profiler

    dataframe_profiler(df=df)


**Output**

`Result on Census Income Data (Adapted from Kohavi, 1996, UCI Machine Learning Repository)` [1]_

.. code-block:: text

    Shape:  (48842, 15) 

    Processing columns: 100%|██████████| 15/15 [00:00<00:00, 74.38it/s]

    Total seconds of processing time: 0.351102

.. raw:: html

    <style type="text/css">
    .tg-wrap {
    width: 100%;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    }
    .tg  {border:none;border-collapse:collapse;border-spacing:0;margin:0px auto;}
    .tg td{border-style:solid;border-width:0px;font-family:Consolas, monospace;font-size:11px;overflow:hidden;padding:0px 6px;
    word-break:normal;}
    .tg th{border-style:solid;border-width:0px;font-family:Consolas, monospace;font-size:11px;font-weight:normal;
    overflow:hidden;padding:0px 6px;word-break:normal;}
    .tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
    .tg .tg-dvpl{border-color:inherit;text-align:right;vertical-align:top}
    .tg .tg-rvpl{border-color:inherit;text-align:right;vertical-align:top}
    </style>
    <div class="tg-wrap">
    <table class="tg">
        <thead>
        <tr>
            <th class="tg-rvpl"></th>
            <th class="tg-rvpl"><span style="font-weight:bold">column</span></th>
            <th class="tg-rvpl"><span style="font-weight:bold">dtype</span></th>
            <th class="tg-0pky"><span style="font-weight:bold">null_total</span></th>
            <th class="tg-0pky"><span style="font-weight:bold">null_pct</span></th>
            <th class="tg-0pky"><span style="font-weight:bold">unique_values_total</span></th>
            <th class="tg-0pky"><span style="font-weight:bold">max_unique_value</span></th>
            <th class="tg-0pky"><span style="font-weight:bold">max_unique_value_total</span></th>
            <th class="tg-0pky"><span style="font-weight:bold">max_unique_value_pct</span></th>
        </tr>
        </thead>
        <tbody>
        <tr>
            <td class="tg-rvpl">0</td>
            <td class="tg-dvpl">age</td>
            <td class="tg-dvpl">int64</td>
            <td class="tg-dvpl">0</td>
            <td class="tg-dvpl">0.00</td>
            <td class="tg-dvpl">74</td>
            <td class="tg-dvpl">36</td>
            <td class="tg-dvpl">1348</td>
            <td class="tg-dvpl">2.76</td>
        </tr>
        <tr>
            <td class="tg-rvpl">1</td>
            <td class="tg-dvpl">workclass</td>
            <td class="tg-dvpl">object</td>
            <td class="tg-dvpl">963</td>
            <td class="tg-dvpl">1.97</td>
            <td class="tg-dvpl">9</td>
            <td class="tg-dvpl">Private</td>
            <td class="tg-dvpl">33906</td>
            <td class="tg-dvpl">69.42</td>
        </tr>
        <tr>
            <td class="tg-rvpl">2</td>
            <td class="tg-dvpl">fnlwgt</td>
            <td class="tg-dvpl">int64</td>
            <td class="tg-dvpl">0</td>
            <td class="tg-dvpl">0.00</td>
            <td class="tg-dvpl">28523</td>
            <td class="tg-dvpl">203488</td>
            <td class="tg-dvpl">21</td>
            <td class="tg-dvpl">0.04</td>
        </tr>
        <tr>
            <td class="tg-rvpl">3</td>
            <td class="tg-dvpl">education</td>
            <td class="tg-dvpl">object</td>
            <td class="tg-dvpl">0</td>
            <td class="tg-dvpl">0.00</td>
            <td class="tg-dvpl">16</td>
            <td class="tg-dvpl">HS-grad</td>
            <td class="tg-dvpl">15784</td>
            <td class="tg-dvpl">32.32</td>
        </tr>
        <tr>
            <td class="tg-rvpl">4</td>
            <td class="tg-dvpl">education-num</td>
            <td class="tg-dvpl">int64</td>
            <td class="tg-dvpl">0</td>
            <td class="tg-dvpl">0.00</td>
            <td class="tg-dvpl">16</td>
            <td class="tg-dvpl">9</td>
            <td class="tg-dvpl">15784</td>
            <td class="tg-dvpl">32.32</td>
        </tr>
        <tr>
            <td class="tg-rvpl">5</td>
            <td class="tg-dvpl">marital-status</td>
            <td class="tg-dvpl">object</td>
            <td class="tg-dvpl">0</td>
            <td class="tg-dvpl">0.00</td>
            <td class="tg-dvpl">7</td>
            <td class="tg-dvpl">Married-civ-spouse</td>
            <td class="tg-dvpl">22379</td>
            <td class="tg-dvpl">45.82</td>
        </tr>
        <tr>
            <td class="tg-rvpl">6</td>
            <td class="tg-dvpl">occupation</td>
            <td class="tg-dvpl">object</td>
            <td class="tg-dvpl">966</td>
            <td class="tg-dvpl">1.98</td>
            <td class="tg-dvpl">15</td>
            <td class="tg-dvpl">Prof-specialty</td>
            <td class="tg-dvpl">6172</td>
            <td class="tg-dvpl">12.64</td>
        </tr>
        <tr>
            <td class="tg-rvpl">7</td>
            <td class="tg-dvpl">relationship</td>
            <td class="tg-dvpl">object</td>
            <td class="tg-dvpl">0</td>
            <td class="tg-dvpl">0.00</td>
            <td class="tg-dvpl">6</td>
            <td class="tg-dvpl">Husband</td>
            <td class="tg-dvpl">19716</td>
            <td class="tg-dvpl">40.37</td>
        </tr>
        <tr>
            <td class="tg-rvpl">8</td>
            <td class="tg-dvpl">race</td>
            <td class="tg-dvpl">object</td>
            <td class="tg-dvpl">0</td>
            <td class="tg-dvpl">0.00</td>
            <td class="tg-dvpl">5</td>
            <td class="tg-dvpl">White</td>
            <td class="tg-dvpl">41762</td>
            <td class="tg-dvpl">85.50</td>
        </tr>
        <tr>
            <td class="tg-rvpl">9</td>
            <td class="tg-dvpl">sex</td>
            <td class="tg-dvpl">object</td>
            <td class="tg-dvpl">0</td>
            <td class="tg-dvpl">0.00</td>
            <td class="tg-dvpl">2</td>
            <td class="tg-dvpl">Male</td>
            <td class="tg-dvpl">32650</td>
            <td class="tg-dvpl">66.85</td>
        </tr>
        <tr>
            <td class="tg-rvpl">10</td>
            <td class="tg-dvpl">capital-gain</td>
            <td class="tg-dvpl">int64</td>
            <td class="tg-dvpl">0</td>
            <td class="tg-dvpl">0.00</td>
            <td class="tg-dvpl">123</td>
            <td class="tg-dvpl">0</td>
            <td class="tg-dvpl">44807</td>
            <td class="tg-dvpl">91.74</td>
        </tr>
        <tr>
            <td class="tg-rvpl">11</td>
            <td class="tg-dvpl">capital-loss</td>
            <td class="tg-dvpl">int64</td>
            <td class="tg-dvpl">0</td>
            <td class="tg-dvpl">0.00</td>
            <td class="tg-dvpl">99</td>
            <td class="tg-dvpl">0</td>
            <td class="tg-dvpl">46560</td>
            <td class="tg-dvpl">95.33</td>
        </tr>
        <tr>
            <td class="tg-rvpl">12</td>
            <td class="tg-dvpl">hours-per-week</td>
            <td class="tg-dvpl">int64</td>
            <td class="tg-dvpl">0</td>
            <td class="tg-dvpl">0.00</td>
            <td class="tg-dvpl">96</td>
            <td class="tg-dvpl">40</td>
            <td class="tg-dvpl">22803</td>
            <td class="tg-dvpl">46.69</td>
        </tr>
        <tr>
            <td class="tg-rvpl">13</td>
            <td class="tg-dvpl">native-country</td>
            <td class="tg-dvpl">object</td>
            <td class="tg-dvpl">274</td>
            <td class="tg-dvpl">0.56</td>
            <td class="tg-dvpl">42</td>
            <td class="tg-dvpl">United-States</td>
            <td class="tg-dvpl">43832</td>
            <td class="tg-dvpl">89.74</td>
        </tr>
        <tr>
            <td class="tg-rvpl">14</td>
            <td class="tg-dvpl">income</td>
            <td class="tg-dvpl">object</td>
            <td class="tg-dvpl">0</td>
            <td class="tg-dvpl">0.00</td>
            <td class="tg-dvpl">4</td>
            <td class="tg-dvpl">&lt;=50K</td>
            <td class="tg-dvpl">24720</td>
            <td class="tg-dvpl">50.61</td>
        </tr>
        </tbody>
    </table>
    </div>

\


DataFrame Column Names
^^^^^^^^^^^^^^^^^^^^^^^^^

``unique_values_total``
    This column indicates the total number of unique values present in each column of the DataFrame. It measures the distinct values that a column holds. For example, in the ``age`` column, there are 74 unique values, meaning the ages vary across 74 distinct entries.

``max_unique_value``
    This column shows the most frequently occurring value in each column. For example, in the ``workclass`` column, the most common value is ``Private``, indicating that this employment type is the most represented in the dataset. For numeric columns like ``capital-gain`` and ``capital-loss``, the most common value is ``0``, which suggests that the majority of individuals have no capital gain or loss.

``max_unique_value_total``
    This represents the count of the most frequently occurring value in each column. For instance, in the ``native-country`` column, the value ``United-States`` appears ``43,832`` times, indicating that the majority of individuals in the dataset are from the United States.

``max_unique_value_pct``
    This column shows the percentage that the most frequent value constitutes of the total number of rows. For example, in the ``race`` column, the value ``White`` makes up ``85.5%`` of the data, suggesting a significant majority of the dataset belongs to this racial group.

Calculation Details
^^^^^^^^^^^^^^^^^^^^^^^^^

- ``unique_values_total`` is calculated using the ``nunique()`` function, which counts the number of unique values in a column.
- ``max_unique_value`` is determined by finding the value with the highest frequency using ``value_counts()``. For string columns, any missing values (if present) are replaced with the string ``"null"`` before computing the frequency.
- ``max_unique_value_total`` is the frequency count of the ``max_unique_value``.
- ``max_unique_value_pct`` is the percentage of ``max_unique_value_total`` divided by the total number of rows in the DataFrame, providing an idea of how dominant the most frequent value is.

This analysis helps in identifying columns with a high proportion of dominant values, like ``<=50K`` in the ``income`` column, which appears ``24,720`` times, making up ``50.61%`` of the entries. This insight can be useful for understanding data distributions, identifying potential data imbalances, or even spotting opportunities for feature engineering in further data processing steps.

Generating Summary Tables for Variable Combinations
-----------------------------------------------------
**Generate and save summary tables for all possible combinations of specified variables in a DataFrame to an Excel file, complete with formatting and progress tracking.**

.. function:: summarize_all_combinations(df, variables, data_path, data_name, min_length=2)

    Generate summary tables for all possible combinations of the specified variables in the DataFrame and save them to an Excel file with a Table of Contents.

    :param df: The pandas DataFrame containing the data.
    :type df: pandas.DataFrame

    :param variables: List of column names from the DataFrame to generate combinations.
    :type variables: list of str

    :param data_path: Directory path where the output Excel file will be saved.
    :type data_path: str

    :param data_name: Name of the output Excel file.
    :type data_name: str

    :param min_length: Minimum size of the combinations to generate. Defaults to ``2``.
    :type min_length: int, optional

    :returns: A tuple containing:
              - A dictionary where keys are tuples of column names (combinations) and values are the corresponding summary DataFrames.
              - A list of all generated combinations, where each combination is represented as a tuple of column names.
    :rtype: tuple(dict, list)

.. admonition:: Notes

    - **Excel Output**:
        - Each combination is saved as a separate sheet in an Excel file.
        - A "Table of Contents" sheet is created with hyperlinks to each combination's summary table.
        - Sheet names are truncated to 31 characters to meet Excel's constraints.
    - **Formatting**:
        - Headers in all sheets are bold, left-aligned, and borderless.
        - Columns are auto-fitted to content length for improved readability.
        - A left-aligned format is applied to all columns in the output.
    - The function uses ``tqdm`` progress bars for tracking:
        - Combination generation.
        - Writing the Table of Contents.
        - Writing individual summary tables to Excel.

**The function returns two outputs**:

    1. ``summary_tables``: A dictionary where each key is a tuple representing a combination 
    of variables, and each value is a DataFrame containing the summary table for that combination. 
    Each summary table includes the count and proportion of occurrences for each unique combination of values.

    2. ``all_combinations``: A list of all generated combinations of the specified variables. 
    This is useful for understanding which combinations were analyzed and included in the summary tables.

**Implementation Example**

Below, we use the ``summarize_all_combinations`` function to generate summary tables for the specified 
variables from a DataFrame containing the census data [1]_.

.. note:: 

    Before proceeding with any further examples in this documentation, ensure that the ``age`` variable is binned into a new variable, ``age_group``.  
    Detailed instructions for this process can be found under :ref:`Binning Numerical Columns <Binning_Numerical_Columns>`.


.. code-block:: python

    from eda_toolkit import summarize_all_combinations

    # Define unique variables for the analysis
    unique_vars = [
        "age_group",
        "workclass",
        "education",
        "occupation",
        "race",
        "sex",
        "income",
    ]

    # Generate summary tables for all combinations of the specified variables
    summary_tables, all_combinations = summarize_all_combinations(
        df=df,
        data_path=data_output,
        variables=unique_vars,
        data_name="census_summary_tables.xlsx",
    )

    # Print all combinations of variables
    print(all_combinations)

**Output**

.. code-block:: text

    Generating combinations: 100%|██████████| 120/120 [00:01<00:00, 76.56it/s]
    Writing summary tables: 100%|██████████| 120/120 [00:41<00:00,  2.87it/s]
    Finalizing Excel file: 100%|██████████| 1/1 [00:00<00:00, 13706.88it/s]
    Data saved to ../data_output/census_summary_tables.xlsx

.. code-blocK:: text 

    [('age_group', 'workclass'),
    ('age_group', 'education'),
    ('age_group', 'occupation'),
    ('age_group', 'race'),
    ('age_group', 'sex'),
    ('age_group', 'income'),
    ('workclass', 'education'),
    ('workclass', 'occupation'),
    ('workclass', 'race'),
    ('workclass', 'sex'),
    ('workclass', 'income'),
    ('education', 'occupation'),
    ('education', 'race'),
    ('education', 'sex'),
    ('education', 'income'),
    ('occupation', 'race'),
    ('occupation', 'sex'),
    ('occupation', 'income'),
    ('race', 'sex'),
    ('race', 'income'),
    ('sex', 'income'),
    ('age_group', 'workclass', 'education'),
    ('age_group', 'workclass', 'occupation'),
    ('age_group', 'workclass', 'race'),
    ('age_group', 'workclass', 'sex'),
    ('age_group', 'workclass', 'income'),
    ('age_group', 'education', 'occupation'),
    ('age_group', 'education', 'race'),
    ('age_group', 'education', 'sex'),
    ('age_group', 'education', 'income'),
    ('age_group', 'occupation', 'race'),
    ('age_group', 'occupation', 'sex'),
    ('age_group', 'occupation', 'income'),
    ('age_group', 'race', 'sex'),
    ('age_group', 'race', 'income'),
    ('age_group', 'sex', 'income'),
    ('workclass', 'education', 'occupation'),
    ('workclass', 'education', 'race'),
    ('workclass', 'education', 'sex'),
    ('workclass', 'education', 'income'),
    ('workclass', 'occupation', 'race'),
    ('workclass', 'occupation', 'sex'),
    ('workclass', 'occupation', 'income'),
    ('workclass', 'race', 'sex'),
    ('workclass', 'race', 'income'),
    ('workclass', 'sex', 'income'),
    ('education', 'occupation', 'race'),
    ('education', 'occupation', 'sex'),
    ('education', 'occupation', 'income'),
    ('education', 'race', 'sex'),
    ('education', 'race', 'income'),
    ('education', 'sex', 'income'),
    ('occupation', 'race', 'sex'),
    ('occupation', 'race', 'income'),
    ('occupation', 'sex', 'income'),
    ('race', 'sex', 'income'),
    ('age_group', 'workclass', 'education', 'occupation'),
    ('age_group', 'workclass', 'education', 'race'),
    ('age_group', 'workclass', 'education', 'sex'),
    ('age_group', 'workclass', 'education', 'income'),
    ('age_group', 'workclass', 'occupation', 'race'),
    ('age_group', 'workclass', 'occupation', 'sex'),
    ('age_group', 'workclass', 'occupation', 'income'),
    ('age_group', 'workclass', 'race', 'sex'),
    ('age_group', 'workclass', 'race', 'income'),
    ('age_group', 'workclass', 'sex', 'income'),
    ('age_group', 'education', 'occupation', 'race'),
    ('age_group', 'education', 'occupation', 'sex'),
    ('age_group', 'education', 'occupation', 'income'),
    ('age_group', 'education', 'race', 'sex'),
    ('age_group', 'education', 'race', 'income'),
    ('age_group', 'education', 'sex', 'income'),
    ('age_group', 'occupation', 'race', 'sex'),
    ('age_group', 'occupation', 'race', 'income'),
    ('age_group', 'occupation', 'sex', 'income'),
    ('age_group', 'race', 'sex', 'income'),
    ('workclass', 'education', 'occupation', 'race'),
    ('workclass', 'education', 'occupation', 'sex'),
    ('workclass', 'education', 'occupation', 'income'),
    ('workclass', 'education', 'race', 'sex'),
    ('workclass', 'education', 'race', 'income'),
    ('workclass', 'education', 'sex', 'income'),
    ('workclass', 'occupation', 'race', 'sex'),
    ('workclass', 'occupation', 'race', 'income'),
    ('workclass', 'occupation', 'sex', 'income'),
    ('workclass', 'race', 'sex', 'income'),
    ('education', 'occupation', 'race', 'sex'),
    ('education', 'occupation', 'race', 'income'),
    ('education', 'occupation', 'sex', 'income'),
    ('education', 'race', 'sex', 'income'),
    ('occupation', 'race', 'sex', 'income'),
    ('age_group', 'workclass', 'education', 'occupation', 'race'),
    ('age_group', 'workclass', 'education', 'occupation', 'sex'),
    ('age_group', 'workclass', 'education', 'occupation', 'income'),
    ('age_group', 'workclass', 'education', 'race', 'sex'),
    ('age_group', 'workclass', 'education', 'race', 'income'),
    ('age_group', 'workclass', 'education', 'sex', 'income'),
    ('age_group', 'workclass', 'occupation', 'race', 'sex'),
    ('age_group', 'workclass', 'occupation', 'race', 'income'),
    ('age_group', 'workclass', 'occupation', 'sex', 'income'),
    ('age_group', 'workclass', 'race', 'sex', 'income'),
    ('age_group', 'education', 'occupation', 'race', 'sex'),
    ('age_group', 'education', 'occupation', 'race', 'income'),
    ('age_group', 'education', 'occupation', 'sex', 'income'),
    ('age_group', 'education', 'race', 'sex', 'income'),
    ('age_group', 'occupation', 'race', 'sex', 'income'),
    ('workclass', 'education', 'occupation', 'race', 'sex'),
    ('workclass', 'education', 'occupation', 'race', 'income'),
    ('workclass', 'education', 'occupation', 'sex', 'income'),
    ('workclass', 'education', 'race', 'sex', 'income'),
    ('workclass', 'occupation', 'race', 'sex', 'income'),
    ('education', 'occupation', 'race', 'sex', 'income'),
    ('age_group', 'workclass', 'education', 'occupation', 'race', 'sex'),
    ('age_group', 'workclass', 'education', 'occupation', 'race', 'income'),
    ('age_group', 'workclass', 'education', 'occupation', 'sex', 'income'),
    ('age_group', 'workclass', 'education', 'race', 'sex', 'income'),
    ('age_group', 'workclass', 'occupation', 'race', 'sex', 'income'),
    ('age_group', 'education', 'occupation', 'race', 'sex', 'income'),
    ('workclass', 'education', 'occupation', 'race', 'sex', 'income'),
    ('age_group',
    'workclass',
    'education',
    'occupation',
    'race',
    'sex',
    'income')]


When applied to the US Census data, the output Excel file will contain summary tables for all possible combinations of the specified variables. 
The first sheet will be a Table of Contents with hyperlinks to each summary table.

.. raw:: html

   <div class="no-click">

.. image:: ../assets/summarize_combos.gif
   :alt: EDA Toolkit Logo
   :align: left
   :width: 900px

.. raw:: html

   </div>

.. raw:: html
   
   <div style="height: 106px;"></div>



Saving DataFrames to Excel with Customized Formatting
-----------------------------------------------------
**Save multiple DataFrames to separate sheets in an Excel file with progress tracking and formatting.**

This section explains how to save multiple DataFrames to separate sheets in an 
Excel file with customized formatting using the ``save_dataframes_to_excel`` function.

.. function:: save_dataframes_to_excel(file_path, df_dict, decimal_places=0)

    Save DataFrames to an Excel file, applying formatting and autofitting columns.

    :param file_path: Full path to the output Excel file.
    :type file_path: str

    :param df_dict: Dictionary where keys are sheet names and values are DataFrames to save.
    :type df_dict: dict

    :param decimal_places: Number of decimal places to round numeric columns. Default is ``0``. When set to ``0``, numeric columns are saved as integers.
    :type decimal_places: int

.. admonition:: Notes

    - **Progress Tracking**: The function uses ``tqdm`` to display a progress bar while saving DataFrames to Excel sheets.
    - **Column Formatting**:
        - Columns are autofitted to content length and left-aligned by default.
        - Numeric columns are rounded to the specified decimal places and formatted accordingly.
        - Non-numeric columns are left-aligned.
    - **Header Styling**:
        - Headers are bold, left-aligned, and borderless.
    - **Dependencies**: This function requires the ``xlsxwriter`` library.

**The function performs the following tasks**:

- Writes each DataFrame to its respective sheet in the Excel file.
- Rounds numeric columns to the specified number of decimal places.
- Applies customized formatting to headers and cells.
- Autofits columns based on content length for improved readability.
- Tracks the saving process with a progress bar, making it user-friendly for large datasets.


**Implementation Example**

Below, we use the ``save_dataframes_to_excel`` function to save two DataFrames: 
the original DataFrame and a filtered DataFrame with ages between `18` and `40`.

.. code-block:: python

    from eda_toolkit import save_dataframes_to_excel

    file_name = "df_census.xlsx"  # Name of the output Excel file
    file_path = os.path.join(data_path, file_name) 

    # filter DataFrame to Ages 18-40
    filtered_df = df[(df["age"] > 18) & (df["age"] < 40)]

    df_dict = {
        "original_df": df,
        "ages_18_to_40": filtered_df,
    }

    save_dataframes_to_excel(
        file_path=file_path,
        df_dict=df_dict,
        decimal_places=0,
    )


**Output**

.. code-block:: text 

    Saving DataFrames: 100%|██████████| 2/2 [00:08<00:00,  4.34s/it]
    DataFrames saved to ../data/df_census.xlsx

The output Excel file will contain the original DataFrame and a filtered DataFrame as a separate tab with ages 
between `18` and `40`, each on separate sheets with customized formatting.


Creating Contingency Tables
----------------------------

**Create a contingency table from one or more columns in a DataFrame, with sorting options.**

This section explains how to create contingency tables from one or more columns in a DataFrame, with options to sort the results using the ``contingency_table`` function.

.. function:: contingency_table(df, cols=None, sort_by=0)

    :param df: The DataFrame to analyze.
    :type df: pandas.DataFrame
    :param cols: Name of the column (as a string) for a single column or list of column names for multiple columns. Must provide at least one column.
    :type cols: str or list of str, optional
    :param sort_by: Enter ``0`` to sort results by column groups; enter ``1`` to sort results by totals in descending order. Defaults to ``0``.
    :type sort_by: int, optional
    :raises ValueError: If no columns are specified or if ``sort_by`` is not ``0`` or ``1``.
    :returns: A DataFrame containing the contingency table with the specified columns, a ``'Total'`` column representing the count of occurrences, and a ``'Percentage'`` column representing the percentage of the total count.
    :rtype: pandas.DataFrame

**Implementation Example**

Below, we use the ``contingency_table`` function to create a contingency table 
from the specified columns in a DataFrame containing census data [1]_

.. code-block:: python

    from eda_toolkit import contingency_table

    contingency_table(
        df=df,
        cols=[
            "age_group",
            "workclass",
            "race",
            "sex",
        ],
        sort_by=1,
    )

.. note:: 

    You may notice a new variable, ``age_group``, is introduced. The logic for 
    generating this variable is :ref:`provided here <Binning_Numerical_Columns>`.


**Output**

The output will be a contingency table with the specified columns, showing the 
total counts and percentages of occurrences for each combination of values. The 
table will be sorted by the ``'Total'`` column in descending order because ``sort_by`` 
is set to ``1``.


.. code-block:: text

    
        age_group     workclass                race     sex  Total  Percentage
    0       30-39       Private               White    Male   5856       11.99
    1       18-29       Private               White    Male   5623       11.51
    2       40-49       Private               White    Male   4267        8.74
    3       18-29       Private               White  Female   3680        7.53
    4       50-59       Private               White    Male   2565        5.25
    ..        ...           ...                 ...     ...    ...         ...
    467     50-59   Federal-gov               Other    Male      1        0.00
    468     50-59     Local-gov  Asian-Pac-Islander  Female      1        0.00
    469     70-79  Self-emp-inc               Black    Male      1        0.00
    470     80-89     Local-gov  Asian-Pac-Islander    Male      1        0.00
    471                                                      48842      100.00

    [472 rows x 6 columns]


\

Generating Summaries (Table 1)
----------------------------------------

Create a summary statistics table for both categorical and continuous variables 
in a DataFrame. This section describes how to generate a summary "Table 1" from 
a given dataset using the ``generate_table1`` function. It supports automatic detection 
of variable types, pretty-printing, optional export to Markdown, and *p*-value adjustments.

.. function:: generate_table1(df, apply_bonferroni=False, apply_bh_fdr=False, categorical_cols=None, continuous_cols=None, decimal_places=2, export_markdown=False, drop_columns=None, drop_variables=None, markdown_path=None, max_categories=None, detect_binary_numeric=True, return_markdown_only=False, value_counts=False, include_types="both", combine=True, groupby_col=None, use_fisher_exact=False, use_welch=True)

   :param df: Input DataFrame containing the data to summarize.
   :type df: pandas.DataFrame

   :param apply_bonferroni: Whether to apply Bonferroni correction to *p*-values.
   :type apply_bonferroni: bool, optional

   :param apply_bh_fdr: Whether to apply Benjamini-Hochberg FDR correction to *p*-values.
   :type apply_bh_fdr: bool, optional

   :param categorical_cols: List of categorical column names. If None, inferred automatically.
   :type categorical_cols: list of str, optional

   :param continuous_cols: List of continuous column names. If None, inferred automatically.
   :type continuous_cols: list of str, optional

   :param decimal_places: Number of decimal places for rounding statistics.
   :type decimal_places: int, optional

   :param export_markdown: Whether to export the table(s) to Markdown files.
   :type export_markdown: bool, optional

   :param drop_columns: Column name or list of column names to drop from the final output.
   :type drop_columns: str or list of str, optional

   :param drop_variables: Variable name or list of variables to exclude from output.
   :type drop_variables: str or list of str, optional

   :param markdown_path: Output path or filename prefix for Markdown export.
   :type markdown_path: str or Path, optional

   :param max_categories: Maximum number of category levels to display in value counts.
   :type max_categories: int, optional

   :param detect_binary_numeric: Whether to reclassify numeric variables with ≤2 unique values as categorical.
   :type detect_binary_numeric: bool, optional

   :param return_markdown_only: If ``True``, returns Markdown string(s) instead of DataFrame(s).
   :type return_markdown_only: bool, optional

   :param value_counts: If ``True``, include value counts and proportions for categorical variables.
   :type value_counts: bool, optional

   :param include_types: Which types of variables to include: ``"categorical"``, ``"continuous"``, or ``"both"``.
   :type include_types: str

   :param combine: If ``True``, return a single DataFrame when ``include_types`` is ``"both"``; otherwise, return tuple.
   :type combine: bool, optional

   :param groupby_col: Optional column name for binary group comparisons (e.g., treatment vs. control).
   :type groupby_col: str, optional

   :param use_fisher_exact: Whether to use Fisher's Exact Test for 2x2 categorical comparisons.
   :type use_fisher_exact: bool, optional

   :param use_welch: Whether to use Welch’s t-test (default). If ``False``, uses Student’s t-test.
   :type use_welch: bool, optional

   :returns:
      - If ``include_types="both"`` and ``combine=False``: tuple of two DataFrames (continuous, categorical)
      - If ``include_types="both"`` and ``combine=True``: single combined DataFrame
      - If ``include_types="continuous"`` or ``"categorical"``: single DataFrame
      - If ``export_markdown=True`` and ``return_markdown_only=True``: returns Markdown string or dict of strings
      - Grouped continuous variables display ``mean (SD)`` per group (e.g. ``3.45 (1.23)``)
      - Grouped categorical variables display ``n (%)`` per group

   :rtype: pandas.DataFrame or tuple or str or dict

.. note::

   - Bonferroni and Benjamini-Hochberg FDR corrections are mutually exclusive;
     passing both raises a ``ValueError``.
   - When ``apply_bh_fdr=True``, the BH correction is applied globally across
     all p-values (both continuous and categorical) simultaneously.
   - When ``groupby_col`` is set and a categorical variable produces a crosstab
     with fewer or more than two group columns, that variable is skipped with a
     ``UserWarning`` rather than silently dropped.
   - ``drop_columns`` and ``drop_variables`` are applied to the returned
     DataFrames unconditionally, regardless of whether ``export_markdown``
     is set.
   - Value counts rows are only generated when ``include_types`` is
     ``"categorical"`` or ``"both"``, never when ``"continuous"``.

.. important::

    By default, ``combine=True``, so the function returns a single DataFrame containing  
    both continuous and categorical summaries. This may introduce visual clutter,  
    as categorical rows do not use columns like mean, standard deviation, median, min, or max.  
    These columns are automatically removed when generating a categorical-only summary.  

    To separate the summaries for clarity or further processing, set ``combine=False``  
    and unpack the result into two distinct objects:

    .. code-block:: python

        df_cont, df_cat = generate_table1(df, combine=False)

    This provides greater flexibility for formatting, exporting, or downstream analysis.

.. important::

   When using ``combine=False``, the function returns a **tuple of two** ``TableWrapper`` objects: one for continuous variables and one for categorical variables.

   The ``TableWrapper`` class is a lightweight wrapper designed to override the string representation of a DataFrame, enabling pretty-print formatting (e.g., tables) when the result is printed in a Jupyter cell. The wrapper preserves full access to the underlying DataFrame through attribute forwarding.

   .. code-block:: python

      class TableWrapper:
          """
          Wraps a DataFrame to override its string output without affecting
          Jupyter display.
          """
          def __init__(self, df, string):
              self._df = df
              self._string = string

          def __str__(self):
              return self._string

          def __getattr__(self, attr):
              return getattr(self._df, attr)

          def __getitem__(self, key):
              return self._df[key]

          def __len__(self):
              return len(self._df)

          def __iter__(self):
              return iter(self._df)

   Because ``TableWrapper`` overrides ``__str__`` but not ``__repr__``, assigning the result of ``generate_table1()`` to a single variable like this::

       table1 = generate_table1(df, combine=False)

   will show a tuple of object addresses instead of nicely formatted tables::

       (<eda_toolkit.data_manager.TableWrapper at 0x...>, <eda_toolkit.data_manager.TableWrapper at 0x...>)

   To avoid this, you have **two preferred options**:

   1. **Assign the output to two separate variables**::

          table1_cont, table1_cat = generate_table1(df, combine=False)

      Then display them individually::

          table1_cont
          table1_cat

   2. **Don’t assign the result at all** when calling from a notebook or REPL cell; this will trigger automatic pretty-printing of both tables, with a blank line in between::

          generate_table1(df, combine=False)

   This design keeps the output clean for interactive use while still supporting unpacking in scripts and pipelines.

.. rubric:: Implementation Examples
    :class: rubric-large

Example 1: Mixed Summary Table ``(value_counts=False)``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the example below, we generate a summary table from a dataset containing both 
categorical and continuous variables. We explicitly define which columns fall into 
each category,although the ``generate_table1`` function also supports automatic 
detection of variable types if desired.

The summary output is automatically pretty-printed in the console using the 
``table1_to_str`` utility. This formatting is applied behind the scenes whenever 
a summary table is printed, making it especially helpful for reading outputs 
within notebooks or logging environments.

In this case, we specify ``export_markdown=True`` and provide a filename via
``markdown_path``. This allows the summary to be exported in Markdown format
for use in reports, documentation, or publishing platforms like Jupyter Book or Quarto.
When ``include_types="both"`` and ``combine=True`` (the default), both continuous and 
categorical summaries are merged into a single DataFrame and written to two separate 
Markdown files with ``_continuous.md`` and ``_categorical.md`` suffixes.

We also set ``value_counts=False`` to limit each categorical variable to a single 
summary row, rather than expanding into one row per category-level value.

.. code-block:: python

    from eda_toolkit import generate_table1

    table1 = generate_table1(
        df=df,
        categorical_cols=["sex", "race", "workclass"],
        continuous_cols=["hours-per-week", "age", "education-num"],
        value_counts=False,
        max_categories=3,
        export_markdown=True,
        decimal_places=0,
        markdown_path="table1_summary.md",
    )

    print(table1)


**Output** 

.. code-block:: text

    Variable       | Type        | Mean | SD | Median | Min | Max | Mode    | Missing (n) | Missing (%) | Count  | Proportion (%) 
   ----------------|-------------|------|----|--------|-----|-----|---------|-------------|-------------|--------|----------------
    hours-per-week | Continuous  | 40   | 12 | 40     | 1   | 99  | 40      | 0           | 0           | 48,842 | 100            
    age            | Continuous  | 39   | 14 | 37     | 17  | 90  | 36      | 0           | 0           | 48,842 | 100            
    education-num  | Continuous  | 10   | 3  | 10     | 1   | 16  | 9       | 0           | 0           | 48,842 | 100            
    sex            | Categorical |      |    |        |     |     | Male    | 0           | 0           | 48,842 | 100            
    race           | Categorical |      |    |        |     |     | White   | 0           | 0           | 48,842 | 100            
    workclass      | Categorical |      |    |        |     |     | Private | 963         | 2           | 47,879 | 98      


.. note::

    If ``categorical_cols`` or ``continuous_cols`` are not specified, ``generate_table1``  
    will automatically detect them based on the column data types. Additionally, numeric  
    columns with two or fewer unique values can be reclassified as categorical using  
    the ``detect_binary_numeric=True`` setting (enabled by default).  
    
    When ``value_counts=True``, one row will be generated for each category-value pair  
    rather than for the variable as a whole.


Example 2: Mixed Summary Table ``(value_counts=True)``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this example, we call ``generate_table1`` without manually specifying which 
columns are categorical or continuous. Instead, the function automatically detects 
variable types based on data types. Numeric columns with two or fewer unique values 
are also reclassified as categorical by default 
(controlled via ``detect_binary_numeric=True``).

We set ``value_counts=True`` to generate a separate summary row for each unique value 
within a categorical variable, rather than a single row per variable. To keep 
the output concise, we limit each breakdown to the top 3 most frequent values 
using ``max_categories=3``.

We also enable ``export_markdown=True`` to export the summaries in Markdown format. 
While you can specify a custom markdown_path, if none is provided, the output files 
are saved to the current working directory.

Since ``include_types="both"`` is the default and ``combine=True`` by default as well, 
the underlying summaries are merged into a single DataFrame for display, but two 
separate Markdown files are still generated with suffixes that reflect the type of 
summary:

- ``table1_summary_continuous.md``
- ``table1_summary_categorical.md``

This setup is ideal for detailed reporting, especially when working with 
downstream tools like Jupyter Book, Quarto, or static site generators.


.. code-block:: python

    from eda_toolkit import generate_table1

    table1_cont, table1_cat = generate_table1(
        df=df,
        value_counts=True,
        max_categories=3,
        combine=False,
        export_markdown=True,
        markdown_path="table1_summary.md",
    )

    table1_cont = table1_cont.drop(columns=["Type", "Mode"])

**Output**


``table1_cont``

.. raw:: html
    

    <style type="text/css">
    .tg  {border-collapse:collapse;border-spacing:0;margin:0px auto;}
    .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
    overflow:hidden;padding:0px 0px;word-break:normal;}
    .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
    font-weight:normal;overflow:hidden;padding:0px 0px;word-break:normal;}
    .tg .tg-2b7s{text-align:right;vertical-align:bottom}
    .tg .tg-6ic8{border-color:inherit;font-weight:bold;text-align:right;vertical-align:top}
    .tg .tg-l2oz{font-weight:bold;text-align:right;vertical-align:top}
    .tg .tg-amwm{font-weight:bold;text-align:center;vertical-align:top}
    .tg .tg-jkyp{border-color:inherit;text-align:right;vertical-align:bottom}
    .tg .tg-8d8j{text-align:center;vertical-align:bottom}
    @media screen and (max-width: 767px) {.tg {width: auto !important;}.tg col {width: auto !important;}.tg-wrap {overflow-x: auto;-webkit-overflow-scrolling: touch;margin: auto 0px;}}</style>
    <div class="tg-wrap"><table class="tg" style="undefined;table-layout: fixed; width: 696px"><colgroup>
    <col style="width: 100px">
    <col style="width: 73px">
    <col style="width: 73px">
    <col style="width: 73px">
    <col style="width: 65px">
    <col style="width: 85px">
    <col style="width: 55px">
    <col style="width: 53px">
    <col style="width: 46px">
    <col style="width: 73px">
    </colgroup>
    <thead>
    <tr>
        <th class="tg-6ic8">Variable</th>
        <th class="tg-6ic8">Mean</th>
        <th class="tg-6ic8">SD</th>
        <th class="tg-l2oz">Median</th>
        <th class="tg-l2oz">Min</th>
        <th class="tg-l2oz">Max</th>
        <th class="tg-amwm">Missing (n)</th>
        <th class="tg-amwm">Missing (%)</th>
        <th class="tg-amwm">Count</th>
        <th class="tg-amwm">Proportion (%)</th>
    </tr></thead>
    <tbody>
    <tr>
        <td class="tg-jkyp">age</td>
        <td class="tg-jkyp">38.64</td>
        <td class="tg-jkyp">13.71</td>
        <td class="tg-2b7s">37</td>
        <td class="tg-2b7s">17</td>
        <td class="tg-2b7s">90</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">48,842</td>
        <td class="tg-8d8j">100</td>
    </tr>
    <tr>
        <td class="tg-jkyp">capital-gain</td>
        <td class="tg-jkyp">1,079.07</td>
        <td class="tg-jkyp">7,452.02</td>
        <td class="tg-2b7s">0</td>
        <td class="tg-2b7s">0.00</td>
        <td class="tg-2b7s">99,999.00</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">48,842</td>
        <td class="tg-8d8j">100</td>
    </tr>
    <tr>
        <td class="tg-2b7s">capital-loss</td>
        <td class="tg-2b7s">87.5</td>
        <td class="tg-2b7s">403</td>
        <td class="tg-2b7s">0</td>
        <td class="tg-2b7s">0.00</td>
        <td class="tg-2b7s">4,356.00</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">48,842</td>
        <td class="tg-8d8j">100</td>
    </tr>
    <tr>
        <td class="tg-2b7s">education-num</td>
        <td class="tg-2b7s">10.08</td>
        <td class="tg-2b7s">2.57</td>
        <td class="tg-2b7s">10</td>
        <td class="tg-2b7s">1</td>
        <td class="tg-2b7s">16</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">48,842</td>
        <td class="tg-8d8j">100</td>
    </tr>
    <tr>
        <td class="tg-2b7s">fnlwgt</td>
        <td class="tg-2b7s">189,664.13</td>
        <td class="tg-2b7s">105,604.03</td>
        <td class="tg-2b7s">178,144.50</td>
        <td class="tg-2b7s">12,285.00</td>
        <td class="tg-2b7s">1,490,400.00</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">48,842</td>
        <td class="tg-8d8j">100</td>
    </tr>
    <tr>
        <td class="tg-2b7s">hours-per-week</td>
        <td class="tg-2b7s">40.42</td>
        <td class="tg-2b7s">12.39</td>
        <td class="tg-2b7s">40</td>
        <td class="tg-2b7s">1</td>
        <td class="tg-2b7s">99</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">48,842</td>
        <td class="tg-8d8j">100</td>
    </tr>
    </tbody></table></div>

.. raw:: html
   
   <div style="height: 50px;"></div>
   
``table1_cat``

.. raw:: html

    <style type="text/css">
    .tg  {border-collapse:collapse;border-spacing:0;margin:0px auto;}
    .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
    overflow:hidden;padding:0px 0px;word-break:normal;}
    .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
    font-weight:normal;overflow:hidden;padding:0px 0px;word-break:normal;}
    .tg .tg-2b7s{text-align:right;vertical-align:bottom}
    .tg .tg-l2oz{font-weight:bold;text-align:right;vertical-align:top}
    .tg .tg-amwm{font-weight:bold;text-align:center;vertical-align:top}
    .tg .tg-8d8j{text-align:center;vertical-align:bottom}
    @media screen and (max-width: 767px) {.tg {width: auto !important;}.tg col {width: auto !important;}.tg-wrap {overflow-x: auto;-webkit-overflow-scrolling: touch;margin: auto 0px;}}</style>
    <div class="tg-wrap"><table class="tg" style="margin-left: 11px;undefined;table-layout: fixed; width: 663px"><colgroup>
    <col style="width: 250px">
    <col style="width: 72px">
    <col style="width: 120px">
    <col style="width: 61px">
    <col style="width: 61px">
    <col style="width: 44px">
    <col style="width: 77px">
    </colgroup>
    <thead>
    <tr>
        <th class="tg-l2oz">Variable</th>
        <th class="tg-l2oz">Type</th>
        <th class="tg-l2oz">Mode</th>
        <th class="tg-amwm">Missing (n)</th>
        <th class="tg-amwm">Missing (%)</th>
        <th class="tg-amwm">Count</th>
        <th class="tg-amwm">Proportion (%)</th>
    </tr></thead>
    <tbody>
    <tr>
        <td class="tg-2b7s">workclass = Private</td>
        <td class="tg-2b7s">Categorical</td>
        <td class="tg-2b7s">Private</td>
        <td class="tg-8d8j">963</td>
        <td class="tg-8d8j">1.97</td>
        <td class="tg-8d8j">33,906</td>
        <td class="tg-8d8j">69.42</td>
    </tr>
    <tr>
        <td class="tg-2b7s">workclass = Self-emp-not-inc</td>
        <td class="tg-2b7s">Categorical</td>
        <td class="tg-2b7s">Private</td>
        <td class="tg-8d8j">963</td>
        <td class="tg-8d8j">1.97</td>
        <td class="tg-8d8j">3,862</td>
        <td class="tg-8d8j">7.91</td>
    </tr>
    <tr>
        <td class="tg-2b7s">workclass = Local-gov</td>
        <td class="tg-2b7s">Categorical</td>
        <td class="tg-2b7s">Private</td>
        <td class="tg-8d8j">963</td>
        <td class="tg-8d8j">1.97</td>
        <td class="tg-8d8j">3,136</td>
        <td class="tg-8d8j">6.42</td>
    </tr>
    <tr>
        <td class="tg-2b7s">education = HS-grad</td>
        <td class="tg-2b7s">Categorical</td>
        <td class="tg-2b7s">HS-grad</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">15,784</td>
        <td class="tg-8d8j">32.32</td>
    </tr>
    <tr>
        <td class="tg-2b7s">education = Some-college</td>
        <td class="tg-2b7s">Categorical</td>
        <td class="tg-2b7s">HS-grad</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">10,878</td>
        <td class="tg-8d8j">22.27</td>
    </tr>
    <tr>
        <td class="tg-2b7s">education = Bachelors</td>
        <td class="tg-2b7s">Categorical</td>
        <td class="tg-2b7s">HS-grad</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">8,025</td>
        <td class="tg-8d8j">16.43</td>
    </tr>
    <tr>
        <td class="tg-2b7s">marital-status =&nbsp;&nbsp;&nbsp;Married-civ-spouse</td>
        <td class="tg-2b7s">Categorical</td>
        <td class="tg-2b7s">Married-civ-spouse</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">22,379</td>
        <td class="tg-8d8j">45.82</td>
    </tr>
    <tr>
        <td class="tg-2b7s">marital-status = Never-married</td>
        <td class="tg-2b7s">Categorical</td>
        <td class="tg-2b7s">Married-civ-spouse</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">16,117</td>
        <td class="tg-8d8j">33</td>
    </tr>
    <tr>
        <td class="tg-2b7s">marital-status = Divorced</td>
        <td class="tg-2b7s">Categorical</td>
        <td class="tg-2b7s">Married-civ-spouse</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">6,633</td>
        <td class="tg-8d8j">13.58</td>
    </tr>
    <tr>
        <td class="tg-2b7s">occupation = Prof-specialty</td>
        <td class="tg-2b7s">Categorical</td>
        <td class="tg-2b7s">Prof-specialty</td>
        <td class="tg-8d8j">966</td>
        <td class="tg-8d8j">1.98</td>
        <td class="tg-8d8j">6,172</td>
        <td class="tg-8d8j">12.64</td>
    </tr>
    <tr>
        <td class="tg-2b7s">occupation = Craft-repair</td>
        <td class="tg-2b7s">Categorical</td>
        <td class="tg-2b7s">Prof-specialty</td>
        <td class="tg-8d8j">966</td>
        <td class="tg-8d8j">1.98</td>
        <td class="tg-8d8j">6,112</td>
        <td class="tg-8d8j">12.51</td>
    </tr>
    <tr>
        <td class="tg-2b7s">occupation = Exec-managerial</td>
        <td class="tg-2b7s">Categorical</td>
        <td class="tg-2b7s">Prof-specialty</td>
        <td class="tg-8d8j">966</td>
        <td class="tg-8d8j">1.98</td>
        <td class="tg-8d8j">6,086</td>
        <td class="tg-8d8j">12.46</td>
    </tr>
    <tr>
        <td class="tg-2b7s">relationship = Husband</td>
        <td class="tg-2b7s">Categorical</td>
        <td class="tg-2b7s">Husband</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">19,716</td>
        <td class="tg-8d8j">40.37</td>
    </tr>
    <tr>
        <td class="tg-2b7s">relationship = Not-in-family</td>
        <td class="tg-2b7s">Categorical</td>
        <td class="tg-2b7s">Husband</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">12,583</td>
        <td class="tg-8d8j">25.76</td>
    </tr>
    <tr>
        <td class="tg-2b7s">relationship = Own-child</td>
        <td class="tg-2b7s">Categorical</td>
        <td class="tg-2b7s">Husband</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">7,581</td>
        <td class="tg-8d8j">15.52</td>
    </tr>
    <tr>
        <td class="tg-2b7s">race = White</td>
        <td class="tg-2b7s">Categorical</td>
        <td class="tg-2b7s">White</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">41,762</td>
        <td class="tg-8d8j">85.5</td>
    </tr>
    <tr>
        <td class="tg-2b7s">race = Black</td>
        <td class="tg-2b7s">Categorical</td>
        <td class="tg-2b7s">White</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">4,685</td>
        <td class="tg-8d8j">9.59</td>
    </tr>
    <tr>
        <td class="tg-2b7s">race = Asian-Pac-Islander</td>
        <td class="tg-2b7s">Categorical</td>
        <td class="tg-2b7s">White</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">1,519</td>
        <td class="tg-8d8j">3.11</td>
    </tr>
    <tr>
        <td class="tg-2b7s">sex = Male</td>
        <td class="tg-2b7s">Categorical</td>
        <td class="tg-2b7s">Male</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">32,650</td>
        <td class="tg-8d8j">66.85</td>
    </tr>
    <tr>
        <td class="tg-2b7s">sex = Female</td>
        <td class="tg-2b7s">Categorical</td>
        <td class="tg-2b7s">Male</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">16,192</td>
        <td class="tg-8d8j">33.15</td>
    </tr>
    <tr>
        <td class="tg-2b7s">native-country = United-States</td>
        <td class="tg-2b7s">Categorical</td>
        <td class="tg-2b7s">United-States</td>
        <td class="tg-8d8j">274</td>
        <td class="tg-8d8j">0.56</td>
        <td class="tg-8d8j">43,832</td>
        <td class="tg-8d8j">89.74</td>
    </tr>
    <tr>
        <td class="tg-2b7s">native-country = Mexico</td>
        <td class="tg-2b7s">Categorical</td>
        <td class="tg-2b7s">United-States</td>
        <td class="tg-8d8j">274</td>
        <td class="tg-8d8j">0.56</td>
        <td class="tg-8d8j">951</td>
        <td class="tg-8d8j">1.95</td>
    </tr>
    <tr>
        <td class="tg-2b7s">native-country = ?</td>
        <td class="tg-2b7s">Categorical</td>
        <td class="tg-2b7s">United-States</td>
        <td class="tg-8d8j">274</td>
        <td class="tg-8d8j">0.56</td>
        <td class="tg-8d8j">583</td>
        <td class="tg-8d8j">1.19</td>
    </tr>
    <tr>
        <td class="tg-2b7s">income = &lt;=50K</td>
        <td class="tg-2b7s">Categorical</td>
        <td class="tg-2b7s">&lt;=50K</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">24,720</td>
        <td class="tg-8d8j">50.61</td>
    </tr>
    <tr>
        <td class="tg-2b7s">income = &lt;=50K.</td>
        <td class="tg-2b7s">Categorical</td>
        <td class="tg-2b7s">&lt;=50K</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">12,435</td>
        <td class="tg-8d8j">25.46</td>
    </tr>
    <tr>
        <td class="tg-2b7s">income = &gt;50K</td>
        <td class="tg-2b7s">Categorical</td>
        <td class="tg-2b7s">&lt;=50K</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">0</td>
        <td class="tg-8d8j">7,841</td>
        <td class="tg-8d8j">16.05</td>
    </tr>
    </tbody></table></div>

.. raw:: html
   
   <div style="height: 50px;"></div>

Example 3: Group Comparisons (*P*-Values)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this example we first turn the continuous `fnlwgt` variable into two new categorical factors:

1. **Equal-width bins** (``fnlwgt_bin``), so each interval spans the same numeric range.  
2. **Quantile bins** (``fnlwgt_bin_quantile``), so each bin holds roughly the same number of observations.


After creating those, we build a mixed summary table that computes *p*-values for the two income groups (``<=50K`` vs. ``>50K``), alongside other categorical variables.

.. code-block:: python

    import pandas as pd

    # Equal-width bins
    df["fnlwgt_bin"] = pd.cut(
        df["fnlwgt"],
        bins=5,
        labels=[f"Bin {i}" for i in range(1, 6)],
        include_lowest=True,
    )
    # Select our new bins plus other categorical fields
    df_table1_cat = df[["fnlwgt_bin", "age_group", "income"]]


.. code-block:: python

    from eda_toolkit import generate_table1

    # Generate Table 1 comparing income groups
    p_value_table_1_cat = generate_table1(
        df=df_table1_cat,
        value_counts=True,
        include_types="categorical",
        export_markdown=True,
        groupby_col="income",
        drop_columns=[
            "Missing (n)",
            "Missing (%)",
            "income",   # drop the raw income column itself
            "Type",     # drop internal type metadata
            "Mode",     # drop mode metadata
        ],
        drop_variables="income",
    )

    print(p_value_table_1_cat)

.. code-block:: text

    Using Chi-squared test for variable: fnlwgt_bin_width
    Using Chi-squared test for variable: age_group
    Using Chi-squared test for variable: sex
    Using Chi-squared test for variable: marital-status
    Using Chi-squared test for variable: income


**Output**


.. raw:: html

    <style type="text/css">
    .tg  {border-collapse:collapse;border-spacing:0;margin:0px auto;}
    .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
    overflow:hidden;padding:0px 0px;word-break:normal;}
    .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
    font-weight:normal;overflow:hidden;padding:0px 0px;word-break:normal;}
    .tg .tg-2b7s{text-align:right;vertical-align:bottom}
    .tg .tg-l2oz{font-weight:bold;text-align:right;vertical-align:top}
    .tg .tg-amwm{font-weight:bold;text-align:right;vertical-align:top}
    .tg .tg-8d8j{text-align:right;vertical-align:bottom}
    @media screen and (max-width: 767px) {.tg {width: auto !important;}.tg col {width: auto !important;}.tg-wrap {overflow-x: auto;-webkit-overflow-scrolling: touch;margin: auto 0px;}}
    </style>
    <div class="tg-wrap">
      <table class="tg" style="table-layout: fixed; width: 696px">
        <colgroup>
          <col style="width: 95px">
          <col style="width: 65px">
          <col style="width: 65px">
          <col style="width: 65px">
          <col style="width: 65px">
          <col style="width: 65px">
        </colgroup>
        <thead>
          <tr>
            <th class="tg-l2oz">Variable</th>
            <th class="tg-amwm">Count</th>
            <th class="tg-amwm">Proportion (%)</th>
            <th class="tg-amwm">&le;50K (n = 37,155)</th>
            <th class="tg-amwm">&gt;50K (n = 11,687)</th>
            <th class="tg-amwm">P-value</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="tg-2b7s">fnlwgt_bin_width</td>
            <td class="tg-8d8j">48,842</td>
            <td class="tg-8d8j">100.00</td>
            <td class="tg-8d8j">37,155</td>
            <td class="tg-8d8j">11,687</td>
            <td class="tg-8d8j">0.66</td>
          </tr>
          <tr>
            <td class="tg-2b7s">fnlwgt_bin_width = Bin 1</td>
            <td class="tg-8d8j">42,729</td>
            <td class="tg-8d8j">87.48</td>
            <td class="tg-8d8j">32,517 (87.52%)</td>
            <td class="tg-8d8j">10,212 (87.38%)</td>
            <td class="tg-8d8j"></td>
          </tr>
          <tr>
            <td class="tg-2b7s">fnlwgt_bin_width = Bin 2</td>
            <td class="tg-8d8j">5,898</td>
            <td class="tg-8d8j">12.08</td>
            <td class="tg-8d8j">4,466 (12.02%)</td>
            <td class="tg-8d8j">1,432 (12.25%)</td>
            <td class="tg-8d8j"></td>
          </tr>
          <tr>
            <td class="tg-2b7s">fnlwgt_bin_width = Bin 3</td>
            <td class="tg-8d8j">186</td>
            <td class="tg-8d8j">0.38</td>
            <td class="tg-8d8j">148 (0.40%)</td>
            <td class="tg-8d8j">38 (0.33%)</td>
            <td class="tg-8d8j"></td>
          </tr>
          <tr>
            <td class="tg-2b7s">fnlwgt_bin_width = Bin 4</td>
            <td class="tg-8d8j">22</td>
            <td class="tg-8d8j">0.05</td>
            <td class="tg-8d8j">18 (0.05%)</td>
            <td class="tg-8d8j">4 (0.03%)</td>
            <td class="tg-8d8j"></td>
          </tr>
          <tr>
            <td class="tg-2b7s">fnlwgt_bin_width = Bin 5</td>
            <td class="tg-8d8j">7</td>
            <td class="tg-8d8j">0.01</td>
            <td class="tg-8d8j">6 (0.02%)</td>
            <td class="tg-8d8j">1 (0.01%)</td>
            <td class="tg-8d8j"></td>
          </tr>
          <tr>
            <td class="tg-2b7s">age_group</td>
            <td class="tg-8d8j">48,842</td>
            <td class="tg-8d8j">100.00</td>
            <td class="tg-8d8j">37,155</td>
            <td class="tg-8d8j">11,687</td>
            <td class="tg-8d8j">0.00</td>
          </tr>
          <tr>
            <td class="tg-2b7s">age_group = 18–29</td>
            <td class="tg-8d8j">13,920</td>
            <td class="tg-8d8j">28.50</td>
            <td class="tg-8d8j">13,174 (35.46%)</td>
            <td class="tg-8d8j">746 (6.38%)</td>
            <td class="tg-8d8j"></td>
          </tr>
          <tr>
            <td class="tg-2b7s">age_group = 30–39</td>
            <td class="tg-8d8j">12,929</td>
            <td class="tg-8d8j">26.47</td>
            <td class="tg-8d8j">9,468 (25.48%)</td>
            <td class="tg-8d8j">3,461 (29.61%)</td>
            <td class="tg-8d8j"></td>
          </tr>
          <tr>
            <td class="tg-2b7s">age_group = 40–49</td>
            <td class="tg-8d8j">10,724</td>
            <td class="tg-8d8j">21.96</td>
            <td class="tg-8d8j">6,738 (18.13%)</td>
            <td class="tg-8d8j">3,986 (34.11%)</td>
            <td class="tg-8d8j"></td>
          </tr>
          <tr>
            <td class="tg-2b7s">age_group = 50–59</td>
            <td class="tg-8d8j">6,619</td>
            <td class="tg-8d8j">13.55</td>
            <td class="tg-8d8j">4,110 (11.06%)</td>
            <td class="tg-8d8j">2,509 (21.47%)</td>
            <td class="tg-8d8j"></td>
          </tr>
          <tr>
            <td class="tg-2b7s">age_group = 60–69</td>
            <td class="tg-8d8j">3,054</td>
            <td class="tg-8d8j">6.25</td>
            <td class="tg-8d8j">2,245 (6.04%)</td>
            <td class="tg-8d8j">809 (6.92%)</td>
            <td class="tg-8d8j"></td>
          </tr>
          <tr>
            <td class="tg-2b7s">age_group = 70–79</td>
            <td class="tg-8d8j">815</td>
            <td class="tg-8d8j">1.67</td>
            <td class="tg-8d8j">668 (1.80%)</td>
            <td class="tg-8d8j">147 (1.26%)</td>
            <td class="tg-8d8j"></td>
          </tr>
          <tr>
            <td class="tg-2b7s">age_group = &lt; 18</td>
            <td class="tg-8d8j">595</td>
            <td class="tg-8d8j">1.22</td>
            <td class="tg-8d8j">595 (1.60%)</td>
            <td class="tg-8d8j">0 (0.00%)</td>
            <td class="tg-8d8j"></td>
          </tr>
          <tr>
            <td class="tg-2b7s">age_group = 80–89</td>
            <td class="tg-8d8j">131</td>
            <td class="tg-8d8j">0.27</td>
            <td class="tg-8d8j">115 (0.31%)</td>
            <td class="tg-8d8j">16 (0.14%)</td>
            <td class="tg-8d8j"></td>
          </tr>
          <tr>
            <td class="tg-2b7s">age_group = 90–99</td>
            <td class="tg-8d8j">55</td>
            <td class="tg-8d8j">0.11</td>
            <td class="tg-8d8j">42 (0.11%)</td>
            <td class="tg-8d8j">13 (0.11%)</td>
            <td class="tg-8d8j"></td>
          </tr>
          <tr>
            <td class="tg-2b7s">age_group = 100 +</td>
            <td class="tg-8d8j">0</td>
            <td class="tg-8d8j">0.00</td>
            <td class="tg-8d8j">0 (0.00%)</td>
            <td class="tg-8d8j">0 (0.00%)</td>
            <td class="tg-8d8j"></td>
          </tr>
        </tbody>
      </table>
    </div>

.. raw:: html
   
   <div style="height: 50px;"></div>


.. note::

    - ``groupby_col="income"`` enables group comparison across the two income categories.
    - ``age_group`` and ``fnlwgt_bin_width`` are summarized as categorical variables with frequency counts and group-wise breakdowns.
    - ``value_counts=True`` includes one row per unique value in each categorical variable.
    - ``drop_columns`` and ``drop_variables`` help simplify the final output for presentation by removing metadata and redundant columns.
    - ``export_markdown=True`` writes the summary table to a Markdown file for convenient reporting and sharing.


This example illustrates how the same function can be used to perform basic univariate statistical testing across groups while producing a ready-to-export Markdown summary.

.. raw:: html
   
   <div style="height: 50px;"></div>


Highlighting Specific Columns in a DataFrame
---------------------------------------------

This section explains how to highlight specific columns in a DataFrame using the ``highlight_columns`` function.

**Highlight specific columns in a DataFrame with a specified background color.**

.. function:: highlight_columns(df, columns, color="yellow")

    :param df: The DataFrame to be styled.
    :type df: pandas.DataFrame
    :param columns: List of column names to be highlighted.
    :type columns: list of str
    :param color: The background color to be applied for highlighting (default is ``"yellow"``).
    :type color: str, optional

    :returns: A Styler object with the specified columns highlighted.
    :rtype: pandas.io.formats.style.Styler

**Implementation Example**

Below, we use the ``highlight_columns`` function to highlight the ``age`` and ``education`` 
columns in the first 5 rows of the census [1]_ DataFrame with a pink background color.

.. code-block:: python

    from eda_toolkit import highlight_columns

    highlighted_df = highlight_columns(
        df=df.head(),
        columns=["age", "education"],
        color="#F8C5C8",
    )

    highlighted_df

**Output**

The output will be a DataFrame with the specified columns highlighted in the given background color. 
The ``age`` and ``education`` columns will be highlighted in pink.

The resulting styled DataFrame can be displayed in a Jupyter Notebook or saved to an 
HTML file using the ``.render()`` method of the Styler object.


.. raw:: html

    <style type="text/css">
    .tg  {border:none;border-collapse:collapse;border-spacing:0;margin:0px auto;}
    .tg td{border-style:solid;border-width:0px;font-family:monospace, sans-serif;font-size:11px;overflow:hidden;padding:0px 5px;
    word-break:normal;}
    .tg th{border-style:solid;border-width:0px;font-family:monospace, sans-serif;font-size:11px;font-weight:normal;
    overflow:hidden;padding:0px 5px;word-break:normal;}
    .tg .tg-zv36{background-color:#ffffff;border-color:inherit;font-weight:bold;text-align:left;vertical-align:top}
    .tg .tg-c6of{background-color:#ffffff;border-color:inherit;text-align:left;vertical-align:top}
    .tg .tg-7g6k{background-color:#ffffff;border-color:inherit;font-weight:bold;text-align:center;vertical-align:top}
    .tg .tg-3xi5{background-color:#ffffff;border-color:inherit;text-align:center;vertical-align:top}
    .tg .tg-6qlg{background-color:#FFCCCC;border-color:inherit;text-align:center;vertical-align:top}
    @media screen and (max-width: 767px) {.tg {width: auto !important;}.tg col {width: auto !important;}.tg-wrap {overflow-x: auto;-webkit-overflow-scrolling: touch;margin: auto 0px;}}</style>
    <div class="tg-wrap"><table class="tg"><thead>
    <tr>
        <th class="tg-c6of"></th>
        <th class="tg-7g6k">age</th>
        <th class="tg-7g6k">workclass</th>
        <th class="tg-7g6k">fnlwgt</th>
        <th class="tg-7g6k">education</th>
        <th class="tg-7g6k">education-num</th>
        <th class="tg-7g6k">marital-status</th>
        <th class="tg-7g6k">occupation</th>
        <th class="tg-7g6k">relationship</th>
    </tr></thead>
    <tbody>
    <tr>
        <td class="tg-zv36">census_id</td>
        <td class="tg-3xi5"></td>
        <td class="tg-3xi5"></td>
        <td class="tg-3xi5"></td>
        <td class="tg-3xi5"></td>
        <td class="tg-3xi5"></td>
        <td class="tg-3xi5"></td>
        <td class="tg-3xi5"></td>
        <td class="tg-3xi5"></td>
    </tr>
    <tr>
        <td class="tg-c6of">582248222</td>
        <td class="tg-6qlg">39</td>
        <td class="tg-3xi5">State-gov</td>
        <td class="tg-3xi5">77516</td>
        <td class="tg-6qlg">Bachelors</td>
        <td class="tg-3xi5">13</td>
        <td class="tg-3xi5">Never-married</td>
        <td class="tg-3xi5">Adm-clerical</td>
        <td class="tg-3xi5">Not-in-family</td>
    </tr>
    <tr>
        <td class="tg-c6of">561810758</td>
        <td class="tg-6qlg">50</td>
        <td class="tg-3xi5">Self-emp-not-inc</td>
        <td class="tg-3xi5">83311</td>
        <td class="tg-6qlg">Bachelors</td>
        <td class="tg-3xi5">13</td>
        <td class="tg-3xi5">Married-civ-spouse</td>
        <td class="tg-3xi5">Exec-managerial</td>
        <td class="tg-3xi5">Husband</td>
    </tr>
    <tr>
        <td class="tg-c6of">598098459</td>
        <td class="tg-6qlg">38</td>
        <td class="tg-3xi5">Private</td>
        <td class="tg-3xi5">215646</td>
        <td class="tg-6qlg">HS-grad</td>
        <td class="tg-3xi5">9</td>
        <td class="tg-3xi5">Divorced</td>
        <td class="tg-3xi5">Handlers-cleaners</td>
        <td class="tg-3xi5">Not-in-family</td>
    </tr>
    <tr>
        <td class="tg-c6of">776705221</td>
        <td class="tg-6qlg">53</td>
        <td class="tg-3xi5">Private</td>
        <td class="tg-3xi5">234721</td>
        <td class="tg-6qlg">11th</td>
        <td class="tg-3xi5">7</td>
        <td class="tg-3xi5">Married-civ-spouse</td>
        <td class="tg-3xi5">Handlers-cleaners</td>
        <td class="tg-3xi5">Husband</td>
    </tr>
    <tr>
        <td class="tg-c6of">479262902</td>
        <td class="tg-6qlg">28</td>
        <td class="tg-3xi5">Private</td>
        <td class="tg-3xi5">338409</td>
        <td class="tg-6qlg">Bachelors</td>
        <td class="tg-3xi5">13</td>
        <td class="tg-3xi5">Married-civ-spouse</td>
        <td class="tg-3xi5">Prof-specialty</td>
        <td class="tg-3xi5">Wife</td>
    </tr>
    </tbody></table></div>

\

.. _Binning_Numerical_Columns:

Binning Numerical Columns
---------------------------

Binning numerical columns is a technique used to convert continuous numerical 
data into discrete categories or "bins." This is especially useful for simplifying 
analysis, creating categorical features from numerical data, or visualizing the 
distribution of data within specific ranges. The process of binning involves 
dividing a continuous range of values into a series of intervals, or "bins," and 
then assigning each value to one of these intervals.

.. note::

    The code snippets below create age bins and assign a corresponding age group 
    label to each age in the DataFrame. The ``pd.cut`` function from pandas is used to 
    categorize the ages and assign them to a new column, ``age_group``. Adjust the bins 
    and labels as needed for your specific data.


Below, we use the ``age`` column of the census data [1]_ from the UCI Machine Learning Repository as an example:

1. **Bins Definition**:
   The bins are defined by specifying the boundaries of each interval. For example, 
   in the code snippet below, the ``bin_ages`` list specifies the boundaries for age groups:

   .. code-block:: python

        bin_ages = [
            0,
            18,
            30,
            40,
            50,
            60,
            70,
            80,
            90,
            100,
            float("inf"),
        ]


   Each pair of consecutive elements in ``bin_ages`` defines a bin. For example:
   
   - The first bin is ``[0, 18)``,
   - The second bin is ``[18, 30)``,
   - and so on.  

\

2. **Labels for Bins**:
   The ``label_ages`` list provides labels corresponding to each bin:

   .. code-block:: python

        label_ages = [
            "< 18",
            "18-29",
            "30-39",
            "40-49",
            "50-59",
            "60-69",
            "70-79",
            "80-89",
            "90-99",
            "100 +",
        ]

   These labels are used to categorize the numerical values into meaningful groups.

3. **Applying the Binning**:
   The `pd.cut <https://pandas.pydata.org/docs/reference/api/pandas.cut.html>`_ function 
   from Pandas is used to apply the binning process. For each value in the ``age`` 
   column of the DataFrame, it assigns a corresponding label based on which bin the 
   value falls into. Here, ``right=False`` indicates that each bin includes the 
   left endpoint but excludes the right endpoint. For example, if ``bin_ages = 
   [0, 10, 20, 30]``, then a value of ``10`` will fall into the bin ``[10, 20)`` and 
   be labeled accordingly.

   .. code-block:: python

       df["age_group"] = pd.cut(
           df["age"],
           bins=bin_ages,
           labels=label_ages,
           right=False,
       )

   **Mathematically**, for a given value `x` in the ``age`` column:

   .. math::

       \text{age\_group} = 
       \begin{cases} 
        < 18 & \text{if } 0 \leq x < 18 \\
        18-29 & \text{if } 18 \leq x < 30 \\
        \vdots \\
        100 + & \text{if } x \geq 100 
       \end{cases}

   The parameter ``right=False`` in ``pd.cut`` means that the bins are left-inclusive 
   and right-exclusive, except for the last bin, which is always right-inclusive 
   when the upper bound is infinity (``float("inf")``).

Group-by Imputer
-------------------

**Impute missing values using group-level statistics with optional fallback logic.**

The ``groupby_imputer`` function provides a simple, transparent, and statistically
grounded approach for imputing missing values in a DataFrame using **group-specific
summary statistics**. Instead of applying a single global imputation value, this
function computes statistics within meaningful subgroups, preserving structure
and heterogeneity in the data.

This approach is especially useful when missingness depends on categorical
attributes such as demographic groups, job categories, or experimental conditions.

**Key Features**

- **Group-aware imputation** using one or more categorical variables
- Supports common summary statistics: mean, median, min, max
- **Fallback logic** for sparse or empty groups
- Option to **preserve the original column** or overwrite in place
- Fully vectorized and interpretable, no black-box modeling

.. function:: groupby_imputer(df, impute_col, by, stat="mean", fallback="global", as_new_col=True, new_col_name=None)

    :param df: Input DataFrame containing missing values to impute.
    :type df: pandas.DataFrame

    :param impute_col: Name of the column containing missing values.
    :type impute_col: str

    :param by: One or more categorical columns used to define groups.
        Group-level statistics are computed within each unique combination
        of these columns.
    :type by: str or list of str

    :param stat: Summary statistic used for imputation.
        Supported values are ``"mean"``, ``"median"``, ``"min"``, and ``"max"``.
    :type stat: str, optional

    :param fallback: Value used when a group contains no non-null observations
        for ``impute_col``.
        - ``"global"`` uses the overall statistic computed across the entire column
        - A numeric value (int or float) uses a fixed fallback
    :type fallback: str or int or float, optional

    :param as_new_col: If ``True``, a new imputed column is created and the original
        column is left unchanged. If ``False``, imputation is performed in place.
    :type as_new_col: bool, optional

    :param new_col_name: Optional custom name for the imputed column.
        Ignored if ``as_new_col=False``.
    :type new_col_name: str, optional

    :returns: A DataFrame with missing values imputed according to group-level
        statistics and fallback logic.
    :rtype: pandas.DataFrame

    :raises ValueError:
        - If ``stat`` is not one of ``"mean"``, ``"median"``, ``"min"``, or ``"max"``.

.. admonition:: Notes

    - Group statistics are computed using non-null values only.
    - If a group contains only missing values, the fallback value is applied.
    - Using ``as_new_col=True`` is recommended for exploratory workflows to
      preserve the original data for comparison.
    - This method is deterministic and fully interpretable, making it suitable
      for regulated or audited modeling environments.

\

.. rubric:: Group-wise Imputation Examples
    :class: rubric-large

In the example below, missing values are introduced artificially into the
``"age"`` column of the Adult Income dataset. The goal is to impute these missing
values using **group-level means**, defined by combinations of ``"workclass"``
and ``"education"``.

Two fallback strategies are demonstrated:

1. **Global fallback**, where groups with insufficient data fall back to the
   overall mean
2. **Fixed-value fallback**, where a constant value is used instead

.. code-block:: python

    from eda_toolkit import groupby_imputer
    import numpy as np

    # Introduce missingness for demonstration
    df.loc[
        df.sample(frac=0.3, random_state=42).index, "age"
    ] = np.nan

    # 1. Group-wise mean imputation with global fallback
    X_global = groupby_imputer(
        df=df,
        impute_col="age",
        by=["workclass", "education"],
        stat="mean",
        fallback="global",
        as_new_col=True,
    )

    print("\n### Head with global fallback ###")
    print(X_global[["age", "age_mean_imputed"]].head())

    print("Means:")
    print(f"Original df['age'].mean(): {df['age'].mean()}")
    print(f"Imputed (global fallback) mean: {X_global['age_mean_imputed'].mean()}")


**Output**

.. code-block:: text

    ### Head with global fallback ###
                age  age_mean_imputed
    census_id                        
    582248222   NaN         38.495238
    561810758   NaN         45.110837
    598098459  38.0         38.000000
    776705221  53.0         53.000000
    479262902   NaN         37.249330
    Means:
    Original df['age'].mean(): 38.597911608997045
    Imputed (global fallback) mean: 38.621605730469135

.. code-block:: python

    from eda_toolkit import groupby_imputer
    import numpy as np

    # Introduce missingness for demonstration
    df.loc[
        df.sample(frac=0.3, random_state=42).index, "age"
    ] = np.nan

    # 2. Group-wise mean imputation with fixed fallback
    X_fixed = groupby_imputer(
        df=df,
        impute_col="age",
        by=["workclass", "education"],
        stat="mean",
        fallback=50,
        as_new_col=True,
    )

    print("\n### Head with fixed fallback=50 ###")
    print(X_fixed[["age", "age_mean_imputed"]].head())
    print("Means:")
    print(f"Original df['age'].mean(): {df['age'].mean()}")
    print(f"Imputed (fixed fallback=50) mean: {X_fixed['age_mean_imputed'].mean()}")

    print("\n### Comparison summary ###")
    print(f"Missingness in original age: {df['age'].isna().mean()}")
    print(f"Global fallback mean: {X_global['age_mean_imputed'].mean()}")
    print(f"Fixed fallback=50 mean: {X_fixed['age_mean_imputed'].mean()}")

**Output**

.. code-block:: text

    ### Head with fixed fallback=50 ###
        age  age_mean_imputed
    0   NaN         38.495238
    1   NaN         45.110837
    2  38.0         38.000000
    3  53.0         53.000000
    4   NaN         37.249330

    Means:
    Original df['age'].mean(): 38.597911608997045
    Imputed (fixed fallback=50) mean: 38.6904730183637

    ### Comparison summary ###
    Missingness in original age: 0.30000818967282256
    Global fallback mean: 38.621605730469135
    Fixed fallback=50 mean: 38.6904730183637


**Interpretation**

- Group-level imputation preserves differences across workclass and education
  categories that would be lost under global imputation.
- The global fallback maintains consistency with the original distribution.
- Fixed fallback values may be useful for domain-driven constraints but can
  introduce bias if not chosen carefully.

Group-aware imputation provides a strong baseline that often outperforms naive
global strategies while remaining transparent and easy to audit.


Delete Inactive DataFrames
-----------------------------

**Safely clean up unused pandas DataFrames from a namespace to reduce memory usage**

The ``del_inactive_dataframes`` utility is designed to help manage memory in
interactive environments such as Jupyter notebooks, scripts, and cloud runtimes.
It inspects a namespace (for example, ``globals()`` or a custom dictionary),
identifies pandas DataFrames, and optionally deletes those that are no longer
needed.

Unlike manual ``del`` calls, this function provides **visibility, safety, and
auditability**:

- Preview what would be deleted before committing
- Preserve explicitly named DataFrames
- Handle Jupyter output-cache variables that can silently retain memory
- Optionally track memory usage before and after cleanup
- Produce readable summaries using Rich tables when available

This makes it particularly useful during exploratory analysis, large ETL
pipelines, and long-running notebooks.

**Key Capabilities**

- **Selective deletion** based on an explicit keep list
- **Dry-run mode** to preview deletions without modifying state
- Optional inclusion of IPython cache variables (e.g. ``_14``, ``_27``)
- Optional **garbage collection** after deletion
- Optional **memory tracking** at the DataFrame and process level
- Works with ``globals()``, ``locals()``, or any user-managed namespace dictionary

.. function:: del_inactive_dataframes(dfs_to_keep, del_dataframes=False, namespace=None, include_ipython_cache=False, dry_run=False, run_gc=True, track_memory=False, memory_mode="dataframes", verbose=True)

    :param dfs_to_keep: Name or names of DataFrame variables to preserve.
        All other DataFrames may be deleted when ``del_dataframes=True``.
    :type dfs_to_keep: str or iterable of str

    :param del_dataframes: Whether to actually delete inactive DataFrames.
        If ``False``, the function only reports what would be deleted.
    :type del_dataframes: bool, optional

    :param namespace: Namespace dictionary to inspect and optionally modify.
        If ``None``, the function uses ``globals()`` of the calling scope.
    :type namespace: dict, optional

    :param include_ipython_cache: Whether to include IPython output-cache
        variables (e.g. ``_14``) when searching for DataFrames.
    :type include_ipython_cache: bool, optional

    :param dry_run: If ``True``, show planned deletions without deleting anything.
    :type dry_run: bool, optional

    :param run_gc: Whether to call ``gc.collect()`` after deletions occur.
    :type run_gc: bool, optional

    :param track_memory: Whether to record memory usage before and after cleanup.
    :type track_memory: bool, optional

    :param memory_mode: Controls which memory metrics are reported:
        - ``"dataframes"`` reports total pandas DataFrame memory
        - ``"all"`` also reports process RSS (requires ``psutil``)
    :type memory_mode: str, optional

    :param verbose: Whether to print formatted output. If ``False``, the function
        returns results silently.
    :type verbose: bool, optional

    :returns: Summary dictionary describing detected, deleted, and remaining
        DataFrames, along with optional memory metrics.
    :rtype: dict

    :raises ValueError:
        - If ``memory_mode`` is not one of ``"dataframes"`` or ``"all"``.

.. admonition:: Notes

    - A namespace is simply a dictionary mapping variable names to objects.
    - Deletion is performed by removing keys from the namespace dictionary.
    - Modifying ``locals()`` inside a function is not guaranteed to free memory.
      For reliable cleanup inside functions, store DataFrames in a dict and
      pass that dict as ``namespace``.
    - Process RSS memory may not decrease immediately even after garbage collection.

.. rubric:: Implementation Examples
    :class: rubric-large

The following examples demonstrate common and advanced usage patterns for
``del_inactive_dataframes``. Each example recreates its own DataFrames so behavior
is isolated and easy to follow.

Because ``del_inactive_dataframes`` inspects a namespace dictionary, these examples
explicitly pass ``namespace=globals()`` so the function can see variables defined
in this script or notebook.


Example 1: List Active DataFrames (No Deletion)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Inspect which DataFrames are currently active without deleting anything.

.. code-block:: python

    from eda_toolkit import del_inactive_dataframes

    df_main = pd.DataFrame({"a": range(10)})
    df_tmp = pd.DataFrame({"b": range(100)})

    del_inactive_dataframes(
        dfs_to_keep = ["df"],
        del_dataframes=False,
        namespace=globals(),
    )

**Output**

.. code-block:: text

    ──────────────────────────────────────── Active DataFrames ────────────────────────────────────────
    Current Active  
        DataFrames    
    ┏━━━━━━━━━━━━━━━━┓
    ┃ DataFrame Name ┃
    ┡━━━━━━━━━━━━━━━━┩
    │ _              │
    │ __             │
    │ ___            │
    │ df             │
    │ df_copy        │
    │ df_main        │
    │ df_tmp         │
    │ sampled_df     │
    └────────────────┘
    {'active': ['_',
    '__',
    '___',
    'df',
    'df_copy',
    'df_main',
    'df_tmp',
    'sampled_df'],
    'to_delete': [],
    'deleted': [],
    'remaining': [],
    'used_rich': True,
    'memory': None}


Example 2: Delete Everything Except a Single DataFrame
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Remove all DataFrames except the one explicitly listed.

.. code-block:: python

    from eda_toolkit import del_inactive_dataframes

    df_main = pd.DataFrame({"a": range(10)})
    df_tmp = pd.DataFrame({"b": range(100)})

    del_inactive_dataframes(
        dfs_to_keep = ["df"],
        del_dataframes=True,
        namespace=globals(),
    )

**Output**

.. code-block:: text

    ──────────────────────────────────────── Active DataFrames ────────────────────────────────────────
    Current Active  
        DataFrames    
    ┏━━━━━━━━━━━━━━━━┓
    ┃ DataFrame Name ┃
    ┡━━━━━━━━━━━━━━━━┩
    │ X              │
    │ X_fixed        │
    │ X_global       │
    │ data           │
    │ df             │
    │ df_impute      │
    │ df_main        │
    │ df_strip       │
    │ df_table1_cat  │
    │ df_tmp         │
    │ filtered_df    │
    │ y              │
    └────────────────┘
    ──────────────────────────────────────── Planned Deletions ────────────────────────────────────────
    DataFrames Marked 
    for Deletion   
    ┏━━━━━━━━━━━━━━━━┓
    ┃ DataFrame Name ┃
    ┡━━━━━━━━━━━━━━━━┩
    │ X              │
    │ X_fixed        │
    │ X_global       │
    │ data           │
    │ df_impute      │
    │ df_main        │
    │ df_strip       │
    │ df_table1_cat  │
    │ df_tmp         │
    │ filtered_df    │
    │ y              │
    └────────────────┘
    ──────────────────────────────────────── Deleted DataFrames ────────────────────────────────────────
    Deleted DataFrames
    ┏━━━━━━━━━━━━━━━━┓
    ┃ DataFrame Name ┃
    ┡━━━━━━━━━━━━━━━━┩
    │ X              │
    │ X_fixed        │
    │ X_global       │
    │ data           │
    │ df_impute      │
    │ df_main        │
    │ df_strip       │
    │ df_table1_cat  │
    │ df_tmp         │
    │ filtered_df    │
    │ y              │
    └────────────────┘
    ─────────────────────────────────────── Remaining DataFrames ───────────────────────────────────────
    Remaining Active 
        DataFrames    
    ┏━━━━━━━━━━━━━━━━┓
    ┃ DataFrame Name ┃
    ┡━━━━━━━━━━━━━━━━┩
    │ df             │
    └────────────────┘
    {'active': ['X',
    'X_fixed',
    'X_global',
    'data',
    'df',
    'df_impute',
    'df_main',
    'df_strip',
    'df_table1_cat',
    'df_tmp',
    'filtered_df',
    'y'],
    'to_delete': ['X',
    'X_fixed',
    'X_global',
    'data',
    'df_impute',
    'df_main',
    'df_strip',
    'df_table1_cat',
    'df_tmp',
    'filtered_df',
    'y'],
    'deleted': ['X',
    'X_fixed',
    'X_global',
    'data',
    'df_impute',
    'df_main',
    'df_strip',
    'df_table1_cat',
    'df_tmp',
    'filtered_df',
    'y'],
    'remaining': ['df'],
    'used_rich': True,
    'memory': None}

Example 3: Dry Run (Preview Deletions)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Preview which DataFrames *would* be deleted without actually removing them.

.. code-block:: python

    from eda_toolkit import del_inactive_dataframes

    df_main = pd.DataFrame({"a": range(10)})
    df_tmp = pd.DataFrame({"b": range(100)})

    del_inactive_dataframes(
        dfs_to_keep = ["df"],
        del_dataframes=True,
        dry_run=True,
        namespace=globals(),
    )

**Output**

.. code-block:: text

    ──────────────────────────────────────── Active DataFrames ────────────────────────────────────────
    Current Active  
        DataFrames    
    ┏━━━━━━━━━━━━━━━━┓
    ┃ DataFrame Name ┃
    ┡━━━━━━━━━━━━━━━━┩
    │ __             │
    │ ___            │
    │ df             │
    │ df_copy        │
    │ df_main        │
    │ df_tmp         │
    │ sampled_df     │
    └────────────────┘
    ──────────────────────────────────────── Planned Deletions ────────────────────────────────────────
    DataFrames Marked 
    for Deletion   
    ┏━━━━━━━━━━━━━━━━┓
    ┃ DataFrame Name ┃
    ┡━━━━━━━━━━━━━━━━┩
    │ __             │
    │ ___            │
    │ df_copy        │
    │ df_main        │
    │ df_tmp         │
    │ sampled_df     │
    └────────────────┘
    Dry run enabled. No DataFrames were deleted.
    ─────────────────────────────────────── Remaining DataFrames ───────────────────────────────────────
    Remaining Active 
        DataFrames    
    ┏━━━━━━━━━━━━━━━━┓
    ┃ DataFrame Name ┃
    ┡━━━━━━━━━━━━━━━━┩
    │ __             │
    │ ___            │
    │ df             │
    │ df_copy        │
    │ df_main        │
    │ df_tmp         │
    │ sampled_df     │
    └────────────────┘
    {'active': ['__', '___', 'df', 'df_copy', 'df_main', 'df_tmp', 'sampled_df'],
    'to_delete': ['__', '___', 'df_copy', 'df_main', 'df_tmp', 'sampled_df'],
    'deleted': [],
    'remaining': ['__',
    '___',
    'df',
    'df_copy',
    'df_main',
    'df_tmp',
    'sampled_df'],
    'used_rich': True,
    'memory': None}

This mode is recommended before running destructive cleanup steps.


Example 4: Include IPython Output Cache Variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In Jupyter notebooks, output cache variables such as ``_14`` may reference large
DataFrames. These are ignored by default but can be included explicitly.

.. code-block:: python

    from eda_toolkit import del_inactive_dataframes

    df_main = pd.DataFrame({"a": range(10)})
    df_tmp = pd.DataFrame({"b": range(100)})

    _ = df_tmp  # simulates an IPython output cache reference

    del_inactive_dataframes(
        dfs_to_keep = ["df"],
        del_dataframes=True,
        include_ipython_cache=True,
        namespace=globals(),
    )

**Output**

.. code-block:: text

    ──────────────────────────────────────── Active DataFrames ────────────────────────────────────────
    Current Active  
        DataFrames    
    ┏━━━━━━━━━━━━━━━━┓
    ┃ DataFrame Name ┃
    ┡━━━━━━━━━━━━━━━━┩
    │ _              │
    │ _10            │
    │ _19            │
    │ _8             │
    │ df             │
    │ df_main        │
    │ df_tmp         │
    └────────────────┘
    ──────────────────────────────────────── Planned Deletions ────────────────────────────────────────
    DataFrames Marked 
    for Deletion   
    ┏━━━━━━━━━━━━━━━━┓
    ┃ DataFrame Name ┃
    ┡━━━━━━━━━━━━━━━━┩
    │ _              │
    │ _10            │
    │ _19            │
    │ _8             │
    │ df_main        │
    │ df_tmp         │
    └────────────────┘
    ──────────────────────────────────────── Deleted DataFrames ────────────────────────────────────────
    Deleted DataFrames
    ┏━━━━━━━━━━━━━━━━┓
    ┃ DataFrame Name ┃
    ┡━━━━━━━━━━━━━━━━┩
    │ _              │
    │ _10            │
    │ _19            │
    │ _8             │
    │ df_main        │
    │ df_tmp         │
    └────────────────┘
    ─────────────────────────────────────── Remaining DataFrames ───────────────────────────────────────
    Remaining Active 
        DataFrames    
    ┏━━━━━━━━━━━━━━━━┓
    ┃ DataFrame Name ┃
    ┡━━━━━━━━━━━━━━━━┩
    │ df             │
    └────────────────┘
    {'active': ['_', '_10', '_19', '_8', 'df', 'df_main', 'df_tmp'],
    'to_delete': ['_', '_10', '_19', '_8', 'df_main', 'df_tmp'],
    'deleted': ['_', '_10', '_19', '_8', 'df_main', 'df_tmp'],
    'remaining': ['df'],
    'used_rich': True,
    'memory': None}

Example 5: Track DataFrame Memory Usage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Report total DataFrame memory usage before and after cleanup.

.. code-block:: python

    from eda_toolkit import del_inactive_dataframes

    df_main = pd.DataFrame({"a": range(10)})
    df_tmp = pd.DataFrame({"b": range(100)})

    del_inactive_dataframes(
        dfs_to_keep = ["df"],
        del_dataframes=True,
        track_memory=True,
        namespace=globals(),
    )


**Output**

.. code-block:: text

    ──────────────────────────────────────── Active DataFrames ────────────────────────────────────────
    Current Active  
        DataFrames    
    ┏━━━━━━━━━━━━━━━━┓
    ┃ DataFrame Name ┃
    ┡━━━━━━━━━━━━━━━━┩
    │ df             │
    │ df_main        │
    │ df_tmp         │
    └────────────────┘
    ──────────────────────────────────────── Planned Deletions ────────────────────────────────────────
    DataFrames Marked 
    for Deletion   
    ┏━━━━━━━━━━━━━━━━┓
    ┃ DataFrame Name ┃
    ┡━━━━━━━━━━━━━━━━┩
    │ df_main        │
    │ df_tmp         │
    └────────────────┘
    ──────────────────────────────────────── Deleted DataFrames ────────────────────────────────────────
    Deleted DataFrames
    ┏━━━━━━━━━━━━━━━━┓
    ┃ DataFrame Name ┃
    ┡━━━━━━━━━━━━━━━━┩
    │ df_main        │
    │ df_tmp         │
    └────────────────┘
    ─────────────────────────────────────── Remaining DataFrames ───────────────────────────────────────
    Remaining Active 
        DataFrames    
    ┏━━━━━━━━━━━━━━━━┓
    ┃ DataFrame Name ┃
    ┡━━━━━━━━━━━━━━━━┩
    │ df             │
    └────────────────┘
    ────────────────────────────────────────────── Memory ──────────────────────────────────────────────
                Memory Usage (MB)              
    ┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━┳━━━━━━━┓
    ┃ Metric           ┃ Before ┃ After ┃ Delta ┃
    ┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━╇━━━━━━━┩
    │ DataFrames total │   30.2 │  30.2 │  -0.0 │
    └──────────────────┴────────┴───────┴───────┘
    {'active': ['df', 'df_main', 'df_tmp'],
    'to_delete': ['df_main', 'df_tmp'],
    'deleted': ['df_main', 'df_tmp'],
    'remaining': ['df'],
    'used_rich': True,
    'memory': {'dataframes_mb': {'before': 30.237445831298828,
    'after': 30.23635482788086,
    'delta': -0.00109100341796875},
    'mode': 'dataframes'}}

    This mode uses ``pandas.DataFrame.memory_usage(deep=True)`` for reporting.


Example 6: Track DataFrame Memory and Process RSS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Enable power-user memory tracking, including process-level RSS when available.

.. code-block:: python

    df_main = pd.DataFrame({"a": range(10)})
    df_tmp = pd.DataFrame({"b": range(100)})

    del_inactive_dataframes(
        dfs_to_keep = ["df"],
        del_dataframes=True,
        track_memory=True,
        memory_mode="all",
        namespace=globals(),
    )

**Output**

.. code-block:: text

    ──────────────────────────────────────── Active DataFrames ────────────────────────────────────────
    Current Active  
        DataFrames    
    ┏━━━━━━━━━━━━━━━━┓
    ┃ DataFrame Name ┃
    ┡━━━━━━━━━━━━━━━━┩
    │ df             │
    │ df_main        │
    │ df_tmp         │
    └────────────────┘
    ──────────────────────────────────────── Planned Deletions ────────────────────────────────────────
    DataFrames Marked 
    for Deletion   
    ┏━━━━━━━━━━━━━━━━┓
    ┃ DataFrame Name ┃
    ┡━━━━━━━━━━━━━━━━┩
    │ df_main        │
    │ df_tmp         │
    └────────────────┘
    ──────────────────────────────────────── Deleted DataFrames ────────────────────────────────────────
    Deleted DataFrames
    ┏━━━━━━━━━━━━━━━━┓
    ┃ DataFrame Name ┃
    ┡━━━━━━━━━━━━━━━━┩
    │ df_main        │
    │ df_tmp         │
    └────────────────┘
    ─────────────────────────────────────── Remaining DataFrames ───────────────────────────────────────
    Remaining Active 
        DataFrames    
    ┏━━━━━━━━━━━━━━━━┓
    ┃ DataFrame Name ┃
    ┡━━━━━━━━━━━━━━━━┩
    │ df             │
    └────────────────┘
    ────────────────────────────────────────────── Memory ──────────────────────────────────────────────
                Memory Usage (MB)              
    ┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━┳━━━━━━━┓
    ┃ Metric           ┃ Before ┃ After ┃ Delta ┃
    ┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━╇━━━━━━━┩
    │ Process RSS      │  403.6 │ 403.6 │  +0.0 │
    │ DataFrames total │   30.2 │  30.2 │  -0.0 │
    └──────────────────┴────────┴───────┴───────┘
    {'active': ['df', 'df_main', 'df_tmp'],
    'to_delete': ['df_main', 'df_tmp'],
    'deleted': ['df_main', 'df_tmp'],
    'remaining': ['df'],
    'used_rich': True,
    'memory': {'dataframes_mb': {'before': 30.237445831298828,
    'after': 30.23635482788086,
    'delta': -0.00109100341796875},
    'mode': 'all',
    'process_mb': {'before': 403.5546875, 'after': 403.5546875, 'delta': 0.0}}}

Process RSS reporting requires ``psutil`` and may not immediately decrease
after garbage collection.


Example 7: Programmatic Usage (No Console Output)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Suppress console output and consume the returned summary dictionary directly.

.. code-block:: python

    from eda_toolkit import del_inactive_dataframes

    df_main = pd.DataFrame({"a": range(10)})
    df_tmp = pd.DataFrame({"b": range(100)})

    summary = del_inactive_dataframes(
        ["df_main"],
        del_dataframes=True,
        verbose=False,
        track_memory=True,
        namespace=globals(),
    )

    print(summary)


**Output**

.. code-block:: text

    Returned summary dict:
    {'active': ['df_main', 'df_tmp'], 'to_delete': ['df_tmp'], 'deleted': ['df_tmp'], 
    'remaining': ['df_main'], 'used_rich': False, 'memory': {'dataframes_mb': 
    {'before': 0.00109100341796875, 'after': 0.000202178955078125, 
    'delta': -0.000888824462890625}, 'mode': 'dataframes'}}

This pattern is useful in pipelines, automated scripts, and testing workflows.


**When to Use This Utility**

- Long-lived Jupyter notebooks with many intermediate DataFrames
- Cloud notebooks with limited RAM
- ETL pipelines with staged intermediate results
- Teaching environments where reproducibility and clarity matter
- Any workflow where memory pressure needs to be controlled explicitly

This function is intentionally conservative, explicit, and observable, favoring
safe cleanup over implicit or destructive behavior.



.. [1] Kohavi, R. (1996). *Census Income*. UCI Machine Learning Repository. `https://doi.org/10.24432/C5GP7S <https://doi.org/10.24432/C5GP7S>`_.

