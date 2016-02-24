from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django_enumfield import enum
from django.contrib.auth.models import User
from eduhub.common import TimestampedModel
from urllib.parse import urlparse, parse_qs
from django.utils import timezone


# Tie users to things through this - one will be created for each user.
class UserProfile(TimestampedModel):
    VIDEO = 0
    WIKI = 1
    SLIDES = 2
    LECTURE = 3 # Video leture
    COURSE = 4
    RESEARCH_PAPER = 5
    PDF = 6
    PROBLEM_SET = 7

    TYPE_CHOICES = (
        (VIDEO, "Video"),
        (WIKI, "Wiki"),
        (SLIDES, "Slides"),
        (LECTURE, "Lecture"),
        (COURSE, "Course"),
        (RESEARCH_PAPER, "Research Paper"),
        (PDF, "PDF"),
        (PROBLEM_SET, "Problem Set"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    learning_style = models.CharField(max_length=30, choices=TYPE_CHOICES, default=VIDEO)

    def __str__(self):
        return str(self.user)


# Arbitrary grouping of topics - used to group prereqs or curricula
class TopicSet(TimestampedModel):
    name = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    topics = models.ManyToManyField('Topic', related_name='member_of_sets')

    def __str__(self):
        return self.name


# A specifc topic in the tree / DAG of topics. It has zero or more 'parent' topics and 0 or more subtopics
class Topic(MPTTModel, TimestampedModel):
    name = models.CharField(max_length=500)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    description = models.TextField(blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


# A resource for learning a set of topics (e.g. a video or pdf)
# Resources have prereqs (RequiredTopics) and CoveredTopics
# Users can rate Resources based on how good they are and how technical they are
class Resource(TimestampedModel):
    VIDEO = 0
    WIKI = 1
    SLIDES = 2
    LECTURE = 3 # Video leture
    COURSE = 4
    RESEARCH_PAPER = 5
    PDF = 6
    PROBLEM_SET = 7

    TYPE_CHOICES = (
        (VIDEO, "Video"),
        (WIKI, "Wiki"),
        (SLIDES, "Slides"),
        (LECTURE, "Lecture"),
        (COURSE, "Course"),
        (RESEARCH_PAPER, "Research Paper"),
        (PDF, "PDF"),
        (PROBLEM_SET, "Problem Set"),
    )

    name = models.CharField(max_length=500)
    type = models.CharField(max_length=30, choices=TYPE_CHOICES, default=VIDEO)
    covered_topics = models.ManyToManyField(Topic, through='CoveredTopic', related_name='covered_by')
    required_topics = models.ManyToManyField(Topic, through='RequiredTopic', related_name='required_by')
    url = models.CharField(max_length=250, null=True) # these should be validated
    # user = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name='creator')
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE, related_name='sources', null=True)
    views = models.PositiveIntegerField(default=0)

    def get_embed_type_and_html(self):
        parsed = urlparse(self.url)
        domain = parsed.netloc.lower()
        domain = domain[4:] if domain[0:4] == 'www.' else domain
        if domain == 'youtube.com':
            base = '<iframe width="420" height="315" src="%s" frameborder="0" allowfullscreen></iframe>'
            if 'embed' in parsed.path.lower():
                return base % self.url
            # attempt to pull v= from query
            query_args = parse_qs(parsed.query)
            if 'v' in query_args:
                return 'video', base % ('https://www.youtube.com/embed/%s' % query_args['v'][0])
            # else fallback to a link

        if self.url[-4:] == '.pdf':
            return 'pdf', ("<object data='%s' type='application/pdf' width='100%%' height='800px'>Your browser does not support embedded PDF files.</object>" % self.url)

        if 'wikipedia' in self.url:
            return 'wiki', '<a class="embedly-card" href="%s">%s</a><script async src="//cdn.embedly.com/widgets/platform.js" charset="UTF-8"></script>' % (self.url, self.name)

        return 'link', '<a href="%s" title="%s">%s</a>' % (self.url, self.name, self.name)

    def __str__(self):
        return self.name


# A tag for a resource. Tags are used when a resource has attributes that don't neatly fit into topics
class Tag(TimestampedModel):
    name = models.CharField(max_length=30)
    resources = models.ManyToManyField(Resource, related_name='tags')


# A resource provider (e.g. Wikipedia, Khan Academy, a specific YT channel, etc)
class Provider(TimestampedModel):
    name = models.CharField(max_length=500)
    url = models.CharField(max_length=250, null=True)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


# A rating saying how 'good' a resource is at teaching a given subject. Basically how effective the lesson is
class GoodRating(TimestampedModel):
    review = models.TextField(blank=True)
    stars = models.PositiveSmallIntegerField()
    poster = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name='good_ratings')
    resource = models.ForeignKey('Resource', on_delete=models.CASCADE, related_name='good_ratings')


# A rating to gauge the technicality and depth of the resource. Does it scratch the surface or get into nitty gritty details?
class TechRating(TimestampedModel):
    review = models.TextField(blank=True)
    stars = models.PositiveSmallIntegerField()
    poster = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name='tech_ratings')
    resource = models.ForeignKey('Resource', on_delete=models.CASCADE, related_name='tech_ratings')


# A post by a User in the comments section of a resource
class Post(MPTTModel):
    forum = models.ForeignKey('Resource', on_delete=models.CASCADE, related_name='source_fourm', null=True)
    text = models.TextField(max_length= 2000)
    #reply = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True, related_name="replies")
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name="posts")
    parent = TreeForeignKey('self', null=True, blank=True, related_name='replies', db_index=True)
    title = models.CharField(max_length=500, blank=True)

    # Sorta bad practice to use these parameters but this makes things work more smoothly so honestly fuck it.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['created_at']

    def __str__(self):
        return "Post: %s" % str(self.pk)

###########################
# "through" models
###########################

# A Topic that a resource covers. e.g. a video titled "Binary Search Trees" would list "Binary Search Trees"" as a CoveredTopic
class CoveredTopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)


# A Prereq to a resource. e.g. a Minimum Spanning Tree  resource might have "Graphs" or "Trees" as a prereq
class RequiredTopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
