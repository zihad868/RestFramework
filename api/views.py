from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Items
from base.serializers import ItemsSerializers

@api_view(['GET'])
def getData(request):
    item = Items.objects.all();
    serializer = ItemsSerializers(item, many=True)
    return Response(serializer.data)