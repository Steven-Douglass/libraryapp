from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the library index.")

def author_detail(request, author_id):
    return HttpResponse("You're looking at author %s." % author_id)

def book_detail(request, book_id):
    return HttpResponse("You're looking at book %s." % book_id)

def library_detail(request, library_id):
    return HttpResponse("You're looking at library %s." % library_id)

def member_detail(request, member_id):
    return HttpResponse("You're looking at member %s." % member_id)