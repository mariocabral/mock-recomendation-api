from abc import ABC, abstractmethod
from engines.domain.recomendationParameters import RecommendationParams
from engines.domain.recomendationResult import RecommendationResult


class RecommendationStrategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def recommendation_algorithm(self, params: RecommendationParams) -> RecommendationResult:
        pass
