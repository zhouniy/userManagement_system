from django.shortcuts import render, redirect
from web_management import models
from web_management.utils.form import UserModelForm
from web_management.utils.pagination import Pagination


def user_list(request):
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["username__contains"] = search_data
    queryset = models.Userinfo.objects.filter(**data_dict)
    page_obj = Pagination(request, queryset)
    context = {
        "queryset": page_obj.page_queryset,
        "page_string": page_obj.get_page_html,
        "search_data": search_data,
    }
    return render(request, 'user_list.html', context)


def user_add(request):
    if request.method == "GET":
        form = UserModelForm()
        return render(request, 'user_add.html', {"form": form})
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    return render(request, 'user_add.html', {"form": form})


def user_delete(request, nid):
    models.Userinfo.objects.filter(id=nid).delete()
    return redirect("/user/list/")


def user_edit(request, nid):
    row = models.Userinfo.objects.filter(id=nid).first()
    if request.method == "GET":
        form = UserModelForm(instance=row)
        return render(request, 'user_edit.html', {"form": form})
    form = UserModelForm(data=request.POST, instance=row)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    return render(request, 'user_edit.html', {"form": form})