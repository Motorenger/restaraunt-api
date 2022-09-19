from rest_framework import serializers

from .models import Restaurant, VoteMenus


class RestMenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ("current_menu",)


class VoteMenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = VoteMenus
        # fields = ("menu", "votes")
        exclude = ("restaurant",)
