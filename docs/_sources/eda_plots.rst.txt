.. _eda_plots:   

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

Creating Effective Visualizations
==================================

This section focuses on practical strategies and techniques for designing clear 
and impactful visualizations using the diverse plotting tools provided in the EDA Toolkit.

Heuristics for Visualizations
------------------------------

When creating visualizations, there are several key heuristics to keep in mind:

- **Clarity**: The visualization should clearly convey the intended information without 
  ambiguity.
- **Simplicity**: Avoid overcomplicating visualizations with unnecessary elements; focus on 
  the data and insights.
- **Consistency**: Ensure consistent use of colors, shapes, and scales across visualizations 
  to facilitate comparisons.

Methodologies
--------------

The EDA Toolkit supports the following methodologies for creating effective visualizations:

- **KDE and Histograms Plots**: Useful for showing the distribution of a single variable. 
  When combined, these can provide a clearer picture of data density and distribution.

- **Feature Scaling and Outliers**: Identifying outliers is critical for understanding the data's distribution and potential anomalies. 
  The EDA Toolkit offers various methods for outlier detection, including enhanced visualizations using box plots and scatter plots.

- **Stacked Crosstab Plots**: These are used to display multiple data series on the same chart, comparing 
  cumulative quantities across categories. In addition to the visual stacked bar plots, the corresponding 
  crosstab table is printed alongside the visualization, providing detailed numerical insight into how the 
  data is distributed across different categories. This combination allows for both a visual and tabular 
  representation of categorical data, enhancing interpretability.

- **Box and Violin Plots**: Useful for visualizing the distribution of data points, identifying outliers, 
  and understanding the spread of the data. Box plots are particularly effective when visualizing multiple categories 
  side by side, enabling comparisons across groups. Violin plots provide additional insights by showing the 
  distribution's density, giving a fuller picture of the data's distribution shape.

- **Scatter Plots and Best Fit Lines**: Effective for visualizing relationships between two continuous variables. 
  Scatter plots can also be enhanced with regression lines or trend lines to identify relationships more clearly.

- **Correlation Matrices**: Helpful for visualizing the strength of relationships between multiple variables. 
  Correlation heatmaps use color gradients to indicate the degree of correlation, with options for annotating the values directly on the heatmap.


- **Partial Dependence Plots**: Useful for visualizing the relationship between a target variable and one or more features 
  after accounting for the average effect of the other features. These plots are often used in model interpretability 
  to understand how specific variables influence predictions.


Histogram Distribution Plots
=======================================

.. raw:: html

    <a id="plot_distributions"></a>


**Generate histogram and/or density distribution plots (KDE or parametric) for specified columns in a DataFrame.**

The ``plot_distributions`` function is a flexible tool designed for visualizing
the distribution of numerical data using histograms, density plots, or a
combination of both. It supports kernel density estimation (KDE) as well as
parametric probability density functions, and provides extensive control over
plot appearance, layout, scaling, and statistical overlays.

This function is intended for exploratory data analysis where understanding the
shape, spread, and modality of numeric variables is critical.

**Key Features and Parameters**

- **Flexible Plotting**: Supports histogram-only, density-only, or combined
  histogram and density visualizations.
- **Density Estimation**: Density overlays may be rendered using KDE or
  parametric distributions.
- **Customization**: Fine-grained control over colors, binning, layout,
  labels, titles, legends, and font sizes.
- **Scientific Notation Control**: Optional disabling of scientific notation
  on axes for improved readability.
- **Log Scaling**: Supports selective log scaling of variables that span
  multiple orders of magnitude.
- **Output Options**: Supports saving combined figures or per-variable plots
  in PNG or SVG format.

.. function:: plot_distributions(df, vars_of_interest=None, figsize=(5, 5), subplot_figsize=None, hist_color="#0000FF", density_color=None, mean_color="#000000", median_color="#000000", hist_edgecolor="#000000", hue=None, fill=True, fill_alpha=1, n_rows=None, n_cols=None, w_pad=1.0, h_pad=1.0, image_path_png=None, image_path_svg=None, image_filename=None, bbox_inches=None, single_var_image_filename=None, y_axis_label="Density", plot_type="hist", log_scale_vars=None, bins="auto", binwidth=None, label_fontsize=10, tick_fontsize=10, text_wrap=50, disable_sci_notation=False, stat="density", xlim=None, ylim=None, plot_mean=False, plot_median=False, std_dev_levels=None, std_color="#808080", label_names=None, show_legend=True, legend_loc="best", custom_xlabels=None, custom_titles=None, **kwargs)

    :param df: The DataFrame containing the data to plot.
    :type df: pandas.DataFrame
    :param vars_of_interest: List of column names for which to generate distribution plots. If ``'all'``, plots will be generated for all numeric columns.
    :type vars_of_interest: list of str, optional
    :param figsize: Size of each individual plot, default is ``(5, 5)``.
    :type figsize: tuple of int, optional
    :param subplot_figsize: Size of the overall grid of subplots when multiple plots are generated.
    :type subplot_figsize: tuple of int, optional
    :param hist_color: Color of the histogram bars.
    :type hist_color: str, optional
    :param density_color: Color of the density plot. If ``None``, Matplotlib’s default line color is used.
    :type density_color: str, optional
    :param mean_color: Color of the mean line if ``plot_mean`` is True.
    :type mean_color: str, optional
    :param median_color: Color of the median line if ``plot_median`` is True.
    :type median_color: str, optional
    :param hist_edgecolor: Color of the histogram bar edges.
    :type hist_edgecolor: str, optional
    :param hue: Column name to group data by.
    :type hue: str, optional
    :param fill: Whether to fill the histogram bars with color.
    :type fill: bool, optional
    :param fill_alpha: Alpha transparency for histogram fill.
    :type fill_alpha: float, optional
    :param n_rows: Number of rows in the subplot grid.
    :type n_rows: int, optional
    :param n_cols: Number of columns in the subplot grid.
    :type n_cols: int, optional
    :param w_pad: Width padding between subplots.
    :type w_pad: float, optional
    :param h_pad: Height padding between subplots.
    :type h_pad: float, optional
    :param image_path_png: Directory path to save PNG images.
    :type image_path_png: str, optional
    :param image_path_svg: Directory path to save SVG images.
    :type image_path_svg: str, optional
    :param image_filename: Filename to use when saving combined plots.
    :type image_filename: str, optional
    :param bbox_inches: Bounding box used when saving figures.
    :type bbox_inches: str, optional
    :param single_var_image_filename: Filename prefix used when saving per-variable plots.
    :type single_var_image_filename: str, optional
    :param y_axis_label: Label displayed on the y-axis.
    :type y_axis_label: str, optional
    :param plot_type: Type of plot to generate (``'hist'``, ``'density'``, or ``'both'``).
    :type plot_type: str, optional
    :param log_scale_vars: Variable name(s) to apply log scaling.
    :type log_scale_vars: str or list of str, optional
    :param bins: Histogram bin specification.
    :type bins: int or sequence, optional
    :param binwidth: Width of histogram bins.
    :type binwidth: float, optional
    :param label_fontsize: Font size for axis labels and titles.
    :type label_fontsize: int, optional
    :param tick_fontsize: Font size for tick labels.
    :type tick_fontsize: int, optional
    :param text_wrap: Maximum width before wrapping labels or titles.
    :type text_wrap: int, optional
    :param disable_sci_notation: Disable scientific notation on axes.
    :type disable_sci_notation: bool, optional
    :param stat: Aggregate statistic computed per bin.
    :type stat: str, optional
    :param xlim: Limits for the x-axis.
    :type xlim: tuple or list, optional
    :param ylim: Limits for the y-axis.
    :type ylim: tuple or list, optional
    :param plot_mean: Plot the mean as a vertical line.
    :type plot_mean: bool, optional
    :param plot_median: Plot the median as a vertical line.
    :type plot_median: bool, optional
    :param std_dev_levels: Standard deviation levels to plot.
    :type std_dev_levels: list of int, optional
    :param std_color: Color(s) for standard deviation lines.
    :type std_color: str or list of str, optional
    :param label_names: Custom labels for variables.
    :type label_names: dict, optional
    :param show_legend: Whether to display the legend.
    :type show_legend: bool, optional
    :param legend_loc: Location of the legend.
    :type legend_loc: str, optional
    :param custom_xlabels: Custom x-axis labels per variable.
    :type custom_xlabels: dict, optional
    :param custom_titles: Custom titles per variable.
    :type custom_titles: dict, optional
    :param kwargs: Additional keyword arguments passed to the plotting backend.
    :type kwargs: additional keyword arguments

    :raises ValueError:
        - If ``plot_type`` is not one of ``'hist'``, ``'density'``, or ``'both'``.
        - If ``stat`` is not one of ``'count'``, ``'frequency'``, ``'probability'``, ``'proportion'``, ``'percent'``, or ``'density'``.
        - If ``log_scale_vars`` contains variables that are not present in the DataFrame.
        - If ``fill`` is set to ``False`` and ``hist_edgecolor`` or ``fill_alpha`` is specified.
        - If ``bins`` and ``binwidth`` are both specified.
        - If ``subplot_figsize`` is provided when only one plot is being created.

    :raises UserWarning:
        - If both ``bins`` and ``binwidth`` are specified, which may affect performance.

    :returns: ``None``

.. admonition:: Notes

    If you do not set ``n_rows`` or ``n_cols``, the function will automatically
    calculate an optimal subplot layout based on the number of variables being
    plotted.

    To save images, at least one of ``image_path_png`` or ``image_path_svg`` must
    be specified. Saving is triggered by providing ``image_filename`` or
    ``single_var_image_filename``.


\

Deprecation Notice
--------------------------

.. warning::

    ``kde_distributions`` is deprecated and will be removed in a future release.
    Please use ``plot_distributions`` instead. The deprecated function is
    retained only as a thin wrapper for backward compatibility.

    If you continue to use ``kde_distributions``, you will receive a
    ``DeprecationWarning`` indicating that the function is deprecated.


The following summarizes the key changes from ``kde_distributions`` to
``plot_distributions``:

.. admonition:: Updates

    - **Function rename and deprecation**
    
    - ``kde_distributions`` is now deprecated and serves only as a wrapper.
    - ``plot_distributions`` is the new canonical API.
   
    - Density plotting is no longer limited to KDE.
    - Added support for **parametric density overlays** using distributions from ``scipy.stats``.
    - New parameters introduced:
        
        - ``density_function`` to specify KDE and/or parametric distributions.
        - ``density_fit`` to control the fitting method (``'MLE'`` or ``'MM'``).
    
    - ``kde_color`` has been replaced by ``density_color``.
    - If ``density_color=None``, density overlays use **Matplotlib’s default line color** (typically the standard Python blue, ``C0``).
   
    - ``plot_type`` now supports ``'hist'``, ``'density'``, or ``'both'``.
    - Density plots may consist of KDE, parametric fits, or a combination.   
    - Parameter ordering, naming conventions, and documentation style closely follow the original ``kde_distributions`` API.
    - Existing user code calling ``kde_distributions`` continues to work without modification.


.. raw:: html

    <br>


KDE and Histograms Example
--------------------------------

In the example below, the ``plot_distributions`` function is used to generate
histograms for several variables of interest: ``"age"``, ``"education-num"``,
and ``"hours-per-week"``. These variables represent different demographic and
work-related attributes from the dataset. The ``plot_type="both"`` parameter
ensures that density curves are overlaid on the histograms, providing a
smoothed representation of each variable’s distribution.

By default, density overlays are rendered using kernel density estimation (KDE).
In this example, the density curves are explicitly colored red using
``density_color="red"``. If no density color is provided, the function falls
back to Matplotlib’s default line color.

The visualizations are arranged in a single row of three columns, as specified
by ``n_rows=1`` and ``n_cols=3``. The overall size of the subplot grid is set to
14 inches wide and 4 inches tall using ``subplot_figsize=(14, 4)``, ensuring that
each distribution is displayed clearly without overcrowding.

The ``fill=True`` parameter fills the histogram bars with color, while
``fill_alpha=0.60`` applies partial transparency to allow the density overlays
to remain visible. Spacing between subplots is controlled automatically, with
the figure layout tightened using ``bbox_inches="tight"`` when rendering.

To handle longer titles and labels, the ``text_wrap=50`` parameter ensures that
text wraps cleanly onto multiple lines after 50 characters. The variables listed
in ``vars_of_interest`` are passed directly to the function and plotted in the
order provided.

The y-axis for all plots is labeled as ``"Density"`` via ``y_axis_label="Density"``,
reflecting that both the histogram heights and the density curves represent
probability density. The histograms are divided into 10 bins (``bins=10``),
providing a clear and interpretable view of each distribution.

Finally, the font sizes for axis labels and tick labels are set to 16 points
(``label_fontsize=16``) and 14 points (``tick_fontsize=14``), respectively,
ensuring that all text elements remain legible and presentation-ready.



.. code-block:: python

    from eda_toolkit import plot_distributions

    vars_of_interest = [
        "age",
        "education-num",
        "hours-per-week",
    ]

    plot_distributions(
        df=df,
        n_rows=1,
        n_cols=3,
        subplot_figsize=(14, 4),
        fill=True,
        fill_alpha=0.60,
        text_wrap=50,
        density_color="red",
        bbox_inches="tight",
        vars_of_interest=vars_of_interest,
        y_axis_label="Density",
        bins=10,
        plot_type="both",
        label_fontsize=16,
        tick_fontsize=14,
    )

.. raw:: html

   <div class="no-click">

.. image:: ../assets/kde_density_distributions.svg
   :alt: KDE Distributions - KDE (+) Histograms (Density)
   :align: center
   :width: 950px

.. raw:: html

   </div>

.. raw:: html
   
   <div style="height: 50px;"></div>


Histogram Example (Density)
--------------------------------

In this example, the ``plot_distributions()`` function is used to generate histograms for 
the variables ``"age"``, ``"education-num"``, and ``"hours-per-week"`` but with 
``plot_type="hist"``, meaning no KDE plots are included—only histograms are displayed. 
The plots are arranged in a single row of four columns (``n_rows=1, n_cols=3``), 
with a subplot grid size of `14x4 inches` (``subplot_figsize=(14, 4)``). The histograms are 
divided into `10 bins` (``bins=10``), and the ``y-axis`` is labeled "Density" (``y_axis_label="Density"``).
Font sizes for the axis labels and tick labels are set to `16` and `14` points, 
respectively, ensuring clarity in the visualizations. This setup focuses on the 
histogram representation without the KDE overlay.


.. code-block:: python

    from eda_toolkit import plot_distributions

    vars_of_interest = [
        "age",
        "education-num",
        "hours-per-week",
    ]

    plot_distributions(
        df=df,
        n_rows=1,
        n_cols=3,
        subplot_figsize=(14, 4),
        fill=True,
        text_wrap=50,
        bbox_inches="tight",
        vars_of_interest=vars_of_interest,
        y_axis_label="Density",
        bins=10,
        plot_type="hist",
        label_fontsize=16,
        tick_fontsize=14,
    )


.. raw:: html

   <div class="no-click">

.. image:: ../assets/hist_density_distributions.svg
   :alt: KDE Distributions - Histograms (Density)
   :align: center
   :width: 900px

.. raw:: html

   </div>

.. raw:: html
   
   <div style="height: 50px;"></div>


Histogram Example (Count)
--------------------------------

In this example, the ``plot_distributions()`` function is modified to generate histograms 
with a few key changes. The ``hist_color`` is set to `"orange"`, changing the color of the 
histogram bars. The ``y-axis`` label is updated to "Count" (``y_axis_label="Count"``), 
reflecting that the histograms display the count of observations within each bin. 
Additionally, the stat parameter is set to ``"Count"`` to show the actual counts instead of 
densities. The rest of the parameters remain the same as in the previous example, 
with the plots arranged in a single row of four columns (``n_rows=1, n_cols=3``), 
a subplot grid size of `14x4 inches`, and a bin count of `10`. This setup focuses on 
visualizing the raw counts in the dataset using orange-colored histograms.

.. code-block:: python

    from eda_toolkit import plot_distributions

    vars_of_interest = [
        "age",
        "education-num",
        "hours-per-week",
    ]

    plot_distributions(
        df=df,
        n_rows=1,
        n_cols=3,
        subplot_figsize=(14, 4),
        text_wrap=50,
        hist_color="orange",
        bbox_inches="tight",
        vars_of_interest=vars_of_interest,
        y_axis_label="Count",
        bins=10,
        plot_type="hist",
        stat="Count",
        label_fontsize=16,
        tick_fontsize=14,
    )

.. raw:: html

   <div class="no-click">

.. image:: ../assets/count_hist_distributions.svg
   :alt: KDE Distributions - Histograms (Count)
   :align: center
   :width: 900px

.. raw:: html

   </div>

.. raw:: html
   
   <div style="height: 50px;"></div>

Histogram Example - (Mean and Median) 
----------------------------------------

In this example, the ``plot_distributions()`` function is customized to generate 
histograms that include mean and median lines. The ``mean_color`` is set to ``"blue"`` 
and the ``median_color`` is set to ``"black"`` (default), allowing for a clear distinction
between the two statistical measures. The function parameters are adjusted to 
ensure that both the mean and median lines are plotted ``(plot_mean=True, plot_median=True)``. 
The ``y_axis_label`` remains ``"Density"``, indicating that the histograms 
represent the density of observations within each bin. The histogram bars are 
colored using ``hist_color="brown"``, with a ``fill_alpha=0.60`` while the s
tatistical overlays enhance the interpretability of the data. The layout is 
configured with a single row and multiple columns ``(n_rows=1, n_cols=3)``, and 
the subplot grid size is set to `15x5 inches`. This example highlights how to visualize 
central tendencies within the data using a histogram that prominently displays 
the mean and median.

.. code-block:: python

    from eda_toolkit import plot_distributions

    vars_of_interest = [
        "age",
        "education-num",
        "hours-per-week",
    ]

    plot_distributions(
        df=df,
        n_rows=1,
        n_cols=3,
        subplot_figsize=(14, 4),
        text_wrap=50,
        hist_color="brown",
        bbox_inches="tight",
        vars_of_interest=vars_of_interest,
        y_axis_label="Density",
        bins=10,
        fill_alpha=0.60,
        plot_type="hist",
        stat="Density",
        label_fontsize=16,
        tick_fontsize=14,
        plot_mean=True,
        plot_median=True,
        mean_color="blue",
    )

.. raw:: html

   <div class="no-click">

.. image:: ../assets/density_hist_dist_mean_median.svg
   :alt: KDE Distributions - Histograms (Count)
   :align: center
   :width: 900px

.. raw:: html

   </div>

.. raw:: html
   
   <div style="height: 50px;"></div>



Histogram Example - (Mean, Median, and Std. Deviation)
-------------------------------------------------------------

In this example, the ``plot_distributions()`` function is customized to generate 
a histogram that include mean, median, and 3 standard deviation lines. The 
``mean_color`` is set to ``"blue"`` and the median_color is set to ``"black"``, 
allowing for a clear distinction between these two central tendency measures. 
The function parameters are adjusted to ensure that both the mean and median lines 
are plotted ``(plot_mean=True, plot_median=True)``. The ``y_axis_label`` remains
``"Density"``, indicating that the histograms represent the density of observations 
within each bin. The histogram bars are colored using ``hist_color="brown"``, 
with a ``fill_alpha=0.40``, which adjusts the transparency of the fill color. 
Additionally, standard deviation bands are plotted using colors ``"purple"``, 
``"green"``, and ``"silver"`` for one, two, and three standard deviations, respectively.

The layout is configured with a single row and multiple columns ``(n_rows=1, n_cols=3)``, 
and the subplot grid size is set to `15x5 inches`. This setup is particularly useful for 
visualizing the central tendencies within the data while also providing a clear 
view of the distribution and spread through the standard deviation bands. The 
configuration used in this example showcases how histograms can be enhanced with 
statistical overlays to provide deeper insights into the data.

.. note::

    You have the freedom to choose whether to plot the mean, median, and 
    standard deviation lines. You can display one, none, or all of these simultaneously.

.. code-block:: python

    from eda_toolkit import plot_distributions

    vars_of_interest = [
        "age",
    ]

    plot_distributions(
        df=df,
        figsize=(10, 6),
        text_wrap=50,
        hist_color="brown",
        bbox_inches="tight",
        vars_of_interest=vars_of_interest,
        y_axis_label="Density",
        bins=10,
        fill_alpha=0.40,
        plot_type="both",
        stat="Density",
        density_color="red",
        label_fontsize=16,
        tick_fontsize=14,
        plot_mean=True,
        plot_median=True,
        mean_color="blue",
        std_dev_levels=[
            1,
            2,
            3,
        ],
        std_color=[
            "purple",
            "green",
            "silver",
        ],
    )

.. raw:: html

   <div class="no-click">

.. image:: ../assets/density_hist_dist_age.svg
   :alt: KDE Distributions - Histograms (Count)
   :align: center
   :width: 900px

.. raw:: html

   </div>

.. raw:: html
   
   <div style="height: 50px;"></div>


