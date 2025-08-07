def safe_divide(a: float, b: float) -> float:
    """Divide ``a`` by ``b`` raising a ValueError when ``b`` is zero."""
    if b == 0:
        raise ValueError("division by zero is undefined")
    return a / b
