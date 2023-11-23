from django.db import models

# Create your models here.
class UserDetails(models.Model):
    ROLE_CHOICES = [
        ('Student', 'Student'),
        ('Alumni', 'Alumni'),
    ]
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    dateOfBirth = models.DateField()
    email = models.CharField(max_length=100)
    mobileNo = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=ROLE_CHOICES)
    institute = models.CharField(max_length=100)
    yearOfPassing = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    yearsOfExperience = models.IntegerField()
    company = models.CharField(max_length=100)
    currentScore = models.IntegerField()
    techStack = models.TextField()
    courses = models.TextField()
    plan = models.IntegerField()
    endorsements = models.TextField()


class Forum(models.Model):
    name = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    About = models.TextField()


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Post(models.Model):
    forumID = models.ForeignKey(Forum, on_delete=models.CASCADE)
    postedBy = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    postedTime = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    metaData = models.CharField(max_length=100)
    likes = models.TextField(default='{}')
    comments = models.TextField(default='[]')
    likesCount = models.IntegerField(default=0)
    commentsCount = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)

class Hackathon(models.Model):
    name = models.CharField(max_length=100)
    oneLiner=models.CharField(max_length=100)
    description=models.TextField()
    conductedBy=models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    openToALL = models.CharField(max_length=100)
    postedOn = models.DateTimeField(auto_now_add=True)
    startDate = models.DateTimeField(auto_now_add=True)
    endDate = models.DateTimeField(auto_now_add=True)
    cost = models.IntegerField()
    registeredCount = models.IntegerField()
    winner = models.CharField(max_length=100)
    runnerUp = models.CharField(max_length=100)
    metaData = models.CharField(max_length=100)
    otherWinners = models.CharField(max_length=100)

class HackathonRegistration(models.Model):
    hackathonID = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    teamLeader = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    teamMembers = models.TextField()
    submission = models.CharField(max_length=100)
    submissionTime = models.DateTimeField(auto_now_add=True)
    registeredTime = models.DateTimeField(auto_now_add=True)