KDE and Parametric Density Fit Example
----------------------------------------

In the example below, the ``plot_distributions`` function is used to visualize the
distribution of several numeric variables, including ``"age"``,
``"education-num"``, and ``"hours-per-week"``. 

The ``plot_type="both"`` parameter instructs the function to render both
histograms and density overlays on the same axes. In this case, the density
overlays include a combination of kernel density estimation (KDE) and two
parametric probability density functions, a normal distribution
(``"norm"``) and a log-normal distribution (``"lognorm"``), specified via
``density_function=["kde", "norm", "lognorm"]``.

Each density overlay is rendered in a distinct color, controlled by
``density_color=["blue", "black", "red"]``, allowing the KDE, normal fit, and
log-normal fit to be visually distinguished. The parametric distributions are
fit using maximum likelihood estimation (``density_fit="MLE"``), providing a
statistically principled comparison between empirical density and theoretical
models.

.. note::

    For a detailed mathematical discussion of kernel density estimation,
    parametric density models, and parameter estimation via the
    **Method of Moments (MoM)** and **Maximum Likelihood Estimation (MLE)**, see
    :ref:`density_parameter_estimation`.


.. code-block:: python

    from eda_toolkit import plot_distributions

    vars_of_interest = [
        "age",
    ]

    plot_distributions(
        df=df,
        vars_of_interest=vars_of_interest,
        # layout
        n_rows=1,
        n_cols=3,
        hue=None,
        hist_color="yellow",
        figsize=(10, 6),
        plot_type="both",  
        stat="density",
        density_function=["kde", "norm", "lognorm"],
        density_color=["blue", "black", "red"],
        density_fit="MLE",
        bins=10,
        fill=True,
        y_axis_label="Density",
        text_wrap=50,
        label_fontsize=16,
        tick_fontsize=14,
        legend_loc="best",
        bbox_inches="tight",
        image_filename="age_distribution_norm_fit",
        image_path_png=image_path_png,
        image_path_svg=image_path_svg,
    )

.. raw:: html

   <div class="no-click">

.. image:: ../assets/age_distribution_density_fit.svg
   :alt: KDE Distributions - Histograms (Count)
   :align: center
   :width: 900px

.. raw:: html

   </div>

.. raw:: html
   
   <div style="height: 50px;"></div>


Grouped Distributions
===========================

.. raw:: html

    <a id="grouped_distributions"></a>


**Plot grouped distributions of numeric features given a binary variable.**

The ``grouped_distributions`` function visualizes how selected numeric features
are distributed grouped by a binary grouping variable (for example, an
outcome label or class membership). For each feature, the distributions of the
two groups are overlaid on the same axis, either as histograms or as filled
kernel density curves.

This function is designed for exploratory analysis, subgroup comparison, and
fairness inspection, where understanding distributional differences between two
groups is critical.

**Supported plot styles:**

- ``"hist"``: Overlaid histograms using shared or independent bins
- ``"density"``: Overlaid filled kernel density estimates (always normalized)

**Normalization behavior:**

- ``normalize="count"``: Raw counts (histograms only)
- ``normalize="density"``: Probability density (histograms or density plots)

.. function:: grouped_distributions(df, features, by, *, bins=30, normalize="density", plot_style="hist", alpha=0.6, colors=None, n_rows=None, n_cols=None, common_bins=True, show_legend=True, legend_loc="best", label_fontsize=12, tick_fontsize=10, text_wrap=50, figsize=(10, 6), image_path_png=None, image_path_svg=None, image_filename=None)

    :param df: Input DataFrame containing the features and grouping variable.
    :type df: pandas.DataFrame

    :param features: List of numeric feature column names to plot.
    :type features: list of str

    :param by: Name of the binary column used to condition the distributions.
        The column must contain exactly two unique, non-null values.
    :type by: str

    :param bins: Number of bins or explicit bin edges for histogram plots.
        Default is ``30``.
    :type bins: int or sequence, optional

    :param normalize: Controls histogram normalization. Options are
        ``"density"`` or ``"count"``. Ignored for density plots, which always
        use probability density.
    :type normalize: str, optional

    :param plot_style: Plot type to generate. Options are ``"hist"`` or
        ``"density"``. Default is ``"hist"``.
    :type plot_style: str, optional

    :param alpha: Transparency level for histogram bars or density fills.
        Default is ``0.6``.
    :type alpha: float, optional

    :param colors: Mapping from group value to color. Keys must match the two
        unique values in the ``by`` column. If ``None``, a default color scheme
        is used.
    :type colors: dict, optional

    :param n_rows: Number of subplot rows. If ``None``, determined automatically.
    :type n_rows: int, optional

    :param n_cols: Number of subplot columns. If ``None``, determined automatically.
    :type n_cols: int, optional

    :param common_bins: If ``True``, both groups share identical histogram bin
        edges. Ignored for density plots.
    :type common_bins: bool, optional

    :param show_legend: Whether to display a legend identifying the two groups.
        Default is ``True``.
    :type show_legend: bool, optional

    :param legend_loc: Legend placement passed directly to Matplotlib.
        Default is ``"best"``.
    :type legend_loc: str, optional

    :param label_fontsize: Font size for axis labels and titles.
    :type label_fontsize: int, optional

    :param tick_fontsize: Font size for tick labels and legend text.
    :type tick_fontsize: int, optional

    :param text_wrap: Maximum character width before wrapping titles.
    :type text_wrap: int, optional

    :param figsize: Size of the overall figure in inches.
        Default is ``(10, 6)``.
    :type figsize: tuple of int, optional

    :param image_path_png: Directory path to save the figure as a PNG file.
    :type image_path_png: str, optional

    :param image_path_svg: Directory path to save the figure as an SVG file.
    :type image_path_svg: str, optional

    :param image_filename: Base filename (without extension) for saving the figure.
    :type image_filename: str, optional

    :raises ValueError:
        - If the ``by`` column is not binary.
        - If ``plot_style`` is not one of ``"hist"`` or ``"density"``.
        - If ``normalize`` is not one of ``"density"`` or ``"count"``.
        - If ``plot_style="density"`` and ``normalize!="density"``.
        - If ``image_filename`` is provided but neither
          ``image_path_png`` nor ``image_path_svg`` is specified.
        - If the subplot grid is too small for the number of features.

    :returns: ``None``

.. admonition:: Notes

    - All grouped distributions are plotted as overlays on a single axis
      per feature.
    - Density plots always represent probability density and do not support
      count-based normalization.
    - When ``common_bins=True``, histogram bin edges are computed jointly across
      both groups to enable direct shape comparison.
    - Font sizes are specified in absolute points and may appear small on large
      figures or dense subplot grids.

Grouped Density Plot Example
-------------------------------------

In the example below, the ``grouped_distributions`` function is used to compare
the distributions of several numeric features conditioned on income category.
The grouping variable ``"income"`` is binary (``"<=50K"`` vs ``">50K"``), making
it suitable for grouped overlay plots.

The selected features include demographic and financial attributes:

- ``"age"``
- ``"education-num"``
- ``"hours-per-week"``

The ``plot_style="density"`` option instructs the function to render **filled
kernel density estimates** for each group rather than histograms. Density plots
are always normalized, allowing direct comparison of distributional shape even
when group sizes differ substantially.

Custom colors are explicitly provided via the ``colors`` argument to ensure
consistent visual identification of income groups across all features. The
``alpha=0.6`` parameter applies partial transparency, making overlapping density
regions easier to interpret.

The resulting figure is saved in both PNG and SVG formats using a shared base
filename.

.. code-block:: python

    from eda_toolkit.plots import grouped_distributions

    features = [
        "age",
        "education-num",
        "hours-per-week",
    ]

    group_colors = {
        "<=50K": "black",  # black
        ">50K": "orange",  # orange
    }

    grouped_distributions(
        df=df,
        features=features,
        by="income",
        bins=30,
        colors=group_colors,
        n_rows=1,
        normalize="density",
        alpha=0.6,
        figsize=(14, 4),
        plot_style="density",
        image_path_png=image_path_png,
        image_path_svg=image_path_svg,
        image_filename="grouped_distributions_adult_income",
        label_fontsize=16,
        tick_fontsize=14,
    )

.. raw:: html

   <div class="no-click">

.. image:: ../assets/grouped_dist_adult_income.svg
   :alt: Grouped Histograms with Income Groups
   :align: center
   :width: 900px

.. raw:: html

   </div>

.. raw:: html
   
   <div style="height: 50px;"></div>


Grouped Histogram Plot Example
--------------------------------------

In this example, the ``grouped_distributions`` function is used to visualize
**overlaid grouped histograms** for several numeric features, grouped by
income category. As in the previous example, the grouping variable ``"income"``
is binary (``"<=50K"`` vs ``">50K"``), enabling direct comparison between the two
subpopulations.

Unlike density-based plots, this example uses
``plot_style="hist"``, which renders **binned histograms** rather than smoothed
kernel density estimates. This representation emphasizes the **empirical mass
and frequency structure** of each feature, making it easier to identify discrete
concentration, skewness, and potential outliers.

The histograms are normalized to probability density
(``normalize="density"``), ensuring that the total area under each group’s
histogram integrates to one. This allows meaningful comparison of distribution
shapes even when the two income groups differ in sample size.

A shared binning strategy is used by default, ensuring that both income groups
are evaluated against identical bin edges for each feature. Custom group colors
are applied consistently across all subplots to maintain interpretability.

The resulting figure is saved in both PNG and SVG formats for downstream use in
reports or publications.

.. code-block:: python

    from eda_toolkit.plots import grouped_distributions

    features = [
        "age",
        "education-num",
        "hours-per-week",
    ]

    group_colors = {
        "<=50K": "black",  
        ">50K": "orange",  
    }

    grouped_distributions(
        df=df,
        features=features,
        by="income",
        bins=30,
        n_rows=1,
        colors=group_colors,
        normalize="density",
        alpha=0.6,
        figsize=(14, 4),
        plot_style="hist",
        image_path_png=image_path_png,
        image_path_svg=image_path_svg,
        image_filename="cond_histograms_adult_income_hist",
        label_fontsize=16,
        tick_fontsize=14,
    )

.. raw:: html

   <div class="no-click">

.. image:: ../assets/grouped_dist_adult_income_hist.svg
   :alt: Grouped Histograms with Income Groups
   :align: center
   :width: 900px

.. raw:: html

   </div>

.. raw:: html
   
   <div style="height: 50px;"></div>


Distribution Goodness-of-Fit Plots
=======================================

Generate goodness-of-fit (GOF) diagnostic plots to compare empirical data against 
fitted theoretical distributions or an empirical reference sample.

The ``distribution_gof_plots`` function provides distributional diagnostics to 
evaluate how well one or more candidate probability distributions fit a variable 
from a DataFrame. It supports both theoretical (parametric) comparisons, where 
distribution parameters are estimated via Maximum Likelihood Estimation (MLE) or 
Method of Moments (MM), and empirical QQ comparisons, where sample quantiles are 
compared directly to a reference dataset.

The function currently supports the following diagnostic visualizations:

- Quantile-Quantile (QQ) plots for assessing agreement between quantiles

- CDF-based plots, including optional exceedance (survival) curves via tail control

.. note:: 

    For a detailed mathematical discussion of kernel density estimation, parametric
    density models, and parameter estimation via the **Method of Moments (MoM)** and
    **Maximum Likelihood Estimation (MLE)**, see :ref:`density_parameter_estimation`.


.. function:: distribution_gof_plots(df, var, dist="norm", fit_method="MLE", plot_types=("qq", "cdf"), qq_type="theoretical", reference_data=None, scale="linear", tail="both", figsize=(6, 5), xlim=None, ylim=None, show_reference=True, label_fontsize=10, tick_fontsize=10, legend_loc="best", text_wrap=50, palette=None, image_path_png=None, image_path_svg=None, image_filename=None)

    Generate goodness-of-fit (GOF) diagnostic plots for comparing empirical data
    to theoretical or empirical reference distributions.

    :param df: Input DataFrame containing the data.
    :type df: pandas.DataFrame

    :param var: Column name in ``df`` to evaluate.
    :type var: str

    :param dist: Distribution name(s) to evaluate. Each entry must correspond to a valid continuous distribution in ``scipy.stats`` (e.g., ``"norm"``, ``"lognorm"``, ``"gamma"``).
    :type dist: str or list of str, optional

    :param fit_method: Parameter estimation method for theoretical distributions. Options are:
        - ``"MLE"``: maximum likelihood estimation
        - ``"MM"``: method of moments
    :type fit_method: {"MLE", "MM"}, optional

    :param plot_types: Diagnostic plot type(s) to generate. Options are:
        - ``"qq"``: quantile-quantile plot
        - ``"cdf"``: cumulative distribution function plot (with exceedance behavior controlled by ``tail``)
    :type plot_types: str or list of {"qq", "cdf"}, optional

    :param qq_type: Type of QQ plot to generate:
        - ``"theoretical"``: sample quantiles vs fitted theoretical distribution
        - ``"empirical"``: sample quantiles vs reference empirical distribution
    :type qq_type: {"theoretical", "empirical"}, optional

    :param reference_data: Reference empirical sample used when ``qq_type="empirical"``. Required for empirical QQ plots and ignored otherwise. Must contain at least two observations.
    :type reference_data: numpy.ndarray, optional

    :param scale: Scale applied to the y-axis of applicable plots.
    :type scale: {"linear", "log"}, optional

    :param tail: Tail behavior for CDF-based plots:
        - ``"lower"``: plot CDF only
        - ``"upper"``: plot exceedance probability (``1 - CDF``) only
        - ``"both"``: plot both CDF and exceedance curves
    :type tail: {"lower", "upper", "both"}, optional

    :param figsize: Base figure size (width, height) for each diagnostic plot. When multiple plot types are requested, the total width scales by the number of plots.
    :type figsize: tuple of int, optional

    :param xlim: Limits for the x-axis as (min, max). Applied after all distributions are drawn to ensure consistent scaling.
    :type xlim: tuple of (float, float), optional

    :param ylim: Limits for the y-axis as (min, max). Applied after all distributions are drawn to ensure consistent scaling.
    :type ylim: tuple of (float, float), optional

    :param show_reference: Whether to draw a reference (identity) line on theoretical QQ plots. Ignored for empirical QQ plots.
    :type show_reference: bool, optional

    :param label_fontsize: Font size for axis labels and titles.
    :type label_fontsize: int, optional

    :param tick_fontsize: Font size for tick labels.
    :type tick_fontsize: int, optional

    :param legend_loc: Legend placement passed to Matplotlib (e.g., ``"best"``, ``"upper right"``, ``"lower left"``).
    :type legend_loc: str, optional

    :param text_wrap: Maximum character width for wrapping titles and labels.
    :type text_wrap: int, optional

    :param palette: Mapping from distribution name to color. Keys must match the entries in ``dist``.
    :type palette: dict of {str: str}, optional

    :param image_path_png: Directory path for saving PNG output.
    :type image_path_png: str, optional

    :param image_path_svg: Directory path for saving SVG output.
    :type image_path_svg: str, optional

    :param image_filename: Base filename used when saving plots (without extension).
    :type image_filename: str, optional

    :raises ValueError:
        - If ``plot_types`` contains invalid values (valid: ``"qq"``, ``"cdf"``).
        - If ``qq_type`` is not one of ``"theoretical"`` or ``"empirical"``.
        - If ``scale`` is not one of ``"linear"`` or ``"log"``.
        - If ``tail`` is not one of ``"lower"``, ``"upper"``, or ``"both"``.
        - If ``palette`` is provided but does not define colors for every distribution in ``dist``.
        - If ``qq_type="empirical"`` is used without valid ``reference_data`` (must be provided and contain at least two observations).
        - If ``image_filename`` is provided but neither ``image_path_png`` nor ``image_path_svg`` is specified.

    :returns: ``None``



Theoretical QQ Plot Example
----------------------------

In the example below, the ``distribution_gof_plots`` function is used to generate
**theoretical quantile–quantile (QQ) plots** for the variable ``"age"``. The goal
is to assess how well several candidate parametric distributions fit the empirical
data.

Three commonly used continuous distributions are evaluated:

- Normal distribution (``"norm"``)
- Log-normal distribution (``"lognorm"``)
- Gamma distribution (``"gamma"``)

Each distribution is fit to the data using the default **maximum likelihood
estimation (MLE)** procedure. The ``plot_types="qq"`` argument instructs the
function to generate only QQ plots, while ``qq_type="theoretical"`` specifies that
sample quantiles should be compared against quantiles derived from the fitted
theoretical distributions.

A reference identity line is included via ``show_reference=True``, allowing for
direct visual assessment of deviations from the ideal 1:1 relationship. If the
empirical data follow a given distribution closely, the corresponding points will
align tightly along this reference line.

Distinct colors are assigned to each fitted distribution using the ``palette``
parameter, making it easy to visually compare goodness-of-fit across models. Axis
limits are constrained using ``xlim`` and ``ylim`` to focus the comparison on a
relevant range of values and ensure consistent scaling.

The resulting figure is saved in both PNG and SVG formats using the provided output
paths and filename.

.. code-block:: python

    from eda_toolkit import distribution_gof_plots

    distribution_gof_plots(
        df,
        var="age",
        dist=["norm", "lognorm", "gamma"],
        plot_types="qq",
        qq_type="theoretical",
        show_reference=True,
        image_path_png=image_path_png,
        image_path_svg=image_path_svg,
        palette={
            "norm": "tab:blue",
            "lognorm": "tab:orange",
            "gamma": "tab:green",
        },
        image_filename="gof_qq_age_adult_income",
        xlim=(5, 100),
        ylim=(5, 100),
    )

**Interpretation**

- Points closely following the diagonal reference line indicate a strong agreement
  between the empirical distribution and the theoretical model.
- Systematic curvature suggests skewness or variance mismatches.
- Deviations in the tails highlight poor tail behavior, which is often critical in
  risk modeling, reliability analysis, and anomaly detection contexts.

This diagnostic provides a fast, visual comparison of multiple candidate
distributions and is typically used as a first-pass validation step before making
distributional assumptions in downstream modeling.


.. raw:: html

   <div class="no-click">

.. image:: ../assets/gof_qq_age_adult_income.png
   :alt: Grouped Histograms with Income Groups
   :align: center
   :width: 500px

.. raw:: html

   </div>

.. raw:: html
   
   <div style="height: 50px;"></div>


Empirical QQ Plot Example (Sample vs Reference Data)
-----------------------------------------------------

In this example, the ``distribution_gof_plots`` function is used to generate an
**empirical quantile–quantile (QQ) plot**, comparing the distribution of a target
sample against a **reference empirical distribution**, rather than against a
theoretical model.

Unlike theoretical QQ plots, which compare sample quantiles to quantiles derived
from a fitted parametric distribution, **empirical QQ plots compare quantiles
between two observed samples directly**. This makes them particularly useful for
distributional comparisons across subpopulations, cohorts, or time periods.

Here, the variable ``"age"`` is analyzed for the full dataset and compared against
a reference sample consisting only of observations where ``sex == "Male"``. The
reference data are extracted explicitly and passed via the ``reference_data``
parameter.

Although a distribution name (``"norm"``) is still required for labeling purposes,
**no theoretical distribution is involved in the QQ geometry** when
``qq_type="empirical"``. Instead, matched empirical quantiles from the sample and
reference data are plotted against one another.

.. code-block:: python

    reference_data = df.loc[df["sex"] == "Male", "age"].dropna().values

    from eda_toolkit import distribution_gof_plots

    distribution_gof_plots(
        df,
        var="age",
        dist="norm",
        plot_types="qq",
        qq_type="empirical",
        reference_data=reference_data,
    )

**Interpretation**

- Points lying close to the diagonal indicate that the sample and reference
  distributions are similar across quantiles.
- Systematic deviations from the diagonal reveal distributional shifts, such as
  differences in central tendency, spread, or tail behavior.
- Curvature in the upper or lower quantiles highlights differences in tail
  behavior between the two samples.

Empirical QQ plots are especially valuable for **fairness analysis**, **cohort
comparison**, and **data drift detection**, where direct comparison between groups
is preferred over assumptions of parametric form.

.. raw:: html

   <div class="no-click">

.. image:: ../assets/gof_qq_age_adult_income_empirical_reference.svg
   :alt: Goodness of Fit Empirical QQ Plot
   :align: center
   :width: 500px

.. raw:: html

   </div>

.. raw:: html
   
   <div style="height: 50px;"></div>


CDF Plot Example (Lower and Upper Tails)
----------------------------------------

In this example, the ``distribution_gof_plots`` function is used to generate
**cumulative distribution function (CDF) plots** for the variable ``"age"``,
including both the **lower tail (CDF)** and **upper tail (exceedance probability)**.

Two candidate parametric distributions are evaluated:

- Normal distribution (``"norm"``)
- Log-normal distribution (``"lognorm"``)

The ``plot_types="cdf"`` argument instructs the function to produce CDF-based
diagnostics, while the default ``tail="both"`` setting ensures that **both the
CDF and exceedance curves** are plotted simultaneously. This dual representation
provides a complete view of the distribution’s behavior across the full range of
values.

