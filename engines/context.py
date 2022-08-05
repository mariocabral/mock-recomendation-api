from __future__ import annotations
from engines.strategy.product_strategy import RecommendationStrategy
from engines.domain.recommendation_parameters import RecommendationParams
from engines.domain.recommendation_result import RecommendationResult


class Context:
    """
    The Context defines the interface of interest to clients.
    """

    def __init__(self, strategy: RecommendationStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> RecommendationStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: RecommendationStrategy) -> None:
        self._strategy = strategy

    def get_recommendation(self, params: RecommendationParams) -> RecommendationResult:
        return self._strategy.recommendation_algorithm(params)
