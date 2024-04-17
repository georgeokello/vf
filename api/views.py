from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from baseApp.models import FundiUser, Topic, Session, Activity, TextActivity, VideoActivity, Feedback
from . serializer import UserSerializer, TopicSerializer, SessionSerializer, ActivitySerializer, TextActivitySerializer, VideoActivitySerializer, FeedbackSerializer
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import login_required


# Topic endpoints
@api_view(['GET'])
# @permission_classes([IsAuthenticated])  # Requires authentication
def viewTopic(request):
    topics = Topic.objects.all()
    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data)


# Topic endpoints
@api_view(['GET'])
# @permission_classes([IsAuthenticated])  # Requires authentication
def viewSecTopics(request):
    topics = Topic.objects.filter(cat='secondary')
    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data)

# Topic endpoints
@api_view(['GET'])
# @permission_classes([IsAuthenticated])  # Requires authentication
def viewPriTopics(request):
    topics = Topic.objects.filter(cat='primary')
    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addTopic(request):
    serializer = TopicSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def getTopic(request, id):
    try:
        topic = Topic.objects.get(pk=id)
    except Topic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TopicSerializer(topic)
        return Response(serializer.data)


@api_view(['PUT'])
def updateTopic(request, id):
    try:
        topic = Topic.objects.get(pk=id)
    except Topic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        serializer = TopicSerializer(topic)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteTopic(request, id):
    try:
        tool = Topic.objects.get(pk=id)
    except Topic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    tool.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Session endpoints
@api_view(['POST'])
def addSession(request):
    serializer = SessionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def viewSessions(request, pk):
    try:
        sessions = Session.objects.filter(topic_id=pk)
    except Session.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def getSession(request, id):
    try:
        session = Session.objects.get(pk=id)
    except Session.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SessionSerializer(session)
        return Response(serializer.data)


@api_view(['PUT'])
def updateSession(request, id):
    try:
        session = Topic.objects.get(pk=id)
    except Topic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        serializer = TopicSerializer(session)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteSession(request, id):
    try:
        session = Session.objects.get(pk=id)
    except Session.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    session.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# Activity endpoints
@api_view(['POST'])
def addActivity(request):
    serializer = ActivitySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def getActivity(request, id):
    try:
        activity = Activity.objects.get(pk=id)
    except Activity.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ActivitySerializer(activity)
        return Response(serializer.data)


@api_view(['GET'])
def viewActivities(request, pk):
    try:
        activities = Activity.objects.filter(session_id=pk).select_related('session__topic')
    except Activity.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)


@api_view(['PUT'])
def updateActivity(request, id):
    try:
        activity = Activity.objects.get(pk=id)
    except Activity.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        serializer = ActivitySerializer(activity)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteActivity(request, id):
    try:
        activity = Activity.objects.get(pk=id)
    except Activity.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    activity.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# text activity endpoint
@api_view(['POST'])
def addTextActivity(request):
    if request.method == 'POST':
        serializer = TextActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def deleteTextActivity(request, id):
    pass

def updateTextActivity(request, id):
    pass


@api_view(['GET'])
def viewTextActivities(request, pk):
    try:
        textActivities = TextActivity.objects.filter(activity_id=pk)
    except TextActivity.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TextActivitySerializer(textActivities, many=True)
        return Response(serializer.data)


# video activity endpoints
@api_view(['GET'])
def viewVideoActivities(request, pk):
    try:
        videoActivities = VideoActivity.objects.filter(activity_id=pk)
    except VideoActivity.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VideoActivitySerializer(videoActivities, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def addVideoActivity(request):
    if request.method == 'POST':
        serializer = VideoActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def deleteVideoActivity(request, pk):
    pass

def updateVideoActivity(request, pk):
    pass


@api_view(['POST'])
def login(request):

    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = None
        if '@' in username:
            try:
                user = FundiUser.objects.get(email=username)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):

    if request.method == 'POST':
        try:
            # Delete the user's token to logout
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# feedback endpoints
 
@api_view(['POST'])
def addFeedback(request):
     if request.method == 'POST':
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# video activity endpoints
@api_view(['GET'])
def viewFeedback(request):
    try:
        teacher_feedback = Feedback.objects.all()
    except Feedback.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FeedbackSerializer(teacher_feedback, many=True)
        return Response(serializer.data)