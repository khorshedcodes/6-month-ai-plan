# 6-Month AI Engineering & Developer English Syllabus

> **Core Principle:** Never accept code from AI that you cannot explain. Measure progress by what you can understand, debug, modify, and rebuild without AI—and how clearly you can communicate it in English.

---

## 1. How Every Day Works (Daily 2-Hour Routine)

Every study day follows the **5-Step Learning Method + Developer English**:

| Step | Time | Activity | AI Allowed? |
| :--- | :--- | :--- | :--- |
| **1. Learn** | 25 min | I teach you the day's concept (comparing to JS/React where helpful) and show small examples. | Yes (as teacher) |
| **2. Implement** | 40 min | You write the daily coding exercise in your workspace **on your own**. | **No** |
| **3. Review & Debug** | 20 min | I review your code, point out edge cases, or give hints if you are stuck. | Yes (hints/review) |
| **4. Rebuild / Quiz** | 15 min | You answer 2–3 quick conceptual questions or rewrite a key snippet from memory. | **No** |
| **5. Explain (Dev English)** | 20 min | You write or speak (in text) a short technical explanation, PR description, or standup update in clear professional English. I correct your grammar, vocabulary, and tone. | Yes (feedback) |

---

## 2. How Developer English is Integrated

To get and succeed in a developer job, you don't need poetic English—you need **clear, professional Engineering English**. We will practice 5 real-world workplace formats every week:

1. **Daily "Explain It" Log (Every Day):** Write 3–5 sentences explaining *what* you built, *why* you chose that approach, and *what* could go wrong.
2. **Daily Standup Update (2x/week):** Format: *Yesterday I worked on... Today I am working on... I am blocked by...*
3. **Code Review & PR Descriptions (1x/week):** Writing professional commit messages and Pull Request summaries (`What changed`, `Why`, `How to test`).
4. **Bug Report / Asking for Help (1x/week):** Explaining a bug clearly (*Expected behavior*, *Actual behavior*, *What I tried so far*).
5. **Weekly Mock Interview Question (Day 7 of each week):** Answering 1 behavioral or technical interview question in English during your Weekly Test.

---

## 3. Workspace & Project Folder Structure

We will organize `f:\6 month plan\` cleanly like a real engineering repository:

```text
f:\6 month plan\
├── whatIwant.md                  # Your core philosophy & motivation
├── SYLLABUS.md                   # This complete syllabus & tracker
├── PROGRESS.md                   # Daily progress tracker & English vocabulary log
│
├── month-1-python\               # Weeks 1–3: Python Foundations & OOP/APIs
│   ├── week-01-basics\
│   │   ├── day-01\               # code.py + notes.md (your English explanation)
│   │   ├── day-02\
│   │   ├── ...
│   │   └── day-07-expense-tracker\  # Mini-Project 1 (No AI)
│   ├── week-02-oop-and-files\
│   └── week-03-apis-and-cli\
│
├── month-2-data-and-math\        # Weeks 4–5: NumPy, Pandas, Matplotlib, Math
│   ├── week-04-numpy-pandas\
│   └── week-05-math-and-eda\
│
├── month-3-machine-learning\     # Weeks 6–9: Classical ML & Scikit-Learn
│   └── ...
│
├── month-4-deep-learning\        # Weeks 10–11: Neural Networks & PyTorch
│   └── ...
│
├── month-5-llms-and-rag\         # Weeks 12–16: LLMs, Prompting, Embeddings, RAG
│   └── ...
│
├── month-6-production-ai\        # Weeks 17–24: FastAPI, Postgres/pgvector, Docker, Eval
│   └── ...
│
└── projects\                     # Your 3 Portfolio-Grade Capstone Projects
    ├── 01-spam-classifier\
    ├── 02-document-intelligence\
    └── 03-ai-support-ticket-system\
