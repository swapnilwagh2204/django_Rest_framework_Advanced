# rest framework provides apiclass views,which subclasses django's view class.
import rest_framework.decorators

# REST framework provides an APIView class, which subclasses Django's View class.
# APIView classes are different from regular View classes in the following ways:
# Requests passed to the handler methods will be REST framework's Request instances, not Django's HttpRequest instances.
# Handler methods may return REST framework's Response, instead of Django's HttpResponse. The view will manage content negotiation and setting the correct renderer on the response.
# Any APIException exceptions will be caught and mediated into appropriate responses.
# Incoming requests will be authenticated and appropriate permission and/or throttle checks will be run before dispatching the request to the handler method.


# class based api_view

# from rest_framework.views import APIView
# class StudentAPI(APIView):
#    def get(self, request, format=None):
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({‘msg’: ‘Data Created’ }, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
