
# modelviewset class:
# The ModelViewSet class inherits from GenericAPIView and includes implementations for various actions, by mixing in the behavior of the various mixin classes.
# The actions provided by the ModelViewSet class are list(), retrieve(), create(), update(), partial_update(), and destroy(). You can use any of the standard attributes or method overrides provided by GenericAPIView
# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# ReadOnlyModelViewSet:
# The ReadOnlyModelViewSet class also inherits from GenericAPIView. As with ModelViewSet it also includes implementations for various actions, but unlike ModelViewSet only provides the 'read-only' actions, list() and retrieve(). You can use any of the standard attributes and method overrides available to GenericAPIView
# class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
