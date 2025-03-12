from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product


@api_view(http_method_names=['GET', 'POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        # step 1: collect data from DB (QuerySet)
        products = Product.objects.all()

        # step 2: reformat (serialize) from queryset to list of dictionary
        # list_ = []
        # for i in products:
        #     list_.append({
        #         'id': i.id,
        #         'title': i.title,
        #         'description': i.description,
        #         'price': i.price,
        #     })
        list_ = ProductSerializer(instance=products, many=True).data

        # step 3: return response (data, status=200)
        return Response(data=list_)
    elif request.method == 'POST':
        # create product
        return Response


@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Product not found'})
    # data = ProductSerializer(instance=product).data
    data = ProductSerializer(product).data
    return Response(data=data)
