
from django.shortcuts import get_object_or_404, render, render_to_response, get_list_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from .models import League, Fish, River
from django.views.generic.edit import CreateView
from django import forms
from django.forms import formset_factory, ModelForm, inlineformset_factory, modelformset_factory
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse




class LeageModelForm(forms.ModelForm):
    class Meta:
        model = League
        fields = ('league_name', )
        labels = {
            'league_name': 'League Name'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter League Name here'
                }
            )
        }
RiverFormset = modelformset_factory(
    River,
    fields=('name', ),
    extra=2,
    widgets={
        'name': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Fishing Spot/River Name Here'
            }
        )
    }
)

FishFormset = modelformset_factory(
    Fish,
    fields=('species', ),
    extra=2,
    widgets={
        'species': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Fish Here'
            }
        )
    }
)

class EditRiverDetails(ModelForm):
    class Meta:
        model = Fish
        fields = ('basePoints', )



def workDamnit():
    pass

def create_league_with_rivers(request):
    print('in create league')
    template_name = 'flyFishing/create-league.html'
    if request.method == 'GET':
        leagueform = LeageModelForm(request.GET or None)
        formset = RiverFormset(prefix="river", queryset=River.objects.none())
        fishformset = FishFormset(prefix="fish", queryset=Fish.objects.none())
    elif request.method == 'POST':
        leagueform = LeageModelForm(request.POST)
        formset = RiverFormset(request.POST, prefix='river')
        fishformset = FishFormset(request.POST, prefix='fish')
        if leagueform.is_valid() and formset.is_valid() and fishformset.is_valid():
            # first save this book, as its reference will be used in `Author`
            listRivers = []
            listFish = []
            league = leagueform.save()
            for form in formset:
                # so that `book` instance can be attached.
                
                river = form.save(commit=False)
                river.relatedLeague = league 
                listRivers.append(river)
                river.save()
            print(listRivers) 
    
            for form in fishformset:
                # so that `book` instance can be attached.
                for river in listRivers:
                    cd = form.cleaned_data
                    species = cd.get('species')
                    print(species)
                    # fish = form.save(commit=False)
                    fish = Fish()
                    fish.species = species
                    fish.relatedLeague = league
                    fish.relatedRiver = river
                    fish.basePoints = 1
                    listFish.append(fish)
                    print(fish)
                    fish.save()
            print(listFish)

                
                
           
            return HttpResponseRedirect(reverse('flyFishing:gameDetails', args=(league.id,)))
    return render(request, template_name, {
        'leagueform': leagueform,
        'formset': formset,
        'fishformset': fishformset,
    })



def gameDetails(request, league_id):
   
    league = get_object_or_404(League, id = league_id)
    rivers = get_list_or_404(River, relatedLeague_id = league_id)

    context = {
        'league' : league,
        'rivers' : rivers,
    }
    return render(request, 'flyFishing/league-details.html', context)


def riverDetails (request, river_id):
    river = get_object_or_404(River, id = river_id)
    FishinlineFormSet = inlineformset_factory(River, Fish, EditRiverDetails, extra = 0)


    if request.method == 'GET':
        formset = FishinlineFormSet(instance = river)

    elif request.method == 'POST':
        formset = FishinlineFormSet(request.POST, request.FILES, instance = river)
        # formset = RiverFormset(request.POST, request.FILES)
        if formset.is_valid():
            print('valid')
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return HttpResponseRedirect(reverse('flyFishing:gameDetails', args=(river.relatedLeague.id,)))
    context = {
        'river' : river,
        'formset' : formset,
    }
    return render(request, 'flyFishing/edit-river-details.html', context)


def leagueList(request):
    leagues = League.objects.all()
    return render(request, 'flyFishing/league-list.html', {'leagues' : leagues})


def userProfile (request):
    return render(request, 'flyFishing/user-profile.html')

# Create your views here.

# game has
    # name
    # players
        # regular players
        # admin player
    # rivers
        # rivers have fish
    # fish 
        #  fish have base points
        #  size points
        #  method points
        #  river points
        

# creating a league 
# 1 set a name
# 2 set the areas/rivers you can fish that are available in the game 
# 3 set the fish available in the game you can catch




class CreateLeagueForm(ModelForm):
    class Meta: 
        model = League
        fields = ['league_name']


class AddGameRivers(ModelForm):
    class Meta:
        model = River
        fields = ['name']


class AddGameRFish(ModelForm):
    class Meta:
        model = Fish
        fields = ['species']
    

    




