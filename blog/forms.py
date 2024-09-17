from django import forms  # Importing Django's forms module to create forms based on models.

from .models import Comment  # Importing the Comment model from the current directory's models module.

# Creating a form for the Comment model.
class CommentForm(forms.ModelForm):
    # Meta class to specify which model the form is based on and additional configurations.
    class Meta:
        model = Comment  # The form is built from the Comment model.
        
        # Exclude the 'post' field from the form, as it will likely be handled in the view or automatically.
        exclude = ['post']
        
        # Custom labels for the form fields.
        labels = {
            'user_name': "Your Name",   # Changing the label for the 'user_name' field to "Your Name".
            'user_email': "Your Email",  # Changing the label for the 'user_email' field to "Your Email".
            'text': "Your Comment"  # Changing the label for the 'text' field to "Your Comment".
        }
