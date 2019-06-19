from django.shortcuts import render


def test_exception(request):
    # x = 1 + "1"
    print(request.myuser)
    username = request.session.get("username", "游客")
    return render(request, "middleware/home.html", context={"name": username})
