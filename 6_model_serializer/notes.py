3 levels of validation:
    1.field-level validation--> to the particular validation
    2.object-level validation-->when we need to do validation of multiple fields...then we need object-level validation...by adding method validate() to serializer class.
    it raises a serializers.validationError if necessary, or just return the validated values.
