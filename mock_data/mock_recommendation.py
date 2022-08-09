import json
from mock_data.data.products import products_by_store_and_subsidiary
from mock_data.data.shopping_cart import shopping_cart_by_store_and_subsidiary


def get_product_recommendation(store_id, subsidiary_id, product):
    print(f'Find recommendation of store "{store_id}" subsidiary "{subsidiary_id}" product "{product}"')
    for row in products_by_store_and_subsidiary:
        print(f'Check store "{row["storeId"]}" subsidiary "{row["subsidiaryId"]}" product "{row["external"]}"')
        if row["storeId"] == store_id and row["subsidiaryId"] == subsidiary_id and row["external"] == product:
            print('Recommendation found!')
            return json.dumps(row["recommendation"])
    return json.dumps([])


def get_shopping_cart_recommendation(store_id, subsidiary_id, items):
    print(f'Find recommendation of store "{store_id}" subsidiary "{subsidiary_id}" product "{items}"')
    for row in shopping_cart_by_store_and_subsidiary:
        print(f'Check store "{row["storeId"]}" subsidiary "{row["subsidiaryId"]}"')
        if row["storeId"] == store_id and row["subsidiaryId"] == subsidiary_id:
            print('Recommendation found!')
            return filter_items(row["recommendation"], items, limit=10)
    return json.dumps([])


def filter_items(recommendation, items, limit):
    recommendation_filtered = list(filter(lambda p: p['sku'] not in items, recommendation))
    return json.dumps(recommendation_filtered[0:limit])
