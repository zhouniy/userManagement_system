from django.shortcuts import render, redirect
from web_management import models
from web_management.utils.form import PrettyModelForm
from web_management.utils.pagination import Pagination


def pretty_list(request):
    # for i in range(100):
    #     models.PrettyInfo.objects.create(mobile="18366666666", price=100, level=2, status=2)
    dict_list = {}
    search_data = request.GET.get("q","")
    if search_data:
        dict_list["mobile__contains"] = search_data
    queryset = models.PrettyInfo.objects.filter(**dict_list).order_by("-level")
    page_obj = Pagination(request, queryset)
    context = {
        "search": search_data,
        # 分页完成
        "queryset": page_obj.page_queryset,
        # 总页码
        "page_string": page_obj.get_page_html,
    }
    return render(request, 'pretty_list.html', context)


def pretty_add(request):
    if request.method == "GET":
        form = PrettyModelForm()
        return render(request, "pretty_add.html", {"form": form})
    form = PrettyModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/pretty/list/')
    return render(request, "pretty_add.html", {"form": form})


def pretty_delete(request, nid):
    models.PrettyInfo.objects.filter(id=nid).delete()
    return redirect('/pretty/list/')


def pretty_edit(request, nid):
    row = models.PrettyInfo.objects.filter(id=nid).first()
    if request.method == "GET":
        form = PrettyModelForm(instance=row)
        return render(request, "pretty_edit.html", {"form": form})
    form = PrettyModelForm(data=request.POST, instance=row)
    if form.is_valid():
        form.save()
        return redirect("/pretty/list/")
    return render(request, "pretty_edit.html", {"form": form})