from django.contrib.auth.decorators import permission_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Videos, UserAccount
from rest_framework.viewsets import ModelViewSet
from .serializers import VideoSerializer, UserAccountSerializer
from django.db.models import Q, F
from django.core.files import File

from .storages import loadTo


class VideosViewSet(ModelViewSet):
    serializer_class = VideoSerializer

    def get_queryset(self):
        if 'neid' in self.request.query_params.keys():
            idd = int(self.request.query_params.get('neid'))

            return Videos.objects.filter(~Q(pk=idd))

        if 'id' in self.request.query_params.keys():
            idd = int(self.request.query_params.get('id'))
            Videos.objects.filter(pk=idd).update(views=F('views') + 1)

            return Videos.objects.filter(pk=idd)

        if 'from' in self.request.query_params.keys() and 'to' in self.request.query_params.keys():
            fromm = int(self.request.query_params.get('from'))
            to = int(self.request.query_params.get('to'))

            return Videos.objects.filter(Q(pk__gte=fromm) & Q(pk__lte=to))

        amount = 0
        if 'amount' in self.request.query_params.keys():
            amount = int(self.request.query_params.get('amount'))

        amount = min(Videos.objects.count(), amount)

        return Videos.objects.all()[:amount]

class FindVideoSet(ModelViewSet):
    serializer_class = VideoSerializer

    def get_queryset(self):
        if 'find' in self.request.query_params.keys():
            compare_string = str(self.request.query_params.get('find'))
            videos = Videos.objects.filter(name__contains=compare_string)

            if 'amount' in self.request.query_params.keys():
                amount = int(self.request.query_params.get('amount'))
                if amount < len(videos):
                    videos = videos[:amount]

            return videos

class UserInfoAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user_id = request.user.id

        if 'getme' in request.GET.keys():
            user_data = UserAccount.objects.filter(account_id=user_id)
            if user_data.count() == 0:
                UserAccount.objects.create(account_id=user_id, nickname=request.user.username)

                return Response(UserAccountSerializer(UserAccount.objects.filter(account_id=user_id), many=True).data)
            else:

                return Response(UserAccountSerializer(user_data, many=True).data)

        if 'getuservideo' in request.GET.keys():
            return Response(VideoSerializer(Videos.objects.filter(owner_id=user_id), many=True).data)

    def post(self, request):
        user_id = request.user.id
        folder = '/images'

        if 'nickname' in request.data.keys():
            UserAccount.objects.filter(account_id=user_id).update(nickname=request.data['nickname'])

        if 'description' in request.data.keys():
            UserAccount.objects.filter(account_id=user_id).update(description=request.data['description'])

        if 'avatar' in request.data.keys():
            name = request.data['avatar']
            file = File(request.FILES['avatar'])
            urll = loadTo(name, file, folder)

            UserAccount.objects.filter(account_id=user_id).update(avatar=urll)

        if 'header' in request.data.keys():
            name = request.data['header']
            file = File(request.FILES['header'])
            urll = loadTo(name, file, folder)

            UserAccount.objects.filter(account_id=user_id).update(header=urll)

        return Response({'detail': 'success'})

class VideoAddAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user_id = request.user.id
        folder = '/images'

        if UserAccount.objects.filter(account_id=user_id).count() == 0:
            UserAccount.objects.create(account_id=user_id, nickname=request.user.username)

        if 'name' in request.data.keys() and 'preview' in request.data.keys() and 'video' in request.data.keys():
            name = request.data['name']
            preview_name = request.data['preview']
            preview = request.FILES['preview']
            video_name = request.data['video']
            video = request.FILES['video']
            preview_url = loadTo(preview_name, preview, folder)
            video_url = loadTo(video_name, video, folder)

            avatar = UserAccount.objects.filter(account_id=user_id)[0].avatar
            author_name = UserAccount.objects.filter(account_id=user_id)[0].nickname

            if 'description' in request.data.keys():
                Videos.objects.create(name=name, preview=preview_url, video=video_url,
                                      owner_id=user_id,  description=request.data['description'],
                                      avatar=avatar, author_name=author_name)
            else:
                Videos.objects.create(name=name, preview=preview_url, video=video_url,
                                      owner_id=user_id, description='',
                                      avatar=avatar, author_name=author_name)

        return Response({'detail': 'success'})


