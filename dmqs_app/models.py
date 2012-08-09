from django.db import models

class Dog(models.Model):
    name = models.CharField(null=False, blank=False, max_length=150)

class BestFriend(models.Model):
    person   = models.ForeignKey('Friend')
    nickname = models.CharField(max_length=100, null=True)

    def __unicode__(self):
        return "%s - %s" % (self.person.name, self.nickname)

class Friendship(models.Model):
    best_friend1 = models.ForeignKey('BestFriend',
                                     related_name="reverse_friend")
    best_friend2 = models.ForeignKey('Friend')
    since        = models.DateField(null=False)

    def __unicode__(self):
        return "%s is friend of %s since" % (self.best_friend1, self.best_friend2)

class Friend(models.Model):
    name         = models.CharField(null=False, blank=False, max_length=150)

    dog          = models.ForeignKey(Dog, null=True, blank=True)
    other_dog    = models.OneToOneField(Dog,
                                        null=True,
                                        blank=True,
                                        related_name="other")

    friends      = models.ManyToManyField('self', null=True, blank=True)
    best_friends = models.ManyToManyField(BestFriend,
                                          through=Friendship,
                                          null=True,
                                          blank=True,
                                          related_name="friendship")

    def __unicode__(self):
        return "%s" % (self.name)
