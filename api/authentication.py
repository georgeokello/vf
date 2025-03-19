from rest_framework.authentication import BaseAuthentication, TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings

class CustomTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # Get the Authorization header
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            raise AuthenticationFailed("Authorization header missing")  # Reject requests without token

        try:
            token_type, token = auth_header.split(" ")
            if token_type.lower() != "token":
                raise AuthenticationFailed("Invalid token type")  # Only accept Bearer token
        except ValueError:
            raise AuthenticationFailed("Invalid token format")  # Reject invalid format

        # Check if the provided token matches the custom token in settings
        if token != settings.CUSTOM_AUTH_TOKEN:
            raise AuthenticationFailed("Invalid token")  # Reject invalid token

        # If token matches the custom token, authenticate the request
        return (None, None)  # No user, but token validated
