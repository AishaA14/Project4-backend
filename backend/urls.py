"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from main_app import views
from main_app.views import HabitListCreateView, HabitDetailView


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
# router.register(r'tag', views.TagViewSet)
router.register(r'goal', views.GoalViewSet)
router.register(r'task', views.TaskViewSet)
# router.register(r'habit', views.HabitsForGoalViewSet)
# router.register(r'completedgoal', views.CompletedGoalViewSet)
router.register(r'completedhabit', views.CompletedHabitViewSet)
# router.register(r'completedhabit', views.CompletedHabitViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('home/', views.HomeView.as_view(), name ='home'),
    path('logout/', views.LogoutView.as_view(), name ='logout'),

    path('goal/<int:pk>/', views.GoalViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='goal_detail'),
    path('goal/create/', views.GoalCreate.as_view(), name='goal_create'),

    path('task/<int:pk>/', views.TaskViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='task_detail'),
    path('task/create/', views.TaskCreate.as_view(), name='task_create'),


    # path('goals/<int:goal_pk>/habits/', views.HabitsForGoalViewSet.as_view(), name='habits-for-goal'),
    # path('habit/goal/<int:pk>/', views.HabitViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='habit_detail'),
    #  path('habit/create/goal/<int:pk>/', views.HabitCreate.as_view(), name='habit_create'),
    # path('habits/<int:goal_pk>/', views.HabitListView.as_view(), name='habit_list'),

    path('habits/<int:goal_id>/', HabitListCreateView.as_view(), name='habit-list-create'),
    # for listing and creating habits
    path('habits/<int:pk>/', HabitDetailView.as_view(), name='habit-detail'),
    # for retrieving, updating and deleting a specific habit

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]