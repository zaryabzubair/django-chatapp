from django.shortcuts import render

def index(request, group_name):
    print('Group Name: ', group_name)
    return render(request, 'index.html', {'groupname': group_name})
