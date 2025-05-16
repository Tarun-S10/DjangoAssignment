from django.shortcuts import render

# Dictionary with daily tasks
tasks = {
    'sunday': "Plan the week ahead.",
    'monday': "Prepare for meetings.",
    'tuesday': "Grocery shopping.",
    'wednesday': "Workout session.",
    'thursday': "Check team reports.",
    'friday': "Family movie night.",
    'saturday': "Gardening and relaxation."
}

def index(request):
    return render(request, 'index.html', {'days': tasks.keys()})

def day_view(request, day):
    task = tasks.get(day.lower(), "No task available for this day.")
    return render(request, 'days.html', {'day': day.capitalize(), 'task': task})
