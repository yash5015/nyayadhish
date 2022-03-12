
from django.shortcuts import render, HttpResponseRedirect
from . models import case
from .forms import caseForm

from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def date_algo(assign, tempsize):
    gravity1 = case.objects.filter(gravity=1).values('case_No')
    gravity2 = case.objects.filter(gravity=2).values('case_No')
    gravity3 = case.objects.filter(gravity=3).values('case_No')
    working_dates = ['03January', '04January', '05January', '06January', '07January', '08January', '10January', '11January', '12January', '15January', '17January', '18January', '19January', '20January', '21January', '22January',  '24January', '25January', '27January', '28January', '29January', '31January', '01February', '02February', '03February', '04February', '05February',  '07February', '08February', '09February', '10February', '11February', '12February',  '14February', '15February', '16February', '17February', '18February', '19February', '21February', '22February', '23February', '24February', '25February', '26February',  '28February', '29February', '01March', '02March', '03March', '04March', '05March',  '07March', '08March', '09March', '10March', '11March', '12March', '14March', '15March', '16March', '21March', '22March', '23March', '24March', '25March', '26March', '28March', '29March', '30March', '31March', '01April', '02April', '04April', '05April', '06April', '07April', '08April', '09April', '11April', '12April', '13April', '16April', '18April', '19April', '20April', '21April', '22April', '23April', '25April', '26April', '27April', '28April', '29April', '30April', '02May', '04May', '05May', '06May', '07May', '09May', '10May', '11May', '12May', '13May', '14May', '17May', '18May', '19May', '20May', '21May', '11july', '12july', '13july', '14july', '15july', '16july', '18july', '19july', '20july', '21july', '22july', '23july', '25july', '26july', '27july', '28july', '29july',
                     '30july', '01August', '02August', '03August', '04August', '05August', '06August', '08August', '09August', '10August', '11August', '12August', '13August', '15August', '16August', '17August', '18August', '19August', '20August',  '22August', '23August', '24August', '25August', '26August', '27August', '29August', '30August', '01September', '02September', '03September', '05September', '06September', '07September', '08September', '09September', '10September', '12September', '13September', '14September', '15September', '16September', '17September', '19September', '20September', '21September', '22September', '23September', '24September', '26September', '27September', '28September', '29September', '30September', '01October', '10October', '11October', '12October', '13October', '14October', '15October', '17October', '18October', '19October', '20October', '21October', '22October', '31October', '01November', '02November', '03November', '04November', '05November',  '07November', '08November', '09November', '10November', '11November', '12November', '14November', '15November', '16November', '17November', '18November', '19November', '21November', '22November', '23November', '24November', '25November', '26November', '28November', '29November', '30November', '01December', '02December', '03December', '04December', '05December', '06December', '07December', '08December', '09December', '10December', '11December', '12December', '13December', '14December', '15December', '16December', '17December']
    if(assign % 2 == 0):
        tassign = assign/2

        if(tassign % 2 == 0):
            hard = tassign
            medium = tassign/2
            easy = medium

        else:
            hard = tassign+1
            medium = (assign-hard)/2
            easy = medium

    else:
        tassign = (assign+1)/2
        if(tassign % 2 == 0):
            hard = tassign+1
            medium = (assign-hard)/2
            easy = medium

        else:
            hard = tassign
            medium = (assign-hard)/2
            easy = medium

    if(tempsize > 66):
        tempsize = 66

    finalArray = [[0]*(assign+1) for i in range(tempsize)]

    h1 = 0
    hh1 = 0
    m1 = 0
    mm1 = 0
    ee1 = 0
    e1 = 0
    for i in range(0, tempsize):
        hh1 = hh1+hard
        mm1 = mm1+medium
        ee1 = ee1+easy
        for j in range(0, assign+1):
            if(j == 0):
                finalArray[i][j] = working_dates[i]
            else:
                if(h1 != hh1):
                    finalArray[i][j] = gravity1[h1]['case_No']
                    # print(gravity1[h1]['case_No'])
                    h1 += 1
                elif(m1 != mm1):
                    finalArray[i][j] = gravity2[m1]['case_No']
                    # gravity1[m1]['case_No']
                    m1 += 1
                elif(e1 != ee1):
                    finalArray[i][j] = gravity3[e1]['case_No']
                    # gravity1[e1]['case_No']
                    e1 += 1

    dictt = {}
    for i in range(0, tempsize):
        dictt_list = []
        for j in range(1, assign+1):
            dictt_list.append(finalArray[i][j])
        dictt[finalArray[i][0]] = dictt_list
    # print(dictt)
    final_dictt = {}
    for key, values in dictt.items():
        final_dictt_list = []

        for i in values:
            final_dictt_list.append(
                list(case.objects.filter(case_No=i).values()))
        final_dictt[key] = final_dictt_list

    return final_dictt
