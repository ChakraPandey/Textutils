# I have created a new file - chakra
from django.http import HttpResponse
from django.shortcuts import render

# Code for video no.6
# def index(request):
#     return HttpResponse(''' <h1> hello <h1> <a href="https://www.youtube.com/watch?v=WCTr    
#         o3qabjE&list=RDDS-raAyMxl4&index=4&ab_channel=T-Series"> Pee loon </a>''')      # link inserted using anchor tag

# def about(request):
#     return HttpResponse("bye")

# def chakra(request):
#     return HttpResponse("<h1>pandey</h1>")

# Code for video no.7
def index(request):
   
    return render(request, 'index.html')

# def index(request):
#     return HttpResponse('''   Home <br>
#                         <a href="http://127.0.0.1:8000/capitalizefirst"> capitalizefirst </a><br>
#                         <a href="http://127.0.0.1:8000/newlineremove"> newlineremove </a><br>
#                         <a href="http://127.0.0.1:8000/charcount"> charcount </a><br>
#                         <a href="http://127.0.0.1:8000/spaceremove"> spaceremove </a><br>
#                         <a href="http://127.0.0.1:8000/removepunc"> removepunc </a><br>
#                         ''')

# def capitalizefirst(request):
#     return HttpResponse(''' capitalizefirst <br><a href="http://127.0.0.1:8000/"> Home </a>''')

def newlineremover(request):
    return HttpResponse(''' newlineremove <br><a href="http://127.0.0.1:8000/"> Home </a><br>''')

# def charcount(request):
#     return HttpResponse(''' charcount <br><a href="http://127.0.0.1:8000/"> Home </a> <br>''')

# def spaceremove(request):
#     return HttpResponse('''spaceremove <br><a href="http://127.0.0.1:8000/"> Home </a><br>''')

# def removepunc(request):
#      # get the text
#      djtext=(request.GET.get('text', 'default'))
#      print(djtext)
#      # analyze the text
#      return HttpResponse('''removepunc <br><a href="/"> back </a><br>''') # use this one for back button

# Code for video no.11
def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # check checkbox value
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')
    
    
    # check which check box is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
        
    
    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed  to upper case', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
        # djtext=analyzed
    

    if (newlineremover =="on"):
     
     analyzed=""
     for char in djtext:
        if char != "\n" and char!="\r":
            analyzed=analyzed+char
     params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
     djtext=analyzed
       # Analyze the text
#  return render(request, 'analyze.html', params)

    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            # Only add char to analyzed if it's not an extra space
            if not (djtext[index] == " " and (index + 1 < len(djtext) and djtext[index + 1] == " ")):
                analyzed += char
        
        params = {'purpose': 'Remove Extra Spaces', 'analyzed_text': analyzed}
        djtext = analyzed  # Update djtext with the analyzed text
        # return render(request, 'analyze.html', params)
        # djtext=analyzed
    
    
    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on"):
          return HttpResponse("ERROR") 
    
    return render(request, 'analyze.html', params)


 
          
   
