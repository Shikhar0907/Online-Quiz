from rest_framework import serializers
from .models import quiz_questions

class QuestionSerializer(serializers.ModelSerializer):
    class Meta():
        model = quiz_questions
        fields = '__all__'

    def validate(self,data):
        obj = data.get("questions",None)
        if obj == "":
            raise serializers.ValidationError("Content is required")
        return(data)
