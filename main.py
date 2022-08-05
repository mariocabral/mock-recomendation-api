import logging

from flask import Flask, request
from engines.context import Context
from engines.strategy.product_strategy import ProductRecommendationStrategy
from engines.strategy.shopping_cart_strategy import ShoppingCartRecommendationStrategy
from engines.domain.recommendation_parameters import RecommendationParams
from validator.request_validator import validate

app = Flask(__name__)


@app.route('/v1/recommendation/product/<uuid:store_id>/<uuid:subsidiary_store_id>/<external_id>', methods=['GET'])
@validate
def product_promotion(store_id, subsidiary_store_id, external_id):
    print(f'Recommendation request for store {store_id} subsidiary {subsidiary_store_id} '
          f'with the product {external_id}')
    context = Context(ProductRecommendationStrategy())
    print("Select Recommendation Strategy: product recommendation.")
    return context.get_recommendation(RecommendationParams(store_id=str(store_id),
                                                           subsidiary_id=str(subsidiary_store_id),
                                                           product=external_id))


@app.route('/v1/recommendation/shoppingcart/<uuid:store_id>/<uuid:subsidiary_store_id>', methods=['POST'])
@validate
def shopping_cart_promotion(store_id, subsidiary_store_id):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        shopping_cart_items = request.json
    else:
        return 'Content-Type not supported!'
    print(f'Recommendation request for store {store_id} subsidiary {subsidiary_store_id} '
          f'with the shopping cart items {shopping_cart_items}')
    context = Context(ShoppingCartRecommendationStrategy())
    print("Select Recommendation Strategy: shopping cart recommendation.")
    return context.get_recommendation(RecommendationParams(store_id=str(store_id),
                                                           subsidiary_id=str(subsidiary_store_id),
                                                           shopping_cart_items=shopping_cart_items))


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
