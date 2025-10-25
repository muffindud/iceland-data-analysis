# Exploratory Data Analysis

## Assignment 1: European Development Indicators

### Overview:

This assignment focuses on developing your skills in Exploratory Data Analysis (EDA). You will be working with economic and social indicators to investigate trends within a European country of your choice. The goal is not prediction, but understanding – identifying patterns, anomalies and potential relationships between various indicators. The assignment requires you to formulate research questions, clean and prepare data, perform insightful EDA, and communicate your findings effectively in a written report accompanied by reproducible code.

### Learning Objectives:

Upon completion of this task, students will be able to:

* Formulate relevant research questions based on real-world data.

* Clean, transform, and manipulate large datasets using appropriate tools (R/Python).

* Apply a variety of EDA techniques to uncover patterns and insights in complex data.

* Visualize data effectively to communicate findings clearly and concisely.

* Document code thoroughly for reproducibility and collaboration.

* Write a comprehensive report summarizing the analysis, including limitations and potential future work.

### Data Sources:

For this assignment, we will prioritize data from reputable European sources. Each student must choose a unique European country for their analysis. Only one student per country is allowed. Recommended datasets include:

* IMF Data: The International Monetary Fund provides comprehensive economic data, including GDP, inflation, trade balances, and more. Data is available for download in various formats or through their API.

* Eurostat: The statistical office of the European Union offers a vast range of socio-economic indicators, including population demographics, employment rates, education levels, health statistics, and environmental data. Data is available for download or through their API. Highly recommended as a primary source.

* World Bank DataBank: While we prioritize IMF & Eurostat, the World Bank can be used to supplement data if necessary, particularly for historical comparisons or indicators not readily available from European sources.

* API Access: Students may use APIs (IMF and Eurostat both offer them) to simplify updates and avoid manual data downloads. Refer to their respective documentation for API access details.

### Assignment Tasks:

This assignment is divided into several tasks, each requiring specific deliverables:

#### Phase 1: Country Selection & Data Acquisition (10% of Grade)

* Country Selection: Choose a European country to focus on for your analysis.

* Research Questions: Formulate at least three (3) specific, answerable research questions about the chosen country using available indicators. These should go beyond simple descriptive statistics and aim to explore relationships between variables. Examples: "How has household disposable income correlated with consumer price inflation in Iceland over the past 10 years?", "What is the relationship between unemployment rates and educational attainment levels in Iceland?".

* Indicator Selection: Identify 10 – 20 relevant indicators from the data sources which will help you answer your research questions.

    * Sources: Prioritize data from IMF & Eurostat. Justify your indicator choices.

    * Identifier: Include the identifier/code for each indicator (e.g., Eurostat code: prc_abc_pc - Purchasing power parities, price level).

    * Data Frequency: In the next assignment, you will be working with quarterly and monthly indicators, so the data that you select here should match this requirement. Aim to have at least half of your dataset at monthly frequency.

    * Series Length: Aim to have at least 20 years of data for your analysis, but you should retain the longest possible series for your country, depending on data availability.

    * Key Indicators: As you will need data for GDP (quarterly frequency) and Inflation (monthly frequency) for Assignment 2, make sure to collect this data from the beginning. Aim to have at least

* Overview: Write a short overview (1-2 pages) outlining:

    * Chosen European Country

    * Research Questions

    * Selected Indicators & Justification

    * Planned Approach to Data Acquisition (API or Download – specify source)

#### Phase 2: Data Cleaning and Preparation (20% of Grade)

* Data Acquisition: Obtain the data for your chosen country and selected indicators using either the API or a downloaded dataset.

* Data Cleaning: Address common data quality issues:

    * Missing Values: Handle missing values appropriately (imputation, removal, etc.). Justify your approach.

    * Outliers: Identify and address outliers if necessary. Explain your outlier handling strategy.

    * Data Types: Ensure correct data types for each variable.

    * Data Consistency: Check for inconsistencies in the data (e.g., negative population values).

* Data Transformation: Perform any necessary transformations:

    * Aggregation: Aggregate data to appropriate time intervals (e.g., annual, quarterly) for your analysis.

    * Normalization/Standardization: Consider normalizing or standardizing variables if needed for comparison.

    * Feature Engineering: Create new features from existing ones that might be relevant to your research questions.

* Code Documentation: Thoroughly document all data cleaning and preparation steps in your code with clear comments.

#### Phase 3: Exploratory Data Analysis (EDA) & Visualization (40% of Grade)

* Univariate Analysis: Explore the distribution of each selected indicator individually using appropriate descriptive statistics and visualizations (histograms, box plots, density plots).

* Bivariate Analysis: Investigate relationships between pairs of indicators using:

    * Scatter Plots: Visualize correlations.

    * Correlation: Calculate and visualize correlation between variables.

    * Time Series Plots: Analyze trends over time for individual indicators and combinations.

* Multivariate Analysis (Optional): If appropriate, explore relationships between multiple indicators using techniques like:

    * Pair Plots: Visualize pairwise relationships among several variables.

    * Heatmaps: Display correlation matrices or other multivariate data.

* Visualization Best Practices: Create clear, informative, and visually appealing visualizations with appropriate labels, titles, and legends. Use color effectively to

* Interpretation: Provide insightful interpretations of your EDA results. What patterns, trends, anomalies, or relationships did you discover?

#### Phase 4: Deliverables (30% of Grade)

* Report (5 – 10 pages): A comprehensive report that includes:

    * Introduction: Briefly introduce the chosen country and your research questions.

    * Data & Methods: Describe the data source, selected indicators, data cleaning/preparation steps, and EDA techniques used.

    * Results: Present your key findings from the EDA with supporting visualizations. Clearly answer your research questions based on the evidence.

    * Discussion: Discuss the implications of your findings. What are the limitations of your analysis? What further research could be conducted?

    * Conclusion: Summarize your main conclusions and insights.

* Reproducible Code: Submit all code used for data acquisition, cleaning, preparation, EDA, and visualization in a well-organized manner (e.g., R scripts or Jupyter Notebooks). Code should be:

    * Well-Commented: Explain each step clearly.

    * Modular: Break down the analysis into logical functions or sections.

    * Reproducible: Anyone should be able to run your code and obtain the same results in an online or offline environment.

* Data: All the input data that was used (including the series identifiers).

### Submission Requirements:

* Submit a single zip file containing:

    * Your Final Report (PDF format)

    * All Code Files (Jupyter Notebooks, R scripts, etc.)

    * Data Files (if API was used, upload a .csv table containing the final / merged dataset that you used in the analysis)

    * A README file explaining how to run your code and any specific dependencies.

### Important Notes:

* Focus on quality over quantity. A well-executed analysis of a few key indicators is better than a superficial analysis of many.

* Pay attention to detail in your report and code documentation.

* Submitting code that does not run from beginning to end will yield a failed grade.
