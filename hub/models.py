from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django_enumfield import enum
from django.contrib.auth.models import User
from eduhub.common import TimestampedModel
from urllib.parse import urlparse, parse_qs
from django.utils import timezone


# Tie users to things through this - one will be created for each user.
class UserProfile(TimestampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return str(self.user)


# Arbitrary grouping of topics
class TopicSet(TimestampedModel):
    name = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    topics = models.ManyToManyField('Topic', related_name='member_of_sets')

    def __str__(self):
        return self.name


class Topic(MPTTModel, TimestampedModel):
    name = models.CharField(max_length=500)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    description = models.TextField(blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class EduSource(TimestampedModel):
    name = models.CharField(max_length=500)
    type = models.CharField(max_length=500)
    covered_topics = models.ManyToManyField(Topic, through='CoveredTopic', related_name='covered_by')
    required_topics = models.ManyToManyField(Topic, through='RequiredTopic', related_name='required_by')
    url = models.CharField(max_length=250, null=True) # these should be validated
    # user = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name='creator')
    provider = models.ForeignKey('EduProvider', on_delete=models.CASCADE, related_name='sources', null=True)

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


class EduProvider(TimestampedModel):
    name = models.CharField(max_length=500)
    url = models.CharField(max_length=250, null=True)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class ProviderRating(TimestampedModel):
    review = models.TextField(blank=True)
    stars = models.PositiveSmallIntegerField()
    poster = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name='provider_ratings')
    source = models.ForeignKey('EduProvider', on_delete=models.CASCADE, related_name='provider_ratings')


class Rating(TimestampedModel):
    review = models.TextField(blank=True)
    stars = models.PositiveSmallIntegerField()
    poster = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name='ratings')
    source = models.ForeignKey('EduSource', on_delete=models.CASCADE, related_name='ratings')


class Problem(TimestampedModel):
    problems = models.TextField(max_length=1000)
    stars = models.PositiveSmallIntegerField()
    poster = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name='submitted_problems')
    source = models.ForeignKey('EduSource', on_delete=models.CASCADE, related_name='submitted_problems')


class Solution(TimestampedModel):
    answer = models.TextField(max_length=1000)
    poster = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name='solutions')
    problem = models.ForeignKey('Problem', on_delete=models.CASCADE, related_name='solutions')
    been_graded = models.BooleanField()


class Grading(TimestampedModel):
    feedback = models.TextField(max_length=1000)
    grade = models.PositiveSmallIntegerField()
    grader = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name='your_gradings')
    poster = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name='your_grades')
    answer = models.ForeignKey('Solution', on_delete=models.CASCADE, related_name='grade')
    

class Post(MPTTModel):
    forum = models.ForeignKey('EduSource', on_delete=models.CASCADE, related_name='source_fourm', null=True)
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

# "through" models
class CoveredTopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    edusource = models.ForeignKey(EduSource, on_delete=models.CASCADE)


class RequirementType(enum.Enum):
    STRICTLY_REQUIRED = 0
    RECOMMENDED = 1
    OPTIONAL = 2


class RequiredTopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    edusource = models.ForeignKey(EduSource, on_delete=models.CASCADE)
    level = enum.EnumField(RequirementType)