```

---

## 4. Detailed Day-by-Day Syllabus: Phase 1 (Weeks 1–5)

### Week 1: Python Core Foundations
* **Goal:** Write basic Python scripts from scratch without looking up syntax.
* **English Focus:** Explaining basic logic and writing daily standup updates.

| Day | Coding Topics | Hands-On Task (No AI) | Daily Test / Check | Dev English Task |
| :--- | :--- | :--- | :--- | :--- |
| **Day 1** | Python setup, REPL, variables, `int`, `float`, `str`, `bool`, `type()`, `input()`, `print()`, f-strings | Build a CLI Unit & Currency Converter that handles user input cleanly | Predict output of 5 tricky type-conversion expressions | Write 4 sentences comparing Python variables to JavaScript `let`/`const` |
| **Day 2** | `if`/`elif`/`else`, truthy/falsy values, `and`/`or`/`not`, `for` (`range`, `enumerate`), `while`, `break`/`continue` | Build a Number Guessing Game with attempt limits and hints | Trace a nested loop on paper and state exact outputs | Write a Standup Update: what you built on Day 1 & plan for Day 2 |
| **Day 3** | Functions (`def`), positional vs keyword args, default values, `return`, variable scope, docstrings | Build a Password Strength Validator using modular helper functions | Spot the bug in 3 functions with mutable default arguments or missing returns | Write Google-style docstrings in English for each function you wrote |
| **Day 4** | `list`, `tuple`, `dict`, `set` — indexing, slicing, mutability, `.get()`, `.items()`, when to use which | Build an In-Memory Contact Book (CRUD: add, search, update, delete) | Explain time/memory difference between searching a `list` vs a `set` | Explain in plain English: "Why I chose a `dict` instead of a `list` for contacts" |
| **Day 5** | String methods, list/dict comprehensions, reading/writing `.txt` and `.csv` files (`with open(...)`) | Build a Log File Analyzer that counts `[ERROR]` and `[WARN]` lines and saves a summary | Rewrite 3 `for` loops into clean list comprehensions from memory | Write a short Bug Report describing what happens if a file path doesn't exist |
| **Day 6** | `try`/`except`/`else`/`finally`, raising custom errors, modules (`import`), `venv`, `pip`, `requirements.txt` | Refactor Day 5 analyzer into multiple modules inside a virtual environment with error handling | Unplug internet/break input and prove your script fails gracefully | Write a `README.md` explaining how another developer can set up your `venv` |
| **Day 7** | **WEEK 1 TEST & MINI-PROJECT** | **Build a CLI Expense Tracker (Add, List, Filter by Category, Save/Load File) — 100% Closed-Book** | **Closed-book quiz (10 questions) + Live Code Review of your tracker** | **Mock Interview Q1:** *"Walk me through how your Expense Tracker works from user input to file storage."* |

---

### Week 2: Intermediate Python, OOP & JSON
* **Goal:** Structure larger Python programs using classes, JSON, and automated tests.
* **English Focus:** Writing Pull Request (PR) descriptions and explaining architecture.

| Day | Coding Topics | Hands-On Task (No AI) | Daily Test / Check | Dev English Task |
| :--- | :--- | :--- | :--- | :--- |
| **Day 8** | Classes, `__init__`, `self`, instance vs class attributes, methods, `__str__` / `__repr__` | Convert Expense Tracker items into `Expense` and `ExpenseManager` classes | Explain what `self` is to a JS developer used to `this` | Write a PR description: *"Refactor procedural expense tracker to OOP"* |
| **Day 9** | Inheritance, composition, `@dataclass`, type hints (`list[str]`, `Optional`, `Union`) | Build a Task Management model (`Task`, `BugTask`, `FeatureTask`) with type hints | Add strict type hints to a messy untyped script | Explain in English: *"When to use `@dataclass` vs a regular class"* |
| **Day 10** | Working with `json` module (`loads`, `dumps`, `load`, `dump`), `pathlib`, `datetime` | Add JSON persistence & date filtering to your Task Manager | Handle corrupted JSON file without crashing | Standup Update + explain how serialization works |
| **Day 11** | Iterators, generators (`yield`), `lambda`, `map`, `filter`, `sorted` with custom `key=` | Write a memory-efficient large-file reader using `yield` and custom sorting | Explain why `yield` saves memory compared to returning a list | Explain a performance trade-off in professional English |
| **Day 12** | Writing unit tests with `pytest` (`assert`, `pytest.raises`, fixtures) | Write 8 unit tests for your Week 1/2 code (happy path + edge cases) | Break your code intentionally and verify `pytest` catches it | Write test case descriptions that read like clear English specifications |
| **Day 13** | HTTP requests (`requests` / `httpx`), status codes, query params, headers, `.env` variables | Build a CLI Weather or GitHub Profile fetcher using a public API | Handle rate limits (429), 404s, and timeouts cleanly | Write API documentation for your CLI tool |
| **Day 14** | **WEEK 2 TEST & MINI-PROJECT** | **Build a CLI GitHub Issue / Habit Tracker with JSON/API + `pytest` tests — Closed-Book** | **Closed-book test + code defense** | **Mock Interview Q2:** *"Tell me about a bug you encountered this week and how you debugged it."* |

---

### Week 3: Advanced Python & CLI Engineering
* **Goal:** Write clean, idiomatic, production-style Python without AI assistance.
* **English Focus:** Code review comments and technical trade-off discussions.

| Day | Coding Topics | Hands-On Task (No AI) | Daily Test / Check | Dev English Task |
| :--- | :--- | :--- | :--- | :--- |
| **Day 15** | Decorators, closures, context managers (`__enter__`, `__exit__`) | Write a `@timer` and `@retry` decorator from scratch | Trace execution order of a decorated function | Explain closures and decorators in simple English |
| **Day 16** | Async Python basics (`async`, `await`, `asyncio.gather`) vs synchronous execution | Fetch 5 API endpoints concurrently and compare speed with sync | Explain the event loop (compare to JS Promises/`async-await`) | Write a short technical note comparing JS async vs Python `asyncio` |
| **Day 17** | CLI arguments (`argparse`), logging (`logging` module vs `print`) | Upgrade your API tool with CLI flags (`--user`, `--limit`) and structured logging | Replace all `print()` statements with appropriate log levels | Explain why production systems use `logging` instead of `print` |
| **Day 18** | Packaging, project layout (`src/`), linting (`ruff`), formatting | Structure a multi-file Python package with clean imports | Fix circular import & path issues manually | Write a clear `CONTRIBUTING.md` style guide |
| **Day 19** | Data structures & algorithms refresher in Python (hash maps, two pointers, frequency counting) | Solve 3 practical data-processing problems without external libraries | Analyze Big-O time & space complexity of your solutions | Verbally (in text) walk through your algorithm step-by-step |
| **Day 20** | Review & integration day: combining CLI + API + JSON + Logging + Tests | Build Part 1 of a CLI News/Article Aggregator | Self-review checklist before submitting code | Write a full Pull Request summary for your aggregator |
| **Day 21** | **WEEK 3 TEST (END OF PYTHON MODULE)** | **Complete & defend the CLI Aggregator under timed closed-book conditions** | **Month 1 Python Mastery Exam** | **Mock Interview Q3:** *"How do you ensure your Python code is maintainable and reliable?"* |

---

### Week 4: Data Manipulation (NumPy & Pandas)
* **Goal:** Manipulate matrices and tabular datasets effortlessly.
* **English Focus:** Describing data trends, anomalies, and data cleaning decisions.

| Day | Coding Topics | Hands-On Task (No AI) | Daily Test / Check | Dev English Task |
| :--- | :--- | :--- | :--- | :--- |
| **Day 22** | NumPy arrays, shapes, `dtype`, indexing, slicing, broadcasting, vectorization | Implement matrix operations & prove vectorized NumPy is faster than Python loops | Predict array shapes after broadcasting | Explain "vectorization" without using jargon |
| **Day 23** | Pandas `Series` & `DataFrame`, reading CSVs, `.head()`, `.info()`, `.describe()`, `loc` vs `iloc` | Load a real dirty CSV dataset and inspect its structure | Quiz on `loc` vs `iloc` and boolean indexing | Write an Initial Data Inspection Report in English |
| **Day 24** | Cleaning data: missing values (`isna`, `fillna`, `dropna`), duplicates, type conversion, string cleaning | Clean a messy dataset with missing prices, bad dates, and duplicate rows | Justify why you dropped vs imputed specific columns | Explain your data-cleaning trade-offs to a "Product Manager" |
| **Day 25** | Filtering, sorting, `groupby`, aggregations (`.agg()`), merging/joining DataFrames | Answer 6 business questions from an e-commerce dataset using `groupby` & `merge` | Write complex `groupby` queries from memory | Write an Executive Summary of the 6 business answers |
| **Day 26** | Matplotlib & Seaborn basics: histograms, scatter plots, bar charts, line plots | Create 4 charts showing distributions and relationships in your dataset | Identify which chart type fits which data question | Write clear chart titles, captions, and insights in English |
| **Day 27** | Exploratory Data Analysis (EDA) end-to-end on a fresh dataset | Perform full EDA on a housing or customer churn dataset | Defend your findings against my follow-up questions | Present 3 key takeaways from your data |
| **Day 28** | **WEEK 4 TEST** | **Timed EDA Challenge on an unseen CSV dataset (No AI)** | **Closed-book Pandas/NumPy test** | **Mock Interview Q4:** *"How do you handle missing or corrupted data in a dataset?"* |

---

### Week 5: Math for Machine Learning
* **Goal:** Understand the math *behind* ML so models aren't magic black boxes.
* **English Focus:** Explaining mathematical concepts using intuitive real-world analogies.

| Day | Coding Topics | Hands-On Task (No AI) | Daily Test / Check | Dev English Task |
| :--- | :--- | :--- | :--- | :--- |
| **Day 29** | Mean, median, mode, variance, standard deviation, outliers, distributions | Calculate stats from scratch in pure Python, then verify with NumPy | Explain when mean lies and median tells the truth | Explain standard deviation to a non-technical teammate |
| **Day 30** | Probability basics, conditional probability, Bayes' theorem intuition (critical for Spam Classifier!) | Compute spam word probabilities by hand and in Python | Solve 2 Bayes' theorem word problems | Explain how Bayes' theorem relates to spam filtering |
| **Day 31** | Vectors, dot product, cosine similarity (the foundation of embeddings & RAG!) | Write `dot_product()` and `cosine_similarity()` in pure Python & NumPy | Compute similarity between 3 simple word-count vectors | Explain why cosine similarity measures angle instead of length |
| **Day 32** | Matrices, matrix multiplication (`@`), linear transformations | Implement matrix-vector multiplication and connect it to weights × inputs | Predict output dimensions of matrix multiplications | Explain how a matrix represents a dataset of features |
| **Day 33** | Derivatives, slopes, gradients, and Gradient Descent intuition | Implement 1D Gradient Descent in Python to find the minimum of $f(x) = (x - 3)^2$ | Explain what happens if the learning rate is too big or too small | Explain Gradient Descent using the "walking down a foggy mountain" analogy |
| **Day 34** | Implementing Linear Regression from scratch using NumPy & Gradient Descent | Fit a line $y = wx + b$ to synthetic data without Scikit-Learn | Plot the loss curve decreasing over epochs | Write a technical post explaining your from-scratch Linear Regression |
| **Day 35** | **WEEK 5 TEST** | **Closed-book math & NumPy implementation test** | **Verify you can derive & code cosine similarity + gradient step** | **Mock Interview Q5:** *"What is gradient descent, and what does the learning rate control?"* |

---

## 5. Weeks 6–24 Roadmap & Capstone Projects

### Phase 2: Machine Learning Fundamentals (Weeks 6–9)
* **Week 6:** Supervised vs Unsupervised, Train/Test Split, Linear & Logistic Regression with Scikit-Learn.
* **Week 7:** Decision Trees, Random Forests, Naive Bayes, Text Feature Extraction (Bag of Words, TF-IDF).
* **Week 8:** Overfitting vs Underfitting, Cross-Validation, Confusion Matrix, Precision, Recall, F1-Score, ROC-AUC.
* **Week 9:** **CAPSTONE PROJECT 1 — Spam Classifier** (End-to-end dataset prep, feature extraction, model comparison, error analysis, CLI/API interface).
  * *English Milestone:* Write a complete Model Evaluation Report explaining false positives vs false negatives.

### Phase 3: Deep Learning Introduction (Weeks 10–11)
* **Week 10:** Neurons, Layers, Activation Functions (ReLU, Sigmoid, Softmax), Loss Functions (MSE, Cross-Entropy), Forward & Backward Propagation.
* **Week 11:** PyTorch Tensors, Autograd, `nn.Module`, Training Loops (`zero_grad`, `backward`, `step`), building & training a neural network classifier.
  * *English Milestone:* Explain every line of the standard 5-line PyTorch training step in an interview setting.

### Phase 4: LLMs & AI Application Development (Weeks 12–16)
* **Week 12:** How LLMs work conceptually (Tokens, Embeddings, Attention, Transformers, Context Windows, Temperature).
* **Week 13:** LLM APIs, System Prompts, Few-Shot Prompting, Structured Outputs (JSON Schema / Pydantic), Function/Tool Calling.
* **Week 14:** Text Extraction (PDF/Markdown), Chunking Strategies (fixed, recursive, semantic), Vector Embeddings & Vector Databases.
* **Week 15:** Retrieval-Augmented Generation (RAG) Pipeline: Querying, Top-K Retrieval, Reranking, Context Injection, Citation Grounding.
* **Week 16:** **CAPSTONE PROJECT 2 — Document Intelligence System** (Upload PDFs, chunk, embed, retrieve, answer with citations + RAG evaluation dataset to test hallucinations).
  * *English Milestone:* Record/write an Architecture Walkthrough of your RAG pipeline.

### Phase 5: Production AI Engineering (Weeks 17–24)
* **Week 17:** FastAPI fundamentals: routing, Pydantic validation, dependency injection, async endpoints, error handling.
* **Week 18:** PostgreSQL + SQLAlchemy + `pgvector` (combining relational data with vector search in one database).
* **Week 19:** Background jobs (queues, retries, rate-limit handling, timeouts) & cost/latency tracking.
* **Week 20:** AI Evaluation Pipelines (golden datasets, LLM-as-a-judge, deterministic assertions, regression testing prompts).
* **Week 21:** Docker (`Dockerfile`, `docker-compose` with FastAPI + Postgres), environment security, structured logging & monitoring.
* **Weeks 22–24:** **CAPSTONE PROJECT 3 — Production AI Support Ticket System**
  * **Weeks 22:** Database schema, FastAPI backend, LLM structured classification (category, urgency, sentiment) + confidence scores.
  * **Week 23:** RAG-based suggested replies from help-center docs, background worker, evaluation suite.
  * **Week 24:** Dockerization, deployment, README documentation, and **Final 6-Month Mock Technical Interview**.

---

## 6. How We Structure the 3 Capstone Projects

Every capstone project in `projects/` will follow a professional production structure (not messy single scripts):

```text
projects/01-spam-classifier/
├── README.md                 # Written by YOU: Problem, Architecture, Metrics, How to Run
├── requirements.txt          # Pinned dependencies
├── data/                     # Raw and processed datasets (gitignored if large)
├── notebooks/                # Exploration and error analysis only
├── src/
│   ├── __init__.py
│   ├── preprocess.py         # Data cleaning & feature extraction
│   ├── train.py              # Model training script
│   ├── evaluate.py           # Precision, recall, confusion matrix, error analysis
│   └── predict.py            # Inference function / CLI
└── tests/
    └── test_pipeline.py      # Automated tests with pytest
```

### Rules for Every Project
1. **Architecture First:** Before writing code, you write a short design note in English (`README.md` draft) explaining the inputs, outputs, and data flow.
2. **Milestone Reviews:** We build each module (`preprocess.py`, `train.py`, etc.) one by one. I review each file before you move to the next.
3. **Error Analysis Required:** You must inspect at least 10 examples where your model/AI failed and write in English *why* it failed and how to improve it.
4. **Oral/Written Defense:** A project is only marked "Complete" when you can answer my interview questions about any line of code in the repo.

