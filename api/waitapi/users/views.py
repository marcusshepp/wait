from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# class RegisterView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message': 'User created successfully'}, status=201)
#         return Response(serializer.errors, status=400)
#
# class LoginView(APIView):
#     def post(self, request):
#         from django.contrib.auth import authenticate
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)
#         if user:
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'refresh': str(refresh),
#                 'access': str(refresh.token),
#             })
#         return Response({'error': 'Invalid credentials'}, status=401)
#

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        user = User.objects.create_user(
                username=request.POST['username'], password=request.POST['password'])
        user.save()
        return HttpResponse(status=201)
    return None;
 

