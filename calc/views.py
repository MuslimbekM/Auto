from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase import firebase

auth=firebase.auth
cred = credentials.Certificate(r"C:\Users\user\PycharmProjects\djangoProject\autoproctoring-73cfe-firebase-adminsdk-yx9ny-24bee4b75b.json")
firebase_admin.initialize_app(cred)

db=firestore.client()

data = {
    'student_firstname' : 'Maqsud',
    'student_lastname' : 'Mardiyev'
}
doc_ref = db.collection('students').document(data['student_firstname'])
doc_ref.set(data)

def home(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def postSignup(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')

    user = User.objects.create_user(username, email, password)



