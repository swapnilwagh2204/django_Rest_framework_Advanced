# BytesIO
# A stream implementation using an in-memory bytes buffer. It inherits BufferedIOBase. The buffer is discarded when the close() method is called.
# import io
# stream = io.BytesIO(json_data)


# JSONParser()
# This is used to parse json data to python native data type.
# from rest_framework.parsers import JSONParser
# parsed_data = JSONParser().parse(stream)

# De-serialization:
# Deserialization allows parsed data to be converted back into complex types, after first validating the incoming data.

# Creating Serializer Object
# serializer = StudentSerializer(data = parsed_data)

# Validated Data
# serializer.is_valid()

# serializer.validated_data
# serializer.errors


# serializer.validated_data

# This is the Valid data.
# serializer.validated_data


# create/insert data

# from rest_framework import serializers


# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)

#    def create(self, validated_data):
#    	return Student.objects.create(**validated_data)


# update data:

# from rest_framework import serializers
# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)
#     def update(self, instance, validated_data):
#   	instance.name = validated_data.get('name', instance.name)
#   	instance.roll = validated_data.get('roll', instance.roll)
#   	instance.city = validated_data.get('city', instance.city)
#   	instance.save()
#   	return instance

# complete update data:
# By default, serializers must be passed values for all required fields or they will raise validation errors.
# Required All Data from Front End/Client
# serializer = StudentSerializer(stu, data=pythondata) 
# if serializer.is_valid():
#     serializer.save()


# partial update data:
# Partial Update - All Data not required
# serializer = StudentSerializer(stu, data=pythondata, partial=True)
# if serializer.is_valid():
#     serializer.save()
