from django.shortcuts import redirect, render, resolve_url
from django.http import HttpResponse
from calendar import HTMLCalendar, month
from django.utils.html import mark_safe
import datetime
from schedule.models import task

# Create your views here.
def top(request):
    """html_cal = HTMLCalendar()

    now = datetime.datetime.now()
    year = now.year
    month = now.month

    l = []

    for i in range(0, 12):
        if month + i != 12:
            tuki = (month + i) % 12
        
        else:
            tuki = 12
        
        if tuki == 1:
            year += 1

        l.append(mark_safe(html_cal.formatmonth(year, tuki)))

    result = {
        "test": l
    }"""

    now = datetime.datetime.now()
    year_now = now.year
    month_now = now.month

    year = []
    for i2 in range(0, 12):
        if month_now + i2 != 12:
            tuki = (month_now + i2) % 12
        
        else:
            tuki = 12
        
        if tuki == 1:
            year_now += 1


        l = []
        for a in range(1 , 32):
            try:
                date = datetime.date(year_now, tuki, a)
                l.append(date.strftime("%A"))

            except:
                break

        #print(len(l))
        
        month = []
        week = []
        for i, day in enumerate(l):

            if i == 0:
                n = 0
                if day == "Monday":
                    n = 1
                
                elif day == "Tuesday":
                    n = 2
                
                elif day == "Wednesday":
                    n = 3
                
                elif day == "Thursday":
                    n = 4
                
                elif day == "Friday":
                    n = 5
                
                elif day == "Saturday":
                    n = 6
                
                for _ in range(0, n):
                    week.insert(0, "")
                
                #print(week)
            
            if len(week) == 7:
                month.append(week)
                week = []
            
            week.append(i + 1)

            if i + 1 == len(l):
                for ___ in range(0, 7 - len(week)):
                    week.append("")
                month.append(week)
        
        year.append({"year_number": year_now, "month_number": tuki, "month":month})

    result = {
        "year":year,
    }

    year_now = now.year
    month_now = now.month
    day_now = now.day
    time_now = now.hour

    retu = int("{}{}{}{}".format(year_now, str(month_now).zfill(2), str(day_now).zfill(2), str(time_now).zfill(2)))
    try:
        task_id = task.objects.filter(conect__gte = retu).order_by("conect")[0]
        result["task"] = task_id
    
    except:
        pass

    return render(request, "test.html", result)

def tasks(request, year, month, day):
    tasks = task.objects.filter(year = year, month = month, day = day).order_by("time")

    
    result = {
        "tasks":tasks,
        "year": year,
        "month": month,
        "day": day,
    }
    return render(request, "task.html", result)

def edit(request, year, month, day, id):
    task_id = task.objects.get(id = id)
    if request.method == "POST":
        task_id.content = request.POST["content"]
        task_id.time = request.POST["time"]
        task_id.conect = int("{}{}{}{}".format(year, str(month).zfill(2), str(day).zfill(2), str(request.POST["time"]).zfill(2)))
        task_id.save()
        return redirect("/{}/{}/{}".format(year,month,day))

    else:
        result = {
            "task": task_id,
            "year": year,
            "month": month,
            "day": day,
            "id": id,
        }
        return render(request, "edit.html", result)

def create(request):
    if request.method == "POST":
        task_id = task(conect = int("{}{}{}{}".format(request.POST["year"], str(request.POST["month"]).zfill(2), str(request.POST["day"]).zfill(2), str(request.POST["time"]).zfill(2))), year = request.POST["year"], month = request.POST["month"], day = request.POST["day"], time = request.POST["time"], content = request.POST["content"])
        task_id.save()
        return redirect("/{}/{}/{}".format(request.POST["year"], request.POST["month"], request.POST["day"]))
    
    else:
        HttpResponse("ERROR")

def delete(request, year, month, day, id):
    task_id = task.objects.get(id = id)
    task_id.delete()
    return redirect("/{}/{}/{}".format(year,month,day))