from allauth.account.adapter import DefaultAccountAdapter


class NoNewUsersAccountAdapter(DefaultAccountAdapter):
    # запрет пользователям на регистрацию
    def is_open_for_signup(self, request):
        return False
