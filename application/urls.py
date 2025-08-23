from os import path

from application import admin, views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.Home, name="Home"),
    path("product/", views.product, name="product"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("signout/", views.signout, name="signout"),
    path("order_windows/", views.order_windows, name="order_windows"),
    path("UserDashboard/", views.UserDashboard, name="UserDashboard"),
    path("AdminDashboard/", views.AdminDashboard, name="AdminDashboard"),
    path("confirm_order/", views.confirm_order, name="confirm_order"),
    path("pay/<int:order_id>/", views.payment_page, name="payment_page"),
    path("process-payment/<int:order_id>/", views.process_payment, name="process_payment"),
]
