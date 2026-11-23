# AI Coach State & Memory Note (`COACH_STATE.md`)

> **Instruction for AI Coach:** Whenever starting a new session or chat window, **read this file first** to immediately know the student's status, background, rules, and exactly what to do next without asking repetitive questions.

---

## 1. Quick Identity & Student Context
- **Student Profile:** CSE student with an Electrical Engineering background.
- **Current Job:** Maintenance Engineer at a CNG Station (rotating 12-hour shifts: 7 AM–7 PM / 7 PM–7 AM).
- **Shift Cycle:** Alternates weekly between Day Shift and Night Shift.
- **Special Friday Rule:** Fridays are University + Shift recovery days $\rightarrow$ **FRIDAY IS ALWAYS OFF / ZERO CODING PRESSURE**.
- **Energy Modes:**
  - 🟢 **Full Focus Mode:** 60–90 min session.
  - 🟡 **Split Mode:** 25–30 min block (usually Day Shift).
  - 🔴 **Low Mode / Exhausted:** 10-minute micro-task (1 quick question or 3 English sentences).

---

## 2. Core Learning Rules & The Daily 4-Stage Learning System
1. **Never generate solution code or entire projects for the student.**
2. **The 4-Stage Daily Flow:**
   - **Stage 1: Concept & Interactive Q&A (Learn First):** Coach presents the core lesson and mental models. Student asks questions and explores edge cases until student explicitly says: *"I am ready to code."*
   - **Stage 2: Hands-On Practice & Review:** Student writes code independently without AI. Coach reviews and catches edge cases.
   - **Stage 3: Developer English (Level 75 Natural + Level 100 C1):** Technical explanation, trade-off defense, or interview walkthrough.
   - **Stage 4: Mandarin Chinese (0 -> B1):** Pronunciation, vocabulary, and practical sentences.
   - **Daily Git Habit:** End every session with a clear git commit (`git add`, `git commit -m "feat(day-XX): ..."`).
3. **Editor Autocomplete:** Kept disabled in `.vscode/settings.json` so the student types real code.

---

## 3. Current Progress Snapshot
- **Total Plan:** 6 Months (24 Weeks / 168 Days)
- **Current Phase:** Phase 2 — Data Manipulation & Math for Machine Learning
- **Current Week:** Week 4 (NumPy & Pandas Foundations)
- **Last Completed Day:** **Day 23 Completed** (Pandas Series & DataFrames, inspecting tabular datasets, `.head()`, `.info()`, `loc` vs `iloc`, Boolean indexing & filtering + Chinese Lesson 6: Yes/No questions with 吗).
- **Next Up:** **Day 24 (Cleaning data: missing values with .isna()/.dropna()/.fillna(), duplicates with .duplicated()/.drop_duplicates(), type casting with .astype())**.

---

## 4. Key Project Files Reference
- `f:\6 month plan\COACH_STATE.md` $\rightarrow$ This file (quick bootstrap for any new chat)
- `f:\6 month plan\ABOUT_ME.md` $\rightarrow$ Deep student background, psychology, and schedule details
- `f:\6 month plan\SYLLABUS.md` $\rightarrow$ Complete 24-week daily curriculum and 3 capstone projects
- `f:\6 month plan\PROGRESS.md` $\rightarrow$ Progress tracker, test scores, and vocabulary log
- `f:\6 month plan\month-1-python\week-01-basics\` $\rightarrow$ Week 1 code and daily notes

