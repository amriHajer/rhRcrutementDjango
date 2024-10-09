# users/api/serializers.py

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User, RH, Employe, Candidat

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_rh', 'is_employe', 'is_candidat']


class RhSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'is_rh', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({"error": "passwords do not match"})

        user.set_password(password)
        user.is_rh = True
        user.save()
        RH.objects.create(user=user)

        # Générer des tokens JWT
        refresh = RefreshToken.for_user(user)

        # Retourner les détails de l'utilisateur avec le token
        return {
            'user': {
                'username': user.username,
                'email': user.email,
                'is_rh': user.is_rh,
            },
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


class EmployeSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'is_employe', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({"error": "passwords do not match"})

        user.set_password(password)
        user.is_employe = True
        user.save()
        Employe.objects.create(user=user)

        # Générer des tokens JWT
        refresh = RefreshToken.for_user(user)

        # Retourner les détails de l'utilisateur avec le token
        return {
            'user': {
                'username': user.username,
                'email': user.email,
                'is_employe': user.is_employe,
            },
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


class CandidatSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'is_candidat', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({"error": "passwords do not match"})

        user.set_password(password)
        user.is_candidat = True
        user.save()
        Candidat.objects.create(user=user)

        # Générer des tokens JWT
        refresh = RefreshToken.for_user(user)

        # Retourner les détails de l'utilisateur avec le token
        return {
            'user': {
                'username': user.username,
                'email': user.email,
                'is_candidat': user.is_candidat,
            },
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }























# from rest_framework import serializers
# from users.models import User, RH, Employe, Candidat


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'is_rh']


# class RhSignupSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'is_rh', 'password', 'password2']
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }

#     def save(self, **kwargs):
#         user = User(
#             username=self.validated_data['username'],
#             email=self.validated_data['email']
#         )
#         password = self.validated_data['password']
#         password2 = self.validated_data['password2']

#         if password != password2:
#             raise serializers.ValidationError({"error": "passwords do not match"})

#         user.set_password(password)
#         user.is_rh = True
#         user.save()
#         RH.objects.create(user=user)
#         return user


# class EmployeSignupSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'is_employe', 'password', 'password2']
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }

#     def save(self, **kwargs):
#         user = User(
#             username=self.validated_data['username'],
#             email=self.validated_data['email']
#         )
#         password = self.validated_data['password']
#         password2 = self.validated_data['password2']

#         if password != password2:
#             raise serializers.ValidationError({"error": "passwords do not match"})

#         user.set_password(password)
#         user.is_employe = True
#         user.save()
#         Employe.objects.create(user=user)
#         return user


# class CandidatSignupSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'is_candidat', 'password', 'password2']
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }

#     def save(self, **kwargs):
#         user = User(
#             username=self.validated_data['username'],
#             email=self.validated_data['email']
#         )
#         password = self.validated_data['password']
#         password2 = self.validated_data['password2']

#         if password != password2:
#             raise serializers.ValidationError({"error": "passwords do not match"})

#         user.set_password(password)
#         user.is_candidat = True
#         user.save()
#         Candidat.objects.create(user=user)
#         return user
