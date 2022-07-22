from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'publication_date', 'genre', 'featured')


# class UserSerializer(serializers.ModelSerializer):
#     book_tracker = serializers.PrimaryKeyRelatedField(many=True, queryset=Tracker.objects.all())

#     class Meta:
#         model = User
#         fields = ['id', 'username' 'book_tracker']


# class TrackerSerializer(serializers.ModelSerializer):
#     user = serializers.ReadOnlyField(source='user.username')
#     def get_book_status(self, obj):
#         return obj.get_status_display()

#     book_status = serializers.SerializerMethodField(read_only=True, source=get_book_status)
#     book_details = BookSerializer(source='book', read_only=True )

#     class Meta:
#         model = Tracker
#         fields = ['id', 'status', 'book', 'user', 'book_details']

