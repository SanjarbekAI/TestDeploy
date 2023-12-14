from django.urls import path

from pages.views import *

app_name = "pages"

urlpatterns = [
    path("products/", products_page_view, name="products"),
    path("blogs/", blog_page_view, name="blogs"),
    path("contact/", contact_page_view, name="contact"),
    path("about/", about_page_view, name="about"),
    path("", home_page_view, name="home"),
]