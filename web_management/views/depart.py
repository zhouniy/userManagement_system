from django.shortcuts import render, redirect
from web_management import models
from web_management.utils.pagination import Pagination


def depart_list(request):
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["title__contains"] = search_data
    queryset = models.Department.objects.filter(**data_dict)
    page_obj = Pagination(request, queryset)
    context = {
        "queryset": page_obj.page_queryset,
        "page_string": page_obj.get_page_html,
        "search_data": search_data,
    }
    return render(request, 'depart_list.html', context)


def depart_add(request):
    if request.method == "GET":
        return render(request, 'depart_add.html')
    title = request.POST.get('title')
    models.Department.objects.create(title=title)
    return redirect('/depart/list/')


def depart_delete(request, nid):
    models.Department.objects.filter(id=nid).delete()
    # return render(request, 'depart_list.html')
    return redirect('/depart/list/')


def depart_edit(request, nid):
    if request.method == "GET":
        queryset = models.Department.objects.filter(id=nid).first()
        return render(request, 'depart_edit.html', {"queryset": queryset})
    title = request.POST.get('title')
    models.Department.objects.filter(title=title).update(title)
    return redirect('/depart/list/')