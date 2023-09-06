from this_works_i_swear import do_something
import pytest

def test_something():
  assert isinstance(do_something(), str)
