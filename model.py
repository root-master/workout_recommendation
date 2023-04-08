from typing import Dict

import numpy as np


def normalize_dist(dist: Dict) -> Dict:
    """Normalizes a distribution to a probability dist."""
    total = sum(dist.values())
    for key, value in dist.items():
        dist[key] = value / total
    return dist


def recommend_workout(dist: Dict):
    """Randomly choose an item from a distribution."""
    normal_dist = normalize_dist(dist)
    probs = list(normal_dist.values())
    keys = list(normal_dist.keys())
    choice = np.random.choice(keys, 1, p=probs)[0]
    return choice