def index(request):

       
    return render(request, "flyFishing/index.html") 


def createLeague():
    pass






    # =========================================================================================

# class CreateLeagueForm(ModelForm):
#     class Meta: 
#         model = League
#         fields = ['league_name']


# class FishForm(ModelForm):
#     class Meta: 
#         model = Fish
#         fields = ['species']
    


# class RiverForm(ModelForm):
#     class Meta:
#         model = River
#         fields = ['name']


# class EditRiver(ModelForm):
#     active = forms.BooleanField()
#     class Meta:
#         model = FishPerRiver 
#         fields =['basePoints',]

    

# class EditRiverHOLD(ModelForm):

#     # here we use a dummy `queryset`, because ModelChoiceField
#     # requires some queryset
#     item_field = forms.ModelChoiceField(queryset=Fish.objects.none())
#     active = forms.BooleanField()
#     def __init__(self, league_id):
#         super(EditRiver, self).__init__()
#         self.fields['item_field'].queryset = Fish.objects.filter(relatedLeague=league_id)
    
#     class Meta:
#         model = Fish
#         fields =['basePoints',]


 #   def createLeague(request):
#     # river =  River.objects.all()
#     # print(river)
#     form = CreateLeagueForm()
#     riverFormset = formset_factory(RiverForm, extra=1)
#     fishFormset = formset_factory(FishForm, extra=1)
 
   
  
#     if request.method == "POST":
#         leagueForm = CreateLeagueForm(request.POST)
        
#         riverset = riverFormset(request.POST,  prefix='river')
#         fishSet = fishFormset(request.POST, prefix='fish')
#         print(riverset)
       
#         league = leagueForm.save(commit=True)
#         if(riverset.is_valid()):
            
#             print('both valid')
#             for river in riverset:
#                 cd = river.cleaned_data
                
#                 print(cd)
#                 name = cd.get('name')
#                 river=River(name=name, relatedLeague = league)
#                 river.save()
#         if (fishSet.is_valid()):
#             for fish in fishSet:
#                 cd = fish.cleaned_data
#                 species = cd.get('species')
#                 print(species)        
#                 fish=Fish(species=species, relatedLeague = league)
#                 fish.save()

#             league.rivers = riverset
#             # league.fish = fishSet
           
#         else:
#             message = "Something went wrong"

#         return HttpResponseRedirect(reverse('flyFishing:gameDetails', args=(league.id,)))
#     else:
#         riverset = riverFormset(prefix='river')
#         fishSet = fishFormset(prefix='fish')
#     context={
#         'form' : form,
#         'riverset': riverset,
#         'fishSet' : fishSet,
#         # 'river' : river
#     }
#     return render(request, 'flyFishing/create-league.html', context)


##def gameDetails(request, league_id):
#     print('details')
#     league = get_object_or_404(League, id = league_id)
#     rivers = get_list_or_404(River, relatedLeague_id = league_id)

#     context = {
#         'league' : league,
#         'rivers' : rivers,
#     }
   
  
   
#     return render(request, 'flyFishing/league-details.html', context)


# def riverDetails(request, river_id):
#     print('in details')
#     river = get_object_or_404(River, id = river_id)
#     league = get_object_or_404(League, river = river)

#     fishOptions = Fish.objects.filter(relatedLeague = league)

#     print(river)
#     print(league)
#     # fish = EditRiver()
  
#     print(fishOptions)
#     # EditRiverFormset = formset_factory(EditRiver, EditRiver, extra=0)


#     EditRiverFormset = modelformset_factory(Fish, EditRiver, extra=0)

#     formset = EditRiverFormset(queryset = fishOptions)   

#     context = {
        
#         'river' : river,
#         'formset' : formset

#     } 

#     if request.method == "POST":
#         formset = EditRiverFormset(request.POST, request.FILES, queryset = fishOptions)
        
       
#         print('in post')
#         print(formset.errors)
#         # print(formset.is_valid())
#         if (formset.is_valid()):
#             print('valid')
#             for fish in formset:
                
#                 cd = fish.cleaned_data
#                 points = cd.get('basePoints')
#                 f = FishPerRiver(species= fish.instance, basePoints = points, river=river)
                
#                 f.save()
#                 print(points)
                
        
#         return render(request, 'flyFishing/edit-river-details.html', context)

#     return render(request, 'flyFishing/edit-river-details.html', context)


# def leagueList(request):
#     leagues = League.objects.all()
#     return render(request, 'flyFishing/league-list.html', {'leagues' : leagues})
