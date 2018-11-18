from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, StreamingHttpResponse
from django.forms import Form
from .forms import DeplymentForm
from django.views.decorators.http import condition
import sys, os , time
from subprocess import Popen, PIPE




# Create your views here.


#def stream_response(request):
#    return StreamingHttpResponse(stream_response_generator())

def stream_response_generator(domain,project,warName):

    result = []
    #yield "<div>"+project + " " + warName + " starting deployment on " + domain+"</div>"
    yield '<!DOCTYPE html>                                                                                                   '\
'<html lang="en">                                                                                                  '\
'<head>                                                                                                            '\
'  <title>Bootstrap Example</title>                                                                                '\
'  <meta charset="utf-8">                                                                                          '\
'  <meta name="viewport" content="width=device-width, initial-scale=1">                                            '\
'  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">            '\
'  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>                        '\
'  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>                     '\
'</head>                                                                                                           '\
'<body >' \
'<div class="panel panel-info"><div class="panel-heading"><center>Logs of the deployment script</center></div>' \
'<div style="background-color:black" class="panel-body">'
    process = Popen("ping -n 10 google.com",
                               shell=True,
                               stdout=PIPE,
                               stderr=PIPE)
    for res in process.stdout:

        yield '<font color="white"><div>%s</div></font>'  % res

    yield '</br></br>'
    yield '</div></div>'  + project + " " + warName + " deployed suscessfully on " + domain + ' <a href="">Deployment Page</a>'

    errcode = process.returncode



    if errcode is not None:
        raise Exception('cmd %s failed, see above for details', "ping" )
#    for x in range(1,11):
#        yield "%s\n" % x  # Returns a chunk of the response to the browser
#        time.sleep(1)

def index(request):
    released = {}

    if request.method =='POST' :
        form = DeplymentForm(request.POST)

        if form.is_valid():

            domain=form.cleaned_data['domain']
            project=form.cleaned_data['project']
            warName=form.cleaned_data['warName']

            return StreamingHttpResponse(stream_response_generator(domain,project,warName))

    form = DeplymentForm()
    return render(request,'index.html',dict(form=form))

