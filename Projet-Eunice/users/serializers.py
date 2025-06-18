from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True, label="Confirm password")

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'password2', 
                  'telephone', 'role', 'adresse_geographique', 'horaires_habituels', 'informations_vehicule')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'informations_vehicule': {'required': False, 'allow_blank': True, 'allow_null': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        
        # Si le rôle est CONDUCTEUR, informations_vehicule est requis (ou du moins non vide si fourni)
        # Si le rôle est PASSAGER, informations_vehicule doit être vide/null
        role = attrs.get('role')
        informations_vehicule = attrs.get('informations_vehicule')

        if role == 'CONDUCTEUR' and not informations_vehicule:
            # Vous pouvez choisir de le rendre strictement requis ou de simplement avertir/valider plus tard
            # Pour l'instant, nous allons le rendre requis s'il est conducteur
            # raise serializers.ValidationError({"informations_vehicule": "Vehicle information is required for drivers."})
            pass # La logique du modèle s'en chargera, ou vous pouvez la forcer ici

        if role == 'PASSAGER' and informations_vehicule:
            # Le modèle User.save() s'en chargera, mais on peut aussi valider ici
            attrs['informations_vehicule'] = None 
            # raise serializers.ValidationError({"informations_vehicule": "Passengers cannot have vehicle information."})


        # Vérifier l'unicité de l'email ici aussi, bien que le modèle le fasse au niveau DB
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({"email": "This email address is already in use."})
        
        # Vérifier l'unicité du téléphone si fourni
        telephone = attrs.get('telephone')
        if telephone and User.objects.filter(telephone=telephone).exists():
            raise serializers.ValidationError({"telephone": "This phone number is already in use."})

        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        # La logique de User.save() pour informations_vehicule sera appliquée
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 
                  'telephone', 'role', 'photo_profil', 'adresse_geographique', 
                  'horaires_habituels', 'informations_vehicule', 'date_joined', 'last_login')
        read_only_fields = ('email', 'username', 'role', 'date_joined', 'last_login') # email et username ne devraient pas être modifiables via ce serializer

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, validators=[validate_password])
    new_password_confirm = serializers.CharField(required=True)

    def validate(self, data):
        if data['new_password'] != data['new_password_confirm']:
            raise serializers.ValidationError({"new_password_confirm": "New passwords must match."})
        return data