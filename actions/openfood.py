from actions import wit
from openfood.RequestOpenFood import RequestOpenFood
from openfood.RequestOpenFood import ProductBuilder

def getOpenFoodInfo(request):
    print('--- get_openfood() called ---')
    context = request['context']
    entities = request['entities']

    if context:
        print('context : ', context)
    if entities:
        print('entities : ', entities)


    product = wit.first_entity_value(entities, 'product_id')
    if product:
        res = RequestOpenFood.get_product(barcode=product)
        res = ProductBuilder.clean_data(res)
        context['info'] = res
    else:
        context['info'] = "Can't retrieve any info, sorry"


    return context