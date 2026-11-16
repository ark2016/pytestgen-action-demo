def parcel_size(weight: int) -> str:
    """Return small for 0–2 kg, standard for 3–10 kg, bulky above 10. Reject negatives."""
    if weight < 0:
        raise ValueError("negative weight")
    if weight <= 2:
        return "small"
    if weight <= 10:
        return "standard"
    return "bulky"
