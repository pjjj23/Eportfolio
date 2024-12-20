from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpRequest
from django.contrib import messages
import hashlib
#from .firebase import auth_instance,db   
import time, threading
from django.utils import timezone
import random
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
#from .firebase import storage 
import uuid, math
import json
from django.views.decorators.csrf import csrf_exempt
import os, re
from uuid import uuid4
#import requests
from datetime import datetime, timedelta
import logging
from django.urls import reverse
from django.core.mail import EmailMessage
from django.utils.html import strip_tags
from django.views import View
from collections import Counter


def home(request):
    return render(request, 'index.html')