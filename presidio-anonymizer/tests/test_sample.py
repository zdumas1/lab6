import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    result = sample_run_anonymizer("My name is Bond.", 11, 15)

    # Check the anonymized text
    assert result.text == "My name is BIP."

    # Check that items is a list
    assert isinstance(result.items, list)
    assert len(result.items) == 1

    # Access attributes of the first item
    item = result.items[0]
    assert item.start == 11
    assert item.end == 14
    assert item.entity_type == "PERSON"
    assert item.text == "BIP"
    assert item.operator == "replace"