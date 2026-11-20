# Day 20: Automated Test Suite
# Write your pytest unit tests here independently.
import pytest
from aggregator import Article, NewsAggregator

def test_article_dataclass():
     artical = Article(id=1,title="simple title",url="",score=200,by="khorshed")
     assert artical.title == "simple title"


def test_cache_save_and_load():
      newAgg = NewsAggregator('testcache.json')
      newAgg.fetch_top_stories(2)
      newAgg.load_from_cache()
      assert len(newAgg.articles) == 2