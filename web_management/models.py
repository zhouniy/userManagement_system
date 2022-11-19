from django.db import models


class Admin(models.Model):
    username = models.CharField(verbose_name="管理员账户", max_length=32)
    password = models.CharField(verbose_name="管理员密码", max_length=64)


class Department(models.Model):
    title = models.CharField(verbose_name="部门", max_length=16)

    def __str__(self):
        return self.title


class Userinfo(models.Model):
    username = models.CharField(verbose_name="名字",max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="用户余额", max_digits=10, decimal_places=2, default=0)
    create_time = models.DateField(verbose_name="创建时间")
    depart = models.ForeignKey(verbose_name="部门", to="Department", to_field='id', on_delete=models.CASCADE)
    gender_choices = {
        (1, "男"),
        (2, "女"),
    }
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)


class PrettyInfo(models.Model):
    mobile = models.CharField(verbose_name="手机号",max_length=11)
    price = models.IntegerField(verbose_name="价格")
    level_choices = {
        (1, "1级"),
        (2, "2级"),
        (3, "3级"),
        (4, "4级"),
    }
    level = models.SmallIntegerField(verbose_name="级别", choices=level_choices, default=1)
    status_choices = {
        (1, "已占用"),
        (2, "未占用"),
    }
    status = models.SmallIntegerField(verbose_name="当前状态", choices=status_choices, default=2)