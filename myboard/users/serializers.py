from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password   # 패스워드 검증 도구

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator   # 이메일 중복방지


# 회원가입
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, 
        validators=[UniqueValidator(queryset=User.objects.all())], # 이메일 중복 검증
        )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password":"Password fields didn't match."}
            )
        return data
    
    def create(self,validated_data):
        # CREATE요청에 대해 cretae메서드를 오버라이딩, 유저를 생성하고 토큰을 생성
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return user