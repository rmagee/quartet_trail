# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright 2018 SerialLab Corp.  All rights reserved.

class Singleton(type):
    '''
        Singleton pattern requires for GetUser class
    '''
    def __init__(cls, name, bases, dicts):
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instance 


class NotLoggedInUserException(Exception):
    '''
    '''
    def __init__(self, val='No users have been logged in'):
        self.val = val
        super(NotLoggedInUser, self).__init__()

    def __str__(self):
        return self.val

class LoggedInUser(object):
    __metaclass__ = Singleton

    user = None

    def set_user(self, request):
        if request.user.is_authenticated:
            self.user = request.user

    @property
    def current_user(self):
        '''
            Return current user or raise Exception
        '''
        if self.user is None:
            raise NotLoggedInUserException()
        return self.user

    @property
    def have_user(self):
        return not user is None


class QuartetTrailMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        
        # do stuff before
        response = self.get_response(request)

        if request.method in ['PUT', 'PATCH', 'POST', 'DELETE']:
            import pudb; pudb.set_trace()        
            
        # do stuff after
        return response
