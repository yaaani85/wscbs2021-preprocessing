from brane_preprocessing import preprocess

# local testing
def test_preprocess():
    assert preprocess(True, True) == "Preprocessed data"
