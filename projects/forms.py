from django.forms import ModelForm
from .models import Project, Review


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['vote_total', 'vote_ratio', 'owner', 'tags']

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for k, v in self.fields.items():
            v.widget.attrs.update({'class': 'input'})


class ReviewFrom(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {
            'value': 'Place your vote',
            'body': 'Add a comment with your vote'
        }

    def __init__(self, *args, **kwargs):
        super(ReviewFrom, self).__init__(*args, **kwargs)

        for k, v in self.fields.items():
            v.widget.attrs.update({'class': 'input'})
