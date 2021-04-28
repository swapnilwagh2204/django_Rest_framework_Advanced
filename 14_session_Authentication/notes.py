# SessionAuthentication:

# This authentication scheme uses Django's default session backend for authentication. Session authentication is appropriate for AJAX clients that are running in the same session context as your website.
# If successfully authenticated, SessionAuthentication provides the following credentials.
# request.user will be a Django User instance.
# request.auth will be None.
# Unauthenticated responses that are denied permission will result in an HTTP 403 Forbidden response.
