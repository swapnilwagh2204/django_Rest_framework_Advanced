from .models import Student
from rest_framework import serializers

# validators://


def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('name should be start with r')


class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=100, validators=[start_with_r])
    # roll = serializers.IntegerField()
    # city = serializers.CharField(max_length=100)

    # we use model serializers here

    class Meta:
        # name=Student.CharField(read_only=True) #for read_only
        name = serializers.CharField(max_length=100, validators=[
                                     start_with_r])  # to use validators

        model = Student
        fields = ['id', 'name', 'roll', 'city']
        # read_only_fields = ['name']
        # fields.exclude = ('')
        # extra_kwargs={'name':{'read_only':'True'}}

   # field level validation

    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('seat full')
        return value

    # object level validation

    def validate(self, data):
        print(data)
        nm = data.get('name')
        ct = data.get('city')
        print(nm, ct)
        if nm.lower() == 'swapnil' and ct.lower() != 'nanded':
            raise serializers.ValidationError("city must be nanded")
        return data


# we dont need below code this in model serializers

# # for adding the data


#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

# # for data update

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.roll = validated_data.get('roll', instance.roll)
#         instance.city = validated_data.get('city', instance.city)
#         instance.save()
#         return instance
