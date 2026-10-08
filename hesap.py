def ucgen(a, b, c):
    """Üç kenarın uzunluğunu alır ve üçgenin alanını hesaplar."""
    s = (a + b + c) / 2
    alan = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return alan
def dortgen(a, b):
    """Dikdörtgenin kısa ve uzun kenarını alır ve alanını hesaplar."""
    return a * b