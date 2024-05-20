from rest_framework import exceptions
from django.utils.translation import gettext_lazy as _

from api.utils import jwt_decode
from api.services import get_user


class CustomJwtAuthentication:
    keyword = "bearer"

    @staticmethod
    def get_authorization_header(request):
        """
        Return request's 'Authorization:' header, as a bytestring.

        Hide some test client ickyness where the header can be unicode.
        """
        auth = request.META.get("HTTP_AUTHORIZATION", b"")
        if isinstance(auth, str):
            # Work around django test client oddness
            auth = auth.split(" ")
        return auth

    def authenticate(self, request):
        """
        Returns a `User` if a correct username and password have been supplied
        using JWT authentication.  Otherwise returns `None`.
        """
        auth = self.get_authorization_header(request)

        if not auth or auth[0].lower() != self.keyword:
            return None

        if len(auth) == 1:
            msg = _("Invalid jwt token header. No credentials provided.")
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _("Invalid jwt token header. Credentials string should not contain spaces.")
            raise exceptions.AuthenticationFailed(msg)

        try:
            auth_decoded = jwt_decode(auth[1])

        except Exception as e:
            msg = _(str(e))
            raise exceptions.AuthenticationFailed(msg)

        userid = auth_decoded["user_id"]
        return self.authenticate_credentials(userid, request)

    def authenticate_credentials(self, userid, request=None):
        """
        Authenticate the userid and password against username and password
        with optional request for context.
        """

        user = get_user(user_id=userid)
        return (user, None)

    def authenticate_header(self, request):
        return self.keyword


class IsAuthenticated:
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)
