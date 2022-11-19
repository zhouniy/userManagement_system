import copy
from copy import deepcopy

from django.utils.safestring import mark_safe


class Pagination(object):
    def __init__(self, request, queryset, page_size=10, page_parm="page", plus=5):
        page = request.GET.get(page_parm, "1")
        if page.isdecimal():
            page = int(page)
        else:
            page = 1

        self.page = page
        self.page_size = page_size
        self.page_parm = page_parm
        self.plus = plus
        self.start = (page - 1) * page_size
        self.end = page * page_size
        self.page_queryset = queryset[self.start:self.end]
        # 数据总数
        total_count = queryset.count()
        # 总页码
        total_page_count, div = divmod(total_count, page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count

        # 处理拼接，跳转页码和搜索条件拼接
        queryset_dict = copy.deepcopy(request.GET)
        queryset_dict._mutable = True
        self.queryset_dict = queryset_dict

        # 获取页码，分页

    def get_page_html(self):
        # 总页码小于11时
        if self.total_page_count <= 2 * self.plus - 1:
            start = 1
            end = self.total_page_count
        else:
            # 当当前页码小于5
            if self.page < self.plus:
                start = 1
                end = 2 * self.plus + 1
            else:
                # 当当前页大于5时
                # 如果当前页+plus 大于总页码
                if (self.page + self.plus) > self.total_page_count:
                    start = self.total_page_count - 2 * self.plus
                    end = self.total_page_count
                else:
                    start = self.page - self.plus
                    end = self.page + self.plus

        # 存放页码的列表
        page_str_list = []
        # 首页
        self.queryset_dict.setlist(self.page_parm, [1])
        page_str_list.append('<li><a href="?{}">首页</a></li>'.format(self.queryset_dict.urlencode()))

        # 上一页
        if self.page > 1:
            self.queryset_dict.setlist(self.page_parm, [self.page - 1])
            prenv = '<li><a href="?{}">上一页</a></li>'.format(self.queryset_dict.urlencode())
        else:
            self.queryset_dict.setlist(self.page_parm, [1])
            prenv = '<li><a href="?{}">上一页</a></li>'.format(self.queryset_dict.urlencode())
        page_str_list.append(prenv)

        for i in range(start, end + 1):
            self.queryset_dict.setlist(self.page_parm, [i])
            if i == self.page:
                ele = "<li class='active'><a href='?{}'>{}</a></li>".format(self.queryset_dict.urlencode(), i)
            else:
                ele = "<li><a href='?{}'>{}</a></li>".format(self.queryset_dict.urlencode(), i)
            page_str_list.append(ele)

        # 下一页
        if self.page < self.total_page_count:
            self.queryset_dict.setlist(self.page_parm, [self.page + 1])
            prenv = '<li><a href="?{}">下一页</a></li>'.format(self.queryset_dict.urlencode())
        else:
            self.queryset_dict.setlist(self.page_parm, [self.total_page_count])
            prenv = '<li><a href="?{}">下一页</a></li>'.format(self.queryset_dict.urlencode())
        page_str_list.append(prenv)

        # 尾页
        self.queryset_dict.setlist(self.page_parm, [self.total_page_count])
        page_str_list.append('<li><a href="?{}">尾页</a></li>'.format(self.queryset_dict.urlencode()))

        search_string = """
                            <li>
                                <form style="float: left;margin-left: -1px" method="get">
                                    <input name="page"
                                           style="position: relative;float:left;display: inline-block;width: 80px;border-radius: 0;"
                                           type="text" class="form-control" placeholder="页码">
                                    <button style="border-radius: 0" class="btn btn-default" type="submit">跳转</button>
                                </form>
                            </li>
                            """
        page_str_list.append(search_string)
        page_string = mark_safe("".join(page_str_list))
        return page_string
