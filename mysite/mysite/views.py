from django.views.defaults import page_not_found

def mi_error_404(request, exception):
    return page_not_found(request,exception,'404.html')