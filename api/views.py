from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from baseApp.models import FundiUser, Topic, Session, Activity, Feedback, Teachers, Profile
from baseApp.models import Theme, Sub_Theme, Chapters
from . serializer import UserSerializer, TopicSerializer, SessionSerializer, ActivitySerializer, FeedbackSerializer, TeacherSerializer
from . serializer import ThemeSerializer, SubThemeSerializer, ChapterSerialzer, ProfileSerializer
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


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
    topics = Topic.objects.filter(cat='Secondary')
    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data)

# Topic endpoints
@api_view(['GET'])
# @permission_classes([IsAuthenticated])  # Requires authentication
def viewPriTopics(request):
    topics = Topic.objects.filter(cat='Primary')
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
    
    if request.method == 'PUT':
        serializer = TopicSerializer(topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        session = Session.objects.get(pk=id)
    except Session.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = SessionSerializer(session, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
    if request.method == 'PUT':
        serializer = ActivitySerializer(activity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteActivity(request, id):
    try:
        activity = Activity.objects.get(pk=id)
    except Activity.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    activity.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


def upload_activity(request):
    if request.method == 'POST':
        media_type = request.POST.get('mediaType')

        if media_type == 'text':
            
            # Process text content (e.g., save to database)
            serializer = ActivitySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        
        elif media_type == 'image':

            serializer = ActivitySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        
        elif media_type == 'video':
            
            serializer = ActivitySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)

    return Response({'error': 'Invalid request method'})


def deleteVideoActivity(request, pk):
    pass

def updateVideoActivity(request, pk):
    pass


@api_view(['GET'])
def getProfile(request):
    # check if user is authenticate 
    if not request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
    


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


# Teachers endpoint
# add teacher
@api_view(['POST'])
def add_teacher(request):
    if request.method == "POST":
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

# views teachers 
@api_view(['GET'])
def view_teachers(request):
    teachers = Teachers.objects.all()
    serializer = TeacherSerializer(teachers, many=True)
    return Response(serializer.data)    


# update teachers
@api_view(['PUT'])
def update_teacher(request, id):
    try:
        teacher = Teachers.objects.get(pk=id)
    except Teachers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
# delete teachers
@api_view(['DELETE'])
def delete_teacher(request, id):
    try:
        teacher = Teachers.objects.get(pk=id)
    except Teachers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    teacher.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# DEAR day
# theme
@api_view(['GET'])
# @permission_classes([IsAuthenticated])  # Requires authentication
def viewTheme(request):
    themes = Theme.objects.all()
    serializer = ThemeSerializer(themes, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addTheme(request):
    serializer = ThemeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def getTheme(request, id):
    try:
        theme = Theme.objects.get(pk=id)
    except Theme.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ThemeSerializer(theme)
        return Response(serializer.data)


@api_view(['PUT'])
def updateTheme(request, id):
    try:
        theme = Theme.objects.get(pk=id)
    except Theme.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = ThemeSerializer(theme, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteTheme(request, id):
    try:
        theme = Theme.objects.get(pk=id)
    except Theme.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    theme.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Sub theme
@api_view(['POST'])
def addSubTheme(request):
    serializer = SubThemeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def viewSubTheme(request, pk):
    try:
        sub_theme = Sub_Theme.objects.filter(theme_id=pk)
    except Sub_Theme.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SubThemeSerializer(sub_theme, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def getSubTheme(request, id):
    try:
        sub_theme = Sub_Theme.objects.get(pk=id)
    except Sub_Theme.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SubThemeSerializer(sub_theme)
        return Response(serializer.data)


@api_view(['PUT'])
def updateSubTheme(request, id):
    try:
        sub_theme = Sub_Theme.objects.get(pk=id)
    except Sub_Theme.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = SubThemeSerializer(sub_theme, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteSubTheme(request, id):
    try:
        sub_theme = Sub_Theme.objects.get(pk=id)
    except Sub_Theme.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    sub_theme.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# Chapter endpoints
@api_view(['POST'])
def addChapter(request):
    serializer = ChapterSerialzer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def getChapter(request, id):
    try:
        chapter = Chapters.objects.get(pk=id)
    except Chapters.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ChapterSerialzer(chapter)
        return Response(serializer.data)


@api_view(['GET'])
def viewChapters(request, pk):
    try:
        chapters = Chapters.objects.filter(sub_theme_id=pk).select_related('sub_theme__theme')
    except Chapters.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ChapterSerialzer(chapters, many=True)
        return Response(serializer.data)


@api_view(['PUT'])
def updateChapter(request, id):
    try:
        chapter = Chapters.objects.get(pk=id)
    except Chapters.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = ChapterSerialzer(chapter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteChapter(request, id):
    try:
        chapters = Chapters.objects.get(pk=id)
    except Chapters.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    chapters.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
