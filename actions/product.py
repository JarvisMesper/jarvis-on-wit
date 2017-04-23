from actions import wit
from openfood.RequestOpenFood import RequestOpenFood
from openfood.RequestOpenFood import ProductBuilder

def get_info(request):
    print('--- get_info() called ---')
    context = request['context']
    entities = request['entities']

    if context:
        print('context : ', context)
    if entities:
        print('entities : ', entities)

    product = wit.first_entity_value(entities, 'product_id')

    if product:
        try:
            # search product in OpenFood.ch API
            res = RequestOpenFood.get_product(barcode=product)
            res = ProductBuilder.clean_data(res)
            context['info'] = res
            if context.get('missing_id') is not None:
                del context['missing_id']
        except:
            context['info'] = "Can't find this product on the OpenFood database"

        # TODO : if the product doesn't exist in openfood, search in another API (eg. openfoodfacts)

    else:
        context['missing_id'] = True
        if context.get('info') is not None:
            del context['info']

    return context


def contains_ingredient(request):
    print('--- contains_ingredient() called ---')
    context = request['context']
    entities = request['entities']

    if context:
        print('context : ', context)
    if entities:
        print('entities : ', entities)

    product = wit.get_from_context_or_entities(context, entities, 'product_id')
    ingredient = wit.get_from_context_or_entities(context, entities, 'ingredient')
    print('product: ', product)
    print('ingredient: ', ingredient)

    if product and ingredient:

        context['answer'] = 'YES' # TODO

        if context.get('missingProduct') is not None:
            del context['missingProduct']
        if context.get('missingProduct') is not None:
            del context['missingProduct']

        if context.get('product_id') is not None:
            del context['product_id']
        if context.get('ingredient') is not None:
            del context['ingredient']

    else:
        if product:
            context['product_id'] = product
        else:
            context['missingProduct'] = True

        if ingredient:
            context['ingredient'] = ingredient
        else:
            context['missingIngredient'] = True

        if context.get('answer') is not None:
            del context['answer']

    print('===============================')
    return context