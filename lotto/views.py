from django.shortcuts import redirect, render
import random


def home(request):
    return render(request, "home.html")


def challenge1(request):
    lotto_list = list()
    while len(lotto_list) < 7:
        i = random.randint(1, 45)
        if i not in lotto_list:
            lotto_list.append(i)
    lotto_list.sort()
    return render(request, "challenge1.html", {"lotto_list": lotto_list})


def challenge2(request):
    return render(request, "challenge2.html")


def challenge2_result(request):
    result = list()
    lotto_list = list()
    try:
        num = int(request.GET.get("num"))
        for _ in range(num):
            while len(lotto_list) < 7:
                i = random.randint(1, 45)
                if i not in lotto_list:
                    lotto_list.append(i)
            lotto_list.sort()
            result.append(lotto_list)
        return render(request, "result.html", {"result": result, "num": num})
    except ValueError:
        return redirect("lotto:challenge2")
