from django.views.generic.edit import CreateView
 
 
from .forms import CreateCommentForm
 
 
class CreateCommentView(CreateView):
    '''A view to create a new comment and save it to the database.'''
 
 
    form_class = CreateCommentForm
    template_name = "blog/create_comment_form.html"