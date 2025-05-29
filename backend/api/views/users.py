from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from users.models import Subscription, User

from ..permissions import AnonimOrAuthenticatedReadOnly
from ..serializers.users import (
    PublicUserSerializer,
    SubscriptionActionSerializer,
    SubscribedUserDetailSerializer
)


class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = PublicUserSerializer
    permission_classes = (AnonimOrAuthenticatedReadOnly,)

    @action(
        detail=False,
        methods=['get', 'patch'],
        permission_classes=(permissions.IsAuthenticated,),
        url_path='me'
    )
    def manage_me(self, request):
        if request.method == 'PATCH':
            serializer = PublicUserSerializer(
                request.user, data=request.data,
                partial=True, context={'request': request}
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        serializer = PublicUserSerializer(
            request.user, context={'request': request}
        )
        return Response(serializer.data)

    @action(
        detail=True,
        methods=['post', 'delete'],
        permission_classes=(permissions.IsAuthenticated,),
        url_path='subscribe'
    )
    def manage_subscription(self, request, id=None):
        author = get_object_or_404(User, id=id)
        if request.method == 'POST':
            serializer = SubscriptionActionSerializer(
                data={'subscriber': request.user.id, 'author': author.id}
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_serializer = SubscribedUserDetailSerializer(
                author, context={'request': request}
            )
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        subscription = get_object_or_404(
            Subscription, subscriber=request.user, author=author
        )
        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(
        detail=False,
        methods=['get'],
        permission_classes=(permissions.IsAuthenticated,),
        url_path='subscriptions'
    )
    def list_subscriptions(self, request):
        authors = User.objects.filter(author__subscriber=request.user)
        paginator = PageNumberPagination()
        paginated_authors = paginator.paginate_queryset(authors, request)
        serializer = SubscribedUserDetailSerializer(
            paginated_authors, many=True, context={'request': request}
        )
        return paginator.get_paginated_response(serializer.data)
