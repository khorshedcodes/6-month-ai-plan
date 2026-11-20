# Day 20: Comprehensive System Integration (CLI News & Article Aggregator)

## Learning Objectives
1. Integrate everything from Weeks 1-3 into a single cohesive production CLI tool:
   - CLI flags & options (`argparse`)
   - Structured logging (`logging`)
   - Type hints & `@dataclass`
   - Defensive JSON caching & persistence (`json`, `pathlib.Path`)
   - REST API consumption with timeouts (`requests`)
   - Automated unit tests (`pytest`)
2. Handle network edge cases: offline fallback to local JSON cache.

---

## Daily Task: CLI News & HackerNews Top Stories Aggregator (Without AI)
In `aggregator.py`, build a complete tool:
1. `@dataclass class Article`:
   - `id: int`
   - `title: str`
   - `url: str`
   - `score: int`
   - `by: str`
2. `class NewsAggregator`:
   - `fetch_top_stories(limit: int = 5) -> list[Article]`:
     - Calls HackerNews public API: `https://hacker-news.firebaseio.com/v0/topstories.json` (gets top IDs).
     - Fetches details for top `limit` stories: `https://hacker-news.firebaseio.com/v0/item/{id}.json`.
     - Logs operations at `INFO` and `DEBUG`.
     - **Resilience:** If network fails, falls back to loading cached articles from `cache.json` and logs a `WARNING`!
   - `save_to_cache(articles: list[Article]) -> None`:
     - Serializes articles to `cache.json`.
3. CLI Interface with `argparse`:
   - `--limit`: integer (default 5).
   - `--verbose`: flag to enable `DEBUG` logging.
   - Formatted console display of ranked stories.
4. `test_aggregator.py`:
   - At least 3 unit tests with `pytest` testing serialization, caching, and article modeling.

---

## Developer English Task: Pull Request Review Response (C1)
Simulate responding to a Senior Engineer's PR review comment about offline fallback and caching strategy.

---

## Mandarin Chinese Task: Lesson 3 (Self-Introduction & Routine)
- `我叫...` (*Wǒ jiào...* = My name is...)
- `现在` (*xiànzài* = now)
- `几点` (*jǐ diǎn* = what time)
- Dialogue: Asking and telling the time.
