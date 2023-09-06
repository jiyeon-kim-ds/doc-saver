from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from tags.models import Tag
from tags.serializers import TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Tag.objects.filter(user_id=self.request.user.id)
        return queryset

    def create(self, request, *args, **kwargs):
        req_data = {
            'user': request.user.id,
            'name': request.data.get('name')
        }

        tag_serializer = TagSerializer(data=req_data)
        if tag_serializer.is_valid(raise_exception=True):
            tag_serializer.save()

            return Response({'msg': 'Tag registered successfully'}, status=status.HTTP_201_CREATED)
        