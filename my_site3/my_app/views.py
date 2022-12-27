from django.shortcuts import render

# Create your views here.

def example_view(request):
    return render(request,'my_app/example.html')

def example2_view(request):
    return render(request,'my_app/example2.html')

def variable_view(request):
    #use context to send variables using python
    my_var = {'first_name':'manuel','last_name':'gonzalez',
        'some_list':[1,2,3],'some_dict':{'inside_key':'inside_value'},
        'user_logged_in':True}
    return render(request,'my_app/variable.html',context = my_var)


#to not have to name the template 404
def my_custom_page_not_found_view(request,exception):
    return render(request,'404.html',status=404)