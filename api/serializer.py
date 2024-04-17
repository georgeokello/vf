from rest_framework import serializers
from baseApp.models import FundiUser, Topic, Session, Activity, TextActivity, VideoActivity, Feedback


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundiUser
        fields = ['username', 'email', 'password', 'school', 'subject', 'classTaught']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = FundiUser(
            username=validated_data['username'],
            email=validated_data['email'],
            school=validated_data['school'],
            subject=validated_data['subject'],
            classTaught=validated_data['classTaught']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = "__all__"


class TextActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TextActivity
        fields = "__all__"

class VideoActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoActivity
        fields = "__all__"

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"