# date_algo(2, 5)


def gravity_assign(section):
    grading = 0
    section_list = section.split(",")
    ans = 0
    for i in section_list:
        if(int(i) >= 299 and int(i) <= 377):
            ans = 3
        elif(int(i) >= 53 and int(i) <= 298):
            ans = 2
        elif(int(i) >= 490 and int(i) <= 511):
            ans = 1
        grading = max(grading, ans)
    return 4-grading


def home(request):
    # return render(request, 'index.html')
    return render(request, 'index.html')


def admin(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = caseForm(request.POST)
            if fm.is_valid():
                nameofplaintiff = fm.cleaned_data['Name_of_plaintiff_party']
                nameofdefendant = fm.cleaned_data['Name_of_defendant']
                emailofplaintiff = fm.cleaned_data['Email_of_plaintiff']
                emailofdefedant = fm.cleaned_data['Email_of_defendant']
                phonenoofplaintiff = fm.cleaned_data['Phone_No_of_plaintiff']
                phonenoofdefendant = fm.cleaned_data['Phone_No_of_defendant']
                addressofplaintiff = fm.cleaned_data['Address_of_plaintiff']
                addressofdefendant = fm.cleaned_data['Address_of_defendant']
                section = fm.cleaned_data['section']
                chartsheetdate = fm.cleaned_data['chart_sheet_filling_date']
                caseno = fm.cleaned_data['case_No']
                casetype = fm.cleaned_data['case_type']
                casest = fm.cleaned_data['case_statement']
                last_hearing_date = fm.cleaned_data['last_hearing_date']
                local_gravity = gravity_assign(section)
                reg = case(Name_of_plaintiff_party=nameofplaintiff, Name_of_defendant=nameofdefendant, Email_of_plaintiff=emailofplaintiff, Email_of_defendant=emailofdefedant, Phone_No_of_plaintiff=phonenoofplaintiff, Phone_No_of_defendant=phonenoofdefendant,
                           Address_of_plaintiff=addressofplaintiff, Address_of_defendant=addressofdefendant, section=section, chart_sheet_filling_date=chartsheetdate, case_No=caseno, case_type=casetype, case_statement=casest, last_hearing_date=last_hearing_date, gravity=local_gravity)
                reg.save()
                fm = caseForm()
        else:
            fm = caseForm()
        stud = case.objects.all()
        return render(request, 'admin.html', {'form': fm})
    else:
        return HttpResponseRedirect('/')


def service(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            assign = request.POST['assign']
            tempsize = request.POST['tempsize']
            dictt = date_algo(int(assign), int(tempsize))
            return render(request, 'assign_dates.html', {"dictt": dictt})
        else:
            return render(request, 'service.html')
    else:
        return HttpResponseRedirect('/')


def view_service(request, id):
    # serv = case.objects.get(id=id)
    serv = case.objects.get(pk=id)
    fm = caseForm(instance=serv)
    return render(request, 'view_service.html', {'form': fm})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']

                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Login Successfully ")
                    return HttpResponseRedirect('/')
                return render(request, 'login.html')

        else:
            fm = AuthenticationForm()
        return render(request, 'login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
