# Day 14: Week 2 Automated Test Suite
# Write your pytest unit tests and fixtures here independently.
import pytest
from pathlib import Path
from tracker import Issue, IssueManager

@pytest.fixture
def get_issues():
    return IssueManager(storage_path="issues.json")
    # ism.add_issue(title="Sample Issue",category="Undefined")
    # return ism

def test_add_issue(get_issues):
    title = "Sample Issue"
    category = "Undefined"
  
    r_value = get_issues.add_issue(title=title,category=category)
    assert r_value.title == title
    assert r_value.category == category

def test_close_issue(get_issues):
    title = "Sample Issue"
    category = "Undefined"

    r_value = get_issues.add_issue(title=title,category=category)
    assert get_issues.close_issue(issue_id=1) == True

def test_stream_open_issues(get_issues):
    title = "Sample Issue"
    category = "Undefined"
  
    r_value = get_issues.add_issue(title=title,category=category)
    get_issues.close_issue(issue_id=1)
    title = "Sample Issue 2"
    category = "Undefined"
    r_value = get_issues.add_issue(title=title,category=category)
    open_issues = list(get_issues.stream_open_issues())
    assert len(open_issues) == 1

def test_json_save_and_load(get_issues):
        title = "Sample Issue"
        category = "Undefined"
       
        r_value = get_issues.add_issue(title=title,category=category)
        get_issues.close_issue(issue_id=1)
        title = "Sample Issue 2"
        category = "Undefined"
    
        r_value = get_issues.add_issue(title=title,category=category)
        get_issues.save_to_json()
        new_ism = IssueManager('issues.json')
        new_ism.load_from_json()
        assert len(get_issues.issues) == len(new_ism.issues)


    