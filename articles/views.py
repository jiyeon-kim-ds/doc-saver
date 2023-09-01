from rest_framework import status, viewsets
from rest_framework.response import Response

from articles.models import Article
from articles.serializers import ArticleSerializer
from articles.utils import get_html_from_url, CustomHTMLParser


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = Article.objects.filter(user_id=self.request.user.id)
        return queryset

    def create(self, request, *args, **kwargs):
        req_url = request.data.get('url')
        req_category_id = request.data.get('category_id')
        req_tag_id = request.data.get('tag_id')

        decoded_page = get_html_from_url(req_url)

        parser = CustomHTMLParser()

        parser.feed(decoded_page)

        text = parser.big_text
        title = parser.title

        req_data = {
            'title': title[:255] if len(text) > 255 else title,
            'url': req_url,
            'user': request.user.id,
            'content': text,
            'summary': text[:100] if len(text) > 100 else text,
        }

        article_serializer = ArticleSerializer(data=req_data)
        if article_serializer.is_valid(raise_exception=True):
            article_serializer.save()

        return Response({'msg': 'URL registered successfully'}, status=status.HTTP_201_CREATED)
