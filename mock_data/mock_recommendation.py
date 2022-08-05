from mock_data.data.products import products_by_store_and_subsidiary, shopping_cart_by_store_and_subsidiary
import json


def get_product_recommendation(store_id, subsidiary_id, product):
    print(f'Find recommendation of store "{store_id}" subsidiary "{subsidiary_id}" product "{product}"')
    for r in products_by_store_and_subsidiary:
        print(f'Check store "{r["storeId"]}" subsidiary "{r["subsidiaryId"]}" product "{r["external"]}"')
        if r["storeId"] == store_id and r["subsidiaryId"] == subsidiary_id and r["external"] == product:
            print('Recommendation found!')
            return json.dumps(r["recommendation"])
    return json.dumps([])


def get_shopping_cart_recommendation(store_id, subsidiary_id, items):
    print(f'Find recommendation of store "{store_id}" subsidiary "{subsidiary_id}" product "{items}"')
    for r in shopping_cart_by_store_and_subsidiary:
        print(f'Check store "{r["storeId"]}" subsidiary "{r["subsidiaryId"]}"')
        if r["storeId"] == store_id and r["subsidiaryId"] == subsidiary_id:
            print('Recommendation found!')
            return json.dumps(r["recommendation"])
    return json.dumps([])
