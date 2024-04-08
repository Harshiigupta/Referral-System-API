from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

@api_view(['POST'])
def register(request):
    name = request.data.get('name')
    email = request.data.get('email')
    password = request.data.get('password')
    referral_code = request.data.get('referral_code')

    if not name or not email or not password:
        return Response({'error': 'Name, email, and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=email, email=email, password=password, name=name)

    if referral_code:
        try:
            referrer = User.objects.get(referral_code=referral_code)
            user.referrer = referrer
            user.save()
        except User.DoesNotExist:
            pass

    return Response({'user_id': user.id, 'message': 'User created successfully.'}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_details(request):
    user = request.user
    return Response({'name': user.name, 'email': user.email, 'referral_code': user.referral_code, 'timestamp': user.date_joined})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def referrals(request):
    user = request.user
    referrals = user.referrer.referrals.all()
    page = request.query_params.get('page', 1)
    paginator = paginator(referrals, 20)
    referrals_page = paginator.get_page(page)
    return Response([{'user_id': referral.id, 'timestamp': referral.date_joined} for referral in referrals_page])