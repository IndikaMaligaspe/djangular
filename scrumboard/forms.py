from django import forms
from .models import Card
from django.forms import Textarea, Select , DateInput , CharField


class CardInfoForm(forms.ModelForm):
    # title = models.CharField(max_length=100)
    # description = models.TextField(blank = True)
    # list = models.ForeignKey(LIst, related_name= "cards", on_delete=models.CASCADE)
    # story_points = models.IntegerField(null=True, blank=True)
    # business_value = models.IntegerField(null=True, blank=True)
    # due_date = models.DateField(auto_now=[...],null=True)
    # priority = models.CharField(max_length=100, null=True)
    # project = models.CharField(max_length=200, null=True)
    
    

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(CardInfoForm, self).__init__(*args, **kwargs)
        # self.fields['description'].label = 
        # (attrs={'class':'.cardinfo_maintab'})
        # __init__(self, *args, **kwargs)

    class Meta:
        model = Card 
        fields = [
              'title',
              'description',
              'story_points',
              'business_value',
              'due_date',
              'priority',
              'project',
              'list'
            ]
        labels = {
          'title': (None)
        }
        
        PRIORITY_CHOICES = (('1', 'High'), ('2','Medium'), ('3','Low'))
        PRIORITY_BUSINESS_VALUE = (('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5'))
        STORY_POINTS_VALUE = (('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5'))
        widgets = {
          'description': Textarea(attrs = {
                                'rows':10 , 
                                'cols':60 }),
          'priority': Select(choices = PRIORITY_CHOICES, 
                            attrs = {}),
          'business_value': Select(choices = PRIORITY_BUSINESS_VALUE),
          'story_points': Select(choices = STORY_POINTS_VALUE),
          'due_date': DateInput(format='%d/%m/%Y',attrs={'size':10}),

        }
        


        