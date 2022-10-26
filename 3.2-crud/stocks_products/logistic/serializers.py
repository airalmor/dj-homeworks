from rest_framework import serializers
from logistic.models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['positions', 'address']
        # настройте сериализатор для склада

    def create(self, validated_data):
        positions = validated_data.pop('positions')

        stock = super().create(validated_data)

        for position in positions:
            StockProduct.objects.create(
                stock=stock,
                product=position.get('product'),
                quantity=position.get('quantity'),
                price=position.get('price'))

        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)

        for position in positions:
            product = position.pop('product')
            obj, created = StockProduct.objects.update_or_create(
                product=product,
                stock=stock,
                defaults=position)

        return stock
