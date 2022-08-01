from engines.strategy.strategy import RecommendationStrategy
from engines.domain.recomendationParameters import RecommendationParams
from engines.domain.recomendationResult import RecommendationResult
from mock_data.mock_recommendation import get_product_recommendation


class ProductRecommendationStrategy(RecommendationStrategy):
    def recommendation_algorithm(self, params: RecommendationParams) -> RecommendationResult:
        return get_product_recommendation(
            store_id=params.get('store_id'),
            subsidiary_id=params.get('subsidiary_id'),
            product=params.get('product')
        )
