from django.conf import settings

from rest_auth.serializers import (
    TokenSerializer as DefaultTokenSerializer,
    UserDetailsSerializer as DefaultUserDetailsSerializer,
    LoginSerializer as DefaultLoginSerializer,
    PasswordResetSerializer as DefaultPasswordResetSerializer,
    PasswordResetConfirmSerializer as DefaultPasswordResetConfirmSerializer,
    PasswordChangeSerializer as DefaultPasswordChangeSerializer,
    LockUserSerializer as DefaultLockUserSerializer,
    UnlockUserSerializer as DefaultUnlockUserSerializer)

from .utils import import_callable


serializers = getattr(settings, 'REST_AUTH_SERIALIZERS', {})

TokenSerializer = import_callable(
    serializers.get('TOKEN_SERIALIZER', DefaultTokenSerializer))

UserDetailsSerializer = import_callable(
    serializers.get('USER_DETAILS_SERIALIZER', DefaultUserDetailsSerializer)
)
LockUserSerializer = import_callable(
   serializers.get('LockUserSerializer',DefaultLockUserSerializer)
)
UnlockUserSerializer = import_callable(
   serializers.get('UnlockUserSerializer',DefaultUnlockUserSerializer)
)
LoginSerializer = import_callable(
    serializers.get('LOGIN_SERIALIZER', DefaultLoginSerializer)
)

PasswordResetSerializer = import_callable(
    serializers.get(
        'PASSWORD_RESET_SERIALIZER',
        DefaultPasswordResetSerializer
    )
)

PasswordResetConfirmSerializer = import_callable(
    serializers.get(
        'PASSWORD_RESET_CONFIRM_SERIALIZER',
        DefaultPasswordResetConfirmSerializer
    )
)

PasswordChangeSerializer = import_callable(
    serializers.get(
        'PASSWORD_CHANGE_SERIALIZER',
        DefaultPasswordChangeSerializer
    )
)
