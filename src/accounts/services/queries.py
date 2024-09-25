from django.contrib.auth import get_user_model

User = get_user_model()

# In the case that we need custom field to authenticate user, we can use this function
def authenticate_user(*, username: str, password: str) -> User:
    user = User.objects.filter(username=username).first()
    return user if user and user.check_password(password) else None
