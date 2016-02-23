import random
from django.shortcuts import render
from hub.models import Topic, EduSource, Post
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_check(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('index')

    # Invalid login
    messages.error(request, 'Invalid username/password.')
    return redirect('index')


def do_logout(request):
    logout(request)
    messages.info(request, 'Logged out successfully.')
    return redirect('index')


def index(request):
    return render(request, 'hub/index.html')


def topic_list(request):
    root_topics = Topic.objects.root_nodes()

    return render(request, 'hub/topic_list.html', {'topics': root_topics})


def topic_list_jstree(request):
    children = get_object_or_404(Topic, pk=int(request.GET['node'])).get_children() if 'node' in request.GET else Topic.objects.root_nodes()

    children = [
        {'id': child.id, 'pk': child.id, 'label': child.name, 'load_on_demand': not child.is_leaf_node()}
        for child in children
    ]

    return JsonResponse(children, safe=False)


def randomsource_view(request):
    blah = random.choice(EduSource.objects.all())
    return redirect('edusource_view', pk=blah.pk)


def edusource_view(request, pk):
    edusource = get_object_or_404(EduSource, pk=int(pk))
    return render(request, 'hub/edusource_view.html', {'edusource': edusource})


def topic_detail_json(request, pk):
    topic = get_object_or_404(Topic, pk=int(pk))
    topic_dict = {
        'pk': pk,
        'id': pk,
        'name': topic.name,
        'description': topic.description,
    }

    return JsonResponse(topic_dict)


def topic_edusource_json(request, pk): #, page, sources_per_page,):
    topics = Topic.objects.get(id=int(pk)).get_descendants(include_self=True)
    sources = []
    for topic in topics:
        sources.extend([c for c in topic.covered_by.select_related('provider')])

    return JsonResponse([ {'id' : s.id, 'name' : s.name, 'url' : s.url, 'provider' : s.provider.name, "type" : s.type } for s in sources ], safe=False)


def load_forum_posts(request, pk):
    def fill_post_dict(posts):
        return [{'id' : s.id, 'title' : s.title, 'time': s.created_at, 'text' : s.text, 'poster' : s.user.user.username, 'children' : fill_post_dict(s.get_children()) } for s in posts ]

    forum = get_object_or_404(EduSource, pk=int(pk))
    posts = Post.objects.all().filter(level=0, forum=forum)

    # offset = request.GET['offset'] if 'offset' in request.GET else 0
    # count = request.GET['count'] if 'count' in request.GET else 20
    
    return JsonResponse([ {'id' : s.id, 'time': s.created_at,
               'title': s.title, 'text': s.text, 'poster': s.user.user.username,
               'children' : fill_post_dict(s.get_children())} for s in posts
            ], safe=False
    )

