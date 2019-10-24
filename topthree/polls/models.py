from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Poll(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE, default = 1)
    text = models.CharField(max_length = 255)
    pub_date = models.DateField()

    def __str__(self):
        return self.text

    def user_can_vote(self, user):
        qs = user.vote_set.filter(poll = self)
        if qs.exists():
            return False
        else:
            return True

    @property
    def num_of_votes(self):
        return self.vote_set.count()


    def get_results_dict(self):
        res = []
        for choice in self.choice_set.all():
            d = {}
            d['text'] = choice.choice_text
            d['num_votes'] = choice.num_of_votes
            if not self.num_of_votes:
                d['percentage'] = 0
            else:
                d['percentage'] = round(choice.num_of_votes / self.num_of_votes * 100, 2)
            res.append(d)
        return res

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 255)

    def __str__(self):
        return "{} - {}".format(self.poll.text[:25], self.choice_text[:25])

    @property
    def num_of_votes(self):
        return self.vote_set.count()

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete = models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete = models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.poll.text[:25], self.user)
