from rest_framework import serializers
from .models import Book, Category, Info, Teg

# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     title = serializers.CharField(max_length = 50)
#     description = serializers.CharField()
#     price = serializers.DecimalField(max_digits=10, decimal_places=2)
#     reating = serializers.ChoiceField(choices=Book.RATING)
#     author = serializers.CharField(max_length=50)
#     category = serializers.PrimaryKeyRelatedField(
#         queryset = Category.objects.all()
#     )
#     info = serializers.PrimaryKeyRelatedField(
#         queryset = Info.objects.all()
#     )
#     teg = serializers.PrimaryKeyRelatedField(
#         queryset = Teg.objects.all(),
#         many = True
#     )

class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    def validate(self, attrs):
        if attrs['price'] <=0:
            raise serializers.ValidationError('price cant be 0 or lower than 0!')
        return attrs
    

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'

class TegSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teg
        fields = '__all__'