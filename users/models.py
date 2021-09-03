from django.contrib.auth.models import AbstractBaseUser, Group, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import reverse
from .managers import CustomUserManager


# Custom user model which use auth but we have email instead of username.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False, verbose_name='کارمند')
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت‌نام")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def __str__(self):
        return self.email


# class Customer(CustomUser):
#     class Meta:
#         proxy = True
#         verbose_name = 'مشتری'
#         verbose_name_plural = "مشتری‌ها"
#
#
# class Staff(CustomUser):
#     class Meta:
#         proxy = True
#         # permissions = (
#         #     ("can_add_book",),
#         #     ("can_change_book",),
#         #     ("can_delete_book",),
#         #     ("can_view_book",))
#         verbose_name = 'کارمند'
#         verbose_name_plural = "کارمند‌ها"
#
#
# class Admin(CustomUser):
#     class Meta:
#         proxy = True
#         verbose_name = "ادمین"
#         verbose_name_plural = "ادمین‌ها"

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, null=True, on_delete=models.CASCADE, verbose_name="کاربر")
    name = models.CharField(max_length=200, null=True, verbose_name="نام")
    phone = models.CharField(max_length=15, null=True, verbose_name="تلفن")
    profile_pic = models.ImageField(upload_to='profile_pics/', default="covers/blank_user.jpg", blank=False, null=True,
                                    verbose_name="عکس")

    class Meta:
        verbose_name = "پروفایل"
        verbose_name_plural = "پروفایل‌ها"

    def __str__(self):
        return self.user.email

    def get_absolute_url(self):
        return reverse('profile_update', args=[str(self.id)])

    # For admin site to be able to display book images.
    def admin_image_display(self):
        return mark_safe(f'<img src="{self.profile.url}" width="{90}" height={125} />')

    @receiver(post_save, sender=CustomUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=CustomUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


# Each user should have at least on address.
class Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    zip_code = models.IntegerField()
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = "آدرس"
        verbose_name_plural = "آدرس‌ها"
