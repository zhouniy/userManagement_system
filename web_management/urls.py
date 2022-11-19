from django.urls import path


from .views import depart, user, pretty, admin, logininfo

urlpatterns = [
    # 部门管理
    path('depart/list/', depart.depart_list),
    path('depart/add/', depart.depart_add),
    path('depart/<int:nid>/delete/', depart.depart_delete),
    path('depart/<int:nid>/edit/', depart.depart_edit),


    # 用户管理
    path('user/list/', user.user_list),
    path('user/add/', user.user_add),
    path('user/<int:nid>/delete/', user.user_delete),
    path('user/<int:nid>/edit/', user.user_edit),

    # 靓号管理
    path('pretty/list/', pretty.pretty_list),
    path('pretty/add/', pretty.pretty_add),
    path('pretty/<int:nid>/delete/', pretty.pretty_delete),
    path('pretty/<int:nid>/edit/', pretty.pretty_edit),


    # 管理员管理
    path('admin/list/', admin.admin_list),
    path('admin/add/', admin.admin_add),
    path('admin/<int:nid>/edit/', admin.admin_edit),
    path('admin/<int:nid>/delete/', admin.admin_delete),
    path('admin/<int:nid>/reset/', admin.admin_reset),

    # 登录
    path('login/', logininfo.login),
    path('logout/', logininfo.logout),
    path('image/code/', logininfo.image_code),
]