The CDF curves illustrate the probability that the random variable takes on a
value less than or equal to a given threshold, while the exceedance curves
(``1 − CDF``) highlight the probability of observing values greater than that
threshold. This is especially useful for understanding **upper-tail risk** and
extreme-value behavior.

All plots are rendered on a linear scale, making it easier to compare overall
distributional shape and mid-range behavior between candidate models.

.. code-block:: python

    from eda_toolkit import distribution_gof_plots

    distribution_gof_plots(
        df,
        var="age",
        dist=["norm", "lognorm"],
        plot_types="cdf",
    )

**Interpretation**

- CDF curves that rise more quickly indicate distributions with greater mass at
  lower values.
- Exceedance curves that decay more slowly suggest heavier upper tails and higher
  probability of extreme observations.
- Differences between the normal and log-normal fits are most pronounced in the
  tails, where modeling assumptions often matter most.

CDF and exceedance plots are particularly valuable in **risk analysis**,
**threshold-based decision-making**, and **model selection**, where understanding
tail behavior is as important as central tendency.


.. raw:: html

   <div class="no-click">

.. image:: ../assets/gof_cdf_age_adult_income_empirical_reference.svg
   :alt: Goodness of Fit Empirical QQ Plot
   :align: center
   :width: 500px

.. raw:: html

   </div>

.. raw:: html
   
   <div style="height: 50px;"></div>

Feature Scaling and Outliers
=============================

.. function:: data_doctor(df, feature_name, data_fraction=1, scale_conversion=None, scale_conversion_kws=None, apply_cutoff=False, lower_cutoff=None, upper_cutoff=None, show_plot=True, plot_type="all", figsize=(18, 6), xlim=None, kde_ylim=None, hist_ylim=None, box_violin_ylim=None, save_plot=False, image_path_png=None, image_path_svg=None, apply_as_new_col_to_df=False, kde_kws=None, hist_kws=None, box_violin_kws=None, box_violin="boxplot", label_fontsize=12, tick_fontsize=10, random_state=None)

    Analyze and transform a specific feature in a DataFrame, with options for
    scaling, applying cutoffs, and visualizing the results. This function also
    allows for the creation of a new column with the transformed data if
    specified. Plots can be saved in PNG or SVG format with filenames that
    incorporate the ``plot_type``, ``feature_name``, ``scale_conversion``, and
    ``cutoff`` if cutoffs are applied.

    :param df: The DataFrame containing the feature to analyze.
    :type df: pandas.DataFrame

    :param feature_name: The name of the feature (column) to analyze.
    :type feature_name: str

    :param data_fraction: Fraction of the data to analyze. Default is ``1`` (full dataset). Useful for large datasets where a sample can represent the population. If ``apply_as_new_col_to_df=True``, the full dataset is used (``data_fraction=1``).
    :type data_fraction: float, optional

    :param scale_conversion: Type of conversion to apply to the feature. Options include:
    
        - ``'abs'``: Absolute values
        - ``'log'``: Natural logarithm
        - ``'sqrt'``: Square root
        - ``'cbrt'``: Cube root
        - ``'reciprocal'``: Reciprocal transformation
        - ``'stdrz'``: Standardized (z-score)
        - ``'minmax'``: Min-Max scaling
        - ``'boxcox'``: Box-Cox transformation (positive values only; supports
          ``lmbda`` for specific lambda or ``alpha`` for confidence interval)
        - ``'robust'``: Robust scaling (median and IQR)
        - ``'maxabs'``: Max-abs scaling
        - ``'exp'``: Exponential transformation
        - ``'logit'``: Logit transformation (values between 0 and 1)
        - ``'arcsinh'``: Inverse hyperbolic sine
        - ``'square'``: Squaring the values
        - ``'power'``: Power transformation (Yeo-Johnson).
    :type scale_conversion: str, optional

    :param scale_conversion_kws: Additional keyword arguments to pass to the scaling functions, such as:
    
        - ``'alpha'`` for Box-Cox transformation (returns a confidence interval
          for lambda)
        - ``'lmbda'`` for a specific Box-Cox transformation value
        - ``'quantile_range'`` for robust scaling.
    :type scale_conversion_kws: dict, optional

    :param apply_cutoff: Whether to apply upper and/or lower cutoffs to the feature.
    :type apply_cutoff: bool, optional (default=False)

    :param lower_cutoff: Lower bound to apply if ``apply_cutoff=True``.
    :type lower_cutoff: float, optional

    :param upper_cutoff: Upper bound to apply if ``apply_cutoff=True``.
    :type upper_cutoff: float, optional

    :param show_plot: Whether to display plots of the transformed feature: KDE, histogram, and boxplot/violinplot.
    :type show_plot: bool, optional (default=True)

    :param plot_type: Specifies the type of plot(s) to produce. Options are:
    
        - ``'all'``: Generates KDE, histogram, and boxplot/violinplot.
        - ``'kde'``: KDE plot only.
        - ``'hist'``: Histogram plot only.
        - ``'box_violin'``: Boxplot or violin plot only (specified by
          ``box_violin``).

        If a list or tuple is provided (e.g., ``plot_type=["kde", "hist"]``),
        the specified plots are displayed in a single row with sufficient
        spacing. A ``ValueError`` is raised if an invalid plot type is included.
    :type plot_type: str, list, or tuple, optional (default="all")

    :param figsize: Specifies the figure size for the plots. This applies to all plot types, including single plots (when ``plot_type`` is set to "kde", "hist", or "box_violin") and multi-plot layout when ``plot_type`` is "all".
    :type figsize: tuple or list, optional (default=(18, 6))

    :param xlim: Limits for the x-axis in all plots, specified as ``(xmin, xmax)``.
    :type xlim: tuple or list, optional

    :param kde_ylim: Limits for the y-axis in the KDE plot, specified as ``(ymin, ymax)``.
    :type kde_ylim: tuple or list, optional

    :param hist_ylim: Limits for the y-axis in the histogram plot, specified as ``(ymin, ymax)``.
    :type hist_ylim: tuple or list, optional

    :param box_violin_ylim: Limits for the y-axis in the boxplot or violin plot, specified as ``(ymin, ymax)``.
    :type box_violin_ylim: tuple or list, optional

    :param save_plot: Whether to save the plots as PNG and/or SVG images. If ``True``, the user must specify at least one of ``image_path_png`` or ``image_path_svg``, otherwise a ``ValueError`` is raised.
    :type save_plot: bool, optional (default=False)

    :param image_path_png: Directory path to save the plot as a PNG file. Only used if ``save_plot=True``.
    :type image_path_png: str, optional

    :param image_path_svg: Directory path to save the plot as an SVG file. Only used if ``save_plot=True``.
    :type image_path_svg: str, optional

    :param apply_as_new_col_to_df: Whether to create a new column in the DataFrame with the transformed values. If ``True``, the new column name is generated based on the feature name and the transformation applied:
    
        - ``<feature_name>_<scale_conversion>``: If a transformation is applied.
        - ``<feature_name>_w_cutoff``: If only cutoffs are applied.
        
        For Box-Cox transformation, if ``alpha`` is specified, the confidence interval for lambda is displayed. If ``lmbda`` is specified, the lambda value is displayed.
    :type apply_as_new_col_to_df: bool, optional (default=False)

    :param kde_kws: Additional keyword arguments to pass to the KDE plot (``seaborn.kdeplot``).
    :type kde_kws: dict, optional

    :param hist_kws: Additional keyword arguments to pass to the histogram plot (``seaborn.histplot``).
    :type hist_kws: dict, optional

    :param box_violin_kws: Additional keyword arguments to pass to either boxplot or violinplot.
    :type box_violin_kws: dict, optional

    :param box_violin: Specifies whether to plot a ``boxplot`` or ``violinplot`` if ``plot_type`` is set to ``box_violin``.
    :type box_violin: str, optional (default="boxplot")

    :param label_fontsize: Font size for the axis labels and plot titles.
    :type label_fontsize: int, optional (default=12)

    :param tick_fontsize: Font size for the tick labels on both axes.
    :type tick_fontsize: int, optional (default=10)

    :param random_state: Seed for reproducibility when sampling the data.
    :type random_state: int, optional

    :returns: ``None`` 
        Displays the feature's descriptive statistics, quartile information,
        and outlier details. If a new column is created, confirms the addition to the DataFrame. For Box-Cox, either the lambda or its confidence interval is displayed.

    :raises ValueError: 
        - If an invalid ``scale_conversion`` is provided.
        - If Box-Cox transformation is applied to non-positive values.
        - If ``save_plot=True`` but neither ``image_path_png`` nor ``image_path_svg`` is provided.
        - If an invalid option is provided for ``box_violin``.
        - If an invalid option is provided for ``plot_type``.
        - If the length of transformed data does not match the original feature length.

    .. note::  
        
        When saving plots, the filename will include the ``feature_name``, ``scale_conversion``, each selected ``plot_type``, and, if cutoffs are applied, ``"_cutoff"``. For example, if ``feature_name`` is ``"age"``, ``scale_conversion`` is ``"boxcox"``, and ``plot_type`` is ``"kde"``, with cutoffs applied, the filename will be: ``age_boxcox_kde_cutoff.png`` or ``age_boxcox_kde_cutoff.svg``.


Available Scale Conversions
-----------------------------

The ``scale_conversion`` parameter accepts several options for data scaling, providing flexibility in how you preprocess your data. Each option addresses specific transformation needs, such as normalizing data, stabilizing variance, or adjusting data ranges. Below is the exhaustive list of available scale conversions:

- ``'abs'``: Takes the absolute values of the data, removing any negative signs.
- ``'log'``: Applies the natural logarithm to the data, useful for compressing large ranges and reducing skewness.
- ``'sqrt'``: Applies the square root transformation, often used to stabilize variance.
- ``'cbrt'``: Takes the cube root of the data, which can be useful for transforming both positive and negative values symmetrically.
- ``'stdrz'``: Standardizes the data to have a mean of 0 and a standard deviation of 1, also known as z-score normalization.
- ``'minmax'``: Rescales the data to a specified range, defaulting to [0, 1], ensuring that all values fall within this range.
- ``'boxcox'``: Applies the Box-Cox transformation to stabilize variance and make the data more normally distributed. Only works with positive values and supports passing ``lmbda`` or ``alpha`` for flexibility.
- ``'robust'``: Scales the data based on percentiles (such as the interquartile range), which reduces the influence of outliers.
- ``'maxabs'``: Scales the data by dividing it by its maximum absolute value, preserving the sign of the data while constraining it to the range [-1, 1].
- ``'reciprocal'``: Transforms the data by taking the reciprocal (1/x), which is useful when handling values that are far from zero.
- ``'exp'``: Applies the exponential function to the data, which is useful for modeling exponential growth or increasing the impact of large values.
- ``'logit'``: Applies the logit transformation to data, which is only valid for values between 0 and 1. This is typically used in logistic regression models.
- ``'arcsinh'``: Applies the inverse hyperbolic sine transformation, which is similar to the logarithm but can handle both positive and negative values.
- ``'square'``: Squares the values of the data, effectively emphasizing larger values while downplaying smaller ones.
- ``'power'``: Applies the power transformation (Yeo-Johnson), which is similar to Box-Cox but works for both positive and negative values.

``boxcox`` is just one of the many options available for transforming data in the ``data_doctor`` function, providing versatility to handle different scaling needs.

.. _Box_Cox_Example_1:

Box-Cox Transformation Example 1
----------------------------------

In this example from the US Census dataset [1]_, we demonstrate the usage of the ``data_doctor`` 
function to apply a **Box-Cox transformation** to the ``age`` column in a DataFrame. 
The ``data_doctor`` function provides a flexible way to preprocess data by applying 
various scaling techniques. In this case, we apply the Box-Cox transformation **without any tuning** 
of the ``alpha`` or ``lambda`` parameters, allowing the function to handle the transformation in a 
barebones approach. You can also choose other scaling conversions from the list of available 
options (such as ``'minmax'``, ``'standard'``, ``'robust'``, etc.), depending on your needs.


.. code-block:: python

   from eda_toolkit import data_doctor

   data_doctor(
       df=df,
       feature_name="age",
       data_fraction=0.6,
       scale_conversion="boxcox",
       apply_cutoff=False,
       lower_cutoff=None,
       upper_cutoff=None,
       show_plot=True,
       apply_as_new_col_to_df=True,
       random_state=111,
   )

.. code-block:: text

                DATA DOCTOR SUMMARY REPORT             
    +------------------------------+--------------------+
    | Feature                      | age                |
    +------------------------------+--------------------+
    | Statistic                    | Value              |
    +------------------------------+--------------------+
    | Min                          |             3.6664 |
    | Max                          |             6.8409 |
    | Mean                         |             5.0163 |
    | Median                       |             5.0333 |
    | Std Dev                      |             0.6761 |
    +------------------------------+--------------------+
    | Quartile                     | Value              |
    +------------------------------+--------------------+
    | Q1 (25%)                     |             4.5219 |
    | Q2 (50% = Median)            |             5.0333 |
    | Q3 (75%)                     |             5.5338 |
    | IQR                          |             1.0119 |
    +------------------------------+--------------------+
    | Outlier Bound                | Value              |
    +------------------------------+--------------------+
    | Lower Bound                  |             3.0040 |
    | Upper Bound                  |             7.0517 |
    +------------------------------+--------------------+

    New Column Name: age_boxcox
    Box-Cox Lambda: 0.1748

.. raw:: html

   <div class="no-click">

.. image:: ../assets/age_boxcox_kde_hist_boxplot.svg
   :alt: Box-Cox Transformation W/ Data Doctor
   :align: center
   :width: 900px

.. raw:: html

   </div>

.. raw:: html
   
   <div style="height: 50px;"></div>

.. code-block:: python

    df.head()

