from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Items
from base.serializers import ItemsSerializers

@api_view(['GET'])
def getData(request):
    items = Items.objects.all()
    serializer = ItemsSerializers(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addData(request):
    serializer = ItemsSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)  
    return Response(serializer.errors, status=400) 
