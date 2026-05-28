# store/views/health.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    return Response({
        'service': 'ShopApi',
        'status': 'ok',
        'version': '1.0',
        'message': 'Welcome to ShopApi!'
    })


@api_view(['GET'])
@permission_classes([AllowAny])
def testingcicd(request):
    return Response({
        'status': 'success',
        'message': 'CI/CD working correctly!'
    })