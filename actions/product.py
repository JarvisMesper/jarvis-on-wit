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

            # TODO : if the product doesn't exist in openfood, search in another API (eg. openfoodfacts)

        except:
            context['info'] = "Can't find this product on the OpenFood database"
    else:
        context['missing_id'] = True
        if context.get('info') is not None:
            del context['info']

    return context
