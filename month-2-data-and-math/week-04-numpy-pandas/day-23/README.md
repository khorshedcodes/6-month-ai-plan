# Day 23: Tabular Data with Pandas (Series, DataFrames, Inspection & Indexing)

## Learning Objectives
1. The difference between a Pandas `Series` (1D labeled column) and a `DataFrame` (2D labeled table).
2. Loading real datasets with `pd.read_csv()`.
3. High-level dataset inspection: `.head()`, `.tail()`, `.shape`, `.info()`, `.describe()`.
4. Indexing & Slicing: `loc` (label-based) vs. `iloc` (integer-position based).
5. Boolean Indexing: filtering rows based on conditions (e.g. `df[df["salary"] > 50000]`).

---

## Daily Task: Employee Dataset Inspector
1. Load `employees.csv`.
2. Inspect dataset structure with `.info()` and summary statistics with `.describe()`.
3. Filter rows using `loc` and boolean conditions.
4. Extract specific slices using integer index positions with `iloc`.
