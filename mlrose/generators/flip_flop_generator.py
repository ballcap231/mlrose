""" Classes for defining optimization problem objects."""

# Author: Genevieve Hayes
# License: BSD 3 clause

import numpy as np

from mlrose import FlipFlopOpt


class FlipFlopGenerator:
    @staticmethod
    def generate(seed, size=20):
        np.random.seed(seed)
        problem = FlipFlopOpt(length=size)
        return problem
