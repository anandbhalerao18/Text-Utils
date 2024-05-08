from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text from the GET request
    djtext = request.POST.get('text', 'default')
    print(djtext)
    removepunc = request.POST.get('removepunc', 'off')  # Getting the checkbox value
    fullcaps = request.POST.get('fullcaps', 'off')  
    withoutcaps = request.POST.get('withoutcaps', 'off')
    newlinerem = request.POST.get('newlinerem', 'off')
    countchar = request.POST.get('countchar', 'off')
    extraspacereomver = request.POST.get('extraspacereomver', 'off')
    # Getting the checkbox value
    
    # Check if 'removepunc' is on
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%&*_~'''
        analyzed = ""
        # Remove punctuations
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    elif(fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'change to uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    elif(withoutcaps == 'on'):
        analyzed =""
        for char in djtext:
            analyzed += char.lower()
        params = {'purpose': 'change to uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    elif countchar == 'on':
        char_count = len(djtext)  # Count total characters
        params = {'purpose': 'Count Characters', 'analyzed_text': f'Total characters: {char_count}'}
        return render(request, 'analyze.html', params)

    elif newlinerem == 'on':
        analyzed = ""
        for char in djtext:
            if char not in {"\n", "\r"}:  # Check against a set of newlines
                analyzed += char
        params = {'purpose': 'Remove Newlines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    elif extraspacereomver == 'on':
            analyzed = ""
            for index, char in enumerate(djtext):
                # Check if the current character is a space and the next character exists
                if index < len(djtext) - 1 and djtext[index] == " " and djtext[index + 1] == " ":
                    pass  # Skip double spaces
                else:
                    analyzed += char
            params = {'purpose': 'Remove Extra Spaces', 'analyzed_text': analyzed}
            return render(request, 'analyze.html', params)

    else:
        # If 'removepunc' is off, just pass the original text back
        params = {'purpose': 'No operation performed', 'analyzed_text': djtext}
        return render(request, 'analyze.html', params)
