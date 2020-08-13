from django.shortcuts import render
from django.http import JsonResponse
import datetime
from django.core import serializers

from .models import User

# Create your views here.
def index(request):
    users = User.objects.all()
    # import pdb;pdb.set_trace()
    response = {"ok": True}
    memberDetails = []
    for user in users:
        member = {
            'id': user.user_id,
            'real_name': user.real_name,
            'tz': user.time_zone,
            'activity_periods': []
        }
        for activity in user.activity_set.all():
            member['activity_periods'].append({'start_time': stringinfy_date(activity.startTime),
                                               'end_time': stringinfy_date(activity.endTime)})

        memberDetails.append(member)
    response['members'] = memberDetails
    return JsonResponse(response)

def stringinfy_date(date) :
    return date.strftime("%b-%d-%y %-I:%-M%p")