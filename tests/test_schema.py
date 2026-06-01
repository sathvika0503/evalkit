import sys
import os

sys.path.insert(0, os.path.abspath("."))

from evalkit.schema import load_spec


def test_load_spec():
    spec = load_spec("examples/summarisation.eval.yaml")

    assert spec.suite == "summarisation-v1"