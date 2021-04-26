import rest_framework

# http: // geekyshows.com/api/students

# GET / api/students
# GET / api/students/1
# POST / api/students
# PUT / api/students/1
# PATCH / api/students/1
# DELETE / api/students/1


# Django REST framework is a powerful and flexible toolkit for building Web APIs.

# The Web browsable API is a huge usability win for your developers.
# Authentication policies including packages for OAuth1 and OAuth2.
# Serialization that supports both ORM and non-ORM data sources.
# Customizable all the way down - just use regular function-based views if you don't need the more powerful features.
# Extensive documentation, and great community support.
# Used and trusted by internationally recognized companies including Mozilla, Red Hat, Heroku, and Eventbrite.


# INstalling djangorestframework

# Python
# Django

# The following packages are optional:
# PyYAML, uritemplate (5.1+, 3.0.0+) - Schema generation support.
# Markdown (3.0.0+) - Markdown support for the browsable API.
# Pygments (2.4.0+) - Add syntax highlighting to Markdown processing.
# django-filter (1.0.1+) - Filtering support.
# django-guardian (1.1.1+) - Object level permissions support.

# Install using pip
# 	pip install djangorestframework


# Uninstall using pip
# 	pip uninstall djangorestframework

# INSTALLED_APPS = [
#     ...
#     'rest_framework',
# ]


# urlpatterns = [
#     ...
#     path(api-auth/, include('rest_framework.urls'))
# ]


# Python Json:
# Python has a built in package called json, which is used to work with json data.
# dumps(data) – This is used to convert python object into json string.
# Example:-
# To use json package First we have to import it.
# import json
# python_data = {‘name’: ‘Sonam’, ‘roll’:101 }
# json_data = json.dumps(python_data)
# print(json_data)
# {“name” : “Sonam”, “roll” : 101}


# loads(data) – This is used to parse json string.
# Example:-
# import json
# json_data = {“name” : “Sonam”, “roll” : 101}
# parsed_data = json.loads(json_data)
# print(parsed_data)
# {‘name’ : ‘Sonam’, ‘roll’ : 101}


# serializers

# In Django REST Framework, serializers are responsible for converting complex data such as querysets and model instances to native Python datatypes (called serialization) that can then be easily rendered into JSON, XML or other content types which is understandable by Front End.

# Serializers are also responsible for deserialization which means it allows parsed data to be converted back into complex types, after first validating the incoming data.

# Serialization
# Deserialization

# serializers class:
# A serializer class is very similar to a Django Form and ModelForm class, and includes similar validation flags on the various fields, such as required, max_length and default.
# DRF provides a Serializer class which gives you a powerful, generic way to control the output of your responses, as well as a ModelSerializer class which provides a useful shortcut for creating serializers that deal with model instances and querysets.

# How to create serializers class:

# Create a separate seriealizers.py file to write all serializers

# from rest_framework import serializers
# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)


# serializers fields:

# CharField - A text representation. Optionally validates the text to be shorter than max_length and longer than min_length.
# Syntax:- CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
# max_length - Validates that the input contains no more than this number of characters.
# min_length - Validates that the input contains no fewer than this number of characters.
# allow_blank - If set to True then the empty string should be considered a valid value. If set to False then the empty string is considered invalid and will raise a validation error. Defaults to False.
# trim_whitespace - If set to True then leading and trailing whitespace is trimmed. Defaults to True.
# The allow_null option is also available for string fields, although its usage is discouraged in favor of allow_blank.
# IntegerField - An integer representation.
# Syntax: - IntegerField(max_value=None, min_value=None)
# max_value Validate that the number provided is no greater than this value.
# min_value Validate that the number provided is no less than this value.

# FloatField - A floating point representation.
# Syntax: - FloatField(max_value=None, min_value=None)
# max_value Validate that the number provided is no greater than this value.
# min_value Validate that the number provided is no less than this value.

# DecimalField - A decimal representation, represented in Python by a Decimal instance.
# Syntax:- DecimalField(max_digits, decimal_places, coerce_to_string=None, max_value=None, min_value=None)
# max_digits The maximum number of digits allowed in the number. It must be either None or an integer greater than or equal to decimal_places.
# decimal_places The number of decimal places to store with the number.
# coerce_to_string Set to True if string values should be returned for the representation, or False if Decimal objects should be returned. Defaults to the same value as the COERCE_DECIMAL_TO_STRING settings key, which will be True unless overridden. If Decimal objects are returned by the serializer, then the final output format will be determined by the renderer. Note that setting localize will force the value to True.
# max_value Validate that the number provided is no greater than this value.
# min_value Validate that the number provided is no less than this value.

# Serializer FIeld
# localize Set to True to enable localization of input and output based on the current locale. This will also force coerce_to_string to True. Defaults to False. Note that data formatting is enabled if you have set USE_L10N=True in your settings file.
# rounding Sets the rounding mode used when quantising to the configured precision. Valid values are decimal module rounding modes. Defaults to None.

# SlugField - A RegexField that validates the input against the pattern [a-zA-Z0-9_-]+
# Syntax:- SlugField(max_length=50, min_length=None, allow_blank=False)
