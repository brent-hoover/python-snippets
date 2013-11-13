
class UsersOnline(models.Model):
    # Showing users online
    username    = models.CharField(max_length=100)
    time        = models.DateTimeField()
    url         = models.URLField()

    def __unicode__(self):
        return self.username

def recountUsersOnline():
    users = UsersOnline.objects.all()
    date_now = datetime.now()
    # Deleting expired users
    for user in users:
        dt = date_now - user.time
        if (dt.seconds > 300):
            # User expired
            user.delete()

def addUserOnline(username, url):
    try:
        user = UsersOnline.objects.get(username=username)
        user.time = datetime.now()
    except:
        user = UsersOnline(username=username, time=datetime.now(), url=url)
