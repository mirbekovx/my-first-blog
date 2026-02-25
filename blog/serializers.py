from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    # Добавим дополнительное поле, чтобы видеть имя автора текстом, а не просто ID
    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        # Список полей, которые полетят в JSON
        fields = ['id', 'title', 'content', 'author', 'author_name', 'created_at']
        # Поле author будет заполняться автоматически из текущего юзера,
        # поэтому сделаем его только для чтения в самом JSON
        read_only_fields = ['author', 'created_date']