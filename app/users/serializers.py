from .models import CustomUser
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'restaurant']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def save(self):

        password = self.validated_data['password']

        if CustomUser.objects.filter(email=self.
                                     validated_data['email']).exists():
            raise serializers.ValidationError(
                                        {'error': 'Email already exists!'})

        account = CustomUser(email=self.validated_data['email'],
                             name=self.validated_data['email'].split('@')[0],
                             restaurant=self.validated_data['restaurant'])

        account.set_password(password)
        account.save()

        return account
