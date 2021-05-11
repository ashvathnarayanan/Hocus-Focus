import xlwt
from app.models import *
from django.shortcuts import render
from django.http import HttpResponse

def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="attendance.xls"'
 
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Attendance')
 
    row_num = 0
 
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
 
    columns = ['RegNo', 'Score']
 
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
 
    font_style = xlwt.XFStyle()
 
    rows = Student.objects.all().values_list('regno','score')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
 
    wb.save(response)
    return response

def teacher(request):
	if request.method=="POST":
		return export_users_xls(request)
	return render(request,'teacher.html')

def student(request):
    if request.method=="POST":
        question=Question.objects.get(number=request.POST["qno"],course=request.POST["course"])
        if question.answer==request.POST["chosenoption"]:
            student=Student.objects.all()[0]
            student.score+=1
            student.save()
            return HttpResponse(student.score)
        return HttpResponse("wrong")
    student=Student.objects.all()[0]
    return render(request,'student.html',{"student":student})

def startdn(request):
    trigger=Trigger(name=request.POST["course"],lang=request.POST["lang"])
    trigger.save()
    return HttpResponse("Started DistracNot")

def stopdn(request):
    trigger=Trigger.objects.get(name=request.POST["course"])
    trigger.delete()
    return HttpResponse("Stopped DistracNot")
