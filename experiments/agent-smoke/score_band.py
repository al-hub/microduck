def score_band(score: int) -> str:
    if isinstance(score, bool) or not isinstance(score, int):
        raise TypeError("score must be an integer, not bool")
    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100 inclusive")
    if score < 40:
        return "low"
    if score < 70:
        return "mid"
    return "high"
