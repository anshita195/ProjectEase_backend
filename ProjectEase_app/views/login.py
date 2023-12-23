from rest_framework import viewsets
from rest_framework.views import APIView
from ProjectEase_app.serializers import *
from ProjectEase_app.models import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.http import request, HttpResponse, HttpResponseBadRequest,JsonResponse
import requests
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view

client_id = 'ifYhudyGqhLiWQsxCMJpTuOB54ULVq4mqOvFUuSv'
client_secret_key = 'EN3q19XQZ69bO8E4kq02PzFeMPkPEkxbRZDDMYkvaR5gU9Lqd1bQhMUhnBx2I6F865Y62sLfFmLXMIiEGtVMkXDbKyHfD2ogdpAzXWcpN2Y657sddJ7Td9vK7GBUpnE3'


@api_view(["GET"])
def check_login(request):
    if request.user.is_authenticated:
        # print(request)
        print(request.user,"a")
        current_user = User.objects.get(username=request.user)
        serializer = UserSerializer(current_user)
        return Response({'status': 'logged_in', 'user': serializer.data})
    else:
        return Response({'status': 'not_logged_in'})
class OauthAuthorizeView(APIView):
    def get(self, request):
        state = 'success'
        redirect_uri = 'http://127.0.0.1:8000/projectease/oauth/callback/'
        url = 'https://channeli.in/oauth/authorise/?client_id=' + \
            client_id+'redirect_uri='+redirect_uri + '&state='+state
        return redirect(redirect_uri)




class OauthCallback(APIView):
    def get(self, request):
        code = request.GET.get('code')
        if (code):
            # making post request to get access token
            data = {
                'grant_type': "authorization_code",
                'client_id': client_id,
                'redirect_uri': 'http://127.0.0.1:8000/projectease/oauth/callback/',
                'client_secret': client_secret_key,
                'code': code,

            }
            url = f'https://channeli.in/open_auth/token/'
            print("how")
            response = requests.post(url, data=data).json()
            print(response,"response")
            access_token = response['access_token']
            request.session['access_token'] = access_token
            print(access_token,"abc")

            # making a get request to get data
            url_toget_data = 'https://channeli.in/open_auth/get_user_data/'
            user_data = requests.get(url=url_toget_data,
                                     headers={
                                         "Authorization": f'Bearer {access_token}'
                                     }
                                     ).json()

            # checking if it is maintainer
            is_maintainer = False
            roles = user_data['person']['roles']
            for a in roles:
                if a['role'] == "Maintainer":
                    is_maintainer = True
            if not is_maintainer:
                return HttpResponseBadRequest("Only IMG members can use it", status=400)

            try:
                # enrollment = user_data['student']['enrolmentNumber']
                username = user_data['username']
                existing_user = User.objects.get(username=username)
                existing_user.year = user_data['student']['currentYear']
                existing_user.image = user_data['person']['displayPicture']
                existing_user.email = user_data['contactInformation']['instituteWebmailAddress']
                existing_user.save()
                print(existing_user)
                token = Token.objects.get(user=existing_user)
                print(token.key)
                print("existing")
            except User.DoesNotExist:
                new_user = User.objects.create(
                    username=user_data['username'],
                    password='grsgtrgfsrf',
                    name=user_data['person']['fullName'],
                    year=user_data['student']['currentYear'],
                    enrollment_no=user_data['student']['enrolmentNumber'],
                    email=user_data['contactInformation']['instituteWebmailAddress'],
                    image='https://channeli.in' +
                    user_data['person']['displayPicture'],
                )
                new_user.is_staff = True
                new_user.save()
                print(new_user)
                token = Token.objects.create(user=new_user)

            # return Response(new_user,token)

            return redirect(f'http://localhost:3000/oauth/jump/?token={token.key}')

        else:
            return HttpResponseBadRequest('Authorization code not found')


class Logout(APIView):
    def post(self, request):
        access_token = request.session['access_token']
        data = {
            'client_id': client_id,
            'client_secret': client_secret_key,
            'token': 'access_token',
            'token_type_hint': access_token
        }
        url = ' https://channeli.in/open_auth/revoke_token/'
        requests.post(url=url, data=data)
        return Response({'message': 'Logout successful'})


# https: // channeli. in /oauth/authorise /?client_id = vHvA7kB4GedavN5kSfWRIjvFg1geQQDkJss21yBv &redirect_uri = http: // 127.0.0.1: 8000/taskify/oauth/callback/&state = success
