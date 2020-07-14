from django.shortcuts import render

def makeSport(request):
    # return HttpResponse('homepage')
    sportsList = Sports.objects.all()
    print(sportsList)
    return render(request, 'makeSport.html', {'nameOfOrg':nameOfOrg, 'sportsList':sportsList})

def makeSportMedium(request):
    #this method saves the advertisement information in the database
    advertisement = Advertisements(org = org, EarliestTime = earlyTime, LatestTime = lateTime,sport = sportsList, days = daysList, gender = gender, owner = owner, notes = notes)
    advertisement.save()
    # return HttpResponse('homepage')
    return redirect('organisation:organisationHome', nameOfOrg)
