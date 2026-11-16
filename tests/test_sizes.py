from parcel_demo.sizes import parcel_size


def test_small_parcel():
    assert parcel_size(1) == "small"
