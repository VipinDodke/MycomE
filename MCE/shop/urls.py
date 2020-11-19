from django.urls import path
from.import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="aboutUS"),
    path("contact/", views.contact, name="contactUs"),
    path("tracker/", views.tracker, name="trackingstatus"),
path("prodview/<int:myid>", views.prodview, name="ProdView"),
    path("chackout/", views.chackout, name="chackout"),
    path("search/", views.search, name="Search"),

]
