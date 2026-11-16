def parcel_size(weight: int) -> str:
    """Return small for 0–2 kg and standard above 2 kg. Reject negative weights."""
    if weight < 0:
        raise ValueError("negative weight")
    if weight <= 2:
        return "small"
    return "standard"
