from django.db import models
from django import forms



class Player (models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name



# class River ():


# class Fish():

class League(models.Model):
    league_name =  models.CharField(max_length=200)    
    def __str__(self):
        return self.league_name






class River(models.Model):
    name = models.CharField(max_length=200)
    relatedLeague = models.ForeignKey(League, on_delete=models.CASCADE, null=True)
    # active_fish = models.ManyToManyField(Fish)
    def __str__(self):
        return self.name

class Fish(models.Model):
    species = models.CharField(max_length=200)
    basePoints = models.IntegerField(null=True)
    relatedRiver = models.ForeignKey(River,  related_name='fish', on_delete=models.CASCADE, null=True)
    relatedLeague = models.ForeignKey(League, on_delete=models.CASCADE, null=True)

    # river = models.ManyToManyField(River, related_name = 'river')
    def __str__(self):
        return self.species


# class FishPerRiver(models.Model):
#     species = models.ForeignKey(Fish, on_delete=models.CASCADE, null=True)
#     basePoints = models.IntegerField(null=True)
#     river = models.ForeignKey(River, related_name='fish', on_delete=models.CASCADE, null=True)

#     def __str__(self):
#         return self.species.species


    



    