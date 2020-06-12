

from django.http import HttpResponse

# importing templates

from django.shortcuts import render



def index(request):
   
    return render(request, 'index1.html')







def analyze(request):
    # Get the text
    djtext = request.POST.get('text','default')
    print(djtext)

    # check the checkbox values

    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    

    #check Box value

    if( removepunc == "off" and fullcaps == "off" and newlineremover=="off" and extraspaceremover == "off"):
        return HttpResponse('''<h1 style="color:red">Error: Please aleast select on of the checkbox</h1> ''')

    else:
        analyzed = ""
        if removepunc == "on":
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            
            for char in djtext:
                if char not in punctuations:
                    analyzed = analyzed + char
            
            params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
            
        
            
        

        if(fullcaps == "on"):
            analyzed = ""
            for char in djtext:
                analyzed = analyzed + char.upper()
            params = {'purpose' : 'changed to uppercase' , 'analyzed_text': analyzed}

            djtext=analyzed        # Analysed the text
        


        if(extraspaceremover == "on"):
            analyzed = ""
            for index, char in enumerate(djtext):
                if not(djtext[index] == " " and djtext[index+1] == " "):
                    analyzed = analyzed + char 
            params = {'purpose' : 'extraspaceremover' , 'analyzed_text': analyzed}

        djtext=analyzed    # Analysed the text
        


        if (newlineremover == "on"):
            analyzed = ""
            for char in djtext:
                if char != "\n" and char!= "\r":
                    analyzed = analyzed + char
        
            params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext=analyzed    # Analyze the text

    return render(request , 'analyze.html' , params)

    
 

  

        








