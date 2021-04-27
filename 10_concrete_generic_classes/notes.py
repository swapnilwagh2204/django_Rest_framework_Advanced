# The following classes are the concrete generic views.
# If you're using generic views this is normally the level you'll be working at unless you need heavily customized behavior.
# The view classes can be imported from rest_framework.generics.
# ListAPIView
# CreateAPIView
# RetrieveAPIView
# UpdateAPIView
# DestroyAPIView


# but in concrete api_view
# ListCreateAPIView
# RetrieveUpdateAPIView
# RetrieveDestroyAPIView
# RetrieveUpdateDestroyAPIView

# ListAPIView:
# It is used for read-only endpoints to represent a collection of model instances. It provides a get method handler.
# Extends: GenericAPIView, ListModelMixin

# from rest_framework.generics import ListAPIView
# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# CreateAPIView:
# It is used for create-only endpoints. It provides a post method handler.
# Extends: GenericAPIView, CreateModelMixin

# from rest_framework.generics import CreateAPIView
# class StudentCreate(CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# RetrieveAPIView:
# It is used for read-only endpoints to represent a single model instance. It provides a get method handler.
# Extends: GenericAPIView, RetrieveModelMixin

# from rest_framework.generics import RetrieveAPIView
# class StudentRetrieve(RetrieveAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# UpdateAPIView:
# It is used for update-only endpoints for a single model instance. It provides put and patch method handlers.
# Extends: GenericAPIView, UpdateModelMixin

# from rest_framework.generics import UpdateAPIView
# class StudentUpdate(UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# DestroyAPIView:
# It is used for delete-only endpoints for a single model instance. It provides a delete method handler.
# Extends: GenericAPIView, DestroyModelMixin

# from rest_framework.generics import DestroyAPIView
# class StudentDestroy(DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


from rest_framework.generics import RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
# concrete views:

# ListCreateAPIView:

# It is used for read-write endpoints to represent a collection of model instances. It provides get and post method handlers.
# Extends: GenericAPIView, ListModelMixin, CreateModelMixin

# from rest_framework.generics import ListCreateAPIView
# class StudentListCreate(ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# RetrieveUpdateAPIView:
# It is used for read or update endpoints to represent a single model instance. It provides get, put and patch method handlers.
# Extends: GenericAPIView, RetrieveModelMixin, UpdateModelMixin

# from rest_framework.generics import RetrieveUpdateAPIView
# class StudentRetrieveUpdate(RetrieveUpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# RetrieveUpdateAPIView:

# It is used for read or delete endpoints to represent a single model instance. It provides get and delete method handlers.
# Extends: GenericAPIView, RetrieveModelMixin, DestroyModelMixin

# class StudentRetrieveDestroy(RetrieveDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# RetrieveUpdateDestroyAPIView:
# It is used for read-write-delete endpoints to represent a single model instance. It provides get, put, patch and delete method handlers.
# Extends: GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

# from rest_framework.generics import RetrieveUpdateDestroyAPIView
# class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
