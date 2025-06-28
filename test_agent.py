import pytest
from tools import manage_emails, post_to_social, read_document
from utils import make_accessible
from google.adk.types import ToolContext

class DummyContext(ToolContext):
    pass

def test_manage_emails_read():
    result = manage_emails('gmail', 'read', DummyContext())
    assert 'Email Summary:' in result
    assert 'unread emails' in result
    assert result == make_accessible(result)

def test_post_to_social():
    result = post_to_social('twitter', 'Hello world!', DummyContext())
    assert 'Posted to Twitter' in result
    assert result == make_accessible(result)

def test_read_document_summary():
    result = read_document('gdoc', 'dummy_id', DummyContext())
    assert result.startswith('Summary:')
    assert result == make_accessible(result)

def test_error_message_accessibility():
    # Test unsupported service
    result = manage_emails('yahoo', 'read', DummyContext())
    assert 'Sorry' in result and result == make_accessible(result)
    # Test error in post_to_social
    result = post_to_social('myspace', 'msg', DummyContext())
    assert 'Sorry' in result and result == make_accessible(result)
