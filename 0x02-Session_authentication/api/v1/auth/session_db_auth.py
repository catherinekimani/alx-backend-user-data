#!/usr/bin/env python3
""" SessionDBAuth class """
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """ session auth class with db storage """

    def create_session(self, user_id=None):
        """ create & store new instance of user session """
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        user_session_data = {
            "user_id": user_id,
            "session_id": session_id
        }
        user = UserSession(**user_session_data)
        user.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ return user_id by querying UserSession in the db """
        user_id = UserSession.search({"session_id": session_id})

        if user_id:
            return user_id
        return None

    def destroy_session(self, request=None):
        """ destroy Usersession based on the session ID """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if not session_id:
            return False

        user_session = UserSession.search({"session_id": session_id})

        if user_session:
            user_session[0].remove()
            return True

        return None
