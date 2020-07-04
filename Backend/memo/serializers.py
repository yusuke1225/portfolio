from .models import Memo, Result, Character
from rest_framework import serializers

class ResultSrializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = [
            'id',
            'result'
        ]

class CharacterSrializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = [
            'id',
            'character'
        ]

class MemoSrializer(serializers.ModelSerializer):

    result = ResultSrializer(read_only=True)
    my_chara = CharacterSrializer(read_only=True)
    op_chara = CharacterSrializer(read_only=True)
    result_id = serializers.PrimaryKeyRelatedField(queryset=Result.objects.all(), write_only=True)
    my_chara_id = serializers.PrimaryKeyRelatedField(queryset=Character.objects.all(), write_only=True)
    op_chara_id = serializers.PrimaryKeyRelatedField(queryset=Character.objects.all(), write_only=True)

    def create(self, validated_data):
        validated_data['result'] = validated_data.get('result_id', None)
        validated_data['my_chara'] = validated_data.get('my_chara_id', None)
        validated_data['op_chara'] = validated_data.get('op_chara_id', None)
        if validated_data['result'] is None:
            raise serializers.ValidationError("result not found")
        if validated_data['my_chara'] is None:
            raise serializers.ValidationError("my_chara not found")
        if validated_data['op_chara'] is None:
            raise serializers.ValidationError("op_chara not found")

        del validated_data['result_id'], validated_data['my_chara_id'],validated_data['op_chara_id']

        return Memo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        validated_data['result'] = validated_data.get('result_id', None)
        validated_data['my_chara'] = validated_data.get('my_chara_id', None)
        validated_data['op_chara'] = validated_data.get('op_chara_id', None)
        if validated_data['result'] is None:
            raise serializers.ValidationError("result not found")
        if validated_data['my_chara'] is None:
            raise serializers.ValidationError("my_chara not found")
        if validated_data['op_chara'] is None:
            raise serializers.ValidationError("op_chara not found")

        del validated_data['result_id'], validated_data['my_chara_id'],validated_data['op_chara_id']

        instance.result = validated_data.get('result', instance.result)
        instance.my_chara = validated_data.get('my_chara', instance.my_chara)
        instance.op_chara = validated_data.get('op_chara', instance.op_chara)
        instance.date = validated_data.get('date', instance.date)
        instance.time = validated_data.get('time', instance.time)
        instance.save()

        return instance

    class Meta:
        model = Memo
        fields = [
            'id',
            'date',
            'time',
            'result',
            'my_chara',
            'op_chara',
            'result_id',
            'my_chara_id',
            'op_chara_id',
        ]