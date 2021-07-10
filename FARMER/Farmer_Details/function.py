def handle_uploaded_file(f):  
    with open('static/photo/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  
    return 'static/photo/'+f.name