.. raw:: html

    <style type="text/css">
    .tg-wrap {
      width: 100%;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
    }
    .tg  {border-collapse:collapse;border-spacing:0;margin:0px auto;}
    .tg td{border-color:black;border-style:solid;border-width:1px;font-family:monospace, sans-serif !important;font-size:11px !important;
      overflow:hidden;padding:0px 5px;word-break:normal;}
    .tg th{border-color:black;border-style:solid;border-width:1px;font-family:monospace, sans-serif !important;font-size:11px !important;
      font-weight:normal;overflow:hidden;padding:0px 5px;word-break:normal;}
    .tg .tg-zv4m{border-color:#ffffff;text-align:left;vertical-align:top}
    .tg .tg-8jgo{border-color:#ffffff;text-align:center;vertical-align:top}
    .tg .tg-aw21{border-color:#ffffff;font-weight:bold;text-align:center;vertical-align:top}
    .tg .tg-lightpink{background-color:#FFCCCC; border-width: 0px;} /* Remove borders and apply solid pink color */
    </style>
    <div class="tg-wrap">
    <table class="tg">
      <thead>
        <tr>
          <th class="tg-zv4m"></th>
          <th class="tg-aw21">age</th>
          <th class="tg-aw21">workclass</th>
          <th class="tg-aw21">education</th>
          <th class="tg-aw21">education-num</th>
          <th class="tg-aw21">marital-status</th>
          <th class="tg-aw21">occupation</th>
          <th class="tg-aw21">relationship</th>
          <th class="tg-aw21 tg-lightpink">age_boxcox</th> <!-- Highlighted column -->
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
          <td class="tg-8jgo tg-lightpink"></td>
        </tr>
        <tr>
          <td class="tg-zv4m">582248222</td>
          <td class="tg-8jgo">39</td>
          <td class="tg-8jgo">State-gov</td>
          <td class="tg-8jgo">Bachelors</td>
          <td class="tg-8jgo">13</td>
          <td class="tg-8jgo">Never-married</td>
          <td class="tg-8jgo">Adm-clerical</td>
          <td class="tg-8jgo">Not-in-family</td>
          <td class="tg-8jgo tg-lightpink">5.180807</td>
        </tr>
        <tr>
          <td class="tg-zv4m">561810758</td>
          <td class="tg-8jgo">50</td>
          <td class="tg-8jgo">Self-emp-not-inc</td>
          <td class="tg-8jgo">Bachelors</td>
          <td class="tg-8jgo">13</td>
          <td class="tg-8jgo">Married-civ-spouse</td>
          <td class="tg-8jgo">Exec-managerial</td>
          <td class="tg-8jgo">Husband</td>
          <td class="tg-8jgo tg-lightpink">5.912323</td>
        </tr>
        <tr>
          <td class="tg-zv4m">598098459</td>
          <td class="tg-8jgo">38</td>
          <td class="tg-8jgo">Private</td>
          <td class="tg-8jgo">HS-grad</td>
          <td class="tg-8jgo">9</td>
          <td class="tg-8jgo">Divorced</td>
          <td class="tg-8jgo">Handlers-cleaners</td>
          <td class="tg-8jgo">Not-in-family</td>
          <td class="tg-8jgo tg-lightpink">5.227960</td>
        </tr>
        <tr>
          <td class="tg-zv4m">776705221</td>
          <td class="tg-8jgo">53</td>
          <td class="tg-8jgo">Private</td>
          <td class="tg-8jgo">11th</td>
          <td class="tg-8jgo">7</td>
          <td class="tg-8jgo">Married-civ-spouse</td>
          <td class="tg-8jgo">Handlers-cleaners</td>
          <td class="tg-8jgo">Husband</td>
          <td class="tg-8jgo tg-lightpink">6.389562</td>
        </tr>
        <tr>
          <td class="tg-zv4m">479262902</td>
          <td class="tg-8jgo">28</td>
          <td class="tg-8jgo">Private</td>
          <td class="tg-8jgo">Bachelors</td>
          <td class="tg-8jgo">13</td>
          <td class="tg-8jgo">Married-civ-spouse</td>
          <td class="tg-8jgo">Prof-specialty</td>
          <td class="tg-8jgo">Wife</td>
          <td class="tg-8jgo tg-lightpink">3.850675</td>
        </tr>
      </tbody>
    </table>
    </div>

\

.. note::

    Notice that the :ref:`unique identifiers <Adding_Unique_Identifiers>` function was also applied on the dataframe to generate randomized census IDs for the rows of the data.

**Explanation**

- ``df=df``: We are passing ``df`` as the input DataFrame.
- ``feature_name="age"``: The feature we are transforming is ``age``.
- ``data_fraction=1``: We are using 100% of the data in the ``age`` column. You can adjust this if you want to perform the operation on a subset of the data.
- ``scale_conversion="boxcox"``: This parameter defines the type of scaling we want to apply. In this case, we are using the Box-Cox transformation. You can change ``boxcox`` to any supported scale conversion method.
- ``apply_cutoff=False``: We are not applying any outlier cutoff in this example.
- ``lower_cutoff=None`` and ``upper_cutoff=None``: These are left as ``None`` since we are not applying outlier cutoffs in this case.
- ``show_plot=True``: This option will generate a plot to visualize the distribution of the ``age`` column before and after the transformation.
- ``apply_as_new_col_to_df=True``: This tells the function to apply the transformation and create a new column in the DataFrame. The new column will be named ``age_boxcox``, where ``"boxcox"`` indicates the type of transformation applied.

1. **Box-Cox Transformation**: This transformation normalizes the data by making the distribution more Gaussian-like, which can be beneficial for certain statistical models.
   
2. **No Outlier Handling**: In this example, we are not applying any cutoffs to remove or modify outliers. This means the function will process the entire range of values in the ``age`` column without making adjustments for extreme values.

3. **New Column Creation**: By setting ``apply_as_new_col_to_df=True``, a new column named ``age_boxcox`` will be created in the ``df`` DataFrame, where the transformed values will be stored. This allows us to keep the original ``age`` column intact while adding the transformed data as a new feature.

4. The ``show_plot=True`` parameter will generate a plot that visualizes the distribution of the original ``age`` data alongside the transformed ``age_boxcox`` data. This can help you assess how the Box-Cox transformation has affected the data distribution.


.. _Box_Cox_Example_2:

Box-Cox Transformation Example 2
----------------------------------

In this second example from the US Census dataset [1]_, we apply the Box-Cox 
transformation to the ``age`` column in a DataFrame, but this time with custom 
keyword arguments passed through the ``scale_conversion_kws``. Specifically, we 
provide an ``alpha`` value of `0.8`, :ref:`influencing the confidence interval for the 
transformation <Confidence_Intervals_for_Lambda>`. Additionally, we customize the 
visual appearance of the plots by specifying keyword arguments for the violinplot, 
KDE, and histogram plots. These customizations allow for greater control over the 
visual output.


.. code-block:: python 

    from eda_toolkit import data_doctor

    data_doctor(
        df=df,
        feature_name="age",
        data_fraction=1,
        scale_conversion="boxcox",
        apply_cutoff=False,
        lower_cutoff=None,
        upper_cutoff=None,
        show_plot=True,
        apply_as_new_col_to_df=True,
        scale_conversion_kws={"alpha": 0.8},
        box_violin="violinplot",
        box_violin_kws={"color": "lightblue"},
        kde_kws={"fill": True, "color": "blue"},
        hist_kws={"color": "green"},
        random_state=111,
    )

.. code-block:: text

                DATA DOCTOR SUMMARY REPORT             
    +------------------------------+--------------------+
    | Feature                      | age                |
    +------------------------------+--------------------+
    | Statistic                    | Value              |
    +------------------------------+--------------------+
    | Min                          |             3.6664 |
    | Max                          |             6.8409 |
    | Mean                         |             5.0163 |
    | Median                       |             5.0333 |
    | Std Dev                      |             0.6761 |
    +------------------------------+--------------------+
    | Quartile                     | Value              |
    +------------------------------+--------------------+
    | Q1 (25%)                     |             4.5219 |
    | Q2 (50% = Median)            |             5.0333 |
    | Q3 (75%)                     |             5.5338 |
    | IQR                          |             1.0119 |
    +------------------------------+--------------------+
    | Outlier Bound                | Value              |
    +------------------------------+--------------------+
    | Lower Bound                  |             3.0040 |
    | Upper Bound                  |             7.0517 |
    +------------------------------+--------------------+

    New Column Name: age_boxcox
    Box-Cox C.I. for Lambda: (0.1717, 0.1779)


.. raw:: html

   <div class="no-click">

.. image:: ../assets/age_boxcox_kde_hist_violinplot.svg
   :alt: Box-Cox Transformation W/ Data Doctor
   :align: center
   :width: 900px

.. raw:: html

   </div>

.. raw:: html

   <div style="height: 50px;"></div>


.. note::

    Note that this example specifies The theoretical overview section provides a 
    detailed framework for a :ref:`Box-Cox transformation <Box_Cox_Transformation>`.  

.. code-block:: python

    df.head()

.. raw:: html

    <style type="text/css">
    .tg-wrap {
      width: 100%;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
    }
    .tg  {border-collapse:collapse;border-spacing:0;margin:0px auto;}
    .tg td{border-color:black;border-style:solid;border-width:1px;font-family:monospace, sans-serif !important;font-size:11px !important;
      overflow:hidden;padding:0px 5px;word-break:normal;}
    .tg th{border-color:black;border-style:solid;border-width:1px;font-family:monospace, sans-serif !important;font-size:11px !important;
      font-weight:normal;overflow:hidden;padding:0px 5px;word-break:normal;}
    .tg .tg-zv4m{border-color:#ffffff;text-align:left;vertical-align:top}
    .tg .tg-8jgo{border-color:#ffffff;text-align:center;vertical-align:top}
    .tg .tg-aw21{border-color:#ffffff;font-weight:bold;text-align:center;vertical-align:top}
    .tg .tg-lightpink{background-color:#FFCCCC; border-width: 0px;} /* Remove borders and apply solid pink color */
    </style>
    <div class="tg-wrap">
    <table class="tg">
      <thead>
        <tr>
          <th class="tg-zv4m"></th>
          <th class="tg-aw21">age</th>
          <th class="tg-aw21">workclass</th>
          <th class="tg-aw21">education</th>
          <th class="tg-aw21">education-num</th>
          <th class="tg-aw21">marital-status</th>
          <th class="tg-aw21">occupation</th>
          <th class="tg-aw21">relationship</th>
          <th class="tg-aw21 tg-lightpink">age_boxcox</th> <!-- Highlighted column -->
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
          <td class="tg-8jgo tg-lightpink"></td>
        </tr>
        <tr>
          <td class="tg-zv4m">582248222</td>
          <td class="tg-8jgo">39</td>
          <td class="tg-8jgo">State-gov</td>
          <td class="tg-8jgo">Bachelors</td>
          <td class="tg-8jgo">13</td>
          <td class="tg-8jgo">Never-married</td>
          <td class="tg-8jgo">Adm-clerical</td>
          <td class="tg-8jgo">Not-in-family</td>
          <td class="tg-8jgo tg-lightpink">3.936876</td>
        </tr>
        <tr>
          <td class="tg-zv4m">561810758</td>
          <td class="tg-8jgo">50</td>
          <td class="tg-8jgo">Self-emp-not-inc</td>
          <td class="tg-8jgo">Bachelors</td>
          <td class="tg-8jgo">13</td>
          <td class="tg-8jgo">Married-civ-spouse</td>
          <td class="tg-8jgo">Exec-managerial</td>
          <td class="tg-8jgo">Husband</td>
          <td class="tg-8jgo tg-lightpink">4.019590</td>
        </tr>
        <tr>
          <td class="tg-zv4m">598098459</td>
          <td class="tg-8jgo">38</td>
          <td class="tg-8jgo">Private</td>
          <td class="tg-8jgo">HS-grad</td>
          <td class="tg-8jgo">9</td>
          <td class="tg-8jgo">Divorced</td>
          <td class="tg-8jgo">Handlers-cleaners</td>
          <td class="tg-8jgo">Not-in-family</td>
          <td class="tg-8jgo tg-lightpink">4.521908</td>
        </tr>
        <tr>
          <td class="tg-zv4m">776705221</td>
          <td class="tg-8jgo">53</td>
          <td class="tg-8jgo">Private</td>
          <td class="tg-8jgo">11th</td>
          <td class="tg-8jgo">7</td>
          <td class="tg-8jgo">Married-civ-spouse</td>
          <td class="tg-8jgo">Handlers-cleaners</td>
          <td class="tg-8jgo">Husband</td>
          <td class="tg-8jgo tg-lightpink">5.033257</td>
        </tr>
        <tr>
          <td class="tg-zv4m">479262902</td>
          <td class="tg-8jgo">28</td>
          <td class="tg-8jgo">Private</td>
          <td class="tg-8jgo">Bachelors</td>
          <td class="tg-8jgo">13</td>
          <td class="tg-8jgo">Married-civ-spouse</td>
          <td class="tg-8jgo">Prof-specialty</td>
          <td class="tg-8jgo">Wife</td>
          <td class="tg-8jgo tg-lightpink">5.614411	</td>
        </tr>
      </tbody>
    </table>
    </div>

\

In this example, you can see how the ``data_doctor`` function supports further 
flexibility with customizable plot aesthetics and scaling techniques. The 
Box-Cox transformation is still applied without any tuning of the ``lambda`` parameter, 
while the ``alpha`` value provides a confidence interval for the resulting transformation:

.. code-block:: text

    Box-Cox C.I. for Lambda: (0.1717, 0.1779)

This allows for tailored visualizations with consistent styling across multiple plot types.

Some of the keyword arguments, such as those passed in ``box_violin_kws``, are 
specific to Python version 3.7. For example, in this version, we remove the fill 
color from the boxplot using ``boxprops``. 

.. code-block:: python

    box_violin_kws={
        "boxprops": dict(facecolor="none", edgecolor="blue")
    },

In later Python versions (e.g., 3.11), 
this can be done more easily with ``fill=True``. Therefore, it is important to pass 
any desired keyword arguments based on the correct version of Python you're using.

**Explanation**

- ``df=df``: We are passing ``df`` as the input DataFrame.
- ``feature_name="age"``: The feature we are transforming is ``age``.
- ``data_fraction=1``: We are using 100% of the data in the ``age`` column. You can adjust this if you want to perform the operation on a subset of the data.
- ``scale_conversion="boxcox"``: This parameter defines the type of scaling we want to apply. In this case, we are using the Box-Cox transformation.
- ``apply_cutoff=False``: We are not applying any outlier cutoff in this example.
- ``lower_cutoff=None`` and ``upper_cutoff=None``: These are left as ``None`` since we are not applying outlier cutoffs in this case.
- ``show_plot=True``: This option will generate a plot to visualize the distribution of the ``age`` column before and after the transformation.
- ``apply_as_new_col_to_df=True``: This tells the function to apply the transformation and create a new column in the DataFrame. The new column will be named ``age_boxcox_alpha`` to indicate that an alpha parameter was used in the transformation.
- ``scale_conversion_kws={"alpha":0.8}``: The ``alpha`` keyword argument specifies the confidence interval for the Box-Cox transformation's lambda value, ensuring a confidence interval is returned instead of a single lambda value.
- ``box_violin_kws={"boxprops": dict(facecolor='none', edgecolor="blue")}``: This keyword argument customizes the appearance of the boxplot by removing the fill color and setting the edge color to blue. This syntax is specific to Python 3.7. In later versions (i.e., 3.11+), the ``fill=True`` argument can be used to control this behavior.
- ``kde_kws={"fill":True, "color":"blue"}``: This fills the area under the KDE plot with a blue color, enhancing the plot's visual presentation.
- ``hist_kws={"color":"blue"}``: This colors the histogram bars in blue for visual consistency across plots.
- ``image_path_svg=image_path_svg``: This parameter specifies the path where the resulting plot will be saved as an SVG file.
- ``save_plot=True``: This tells the function to save the plot, and since an image path is provided, the plot will be saved as an SVG file.

1. **Box-Cox Transformation with Confidence Interval**: In this example, we use the Box-Cox transformation with the ``alpha`` parameter set to 0.8, which returns a confidence interval for the lambda value rather than a single value.
   
2. **No Outlier Handling**: Similar to Example 1, no outliers are handled in this transformation.
   
3. **New Column Creation**: The transformed data is added to the DataFrame in a new column named ``age_boxcox_alpha``, where "alpha" indicates the confidence interval applied in the Box-Cox transformation.

4. **Custom Plot Visuals**: The KDE, histogram, and boxplot are customized with blue colors, and specific keyword arguments are provided for the boxplot appearance based on Python version. These changes allow for finer control over the visual aesthetics of the resulting plots.

5. **Plot Saving**: The ``save_plot`` parameter is set to ``True``, and the plot will be saved as an SVG file at the specified location.


Data Fraction Usage
----------------------

In the **Box-Cox transformation** examples, you may notice a difference in the values for ``data_fraction``:

- In :ref:`Box-Cox Example 1 <Box_Cox_Example_1>`, we set ``data_fraction=0.6``.

- In :ref:`Box-Cox Example 2 <Box_Cox_Example_2>`, we used the full data with ``data_fraction=1``.

Despite using a ``data_fraction`` of `0.6` in Example 1, the function still processed 
the entire dataset. The purpose of the ``data_fraction`` parameter is to allow 
users to select a smaller subset of the data for sampling and transformation while 
ensuring the final operation is applied to the full scope of data.

This behavior is intentional, as it serves to:

1. **Ensure Reproducibility**: By using a consistent ``random_state``, the sampled 
subset can reliably represent the dataset, regardless of ``data_fraction``.

2. **Preserve Sampling Assumptions**: Applying the desired operation (e.g., transformations) 
on the full data aligns the sample with the larger population and allows a seamless projection 
of the sample properties to the entire dataset.

Thus, while ``data_fraction`` provides a way to adjust the percentage of data 
used for sampling, the function will always apply the transformation across the 
full dataset, balancing performance efficiency with statistical integrity.


Retaining a Sample for Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To sample the exact subset used in the ``data_fraction=0.6`` calculation, you 
can directly sample from the DataFrame with a consistent random state for 
reproducibility. This method allows you to work with a representative subset of 
the data while preserving the original distribution characteristics.

To sample 60% of the data using the exact logic of the ``data_doctor`` function, 
use the following code:

.. code-block:: python

    sampled_df = df.sample(frac=0.6, random_state=111)

The ``random_state`` parameter ensures that the sampled data remains consistent 
across runs. After creating this subset, you can apply the ``data_doctor`` 
function to ``sampled_df`` as shown below to perform the Box-Cox transformation 
on the ``age`` column:

.. code-block:: python

    from eda_toolkit import data_doctor

    data_doctor(
        df=sampled_df,
        feature_name="age",
        data_fraction=1,
        scale_conversion="boxcox",
        apply_cutoff=False,
        lower_cutoff=None,
        upper_cutoff=None,
        show_plot=True,
        apply_as_new_col_to_df=True,
        random_state=111,
    )

By setting ``data_fraction=1`` within the ``data_doctor`` function, you ensure 
that it operates on the entire ``sampled_df``, which now consists of the selected 
60% subset. To confirm that the sampled data is indeed 60% of the original 
DataFrame, you can print the shape of ``sampled_df`` as follows:

.. code-block:: python

    print(
        f"The sampled dataframe has {sampled_df.shape[0]} rows and {sampled_df.shape[1]} columns."
    )

.. code-block:: bash

    The sampled dataframe has 29305 rows and 16 columns.


We can also inspect the first five rows of the ``sampled_df`` dataframe below:

.. raw:: html

    <style type="text/css">
    .tg-wrap {
      width: 100%;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
    }
    .tg  {border-collapse:collapse;border-spacing:0;margin:0px auto;}
    .tg td{border-color:black;border-style:solid;border-width:1px;font-family:monospace, sans-serif !important;font-size:11px !important;
      overflow:hidden;padding:0px 5px;word-break:normal;}
    .tg th{border-color:black;border-style:solid;border-width:1px;font-family:monospace, sans-serif !important;font-size:11px !important;
      font-weight:normal;overflow:hidden;padding:0px 5px;word-break:normal;}
    .tg .tg-zv4m{border-color:#ffffff;text-align:left;vertical-align:top}
    .tg .tg-8jgo{border-color:#ffffff;text-align:center;vertical-align:top}
    .tg .tg-aw21{border-color:#ffffff;font-weight:bold;text-align:center;vertical-align:top}
    .tg .tg-lightpink{background-color:#FFCCCC; border-width: 0px;} /* Remove borders and apply solid pink color */
    </style>
    <div class="tg-wrap">
    <table class="tg">
      <thead>
        <tr>
          <th class="tg-zv4m"></th>
          <th class="tg-aw21">age</th>
          <th class="tg-aw21">workclass</th>
          <th class="tg-aw21">education</th>
          <th class="tg-aw21">education-num</th>
          <th class="tg-aw21">marital-status</th>
          <th class="tg-aw21">occupation</th>
          <th class="tg-aw21">relationship</th>
          <th class="tg-aw21 tg-lightpink">age_boxcox</th> <!-- Highlighted column -->
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
          <td class="tg-8jgo tg-lightpink"></td>
        </tr>
        <tr>
          <td class="tg-zv4m">408117383</td>
          <td class="tg-8jgo">40</td>
          <td class="tg-8jgo">Private</td>
          <td class="tg-8jgo">Some-college</td>
          <td class="tg-8jgo">10</td>
          <td class="tg-8jgo">Married-civ-spouse</td>
          <td class="tg-8jgo">Machine-op-inspct</td>
          <td class="tg-8jgo">Husband</td>
          <td class="tg-8jgo tg-lightpink">4.355015</td>
        </tr>
        <tr>
          <td class="tg-zv4m">669717925</td>
          <td class="tg-8jgo">58</td>
          <td class="tg-8jgo">Private</td>
          <td class="tg-8jgo">HS-grad</td>
          <td class="tg-8jgo">9</td>
          <td class="tg-8jgo">Married-civ-spouse</td>
          <td class="tg-8jgo">Exec-managerial</td>
          <td class="tg-8jgo">Husband</td>
          <td class="tg-8jgo tg-lightpink">5.086108</td>
        </tr>
        <tr>
          <td class="tg-zv4m">399428377</td>
          <td class="tg-8jgo">41</td>
          <td class="tg-8jgo">Private</td>
          <td class="tg-8jgo">HS-grad</td>
          <td class="tg-8jgo">9</td>
          <td class="tg-8jgo">Separated</td>
          <td class="tg-8jgo">Machine-op-inspct</td>
          <td class="tg-8jgo">Not-in-family</td>
          <td class="tg-8jgo tg-lightpink">5.037743</td>
        </tr>
        <tr>
          <td class="tg-zv4m">961427355</td>
          <td class="tg-8jgo">73</td>
          <td class="tg-8jgo">NaN</td>
          <td class="tg-8jgo">Some-college</td>
          <td class="tg-8jgo">10</td>
          <td class="tg-8jgo">Married-civ-spouse</td>
          <td class="tg-8jgo">NaN</td>
          <td class="tg-8jgo">Husband</td>
          <td class="tg-8jgo tg-lightpink">4.216561</td>
        </tr>
        <tr>
          <td class="tg-zv4m">458295720</td>
          <td class="tg-8jgo">19</td>
          <td class="tg-8jgo">Private</td>
          <td class="tg-8jgo">HS-grad</td>
          <td class="tg-8jgo">9</td>
          <td class="tg-8jgo">Never-married</td>
          <td class="tg-8jgo">Farming-fishing</td>
          <td class="tg-8jgo">Not-in-family</td>
          <td class="tg-8jgo tg-lightpink">5.520438</td>
        </tr>
      </tbody>
    </table>
    </div>


\


Logit Transformation Example
-------------------------------

In this example, we demonstrate the usage of the ``data_doctor`` function to 
apply a **logit transformation** to a feature in a DataFrame. The **logit transformation** 
is used when dealing with data bounded between 0 and 1, as it maps values within 
this range to an unbounded scale in log-odds terms, making it particularly useful 
in fields such as logistic regression.

.. note::

    The ``data_doctor`` function provides a range of scaling options, and in this case, 
    we use the **logit transformation** to illustrate how the transformation is applied. 
    However, it’s important to note that if the feature contains values outside the (0, 1) 
    range, the function will raise a ``ValueError``. This is because the :ref:`logit function 
    is undefined for values less than or equal to 0 and greater than or equal to 1 <Logit_Assumptions>`. 

.. code-block:: python

    from eda_toolkit import data_doctor

    data_doctor(
        df=df,
        feature_name="age",
        data_fraction=1,
        scale_conversion="logit",
        apply_cutoff=False,
        lower_cutoff=None,
        upper_cutoff=None,
        show_plot=True,
        apply_as_new_col_to_df=True,
        random_state=111,
    )

.. error::

    ``ValueError: Logit transformation requires values to be between 0 and 1. Consider using a scaling method such as min-max scaling first.``

If you attempt to apply this transformation to data outside the (0, 1) range, 
such as an unscaled numerical feature, the function will halt and display an 
error message advising you to use an appropriate scaling method first.

If you encounter this error, it is recommended to first scale your data using a 
method like **min-max scaling** to bring it within the (0, 1) range before 
applying the logit transformation.


In this example:

- ``df=df``: Specifies the DataFrame containing the feature.
- ``feature_name="feature_proportion"``: The feature we are transforming should be bounded between 0 and 1.
- ``scale_conversion="logit"``: Sets the transformation to logit. Ensure that ``feature_proportion`` values are within (0, 1) before applying.
- ``show_plot=True``: Generates a plot of the transformed feature.


Plain Outliers Example
--------------------------------

Observed Outliers Sans Cutoffs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this example, we examine the final weight (``fnlwgt``) feature from the US Census 
dataset [1]_, focusing on detecting outliers without applying any scaling 
transformations. The ``data_doctor`` function is used with minimal configuration 
to visualize where outliers are present in the raw data.

By enabling ``apply_cutoff=True`` and selecting ``plot_type=["box_violin", "hist"]``, 
we can clearly identify outliers both visually and numerically. This basic setup 
highlights the outliers without altering the data distribution, making it easy 
to see extreme values that could affect further analysis.

The following code demonstrates this:

.. code-block:: python

    from eda_toolkit import data_doctor

    data_doctor(
        df=df,
        feature_name="fnlwgt",
        data_fraction=0.6,
        plot_type=["box_violin", "hist"],
        hist_kws={"color": "gray"},
        figsize=(8, 4),
        image_path_svg=image_path_svg,
        save_plot=True,
        random_state=111,
    )

.. code-block:: text

                DATA DOCTOR SUMMARY REPORT             
    +------------------------------+--------------------+
    | Feature                      | fnlwgt             |
    +------------------------------+--------------------+
    | Statistic                    | Value              |
    +------------------------------+--------------------+
    | Min                          |        12,285.0000 |
    | Max                          |     1,484,705.0000 |
    | Mean                         |       189,181.3719 |
    | Median                       |       177,955.0000 |
    | Std Dev                      |       105,417.5713 |
    +------------------------------+--------------------+
    | Quartile                     | Value              |
    +------------------------------+--------------------+
    | Q1 (25%)                     |       117,292.0000 |
    | Q2 (50% = Median)            |       177,955.0000 |
    | Q3 (75%)                     |       236,769.0000 |
    | IQR                          |       119,477.0000 |
    +------------------------------+--------------------+
    | Outlier Bound                | Value              |
    +------------------------------+--------------------+
    | Lower Bound                  |       -61,923.5000 |
    | Upper Bound                  |       415,984.5000 |
    +------------------------------+--------------------+

.. raw:: html

   <div class="no-click">

.. image:: ../assets/fnlwgt_None_boxplot_hist.svg
   :alt: Outlier Detection W/ Data Doctor
   :align: center
   :width: 900px

.. raw:: html

   </div>

.. raw:: html

   <div style="height: 20px;"></div>

In this visualization, the boxplot and histogram display outliers prominently, 
showing you exactly where the extreme values lie. This setup serves as a baseline 
view of the raw data, making it useful for assessing the initial distribution 
before any scaling or transformation is applied.


Treated Outliers With Cutoffs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this scenario, we address the extreme values observed in the ``fnlwgt`` feature 
by applying a visual cutoff based on the distribution seen in the previous example. 
Here, we set an approximate upper cutoff of **400,000** to limit the impact of outliers 
without any additional scaling or transformation. By using ``apply_cutoff=True`` along 
with ``upper_cutoff=400000``, we effectively cap the extreme values.

This example also demonstrates how you can further customize the visualization by 
specifying additional histogram keyword arguments with ``hist_kws``. Here, we use 
``bins=20`` to adjust the bin size, creating a smoother view of the feature's 
distribution within the cutoff limits.

In the resulting visualization, you will see that the boxplot and histogram have a 
controlled range due to the applied upper cutoff, limiting the influence of extreme 
outliers on the visual representation. This treatment provides a clearer view of the 
primary distribution, allowing for a more focused analysis on the bulk of the data 
without outliers distorting the scale.

The following code demonstrates this configuration:

.. code-block:: python

    from eda_toolkit import data_doctor

    data_doctor(
        df=df,
        feature_name="fnlwgt",
        data_fraction=0.6,
        apply_as_new_col_to_df=True,
        apply_cutoff=True,
        upper_cutoff=400000,
        plot_type=["box_violin", "hist"],
        hist_kws={"color": "gray", "bins": 20},
        figsize=(8, 4),
        image_path_svg=image_path_svg,
        save_plot=True,
        random_state=111,
    )

.. raw:: html

   <div class="no-click">

.. image:: ../assets/fnlwgt_None_boxplot_hist_cutoff.svg
   :alt: Outlier Detection W/ Data Doctor
   :align: center
   :width: 900px

.. raw:: html

   </div>

.. raw:: html

   <div style="height: 20px;"></div>

.. raw:: html

    <style type="text/css">
    .tg-wrap {
      width: 100%;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
    }
    .tg  {border-collapse:collapse;border-spacing:0;margin:0px auto;}
    .tg td{border-color:black;border-style:solid;border-width:1px;font-family:monospace, sans-serif !important;font-size:11px !important;
      overflow:hidden;padding:0px 5px;word-break:normal;}
    .tg th{border-color:black;border-style:solid;border-width:1px;font-family:monospace, sans-serif !important;font-size:11px !important;
      font-weight:normal;overflow:hidden;padding:0px 5px;word-break:normal;}
    .tg .tg-zv4m{border-color:#ffffff;text-align:left;vertical-align:top}
    .tg .tg-8jgo{border-color:#ffffff;text-align:center;vertical-align:top}
    .tg .tg-aw21{border-color:#ffffff;font-weight:bold;text-align:center;vertical-align:top}
    .tg .tg-lightpink{background-color:#FFCCCC; border-width: 0px;} /* Remove borders and apply solid pink color */
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
          <th class="tg-aw21">marital-status</th>
          <th class="tg-aw21">occupation</th>
          <th class="tg-aw21">relationship</th>
          <th class="tg-aw21 tg-lightpink">fnlwgt_w_cutoff</th> 
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
          <td class="tg-8jgo tg-lightpink"></td>
        </tr>
        <tr>
          <td class="tg-zv4m">582248222</td>
          <td class="tg-8jgo">39</td>
          <td class="tg-8jgo">State-gov	</td>
          <td class="tg-8jgo">77516</td>
          <td class="tg-8jgo">Bachelors</td>
          <td class="tg-8jgo">Never-married</td>
          <td class="tg-8jgo">Adm-clerical</td>
          <td class="tg-8jgo">Not-in-family</td>
          <td class="tg-8jgo tg-lightpink">132222</td> <!-- New cell with data -->
        </tr>
        <tr>
          <td class="tg-zv4m">561810758</td>
          <td class="tg-8jgo">50</td>
          <td class="tg-8jgo">Self-emp-not-inc</td>
          <td class="tg-8jgo">83311</td>
          <td class="tg-8jgo">Bachelors</td>
           <td class="tg-8jgo">Married-civ-spouse</td>
          <td class="tg-8jgo">Exec-managerial</td>
          <td class="tg-8jgo">Husband</td>
           <td class="tg-8jgo tg-lightpink">68624</td> <!-- New cell with data -->
        </tr>
        <tr>
          <td class="tg-zv4m">598098459</td>
          <td class="tg-8jgo">38</td>
          <td class="tg-8jgo">Private</td>
          <td class="tg-8jgo">215646</td>
          <td class="tg-8jgo">HS-grad</td>
          <td class="tg-8jgo">Divorced</td>
          <td class="tg-8jgo">Handlers-cleaners</td>
          <td class="tg-8jgo">Not-in-family</td>
          <td class="tg-8jgo tg-lightpink">161880</td> 
        </tr>
        <tr>
          <td class="tg-zv4m">776705221</td>
          <td class="tg-8jgo">53</td>
          <td class="tg-8jgo">Private</td>
          <td class="tg-8jgo">234721</td>
          <td class="tg-8jgo">11th</td>
          <td class="tg-8jgo">Married-civ-spouse</td>
          <td class="tg-8jgo">Handlers-cleaners</td>
          <td class="tg-8jgo">Husband</td>
          <td class="tg-8jgo tg-lightpink">73402</td> 
        </tr>
        <tr>
          <td class="tg-zv4m">479262902</td>
          <td class="tg-8jgo">28</td>
          <td class="tg-8jgo">Private</td>
          <td class="tg-8jgo">338409</td>
          <td class="tg-8jgo">Bachelors</td>
          <td class="tg-8jgo">Married-civ-spouse</td>
          <td class="tg-8jgo">Prof-specialty</td>
          <td class="tg-8jgo">Wife</td>
          <td class="tg-8jgo tg-lightpink">97261</td> <!-- New cell with data -->
        </tr>
        <tr>
        </tr>
      </tbody>
    </table>
    </div>

\

RobustScaler Outliers Example
--------------------------------

In this example from the US Census dataset [1]_, we apply the :ref:`RobustScaler 
transformation <Robust_Scaler>` to the age column in a DataFrame to address potential outliers. 
The ``data_doctor`` function enables users to apply transformations with specific 
configurations via the ``scale_conversion_kws`` parameter, making it ideal for 
refining how outliers affect scaling.

For this example, we set the following custom keyword arguments:

- Disable centering: By setting ``with_centering=False``, the transformation scales based only on the range, without shifting the median to zero.
- Adjust quantile range: We specify a narrower ``quantile_range`` of (10.0, 90.0) to reduce the influence of extreme values on scaling.

The following code demonstrates this transformation:

.. code-block:: python

    from eda_toolkit import data_doctor

    data_doctor(
        df=df,
        feature_name='age',
        data_fraction=0.6,
        scale_conversion="robust",
        apply_as_new_col_to_df=True,
        scale_conversion_kws={
            "with_centering": False,  # Disable centering
            "quantile_range": (10.0, 90.0)  # Use a custom quantile range
        },
        random_state=111,
    )

.. code-block:: text

                 DATA DOCTOR SUMMARY REPORT             
    +------------------------------+--------------------+
    | Feature                      | age                |
    +------------------------------+--------------------+
    | Statistic                    | Value              |
    +------------------------------+--------------------+
    | Min                          | 0.4722             |
    | Max                          | 2.5000             |
    | Mean                         | 1.0724             |
    | Median                       | 1.0278             |
    | Std Dev                      | 0.3809             |
    +------------------------------+--------------------+
    | Quartile                     | Value              |
    +------------------------------+--------------------+
    | Q1 (25%)                     | 0.7778             |
    | Q2 (Median)                  | 1.0278             |
    | IQR                          | 0.5556             |
    | Q3 (75%)                     | 1.3333             |
    | Q4 (Max)                     | 2.5000             |
    +------------------------------+--------------------+
    | Outlier Bound                | Value              |
    +------------------------------+--------------------+
    | Lower Bound                  | -0.0556            |
    | Upper Bound                  | 2.1667             |
    +------------------------------+--------------------+

    New Column Name: age_robust


.. raw:: html

   <div class="no-click">

.. image:: ../assets/age_robust_boxplot_hist.svg
   :alt: Box-Cox Transformation W/ Data Doctor
   :align: center
   :width: 900px

.. raw:: html

   </div>

.. raw:: html
   
   <div style="height: 50px;"></div>


ECDF Distribution Example
-----------------------------

In this example, we demonstrate the use of the Empirical Cumulative Distribution
Function (ECDF) to visualize the distribution of the ``"age"`` variable from the
US Census Adult Income dataset [1]_.

ECDF plots provide a robust, non-parametric view of a variable’s distribution by
showing the cumulative proportion of observations less than or equal to a given
value. Unlike histograms or kernel density estimates, ECDFs do not rely on binning
or smoothing parameters, making them especially useful for diagnostic analysis.

For a formal mathematical definition and theoretical background of the ECDF,
see the :ref:`Empirical Cumulative Distribution Function (ECDF) <ecdf_theory>`
section in the theoretical overview.

This example uses the ``data_doctor`` function to generate multiple complementary
distribution views for the same feature:

- Kernel Density Estimate (``"kde"``)

- Empirical Cumulative Distribution Function (``"ecdf"``)

- Box and violin plots (``"box_violin"``)

In addition, a logarithmic scaling transformation is applied to the ``"age"``
feature via ``scale_conversion="log"``, allowing the cumulative behavior of the
distribution to be examined after compressing the right tail.

The following code demonstrates this workflow:

.. code-block:: python

    from eda_toolkit import data_doctor

    print("\nRunning data_doctor with plot_type=['kde', 'ecdf', 'box_violin'] ...\n")

    data_doctor(
        df=df,
        feature_name="age",
        plot_type=["kde", "ecdf", "box_violin"],
        scale_conversion="log",
    )

.. code-block:: text

    Running data_doctor with plot_type=['kde', 'ecdf', 'box_violin'] ...

                DATA DOCTOR SUMMARY REPORT             
    +------------------------------+--------------------+
    | Feature                      | age                |
    +------------------------------+--------------------+
    | Statistic                    | Value              |
    +------------------------------+--------------------+
    | Min                          |             2.8332 |
    | Max                          |             4.4998 |
    | Mean                         |             3.5905 |
    | Median                       |             3.6109 |
    | Std Dev                      |             0.3617 |
    +------------------------------+--------------------+
    | Quartile                     | Value              |
    +------------------------------+--------------------+
    | Q1 (25%)                     |             3.3322 |
    | Q2 (50% = Median)            |             3.6109 |
    | Q3 (75%)                     |             3.8712 |
    | IQR                          |             0.5390 |
    +------------------------------+--------------------+
    | Outlier Bound                | Value              |
    +------------------------------+--------------------+
    | Lower Bound                  |             2.5237 |
    | Upper Bound                  |             4.6797 |
    +------------------------------+--------------------+


.. raw:: html

   <div class="no-click">

.. image:: ../assets/age_log_ecdf_boxplot.png
   :alt: Box-Cox Transformation W/ Data Doctor
   :align: center
   :width: 900px

.. raw:: html

   </div>

.. raw:: html
   
   <div style="height: 50px;"></div>



Stacked Crosstab Plots
=======================

**Generate stacked or regular bar plots and crosstabs for specified columns in a DataFrame.**

The ``stacked_crosstab_plot`` function is a powerful tool for visualizing categorical data relationships through stacked bar plots and contingency tables (crosstabs). It supports extensive customization options, including plot appearance, color schemes, and saving output in multiple formats. Users can choose between regular or normalized plots and control whether the function returns the generated crosstabs as a dictionary.

.. function:: stacked_crosstab_plot(df, col, func_col, legend_labels_list, title, kind="bar", width=0.9, rot=0, custom_order=None, image_path_png=None, image_path_svg=None, save_formats=None, color=None, output="both", return_dict=False, figsize=None, outer_pad=10.0, h_pad=5.0, file_prefix=None, logscale=False, plot_type="both", show_legend=True, legend_loc="best", reverse_legend=True, label_fontsize=12, tick_fontsize=10, title_wrap=50, tick_wrap=20, thousands_sep=True, pct_format=True, show_values=False, subtitle=None, remove_stacks=False, xlim=None, ylim=None)

   :param df: The DataFrame containing the data to plot.
   :type df: pandas.DataFrame

   :param col: The name of the column in the DataFrame to be analyzed.
   :type col: str

   :param func_col: List of columns in the DataFrame to generate the
      crosstabs and stack the bars in the plot.
   :type func_col: list of str

   :param legend_labels_list: List of legend labels corresponding to each
      column in ``func_col``.
   :type legend_labels_list: list of list of str

   :param title: List of titles for each plot generated.
   :type title: list of str

   :param kind: Type of plot to generate. ``"bar"`` for vertical bars,
      ``"barh"`` for horizontal bars. Default is ``"bar"``.
   :type kind: str, optional

   :param width: Width of the bars in the bar plot. Default is ``0.9``.
   :type width: float, optional

   :param rot: Rotation angle of the x-axis labels. Default is ``0``.
   :type rot: int, optional

   :param custom_order: Custom order for the categories in ``col``.
   :type custom_order: list, optional

   :param image_path_png: Directory path to save PNG plot images.
   :type image_path_png: str, optional

   :param image_path_svg: Directory path to save SVG plot images.
   :type image_path_svg: str, optional

   :param save_formats: List, string, or tuple of file formats to save
      the plots (e.g. ``["png", "svg"]``). Default is ``None``.
   :type save_formats: list, str, or tuple, optional

   :param color: List of colors to use for the plots. Default is the
      seaborn color palette.
   :type color: list of str or str, optional

   :param output: Specify the output type: ``"plots_only"``,
      ``"crosstabs_only"``, or ``"both"``. Default is ``"both"``.
   :type output: str, optional

   :param return_dict: Return the crosstabs as a dictionary.
      Default is ``False``.
   :type return_dict: bool, optional

   :param figsize: A ``(width, height)`` tuple controlling the figure
      size in inches. Defaults to ``(12, 8)`` if not provided.
   :type figsize: tuple of int, optional

   :param outer_pad: Outer padding around the entire figure, passed to
      ``tight_layout(pad=...)``. Default is ``10.0``.
   :type outer_pad: float, optional

   :param h_pad: Vertical padding between subplots in inches, passed to
      ``tight_layout(h_pad=...)``. Increase this if the title of the
      lower plot overlaps the x-axis labels of the upper plot.
      Default is ``5.0``.
   :type h_pad: float, optional

   :param file_prefix: Prefix for filenames when saving plots.
   :type file_prefix: str, optional

   :param logscale: Apply a logarithmic scale to the y-axis.
      Default is ``False``.
   :type logscale: bool, optional

   :param plot_type: Type of plot to generate: ``"both"``, ``"regular"``,
      or ``"normalized"``. Default is ``"both"``.
   :type plot_type: str, optional

   :param show_legend: Show the legend on the plot. Default is ``True``.
   :type show_legend: bool, optional

   :param legend_loc: Location of the legend on the plot, passed directly
      to ``matplotlib.axes.Axes.legend``. Common options include
      ``"best"``, ``"upper right"``, ``"upper left"``, ``"lower left"``,
      ``"lower right"``, and ``"center"``. Default is ``"best"``.
   :type legend_loc: str, optional

   :param reverse_legend: If ``True``, reverses the legend entry order so
      it matches the visual stack order (top-to-bottom in the legend
      matches top-to-bottom in the bars). Default is ``True``.
   :type reverse_legend: bool, optional

   :param label_fontsize: Font size for axis labels and titles.
      Default is ``12``.
   :type label_fontsize: int, optional

   :param tick_fontsize: Font size for tick labels on the axes.
      Default is ``10``.
   :type tick_fontsize: int, optional

   :param title_wrap: Maximum character width of the plot title text
      before wrapping to a new line. Default is ``50``.
   :type title_wrap: int, optional

   :param tick_wrap: Maximum character width of axis tick label text
      before wrapping to a new line. Applied to x-axis tick labels for
      vertical bar plots and y-axis tick labels for horizontal bar plots.
      Default is ``20``.
   :type tick_wrap: int, optional

   :param thousands_sep: If ``True``, applies a thousands separator
      (e.g. 1,000,000) to the count axis of non-normalized plots.
      Has no effect on normalized plots. Default is ``True``.
   :type thousands_sep: bool, optional

   :param pct_format: If ``True``, formats the count axis of normalized
      plots as percentages (e.g. 0.25 → 25%). Default is ``True``.
   :type pct_format: bool, optional

   :param show_values: If ``True``, annotates each bar segment with its
      value. Regular plots show counts; normalized plots show percentages.
      Segments too small to fit a label are skipped automatically.
      Default is ``False``.
   :type show_values: bool, optional

   :param subtitle: Subtitle text displayed as italic text below each
      figure. Accepts either a single string (applied to all plots) or a
      list of strings with one entry per ``func_col``.
   :type subtitle: str or list of str, optional

   :param remove_stacks: Remove stacks and create a regular bar plot.
      Only works when ``plot_type`` is ``"regular"``. Default is ``False``.
   :type remove_stacks: bool, optional

   :param xlim: Tuple specifying the limits of the x-axis.
   :type xlim: tuple of float, optional

   :param ylim: Tuple specifying the limits of the y-axis.
   :type ylim: tuple of float, optional

   :returns: Dictionary of crosstabs DataFrames if ``return_dict`` is
      ``True``. Otherwise returns ``None``.
   :rtype: dict or None

   :raises ValueError: If ``remove_stacks`` is ``True`` and ``plot_type``
      is not ``"regular"``.
   :raises ValueError: If ``output`` is not one of ``"both"``,
      ``"plots_only"``, or ``"crosstabs_only"``.
   :raises ValueError: If ``plot_type`` is not one of ``"both"``,
      ``"regular"``, or ``"normalized"``.
   :raises ValueError: If lengths of ``title``, ``func_col``, and
      ``legend_labels_list`` are unequal.
   :raises ValueError: If ``subtitle`` is provided and its length does
      not match ``func_col``.
   :raises ValueError: If an invalid save format is specified without
      the corresponding image path.
   :raises KeyError: If any column in ``col`` or ``func_col`` is missing
      from the DataFrame.

   .. admonition:: Notes

      - Ensure ``save_formats`` aligns with provided paths. Specify
        ``image_path_png`` or ``image_path_svg`` when saving as ``"png"``
        or ``"svg"`` respectively.
      - The returned crosstabs dictionary includes both absolute and
        normalized values when ``return_dict=True``.
      - ``figsize``, ``outer_pad``, and ``h_pad`` replace the deprecated
        ``x``, ``y``, and ``p`` parameters from earlier versions.
      - ``title_wrap`` and ``tick_wrap`` replace the deprecated
        ``text_wrap`` parameter.

Stacked Bar Plots With Crosstabs Example
-----------------------------------------

The provided code snippet demonstrates how to use the ``stacked_crosstab_plot`` 
function to generate stacked bar plots and corresponding crosstabs for different 
columns in a DataFrame. Here's a detailed breakdown of the code using the census
dataset as an example [1]_.

First, the ``func_col`` list is defined, specifying the columns ``["sex", "income"]`` 
to be analyzed. These columns will be used in the loop to generate separate plots. 
The ``legend_labels_list`` is then defined, with each entry corresponding to a 
column in ``func_col``. In this case, the labels for the ``sex`` column are 
``["Male", "Female"]``, and for the ``income`` column, they are ``["<=50K", ">50K"]``. 
These labels will be used to annotate the legends of the plots.

Next, the ``title`` list is defined, providing titles for each plot corresponding 
to the columns in ``func_col``. The titles are set to ``["Sex", "Income"]``, 
which will be displayed on top of each respective plot.

.. note::

    The ``legend_labels_list`` parameter should be a list of lists, where each 
    inner list corresponds to the ground truth labels for the respective item in 
    the ``func_col`` list. Each element in the ``func_col`` list represents a 
    column in your DataFrame that you wish to analyze, and the corresponding 
    inner list in ``legend_labels_list`` should contain the labels that will be 
    used in the legend of your plots.


For example:

.. code-block:: python

    # Define the func_col to use in the loop in order of usage
    func_col = ["sex", "income"]

    # Define the legend_labels to use in the loop
    legend_labels_list = [
        ["Male", "Female"],  # Corresponds to "sex"
        ["<=50K", ">50K"],   # Corresponds to "income"
    ]

    # Define titles for the plots
    title = [
        "Sex",
        "Income",
    ]

.. important::
    
    Ensure that ``func_col``, ``legend_labels_list``, and ``title`` have the 
    same number of elements. Each item in ``func_col`` must correspond to a list 
    of labels in ``legend_labels_list`` and a title in ``title`` to ensure the 
    function generates plots with the correct labels and titles.

    Additionally, in this example, remove trailing periods from the ``income`` 
    column to correctly split its contents into two categories.


In this example:

- ``func_col`` contains two elements: ``"sex"`` and ``"income"``. Each corresponds to a specific column in your DataFrame.  
- ``legend_labels_list`` is a nested list containing two inner lists: 

    - The first inner list, ``["Male", "Female"]``, corresponds to the ``"sex"`` column in ``func_col``.
    - The second inner list, ``["<=50K", ">50K"]``, corresponds to the ``"income"`` column in ``func_col``.

- ``title`` contains two elements: ``"Sex"`` and ``"Income"``, which will be used as the titles for the respective plots.


.. note:: 

    Before proceeding with any further examples in this documentation, ensure that the ``age`` variable is binned into a new variable, ``age_group``.  
    Detailed instructions for this process can be found under :ref:`Binning Numerical Columns <Binning_Numerical_Columns>`.


.. code-block:: python

    from eda_toolkit import stacked_crosstab_plot

    stacked_crosstabs = stacked_crosstab_plot(
        df=df,
        col="age_group",
        func_col=func_col,
        legend_labels_list=legend_labels_list,
        title=title,
        kind="bar",
        width=0.8,
        rot=0,
        custom_order=None,
        color=["#00BFC4", "#F8766D"],
        output="both",
        return_dict=True,
        figsize=(14, 8),
        outer_pad=10,
        logscale=False,
        plot_type="both",
        show_legend=True,
        label_fontsize=14,
        tick_fontsize=12,
    )

The above example generates stacked bar plots for ``"sex"`` and ``"income"`` 
grouped by ``"education"``. The plots are executed with legends, labels, and 
tick sizes customized for clarity. The function returns a dictionary of 
crosstabs for further analysis or export.

.. important:: 
    
    **Importance of Correctly Aligning Labels**

    It is crucial to properly align the elements in the ``legend_labels_list``, 
    ``title``, and ``func_col`` parameters when using the ``stacked_crosstab_plot`` 
    function. Each of these lists must be ordered consistently because the function 
    relies on their alignment to correctly assign labels and titles to the 
    corresponding plots and legends. 

    **For instance, in the example above:** 

    - The first element in ``func_col`` is ``"sex"``, and it is aligned with the first set of labels ``["Male", "Female"]`` in ``legend_labels_list`` and the first title ``"Sex"`` in the ``title`` list.
    - Similarly, the second element in ``func_col``, ``"income"``, aligns with the labels ``["<=50K", ">50K"]`` and the title ``"Income"``.

    **Misalignment between these lists would result in incorrect labels or titles being 
    applied to the plots, potentially leading to confusion or misinterpretation of the data. 
    Therefore, it's important to ensure that each list is ordered appropriately and 
    consistently to accurately reflect the data being visualized.**

    **Proper Setup of Lists**

    When setting up the ``legend_labels_list``, ``title``, and ``func_col``, ensure 
    that each element in the lists corresponds to the correct variable in the DataFrame. 
    This involves:

    - **Ordering**: Maintaining the same order across all three lists to ensure that labels and titles correspond correctly to the data being plotted.
    - **Consistency**: Double-checking that each label in ``legend_labels_list`` matches the categories present in the corresponding ``func_col``, and that the ``title`` accurately describes the plot.

    By adhering to these guidelines, you can ensure that the ``stacked_crosstab_plot`` 
    function produces accurate and meaningful visualizations that are easy to interpret and analyze.

.. raw:: html

   <div class="no-click">

.. image:: ../assets/age_group_by_sex.svg
   :alt: stacked bar plot of Age vs. Sex
   :align: center
   :width: 900px

.. raw:: html

   </div>

.. raw:: html
   
   <div style="height: 50px;"></div>

.. raw:: html

   <div class="no-click">

.. image:: ../assets/age_group_income.svg
   :alt: Stacked Bar Plot Age vs. Income
   :align: center
   :width: 900px

.. raw:: html

   </div>

.. raw:: html
   
   <div style="height: 50px;"></div>


.. note::

    When you set ``return_dict=True``, you are able to see the crosstabs printed out 
    as shown below. 

.. raw:: html

    <style type="text/css">
    .tg  {border-collapse:collapse;border-spacing:0;margin:0px auto;}
    .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
    overflow:hidden;padding:0px 5px;word-break:normal;}
    .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
    font-weight:normal;overflow:hidden;padding:0px 5px;word-break:normal;}
    .tg .tg-mwxe{text-align:right;vertical-align:middle}
    .tg .tg-p3ql{background-color:rgba(130, 130, 130, 0.08);text-align:right;vertical-align:middle}
    .tg .tg-yla0{font-weight:bold;text-align:left;vertical-align:middle}
    .tg .tg-7zrl{text-align:left;vertical-align:bottom}
    .tg .tg-zt7h{font-weight:bold;text-align:right;vertical-align:middle}
    .tg .tg-k750{background-color:rgba(130, 130, 130, 0.08);font-weight:bold;text-align:right;vertical-align:middle}
    @media screen and (max-width: 767px) {.tg {width: auto !important;}.tg col {width: auto !important;}.tg-wrap {overflow-x: auto;-webkit-overflow-scrolling: touch;margin: auto 0px;}}
    </style>
    <div class="tg-wrap"><table class="tg"><thead>
    <tr>
        <th class="tg-yla0" colspan="6">Crosstab for sex</th>
    </tr>
    <tr style="height: 10px;"><!-- Added empty row for spacing -->
        <td colspan="6" style="border: none;"></td>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td class="tg-zt7h">sex</td>
        <td class="tg-zt7h">Female</td>
        <td class="tg-zt7h">Male</td>
        <td class="tg-zt7h">Total</td>
        <td class="tg-zt7h">Female_%</td>
        <td class="tg-zt7h">Male_%</td>
    </tr>
    <tr>
        <td class="tg-k750">age_group</td>
        <td class="tg-k750"> </td>
        <td class="tg-k750"> </td>
        <td class="tg-k750"> </td>
        <td class="tg-k750"> </td>
        <td class="tg-k750"> </td>
    </tr>
    <tr>
        <td class="tg-mwxe">&lt; 18</td>
        <td class="tg-mwxe">295</td>
        <td class="tg-mwxe">300</td>
        <td class="tg-mwxe">595</td>
        <td class="tg-mwxe">49.58</td>
        <td class="tg-mwxe">50.42</td>
    </tr>
    <tr>
        <td class="tg-p3ql">18-29</td>
        <td class="tg-p3ql">5707</td>
        <td class="tg-p3ql">8213</td>
        <td class="tg-p3ql">13920</td>
        <td class="tg-p3ql">41</td>
        <td class="tg-p3ql">59</td>
    </tr>
    <tr>
        <td class="tg-mwxe">30-39</td>
        <td class="tg-mwxe">3853</td>
        <td class="tg-mwxe">9076</td>
        <td class="tg-mwxe">12929</td>
        <td class="tg-mwxe">29.8</td>
        <td class="tg-mwxe">70.2</td>
    </tr>
    <tr>
        <td class="tg-p3ql">40-49</td>
        <td class="tg-p3ql">3188</td>
        <td class="tg-p3ql">7536</td>
        <td class="tg-p3ql">10724</td>
        <td class="tg-p3ql">29.73</td>
        <td class="tg-p3ql">70.27</td>
    </tr>
    <tr>
        <td class="tg-mwxe">50-59</td>
        <td class="tg-mwxe">1873</td>
        <td class="tg-mwxe">4746</td>
        <td class="tg-mwxe">6619</td>
        <td class="tg-mwxe">28.3</td>
        <td class="tg-mwxe">71.7</td>
    </tr>
    <tr>
        <td class="tg-p3ql">60-69</td>
        <td class="tg-p3ql">939</td>
        <td class="tg-p3ql">2115</td>
        <td class="tg-p3ql">3054</td>
        <td class="tg-p3ql">30.75</td>
        <td class="tg-p3ql">69.25</td>
    </tr>
    <tr>
        <td class="tg-mwxe">70-79</td>
        <td class="tg-mwxe">280</td>
        <td class="tg-mwxe">535</td>
        <td class="tg-mwxe">815</td>
        <td class="tg-mwxe">34.36</td>
        <td class="tg-mwxe">65.64</td>
    </tr>
    <tr>
        <td class="tg-p3ql">80-89</td>
        <td class="tg-p3ql">40</td>
        <td class="tg-p3ql">91</td>
        <td class="tg-p3ql">131</td>
        <td class="tg-p3ql">30.53</td>
        <td class="tg-p3ql">69.47</td>
    </tr>
    <tr>
        <td class="tg-mwxe">90-99</td>
        <td class="tg-mwxe">17</td>
        <td class="tg-mwxe">38</td>
        <td class="tg-mwxe">55</td>
        <td class="tg-mwxe">30.91</td>
        <td class="tg-mwxe">69.09</td>
    </tr>
    <tr>
        <td class="tg-p3ql">Total</td>
        <td class="tg-p3ql">16192</td>
        <td class="tg-p3ql">32650</td>
        <td class="tg-p3ql">48842</td>
        <td class="tg-p3ql">33.15</td>
        <td class="tg-p3ql">66.85</td>
    </tr>
    <tr style="height: 10px;"><!-- Added empty row for spacing -->
        <td colspan="6" style="border: none;"></td>
    </tr>
    <tr>
        <th class="tg-yla0" colspan="6">Crosstab for income</th>
    </tr>
    <tr style="height: 10px;"><!-- Added empty row for spacing -->
        <td colspan="6" style="border: none;"></td>
    </tr>
    <tr>
        <td class="tg-zt7h">income</td>
        <td class="tg-zt7h">&lt;=50K</td>
        <td class="tg-zt7h">&gt;50K</td>
        <td class="tg-zt7h">Total</td>
        <td class="tg-zt7h">&lt;=50K_%</td>
        <td class="tg-zt7h">&gt;50K_%</td>
    </tr>
    <tr>
        <td class="tg-k750">age_group</td>
        <td class="tg-k750"> </td>
        <td class="tg-k750"> </td>
        <td class="tg-k750"> </td>
        <td class="tg-k750"> </td>
        <td class="tg-k750"> </td>
    </tr>
    <tr>
        <td class="tg-mwxe">&lt; 18</td>
        <td class="tg-mwxe">595</td>
        <td class="tg-mwxe">0</td>
        <td class="tg-mwxe">595</td>
        <td class="tg-mwxe">100</td>
        <td class="tg-mwxe">0</td>
    </tr>
    <tr>
        <td class="tg-p3ql">18-29</td>
        <td class="tg-p3ql">13174</td>
        <td class="tg-p3ql">746</td>
        <td class="tg-p3ql">13920</td>
        <td class="tg-p3ql">94.64</td>
        <td class="tg-p3ql">5.36</td>
    </tr>
    <tr>
        <td class="tg-mwxe">30-39</td>
        <td class="tg-mwxe">9468</td>
        <td class="tg-mwxe">3461</td>
        <td class="tg-mwxe">12929</td>
        <td class="tg-mwxe">73.23</td>
        <td class="tg-mwxe">26.77</td>
    </tr>
    <tr>
        <td class="tg-p3ql">40-49</td>
        <td class="tg-p3ql">6738</td>
        <td class="tg-p3ql">3986</td>
        <td class="tg-p3ql">10724</td>
        <td class="tg-p3ql">62.83</td>
        <td class="tg-p3ql">37.17</td>
    </tr>
    <tr>
        <td class="tg-mwxe">50-59</td>
        <td class="tg-mwxe">4110</td>
        <td class="tg-mwxe">2509</td>
        <td class="tg-mwxe">6619</td>
        <td class="tg-mwxe">62.09</td>
        <td class="tg-mwxe">37.91</td>
    </tr>
    <tr>
        <td class="tg-p3ql">60-69</td>
        <td class="tg-p3ql">2245</td>
        <td class="tg-p3ql">809</td>
        <td class="tg-p3ql">3054</td>
        <td class="tg-p3ql">73.51</td>
        <td class="tg-p3ql">26.49</td>
    </tr>
    <tr>
        <td class="tg-mwxe">70-79</td>
        <td class="tg-mwxe">668</td>
        <td class="tg-mwxe">147</td>
        <td class="tg-mwxe">815</td>
        <td class="tg-mwxe">81.96</td>
        <td class="tg-mwxe">18.04</td>
    </tr>
    <tr>
        <td class="tg-p3ql">80-89</td>
        <td class="tg-p3ql">115</td>
        <td class="tg-p3ql">16</td>
        <td class="tg-p3ql">131</td>
        <td class="tg-p3ql">87.79</td>
        <td class="tg-p3ql">12.21</td>
    </tr>
    <tr>
        <td class="tg-mwxe">90-99</td>
        <td class="tg-mwxe">42</td>
        <td class="tg-mwxe">13</td>
        <td class="tg-mwxe">55</td>
        <td class="tg-mwxe">76.36</td>
        <td class="tg-mwxe">23.64</td>
    </tr>
    <tr>
        <td class="tg-p3ql">Total</td>
        <td class="tg-p3ql">37155</td>
        <td class="tg-p3ql">11687</td>
        <td class="tg-p3ql">48842</td>
        <td class="tg-p3ql">76.07</td>
        <td class="tg-p3ql">23.93</td>
    </tr>
    </tbody></table></div>

\

When you set ``return_dict=True``, you can access these crosstabs as 
DataFrames by assigning them to their own vriables. For example: 

.. code-block:: python 

    crosstab_age_sex = stacked_crosstabs["sex"]
    crosstab_age_income = stacked_crosstabs["income"]


Pivoted Stacked Bar Plots Example
-----------------------------------

Using the census dataset [1]_, to create horizontal stacked bar plots, set the ``kind`` parameter to 
``"barh"`` in the ``stacked_crosstab_plot function``. This option pivots the 
standard vertical stacked bar plot into a horizontal orientation, making it easier 
to compare categories when there are many labels on the ``y-axis``.

For ``kind="barh"``, matplotlib renders categories bottom-to-top by default, so if you want < 18 at the top pass the list in reverse order:

.. code-block:: python

    custom_order = [
        "90-99", "80-89", "70-79", "60-69",
        "50-59", "40-49", "30-39", "18-29", "< 18"
    ]

.. raw:: html

   <div class="no-click">

.. image:: ../assets/age_group_income_pivoted.svg
   :alt: Stacked Bar Plot Age vs. Income (Pivoted)
   :align: center
   :width: 900px

.. raw:: html

   </div>

.. raw:: html
   
   <div style="height: 50px;"></div>


Non-Normalized Stacked Bar Plots Example
----------------------------------------------------

In the census data [1]_, to create stacked bar plots without the normalized versions, 
set the ``plot_type`` parameter to ``"regular"`` in the ``stacked_crosstab_plot`` 
function. This option removes the display of normalized plots beneath the regular 
versions. Alternatively, setting the ``plot_type`` to ``"normalized"`` will display 
only the normalized plots. The example below demonstrates regular stacked bar plots 
for income by age.

.. raw:: html

   <div class="no-click">

.. image:: ../assets/age_group_income_regular.svg
   :alt: Stacked Bar Plot Age vs. Income (Regular)
   :align: center
   :width: 900px

.. raw:: html

   </div>

.. raw:: html
   
   <div style="height: 50px;"></div>


Regular Non-Stacked Bar Plots Example
----------------------------------------------------

In the census data [1]_, to generate regular (non-stacked) bar plots without 
displaying their normalized versions, set the ``plot_type`` parameter to ``"regular"`` 
in the ``stacked_crosstab_plot`` function and enable ``remove_stacks`` by setting 
it to ``True``. This configuration removes any stacked elements and prevents the 
display of normalized plots beneath the regular versions. Alternatively, setting 
``plot_type`` to ``"normalized"`` will display only the normalized plots.

When unstacking bar plots in this fashion, the distribution is aligned in descending 
order, making it easier to visualize the most prevalent categories.

In the example below, the color of the bars has been set to a dark grey (``#333333``), 
and the legend has been removed by setting ``show_legend=False``. This illustrates 
regular bar plots for income by age, without stacking.


.. raw:: html

   <div class="no-click">

.. image:: ../assets/age_group_distribution.svg
   :alt: Bar Plot Age vs. Income (Regular)
   :align: center
   :width: 900px

.. raw:: html

   </div>

.. raw:: html
   
   <div style="height: 50px;"></div>


Outcome Crosstab Plots
=======================

**Visualize the distribution of multiple categorical predictors with respect to a binary outcome.**

The ``outcome_crosstab_plot`` function produces stacked bar plots for each categorical variable provided, segmented by a binary outcome. It supports both count-based and normalized percentage views, optional value annotations, flexible color configurations, and output saving. Each subplot compares a predictor variable against the outcome.

.. function:: outcome_crosstab_plot(df, list_name, outcome, bbox_to_anchor=(0.5, -0.25), w_pad=4, h_pad=4, figsize=(12, 8), label_fontsize=12, tick_fontsize=10, n_rows=None, n_cols=None, label_0=None, label_1=None, normalize=False, show_value_counts=False, color_schema=None, save_plots=False, image_path_png=None, image_path_svg=None, string=None)

    :param df: The DataFrame containing your data.
    :type df: pandas.DataFrame
    :param list_name: List of column names (categorical variables) to plot.
    :type list_name: list of str
    :param outcome: Name of the binary outcome variable.
    :type outcome: str
    :param bbox_to_anchor: Location for legend anchoring. Default is ``(0.5, -0.25)``.
    :type bbox_to_anchor: tuple
    :param w_pad: Padding between columns in the subplot grid.
    :type w_pad: float
    :param h_pad: Padding between rows in the subplot grid.
    :type h_pad: float
    :param figsize: Tuple specifying the overall figure size.
    :type figsize: tuple of int
    :param label_fontsize: Font size for axis labels, titles, and legend text.
    :type label_fontsize: int
    :param tick_fontsize: Font size for tick labels.
    :type tick_fontsize: int
    :param n_rows: Optional number of subplot rows. If not provided, it's auto-calculated.
    :type n_rows: int, optional
    :param n_cols: Optional number of subplot columns. If not provided, it's auto-calculated.
    :type n_cols: int, optional
    :param label_0: Optional custom label for outcome value ``0``.
    :type label_0: str, optional
    :param label_1: Optional custom label for outcome value ``1``.
    :type label_1: str, optional
    :param normalize: If True, show proportions instead of raw counts.
    :type normalize: bool
    :param show_value_counts: If True, append counts or percentages to the legend.
    :type show_value_counts: bool
    :param color_schema: Color mapping options. Can be:
                         - ``None`` (use default colors)
                         - list/tuple (applies across all subplots)
                         - dict mapping variable name to color list
    :type color_schema: ``None``, list, tuple, or dict
    :param save_plots: Whether to save the plots.
    :type save_plots: bool
    :param image_path_png: Directory path to save PNG files.
    :type image_path_png: str, optional
    :param image_path_svg: Directory path to save SVG files.
    :type image_path_svg: str, optional
    :param string: Base name for output files.
    :type string: str, optional

    :returns: ``None``. Displays plots and optionally saves them.
    :rtype: ``None``

.. admonition:: Notes

    - The function assumes a binary outcome. For multiclass, use alternative plotting strategies.
    - You can format outcome axis labels using ``label_0`` and ``label_1`` for better readability.
    - Normalization (``normalize=True``) adjusts bar heights to percentages rather than counts.
    - When ``show_value_counts=True``, each legend entry includes either ``n=`` counts or percentage values.

Outcome Crosstab Example
-------------------------

This example demonstrates how to generate outcome-wise crosstab plots for multiple categorical variables (``race`` and ``sex``) against a binary outcome variable (``income``).

.. code-block:: python

    from eda_toolkit import outcome_crosstab_plot

    bar_list = ["race", "sex"]

    outcome_crosstab_plot(
        df=df,
        list_name=bar_list,
        label_0="<=50K",
        label_1=">50K",
        figsize=(10, 6),
        normalize=False,
        string="outcome_by_feature",
        outcome="income",
        show_value_counts=True,
    )

.. note::

    Ensure that the DataFrame ``df`` contains the specified categorical variables in ``bar_list`` and the binary outcome variable ``income``. The function will generate stacked bar plots for each categorical variable, comparing their distributions against the binary outcome.
    
    In this example:

    - ``df`` is the DataFrame containing your dataset.
    - ``bar_list`` defines the list of categorical variables to compare against ``income``.
    - The labels ``<=50K`` and ``>50K`` are shown on the x-axis instead of default numeric values.
    - Setting ``normalize=False`` plots raw counts instead of percentages.
    - ``show_value_counts=True`` includes value counts in the legend.
    - Output plots are saved as PNG and SVG files to the provided paths with the prefix ``outcome_by_feature``.


.. raw:: html

    <div class="no-click">

.. image:: ../assets/outcome_by_var.svg
   :alt: Outcome vs. Variable
   :align: center
   :width: 900px

.. raw:: html

    </div>

.. raw:: html
   
   <div style="height: 50px;"></div>


Box and Violin Plots
=====================

**Create and save individual boxplots or violin plots, an entire grid of subplots, or both for specified metrics and comparisons.**

The ``box_violin_plot`` function generates individual and/or subplot-based plots of boxplots or violin plots for specified metrics against comparison categories in a DataFrame. It offers extensive customization options, including control over plot type, display mode, axis label rotation, figure size, and saving preferences, making it suitable for a wide range of data visualization needs.

This function supports:

- Rotating plots (swapping x and y axes).
- Adjusting font sizes for axis labels and tick labels.
- Wrapping plot titles for better readability.
- Saving plots in PNG and/or SVG format with customizable file paths.
- Visualizing the distribution of metrics across categories, either individually, as subplots, or both.

.. function:: box_violin_plot(df, metrics_list, metrics_comp, n_rows=None, n_cols=None, image_path_png=None, image_path_svg=None, image_filename=None, show_legend=True, legend_loc="best", plot_type="boxplot", xlabel_rot=0, show_plot="both", rotate_plot=False, custom_order=None, individual_figsize=(6, 4), subplot_figsize=None, label_fontsize=12, tick_fontsize=10, text_wrap=50, xlim=None, ylim=None, **kwargs)

   :param df: The DataFrame containing the data to plot.
   :type df: pandas.DataFrame

   :param metrics_list: List of column names representing the metrics to plot.
   :type metrics_list: list of str

   :param metrics_comp: List of column names representing the comparison
      categories. A plain string is automatically coerced to a
      single-element list.
   :type metrics_comp: list of str or str

   :param n_rows: Number of rows in the subplot grid. Calculated
      automatically if not provided.
   :type n_rows: int, optional

   :param n_cols: Number of columns in the subplot grid. Calculated
      automatically if not provided.
   :type n_cols: int, optional

   :param image_path_png: Directory path to save plots in PNG format.
   :type image_path_png: str, optional

   :param image_path_svg: Directory path to save plots in SVG format.
   :type image_path_svg: str, optional

   :param image_filename: Base filename (without extension) used when
      saving figures. No files are saved if this is not provided. For
      individual plots, the metric name and plot type are appended to
      this base. For subplot grids, the plot type is appended.
   :type image_filename: str, optional

   :param show_legend: Whether to display the legend on the plots.
      Default is ``True``.
   :type show_legend: bool, optional

   :param legend_loc: Location of the legend, passed to Matplotlib's
      ``legend(loc=...)``. Common options include ``"best"``,
      ``"upper right"``, ``"upper left"``, ``"lower left"``,
      ``"lower right"``, and ``"center"``. Default is ``"best"``.
   :type legend_loc: str, optional

   :param plot_type: Type of plot to generate. Options are
      ``"boxplot"`` or ``"violinplot"``. Shorthand aliases ``"box"``
      and ``"violin"`` are also accepted. Default is ``"boxplot"``.
   :type plot_type: str, optional

   :param xlabel_rot: Rotation angle for x-axis labels. Default is ``0``.
   :type xlabel_rot: int, optional

   :param show_plot: Specify the plot display mode: ``"individual"``,
      ``"subplots"``, or ``"both"``. Default is ``"both"``.
   :type show_plot: str, optional

   :param rotate_plot: If ``True``, rotates the plots by swapping the
      x and y axes. Default is ``False``.
   :type rotate_plot: bool, optional

   :param custom_order: Specifies the display order of categories along
      the comparison axis. If ``None``, the default order observed in
      the data is used.
   :type custom_order: list, optional

   :param individual_figsize: Dimensions ``(width, height)`` for
      individual plots. Default is ``(6, 4)``.
   :type individual_figsize: tuple of int, optional

   :param subplot_figsize: Dimensions ``(width, height)`` of the
      subplots. Defaults to a size proportional to the number of rows
      and columns if not provided.
   :type subplot_figsize: tuple of int, optional

   :param label_fontsize: Font size for axis labels. Default is ``12``.
   :type label_fontsize: int, optional

   :param tick_fontsize: Font size for axis tick labels. Default is ``10``.
   :type tick_fontsize: int, optional

   :param text_wrap: Maximum number of characters in plot titles and
      axis labels before wrapping to the next line. Default is ``50``.
   :type text_wrap: int, optional

   :param xlim: Limits for the x-axis as ``(min, max)``.
   :type xlim: tuple of float, optional

   :param ylim: Limits for the y-axis as ``(min, max)``.
   :type ylim: tuple of float, optional

   :param kwargs: Additional keyword arguments passed to the Seaborn
      plotting function. Layout-related keys (``"figsize"``,
      ``"subplot_figsize"``, ``"individual_figsize"``) are automatically
      stripped. If ``palette`` is passed here it takes precedence over
      the internal default and is applied consistently across all
      subplots.

   :returns: ``None``
   :rtype: None

   :raises ValueError: If ``show_plot`` is not one of ``"individual"``,
      ``"subplots"``, or ``"both"``.
   :raises ValueError: If ``rotate_plot`` is not a boolean value.
   :raises ValueError: If ``individual_figsize`` or ``subplot_figsize``
      is not a tuple or list of two numbers.
   :raises ValueError: If ``plot_type`` is not one of ``"boxplot"``,
      ``"violinplot"``, ``"box"``, or ``"violin"``.
   :raises ValueError: If ``image_filename`` is provided but neither
      ``image_path_png`` nor ``image_path_svg`` is specified.

   .. admonition:: Notes

      - ``save_plots`` has been removed. Figures are saved only when
        ``image_filename`` is provided alongside at least one output
        path.
      - ``custom_order`` is passed directly to Seaborn's ``order``
        parameter and controls category ordering on the comparison axis.
      - Shorthand aliases ``"box"`` and ``"violin"`` are accepted for
        ``plot_type``.
      - If ``palette`` is supplied via ``**kwargs``, it is resolved once
        before any plotting loop and applied consistently to all
        subplots.


This function provides the ability to create and save boxplots or violin plots for specified metrics and comparison categories. It supports the generation of individual plots, subplots, or both. Users can customize the appearance, save the plots to specified directories, and control the display of legends and labels.

Box Plots: Subplots Example
-----------------------------

In this example with the US census data [1]_, the ``box_violin_plot`` function is
employed to create subplots of boxplots, comparing different metrics against the
``"age_group"`` column in the DataFrame. The ``metrics_comp`` parameter is set to
``["age_group"]``, meaning that the comparison will be based on different age
groups. The ``metrics_list`` is provided as ``age_boxplot_list``, which contains
the specific metrics to be visualized.

The plots are displayed in a subplots format, as indicated by the
``show_plot="subplots"`` parameter. The ``plot_type`` is set to ``"boxplot"``,
so the function generates boxplots for each metric in the list. The ``x``-axis
labels are rotated by 90 degrees (``xlabel_rot=90``) to ensure legibility, and
the legend is hidden by setting ``show_legend=False``, keeping the plots clean
and focused on the data. The ``image_path_png``, ``image_path_svg``, and
``image_filename`` parameters are specified to save the plots in both PNG and
SVG formats. This configuration provides a comprehensive visual comparison of
the specified metrics across different age groups, with all plots saved for
future reference or publication.


.. code-block:: python

    age_boxplot_list = df[
        [
            "education-num",
            "hours-per-week",
        ]
    ].columns.to_list()


.. code-block:: python

    from eda_toolkit import box_violin_plot

    metrics_comp = ["age_group"]

    box_violin_plot(
        df=df,
        metrics_list=age_boxplot_list,
        metrics_comp=metrics_comp,
        image_path_png=image_path_png,
        image_path_svg=image_path_svg,
        image_filename="age_group_boxplot",
        show_plot="subplots",
        show_legend=False,
        plot_type="boxplot",
        xlabel_rot=90,
    )

.. raw:: html

   <div class="no-click">

.. image:: ../assets/all_plots_comparisons_boxplot.png
   :alt: Box Plot Comparisons
   :align: center
   :width: 900px

.. raw:: html

   </div>

.. raw:: html
   
   <div style="height: 50px;"></div>

Violin Plots: Subplots Example
-------------------------------

In this example with the US census data [1]_, we keep everything the same as the prior example, but change the 
``plot_type`` to ``violinplot``. This adjustment will generate violin plots instead 
of boxplots while maintaining all other settings.


.. code-block:: python

    from eda_toolkit import box_violin_plot

    metrics_comp = ["age_group"]

    box_violin_plot(
        df=df,
        metrics_list=age_boxplot_list,
        metrics_comp=metrics_comp,
        show_plot="subplots",
        show_legend=False,
        plot_type="violinplot",
        xlabel_rot=90,
    )

.. raw:: html

   <div class="no-click">

.. image:: ../assets/all_plots_comparisons_violinplot.png
   :alt: Violin Plot Comparisons
   :align: center
   :width: 900px

.. raw:: html

   </div>

.. raw:: html
   
   <div style="height: 50px;"></div>


Pivoted Violin Plots: Subplots Example
---------------------------------------

In this example with the US census data [1]_, we set ``xlabel_rot=0`` and ``rotate_plot=True`` 
to pivot the plot, changing the orientation of the axes while keeping the ``x-axis`` labels upright. 
This adjustment flips the axes, providing a different perspective on the data distribution.

.. code-block:: python

    from eda_toolkit import box_violin_plot

    metrics_comp = ["age_group"]

    box_violin_plot(
        df=df,
        metrics_list=age_boxplot_list,
        metrics_comp=metrics_comp,
        show_plot="subplots",
        rotate_plot=True,
        show_legend=False,
        plot_type="violinplot",
        xlabel_rot=0,
    )

.. raw:: html

   <div class="no-click">

.. image:: ../assets/all_plots_comparisons_violinplot_pivoted.png
   :alt: Violin Plot Comparisons (Pivoted)
   :align: center
   :width: 900px

.. raw:: html

   </div>

.. raw:: html
   
   <div style="height: 50px;"></div>


Scatter Plots and Best Fit Lines
==================================

Scatter Fit Plot
------------------

**Create and Save Scatter Plots or Subplots of Scatter Plots**

This function, ``scatter_fit_plot``, generates scatter plots for one or more pairs of variables (``x_vars`` and ``y_vars``) from a given DataFrame. The function can produce individual scatter plots or organize multiple scatter plots into a subplots layout, enabling easy visualization of relationships between different pairs of variables in a unified view.

**Optional Features**

- **Best Fit Line**: Adds an optional best fit line to the scatter plots, calculated using linear regression. This provides visual insights into the linear relationship between variables. The equation of the line can also be displayed in the plot's legend.

- **Correlation Coefficient Display**: Displays the Pearson correlation coefficient directly in the plot title, offering a numeric indicator of the linear relationship between variables.

**Customization Options**

The function provides a variety of parameters to customize the appearance and behavior of scatter plots:

- **Color**: Customize point colors with a fixed color or a ``hue`` parameter to group points by a categorical variable.

- **Size and Marker**: Adjust the size of points dynamically based on a variable, and specify custom markers to represent data effectively.

- **Labels and Axis Configuration**: Set axis labels, font sizes, label rotation, and axis limits to ensure readability and focus on relevant data.

**Plot Management**

- **Display Options**: Control how plots are displayed: as individual plots, subplots, or both.

- **Saving Options**: Save the generated plots in PNG or SVG formats. Specify which plots to save (e.g., ``"all"``, ``"individual"``, or ``"subplots"``) and their respective file paths.

**Advanced Features**

- **Combination Plotting**: Automatically generate scatter plots for all combinations of variables when using the ``all_vars`` parameter.

- **Exclusion Rules**: Exclude specific (``x_var``, ``y_var``) combinations from being plotted using the ``exclude_combinations`` parameter.

- **Legend and Aesthetic Adjustments**: Toggle legends, adjust plot size for individual or subplots, and wrap long titles for clarity.

**Error Handling**

The function performs comprehensive input validation to prevent common errors, such as:

- Conflicting inputs for ``all_vars``, ``x_vars``, and ``y_vars``.
- Invalid or missing column names in the DataFrame.
- Incorrectly specified parameters like axis limits or figure sizes.

.. function:: scatter_fit_plot(df, x_vars=None, y_vars=None, all_vars=None, exclude_combinations=None, n_rows=None, n_cols=None, max_cols=4, image_path_png=None, image_path_svg=None, save_plots=None, show_legend=True, legend_loc="best", xlabel_rot=0, show_plot="subplots", rotate_plot=False, individual_figsize=(6, 4), subplot_figsize=None, label_fontsize=12, tick_fontsize=10, text_wrap=50, add_best_fit_line=False, scatter_color="C0", best_fit_linecolor="red", best_fit_linestyle="-", hue=None, hue_palette=None, size=None, sizes=None, marker="o", show_correlation=True, xlim=None, ylim=None, label_names=None, **kwargs)

    Generate scatter plots or subplots of scatter plots for the given ``x_vars`` and ``y_vars``, with optional best fit lines, correlation coefficients, and customizable aesthetics.

    :param df: The DataFrame containing the data for the plots.
    :type df: pandas.DataFrame

    :param x_vars: List of variable names to plot on the ``x-axis``. If a single string is provided, it will be converted into a list with one element.
    :type x_vars: list of str or str, optional

    :param y_vars: List of variable names to plot on the ``y-axis``. If a single string is provided, it will be converted into a list with one element.
    :type y_vars: list of str or str, optional

    :param all_vars: Generates scatter plots for all combinations of variables in this list, overriding ``x_vars`` and ``y_vars``.
    :type all_vars: list of str, optional

    :param exclude_combinations: List of (``x_var``, ``y_var``) combinations to exclude from plotting.
    :type exclude_combinations: list of tuples, optional

    :param n_rows: Number of rows in the subplot grid. Calculated automatically if not specified.
    :type n_rows: int, optional

    :param n_cols: Number of columns in the subplot grid. Calculated automatically if not specified.
    :type n_cols: int, optional

    :param max_cols: Maximum number of columns in the subplot grid. Default is ``4``.
    :type max_cols: int, optional

    :param image_path_png: Directory path to save PNG images of scatter plots.
    :type image_path_png: str, optional

    :param image_path_svg: Directory path to save SVG images of scatter plots.
    :type image_path_svg: str, optional

    :param save_plots: Specify which plots to save (``"all"``, ``"individual"``, or ``"subplots"``); uses a progress bar (``tqdm``) for saving.
    :type save_plots: str, optional

    :param show_legend: Toggle display of the plot legend. Default is ``True``.
    :type show_legend: bool, optional

    :param legend_loc: Location of the legend on the plot. Passed directly to
        ``matplotlib.axes.Axes.legend``. Common options include ``"best"``,
        ``"upper right"``, ``"upper left"``, ``"lower left"``,
        ``"lower right"``, and ``"center"``.
    :type legend_loc: str, optional

    :param xlabel_rot: Angle to rotate ``x-axis`` labels. Default is ``0``.
    :type xlabel_rot: int, optional

    :param show_plot: Controls plot display: ``"individual"``, ``"subplots"``, ``"both"``, or ``"combinations"``. Default is ``"subplots"``. Use ``"combinations"`` to return all valid (``x, y``) variable pairs without generating plots.
    :type show_plot: str, optional

    :param rotate_plot: Rotate plots (swap ``x`` and ``y`` axes). Default is ``False``.
    :type rotate_plot: bool, optional

    :param individual_figsize: Dimensions for individual plot figures (width, height). Default is ``(6, 4)``.
    :type individual_figsize: tuple or list, optional

    :param subplot_figsize: Dimensions for subplots (width, height). Calculated automatically if not specified.
    :type subplot_figsize: tuple or list, optional

    :param label_fontsize: Font size for axis labels. Default is ``12``.
    :type label_fontsize: int, optional

    :param tick_fontsize: Font size for axis ticks. Default is ``10``.
    :type tick_fontsize: int, optional

    :param text_wrap: Maximum title width before wrapping. Default is ``50``.
    :type text_wrap: int, optional

    :param add_best_fit_line: Add a best fit line to scatter plots. Default is ``False``.
    :type add_best_fit_line: bool, optional

    :param scatter_color: Default color for scatter points. Default is ``"C0"``.
    :type scatter_color: str, optional

    :param best_fit_linecolor: Color for the best fit line. Default is ``"red"``.
    :type best_fit_linecolor: str, optional

    :param best_fit_linestyle: Linestyle for the best fit line. Default is ``"-"``.
    :type best_fit_linestyle: str, optional

    :param hue: Column name for grouping variable to color points differently.
    :type hue: str, optional

    :param hue_palette: Colors for each ``hue`` level (requires ``hue``).
    :type hue_palette: dict, list, or str, optional

    :param size: Variable to scale scatter point sizes.
    :type size: str, optional

    :param sizes: Mapping of minimum and maximum point sizes.
    :type sizes: dict, optional

    :param marker: Style of scatter points. Default is ``"o"``.
    :type marker: str, optional

    :param show_correlation: Display correlation coefficient in titles. Default is ``True``.
    :type show_correlation: bool, optional

    :param xlim: Limits for the ``x-axis`` (``min``, ``max``).
    :type xlim: tuple or list, optional

    :param ylim: Limits for the ``y-axis`` (``min``, ``max``).
    :type ylim: tuple or list, optional

    :param label_names: Rename columns for display in titles and labels.
    :type label_names: dict, optional

    :param kwargs: Additional options for ``sns.scatterplot``.
    :type kwargs: dict, optional

    :raises ValueError: See function docstring for detailed error conditions.

    :returns: ``None``. Generates and optionally saves scatter plots.


Regression-Centric Scatter Plots Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this US census data [1]_ example, the ``scatter_fit_plot`` function is 
configured to display the Pearson correlation coefficient and a best fit line 
on each scatter plot. The correlation coefficient is shown in the plot title, 
controlled by the ``show_correlation=True`` parameter, which provides a measure 
of the strength and direction of the linear relationship between the variables. 
Additionally, the ``add_best_fit_line=True`` parameter adds a best fit line to 
each plot, with the equation for the line displayed in the legend. This equation, 
along with the best fit line, helps to visually assess the relationship between 
the variables, making it easier to identify trends and patterns in the data. The 
combination of the correlation coefficient and the best fit line offers both 
a quantitative and visual representation of the relationships, enhancing the 
interpretability of the scatter plots.

.. code-block:: python

    from eda_toolkit import scatter_fit_plot

    scatter_fit_plot(
        df=df,
        x_vars=["age", "education-num"],
        y_vars=["hours-per-week"],
        show_legend=True,
        show_plot="subplots",
        subplot_figsize=None,
        label_fontsize=14,
        tick_fontsize=12,
        add_best_fit_line=True,
        scatter_color="#808080",
        show_correlation=True,
    )


.. raw:: html

   <div class="no-click">

.. image:: ../assets/scatter_plots_1x2_grid.png
   :alt: Scatter Plot Comparisons (with Best Fit Lines)
   :align: center
   :width: 900px

.. raw:: html

   </div>

.. raw:: html
   
   <div style="height: 50px;"></div>

Scatter Plots Grouped by Category Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this example, the ``scatter_fit_plot`` function is used to generate subplots of 
scatter plots that examine the relationships between ``age`` and ``hours-per-week`` 
as well as ``education-num`` and ``hours-per-week``. Compared to the previous 
example, a few key inputs have been changed to adjust the appearance and functionality 
of the plots:

1. **Hue and Hue Palette**: The ``hue`` parameter is set to ``"income"``, meaning that the 
   data points in the scatter plots are colored according to the values in the ``income`` 
   column. A custom color mapping is provided via the ``hue_palette`` parameter, where the 
   income categories ``"<=50K"`` and ``">50K"`` are assigned the colors ``"brown"`` and 
   ``"green"``, respectively. This change visually distinguishes the data points based on 
   income levels.

2. **Scatter Color**: The ``scatter_color`` parameter is set to ``"#808080"``, which applies 
   a grey color to the scatter points when no ``hue`` is provided. However, since a ``hue`` 
   is specified in this example, the ``hue_palette`` takes precedence and overrides this color setting.

3. **Best Fit Line**: The ``add_best_fit_line`` parameter is set to ``False``, meaning that 
   no best fit line is added to the scatter plots. This differs from the previous example where 
   a best fit line was included.

4. **Correlation Coefficient**: The ``show_correlation`` parameter is set to ``False``, so the 
   Pearson correlation coefficient will not be displayed in the plot titles. This is another 
   change from the previous example where the correlation coefficient was included.

5. **Hue Legend**: The ``show_legend`` parameter remains set to ``True``, ensuring that the 
   legend displaying the hue categories (``"<=50K"`` and ``">50K"``) appears on the plots, 
   helping to interpret the color coding of the data points.

These changes allow for the creation of scatter plots that highlight the income levels 
of individuals, with custom color coding and without additional elements like a best 
fit line or correlation coefficient. The resulting subplots are then saved as 
images in the specified paths.


.. code-block:: python

    from eda_toolkit import scatter_fit_plot

    hue_dict = {"<=50K": "brown", ">50K": "green"}

    scatter_fit_plot(
        df=df,
        x_vars=["age", "education-num"],
        y_vars=["hours-per-week"],
        show_legend=True,
        show_plot="subplots",
        label_fontsize=14,
        tick_fontsize=12,
        add_best_fit_line=False,
        scatter_color="#808080",
        hue="income",
        hue_palette=hue_dict,
        show_correlation=False,
    )

.. raw:: html

   <div class="no-click">

.. image:: ../assets/scatter_plots_grid_grouped.png
   :alt: Scatter Plot Comparisons (Grouped)
   :align: center
   :width: 900px

.. raw:: html

   </div>

.. raw:: html
   
   <div style="height: 50px;"></div>


Scatter Plots (All Combinations Example)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this example, the ``scatter_fit_plot`` function is used to generate subplots of scatter plots that explore the relationships between all numeric variables in the ``df`` DataFrame. The function automatically identifies and plots all possible combinations of these variables. Below are key aspects of this example:

1. **All Variables Combination**: The ``all_vars`` parameter is used to automatically generate scatter plots for all possible combinations of numerical variables in the DataFrame. This means you don't need to manually specify ``x_vars`` and ``y_vars``, as the function will iterate through each possible pair.

2. **Subplot Display**: The ``show_plot`` parameter is set to ``"subplots"``, so the scatter plots are displayed in subplots format. This is useful for comparing multiple relationships simultaneously.

3. **Font Sizes**: The ``label_fontsize`` and ``tick_fontsize`` parameters are set to ``14`` and ``12``, respectively. This increases the readability of axis labels and tick marks, making the plots more visually accessible.

4. **Best Fit Line**: The ``add_best_fit_line`` parameter is set to ``True``, meaning that a best fit line is added to each scatter plot. This helps in visualizing the linear relationship between variables.

5. **Scatter Color**: The ``scatter_color`` parameter is set to ``"#808080"``, applying a grey color to the scatter points. This provides a neutral color that does not distract from the data itself.

6. **Correlation Coefficient**: The ``show_correlation`` parameter is set to ``True``, so the Pearson correlation coefficient will be displayed in the plot titles. This helps to quantify the strength of the relationship between the variables.

These settings allow for the creation of scatter plots that comprehensively explore the relationships between all numeric variables in the DataFrame. The plots are saved in subplots format, with added best fit lines and correlation coefficients for deeper analysis. The resulting images can be stored in the specified directory for future reference.

.. code-block:: python

    from eda_toolkit import scatter_fit_plot

    scatter_fit_plot(
        df=df,
        all_vars=df.select_dtypes(np.number).columns.to_list(),
        show_legend=True,
        show_plot="subplots",
        label_fontsize=14,
        tick_fontsize=12,
        add_best_fit_line=True,
        scatter_color="#808080",
        show_correlation=True,
    )

.. raw:: html

   <div class="no-click">

.. image:: ../assets/scatter_plots_grid.png
   :alt: Scatter Plot Comparisons (Grouped2)
   :align: center
   :width: 900px

.. raw:: html

   </div>

.. raw:: html
   
   <div style="height: 50px;"></div>


Scatter Plots: Excluding Specific Combinations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example 1
~~~~~~~~~~~

In this example, the ``scatter_fit_plot`` function is used to generate subplots of 
scatter plots while excluding specific combinations of variables. This allows for 
a more targeted exploration of relationships, omitting plots that may be redundant 
or irrelevant. Below are key aspects of this example:

1. **Exclude Combinations**: The ``exclude_combinations parameter`` is used to 
specify pairs of variables that should be excluded from the scatter plot subplot grid. 

For example:

.. code-block:: text

    ("capital-gain", "hours-per-week")
    ("capital-loss", "capital-gain")
    ("education-num", "hours-per-week") 

This ensures that the generated plots are more relevant to the analysis.

2. **All Variables Combination**: Like the previous example, the ``all_vars`` parameter 
is used to automatically generate scatter plots for all combinations of numerical 
variables in the DataFrame, minus the excluded pairs.

3. **Subplot Display**: The ``show_plot`` parameter is set to ``"subplots"``, allowing for 
simultaneous visualization of multiple relationships in a cohesive layout.

By excluding specific variable combinations, this example demonstrates how to fine-tune the generated scatter plots to focus only on the most meaningful comparisons.

.. code-block:: python

    from eda_toolkit import scatter_fit_plot

    exclude_combinations = [
        ("capital-gain", "hours-per-week"),
        ("capital-loss", "capital-gain"),
        ("capital-loss", "hours-per-week"),
        ("capital-loss", "education-num"),
        ("capital-loss", "fnlwgt"),
        ("education-num", "hours-per-week"),
        ("hours-per-week", "age"),
    ]

    scatter_fit_plot(
        df=df,
        all_vars=df.select_dtypes(np.number).columns.to_list(),
        show_legend=True,
        exclude_combinations=exclude_combinations,
        show_plot="subplots",
        label_fontsize=14,
        tick_fontsize=12,
        add_best_fit_line=True,
        scatter_color="#808080",
        show_correlation=True,
    )


.. raw:: html

   <div class="no-click">

.. image:: ../assets/scatter_plots_grid_exclude.png
   :alt: Scatter Plot Comparisons (Grouped2)
   :align: center
   :width: 900px

.. raw:: html

   </div>

.. raw:: html
   
   <div style="height: 50px;"></div>


Example 2
~~~~~~~~~~~

In this example, the ``scatter_fit_plot`` function is used to generate a list of 
valid (`x`, `y`) combinations without creating any plots. This feature is particularly 
useful when identifying potential variable pairs for further analysis or programmatically 
excluding irrelevant combinations. Below are key aspects of this example:

1. **List of Combinations**: Setting the ``show_plot`` parameter to ``"combinations"`` 
returns a list of all valid combinations of numerical variables. The ``exclude_combinations`` 
parameter is used to omit specific pairs from this list.

2. **Excluded Combinations**: Certain variable pairs are excluded using the ``exclude_combinations`` parameter. For instance:

   - ``("capital-gain", "hours-per-week")``
   - ``("capital-loss", "education-num")``
   - ``("hours-per-week", "age")``

   This ensures the returned list only includes meaningful and relevant combinations.

3. **Order Irrelevance**: The order of variables in each tuple is irrelevant. For example, 
``("capital-gain", "hours-per-week")`` and ``("hours-per-week", "capital-gain")`` are 
considered the same pair, and only one is included in the output.


4. **Efficient Output**: No scatter plots are generated or displayed, making this 
approach efficient for exploratory analysis or preprocessing.

Below is an example illustrating how to retrieve a list of combinations:

.. code-block:: python

    from eda_toolkit import scatter_fit_plot

    exclude_combinations = [
        ("capital-gain", "hours-per-week"),
        ("capital-loss", "capital-gain"),
        ("capital-loss", "hours-per-week"),
        ("capital-loss", "education-num"),
        ("capital-loss", "fnlwgt"),
        ("education-num", "hours-per-week"),
        ("hours-per-week", "age"),
    ]

    combinations = scatter_fit_plot(
        df=df,
        all_vars=df.select_dtypes(np.number).columns.to_list(),
        show_legend=True,
        exclude_combinations=exclude_combinations,
        show_plot="combinations",
        label_fontsize=14,
        tick_fontsize=12,
        add_best_fit_line=True,
        scatter_color="#808080",
        show_correlation=True,
        image_path_png=image_path_png,
        image_path_svg=image_path_svg,
        save_plots="subplots",
    )

    print(combinations)

The returned list of combinations will look like this:

.. code-block:: text

    [
        ('age', 'fnlwgt'),
        ('age', 'education-num'),
        ('age', 'capital-gain'),
        ('age', 'capital-loss'),
        ('fnlwgt', 'education-num'),
        ('fnlwgt', 'capital-gain'),
        ('fnlwgt', 'hours-per-week'),
        ('education-num', 'capital-gain'),
    ]

This feature allows users to explore potential variable relationships before deciding on visualization or further analysis.


Correlation Matrices
=====================

**Generate and Save Customizable Correlation Heatmaps**

The ``flex_corr_matrix`` function is designed to create highly customizable correlation heatmaps for visualizing the relationships between variables in a DataFrame. This function allows users to generate either a full or triangular correlation matrix, with options for annotation, color mapping, and saving the plot in multiple formats.

**Customizable Plot Appearance**

The function provides extensive customization options for the heatmap's appearance:

- **Colormap Selection**: Choose from a variety of colormaps to represent the strength of correlations. The default is ``"coolwarm"``, but this can be adjusted to fit the needs of the analysis.

- **Annotation**: Optionally annotate the heatmap with correlation coefficients, making it easier to interpret the strength of relationships at a glance.

- **Figure Size and Layout**: Customize the dimensions of the heatmap to ensure it fits well within reports, presentations, or dashboards.

**Triangular vs. Full Correlation Matrix**


A key feature of the ``flex_corr_matrix`` function is the ability to generate either a full correlation matrix or only the upper triangle. This option is particularly useful when the matrix is large, as it reduces visual clutter and focuses attention on the unique correlations.

**Label and Axis Configuration**


The function offers flexibility in configuring axis labels and titles:

- **Label Rotation**: Rotate x-axis and y-axis labels for better readability, especially when working with long variable names.
- **Font Sizes**: Adjust the font sizes of labels and tick marks to ensure the plot is clear and readable.
- **Title Wrapping**: Control the wrapping of long titles to fit within the plot without overlapping other elements.

**Plot Display and Saving Options**


The ``flex_corr_matrix`` function allows you to display the heatmap directly or save it as PNG or SVG files for use in reports or presentations. If saving is enabled, you can specify file paths and names for the images.

.. function:: flex_corr_matrix(df, cols=None, annot=True, cmap="coolwarm", save_plots=False, image_path_png=None, image_path_svg=None, image_filename=None, figsize=(10, 10), title=None, label_fontsize=12, tick_fontsize=10, xlabel_rot=45, ylabel_rot=0, xlabel_alignment="right", ylabel_alignment="center_baseline", text_wrap=50, vmin=-1, vmax=1, cbar_label="Correlation Index", triangular=True, label_names=None, cbar_padding=0.8, cbar_width_ratio=0.05, show_colorbar=True, corr_method="pearson", show_significance=False, significance_level=0.05, significance_method="stars", significance_legend_x=0.5, filter_significance=None, **kwargs)

   Creates a correlation heatmap with extensive customization options,
   including triangular masking, alignment adjustments, title wrapping,
   dynamic colorbar scaling, and optional significance overlays.

   :param df: The DataFrame containing the data.
   :type df: pandas.DataFrame

   :param cols: List of column names to include in the correlation matrix.
      If ``None``, all columns are included.
   :type cols: list of str, optional

   :param annot: Whether to annotate the heatmap with correlation
      coefficients. Default is ``True``.
   :type annot: bool, optional

   :param cmap: The colormap to use for the heatmap. Default is
      ``"coolwarm"``.
   :type cmap: str, optional

   :param save_plots: Whether to save the heatmap using the title as the
      filename. For explicit filename control use ``image_filename``
      instead. Default is ``False``.
   :type save_plots: bool, optional

   :param image_path_png: Directory path to save the heatmap as a PNG
      image.
   :type image_path_png: str, optional

   :param image_path_svg: Directory path to save the heatmap as an SVG
      image.
   :type image_path_svg: str, optional

   :param image_filename: Base filename (without extension) for saving
      the figure. When provided, takes precedence over the
      ``save_plots``-derived filename. Requires at least one of
      ``image_path_png`` or ``image_path_svg`` to be set.
   :type image_filename: str, optional

   :param figsize: Width and height of the heatmap figure.
      Default is ``(10, 10)``.
   :type figsize: tuple of int, optional

   :param title: Title of the heatmap. Default is ``None``.
   :type title: str, optional

   :param label_fontsize: Font size for axis labels and title.
      Default is ``12``.
   :type label_fontsize: int, optional

   :param tick_fontsize: Font size for tick labels and colorbar labels.
      Default is ``10``.
   :type tick_fontsize: int, optional

   :param xlabel_rot: Rotation angle for x-axis labels. Default is ``45``.
   :type xlabel_rot: int, optional

   :param ylabel_rot: Rotation angle for y-axis labels. Default is ``0``.
   :type ylabel_rot: int, optional

   :param xlabel_alignment: Horizontal alignment for x-axis labels
      (e.g. ``"center"``, ``"right"``). Default is ``"right"``.
   :type xlabel_alignment: str, optional

   :param ylabel_alignment: Vertical alignment for y-axis labels
      (e.g. ``"center"``, ``"top"``). Default is ``"center_baseline"``.
   :type ylabel_alignment: str, optional

   :param text_wrap: Maximum character width of the title and axis labels
      before wrapping. Default is ``50``.
   :type text_wrap: int, optional

   :param vmin: Minimum value for the heatmap color scale. Default is
      ``-1``.
   :type vmin: float, optional

   :param vmax: Maximum value for the heatmap color scale. Default is
      ``1``.
   :type vmax: float, optional

   :param cbar_label: Label for the colorbar. Default is
      ``"Correlation Index"``.
   :type cbar_label: str, optional

   :param triangular: Whether to show only the upper triangle of the
      correlation matrix, excluding the diagonal. Default is ``True``.
   :type triangular: bool, optional

   :param label_names: A dictionary mapping original column names to
      custom display labels.
   :type label_names: dict, optional

   :param cbar_padding: Padding between the heatmap and the colorbar.
      Default is ``0.8``.
   :type cbar_padding: float, optional

   :param cbar_width_ratio: Relative width of the colorbar compared to
      the heatmap. Default is ``0.05``.
   :type cbar_width_ratio: float, optional

   :param show_colorbar: Whether to display the colorbar. Default is
      ``True``.
   :type show_colorbar: bool, optional

   :param corr_method: Method for computing the correlation matrix.
      Options are ``"pearson"``, ``"spearman"``, or ``"kendall"``. The
      corresponding scipy pairwise function is used when computing
      p-values for significance testing. Default is ``"pearson"``.
   :type corr_method: str, optional

   :param show_significance: If ``True``, overlays significance
      information on heatmap cells based on pairwise p-values computed
      using ``corr_method``. Default is ``False``.
   :type show_significance: bool, optional

   :param significance_level: The p-value threshold below which a
      correlation is considered statistically significant. Used in both
      ``"stars"`` and ``"mask"`` modes. Default is ``0.05``.
   :type significance_level: float, optional

   :param significance_method: How to display significance on the
      heatmap. Options are:

      - ``"stars"``: appends significance stars to each cell annotation
        (:math:`* \; p < 0.05`, :math:`** \; p < 0.01`,
        :math:`*** \; p < 0.001`).
      - ``"mask"``: blanks out cells where the correlation is not
        significant (:math:`p \geq` ``significance_level``).

      Default is ``"stars"``.
   :type significance_method: str, optional

   :param significance_legend_x: Horizontal position of the significance
      legend in figure coordinates when ``show_significance=True`` and
      ``significance_method="stars"``. ``0.0`` is the left edge, ``1.0``
      is the right edge, and ``0.5`` centers the legend. The vertical
      position is computed automatically. Default is ``0.5``.
   :type significance_legend_x: float, optional

   :param filter_significance: If provided, filters the correlation
      matrix to only include variables that have at least one significant
      pairwise correlation at the specified threshold. For example,
      ``filter_significance=0.05`` drops any variable with no p-value
      below ``0.05``. Automatically enables ``show_significance``.
      Default is ``None``.
   :type filter_significance: float or None, optional

   :param kwargs: Additional keyword arguments passed to
      ``sns.heatmap()``.

   :returns: ``None``
   :rtype: None

   :raises ValueError: If ``annot``, ``save_plots``, or ``triangular``
      is not a boolean value.
   :raises ValueError: If ``cols`` is not a list of column names.
   :raises ValueError: If ``save_plots`` is ``True`` but neither
      ``image_path_png`` nor ``image_path_svg`` is specified.
   :raises ValueError: If ``image_filename`` is provided but neither
      ``image_path_png`` nor ``image_path_svg`` is specified.
   :raises ValueError: If ``corr_method`` is not one of ``"pearson"``,
      ``"spearman"``, or ``"kendall"``.
   :raises ValueError: If ``significance_method`` is not one of
      ``"stars"`` or ``"mask"``.
   :raises ValueError: If ``filter_significance`` is not ``None`` and
      is not a positive float.

   .. note::

      - When ``show_significance=True``, the diagonal always displays
        ``"1.00"`` to reflect perfect self-correlation regardless of
        significance method.
      - ``filter_significance`` auto-enables ``show_significance`` so
        the overlay is always visible alongside the filtered matrix.
      - Near-zero correlation values (:math:`|r| < 0.005`) are zeroed
        before plotting to eliminate the ``-0.00`` display artifact.
      - ``image_filename`` takes precedence over ``save_plots`` when
        both are provided.


Triangular Correlation Matrix Example
--------------------------------------

The provided code filters the census [1]_ DataFrame ``df`` to include only numeric columns using 
``select_dtypes(np.number)``. It then utilizes the ``flex_corr_matrix()`` function 
to generate a right triangular correlation matrix, which only displays the 
upper half of the correlation matrix. The heatmap is customized with specific 
colormap settings, title, label sizes, axis label rotations, and other formatting 
options. 

.. note:: 
    
    This triangular matrix format is particularly useful for avoiding 
    redundancy in correlation matrices, as it excludes the lower half, 
    making it easier to focus on unique pairwise correlations. 
    
    The function also includes a labeled color bar, helping users quickly interpret 
    the strength and direction of the correlations.

.. code-block:: python

    # Select only numeric data to pass into the function
    df_num = df.select_dtypes(np.number)

.. code-block:: python

    from eda_toolkit import flex_corr_matrix

    flex_corr_matrix(
        df=df,
        cols=df_num.columns.to_list(),
        annot=True,
        cmap="coolwarm",
        figsize=(10, 8),
        title="US Census Correlation Matrix",
        xlabel_alignment="right",
        label_fontsize=14,
        tick_fontsize=12,
        xlabel_rot=45,
        ylabel_rot=0,
        text_wrap=50,
        vmin=-1,
        vmax=1,
        cbar_label="Correlation Index",
        triangular=True,
    )


.. raw:: html

   <div class="no-click">

.. image:: ../assets/correlation_matrix.svg
   :alt: Correlation Matrix - Triangular
   :align: center
   :width: 900px

.. raw:: html

   </div>

.. raw:: html
   
   <div style="height: 50px;"></div>


Correlation Matrix with Significance Overlay
---------------------------------------------

Building on the triangular correlation matrix above, the following example
extends the visualization by overlaying statistical significance information
directly on each cell. The ``show_significance=True`` parameter activates
pairwise p-value computation using the method specified by ``corr_method``
(Pearson by default). Cells are annotated with significance stars following
the convention :math:`* \; p < 0.05`, :math:`** \; p < 0.01`,
:math:`*** \; p < 0.001`, allowing the reader to distinguish statistically
meaningful correlations at a glance. The ``filter_significance`` parameter
can optionally restrict the matrix to only those variables that share at
least one significant pairwise correlation at the specified threshold,
reducing visual clutter in wide feature sets.

.. code-block:: python

    from eda_toolkit import flex_corr_matrix

    flex_corr_matrix(
        df=df,
        cols=df_num.columns.to_list(),
        annot=True,
        cmap="coolwarm",
        figsize=(10, 8),
        title="US Census Correlation Matrix with Significance",
        xlabel_alignment="right",
        label_fontsize=14,
        tick_fontsize=12,
        xlabel_rot=45,
        ylabel_rot=0,
        text_wrap=50,
        vmin=-1,
        vmax=1,
        cbar_label="Correlation Index",
        triangular=True,
        corr_method="pearson",
        show_significance=True,
        significance_method="stars",
        significance_level=0.05,
    )

.. raw:: html

   <div class="no-click">

.. image:: ../assets/corr_matrix_statistical_significance.svg
   :alt: Correlation Matrix with Significance Overlay
   :align: center
   :width: 900px

.. raw:: html

   </div>

.. raw:: html
   
   <div style="height: 50px;"></div>




Full Correlation Matrix Example
----------------------------------

In this modified census [1]_ example, the key changes are the use of the viridis 
colormap and the decision to plot the full correlation matrix instead of just the 
upper triangle. By setting ``cmap="viridis"``, the heatmap will use a different 
color scheme, which can provide better visual contrast or align with specific 
aesthetic preferences. Additionally, by setting ``triangular=False``, the full 
correlation matrix is displayed, allowing users to view all pairwise correlations, 
including both upper and lower halves of the matrix. This approach is beneficial 
when you want a comprehensive view of all correlations in the dataset.

.. code-block:: python

    from eda_toolkit import flex_corr_matrix

    flex_corr_matrix(
        df=df,
        cols=df_num.columns.to_list(),
        annot=True,
        cmap="viridis",
        figsize=(10, 8),
        title="US Census Correlation Matrix",
        xlabel_alignment="right",
        label_fontsize=14,
        tick_fontsize=12,
        xlabel_rot=45,
        ylabel_rot=0,
        text_wrap=50,
        vmin=-1,
        vmax=1,
        cbar_label="Correlation Index",
        triangular=False,
    )

.. raw:: html

   <div class="no-click">

.. image:: ../assets/correlation_matrix_full.svg
   :alt: Correlation Matrix - Full
   :align: center
   :width: 900px

.. raw:: html

   </div>

.. raw:: html
   
   <div style="height: 50px;"></div>





.. [1] Kohavi, R. (1996). *Census Income*. UCI Machine Learning Repository. `https://doi.org/10.24432/C5GP7S <https://doi.org/10.24432/C5GP7S>`_.
