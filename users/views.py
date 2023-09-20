from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
# Assuming you have a serializer defined for your CustomUser model
from .models import CustomUser  # Import your CustomUser model
from .serializers import CustomUserSerializer

# Create your views here.

def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return JsonResponse({'message': 'Passwords do not match'}, status=400)

        user = CustomUser(username=username)
        user.set_password(password1)
        user.save()

        login(request, user)
        return JsonResponse({'message': 'Registration successful'}, status=200)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'}, status=200)
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=401)

@login_required
def user_logout(request):
    logout(request)
    return JsonResponse({'message': 'Logged out successfully'}, status=200)

@login_required
def profile(request):
    if request.method == 'POST':
        serializer = CustomUserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

