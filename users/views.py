from rest_framework          import status, viewsets
from rest_framework.response import Response

from users.models      import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        req_email = request.data.get('email')

        if User.objects.filter(email=req_email).exists():
            return Response({"msg": "E-mail already exists"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response({"msg": "Successfully signed up"}, status=status.HTTP_201_CREATED)
