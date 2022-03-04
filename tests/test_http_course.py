#!/usr/bin/env python

"""Tests for `http_course` package."""
import http_course

def test_package_publishes_version_info():
    """Tests that the `http_course` publishes the current verion"""

    assert hasattr(http_course, '__version__')
