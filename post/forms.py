from django import forms

from .models import Post, Idea, Proposal 

class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('content', 'detail',)

class IdeaCreateForm(forms.ModelForm):

    class Meta:
        model = Idea
        fields=('content',)


class ProposalCreateForm(forms.ModelForm):

    class Meta:
        model = Proposal
        fields = ('content',)