from django.core.management.base import BaseCommand
from hub.models import Topic, Resource, Provider, CoveredTopic, UserProfile, Post
from django.contrib.auth.models import User

class Command(BaseCommand):
    args = 'help'
    help = 'Run this command after deleting the old db to get a base DB with some topics'

    def _create_topics(self):
        Topic.objects.all().delete()
        Resource.objects.all().delete()
        Provider.objects.all().delete()

        try:
            User.objects.get(username='sample_user').delete()
        except: pass

        try:
            User.objects.get(username='sample_poster').delete()
        except: pass

        #topics
        cs = Topic.objects.create(name="Computer Science", description="the best topic, obviously")

        ds = Topic.objects.create(name="Data Structures", parent=cs, description="making structures out of data. Like a binary bridge")
        graph = Topic.objects.create(name="Graph", parent=ds)
        directed = Topic.objects.create(name="Directed Graphs", parent=graph)
        dag = Topic.objects.create(name="Directed Acyclic Graph", parent=directed)
        scc = Topic.objects.create(name="Strongly Connected Components", parent=directed)
        tree = Topic.objects.create(name="Tree", parent=graph)
        bst = Topic.objects.create(name="Binary Search Tree", parent=ds, description="Not to be confused with BFS and DFS and idk I'm running out of description ideas...")
        rb = Topic.objects.create(name="Red-Black Tree", parent=bst)
        avl = Topic.objects.create(name="AVL Tree", parent=bst)
        splay = Topic.objects.create(name="Splay Tree", parent=bst)
        mp = Topic.objects.create(name="Map", parent=ds, description="A map of the world made out of hashbrown")
        hashmap = Topic.objects.create(name="Hash Map", parent=mp, description="")
        treemap = Topic.objects.create(name="Tree Map", parent=mp)
        queue = Topic.objects.create(name="Queue", parent=ds, description="a queue")
        pqueue = Topic.objects.create(name="Priority Queue", parent=queue)
        stack = Topic.objects.create(name="Stack", parent=ds, description="A stack is a FILO data structure, and it is most definitely not a queue")
        heap = Topic.objects.create(name="Heap", parent=ds)
        fh = Topic.objects.create(name="Fibonacci Heap", parent=heap)
        llist = Topic.objects.create(name="Linked List", parent=ds)
        sll = Topic.objects.create(name="Singly Linked List", parent=llist)
        dll = Topic.objects.create(name="Doubly Linked List", parent=llist)
        skip = Topic.objects.create(name="Skip List", parent=llist)
        array = Topic.objects.create(name="Array", parent=ds)
        matrix = Topic.objects.create(name="Matrix", parent=ds)
        bmatrix = Topic.objects.create(name="Boolean Matrix", parent=ds)
        bfilter = Topic.objects.create(name="Bloom Filter", parent=ds)

        algo = Topic.objects.create(name="Algorithms", parent=cs, description="Doing tasks in smart, and efficient ways")
        sorts = Topic.objects.create(name="Sorting", parent=algo, description="")
        qs = Topic.objects.create(name="Quick Sort", parent=sorts, description="This sort is pretty quick. Usually even faster than the renowned bubble sort!")
        bs = Topic.objects.create(name="Bubble Sort", parent=sorts, description="This is a sort that uses Mr. Bubbles to manipulate and compare data.")
        ms = Topic.objects.create(name="Merge Sort", parent=sorts, description="Merge sort is a recursive divide and conquer algorithm that parallelizes well and is maintains good stability.")
        ins = Topic.objects.create(name="Insertion Sort", parent=sorts, description="")
        ss = Topic.objects.create(name="Selection Sort", parent=sorts, description="")
        bs = Topic.objects.create(name="Bogo Sort", parent=sorts, description="")
        rs = Topic.objects.create(name="Radix Sort", parent=sorts, description="")
        cocks = Topic.objects.create(name="Cocktail Shaker Sort", parent=sorts, description="")
        graphAlgo = Topic.objects.create(name="Graph Algorithms", parent=algo, description="Algorithms that operate upon graphs and charts")
        srch = Topic.objects.create(name="Search/Path Algorithms", parent=graphAlgo)
        astar = Topic.objects.create(name="A star", parent=srch)
        bfs = Topic.objects.create(name="Breadth First Search", parent=srch)
        dfs = Topic.objects.create(name="Depth First Search", parent=srch)
        ford = Topic.objects.create(name="Floyd-Warshall Algorithm", parent=srch)
        kmp = Topic.objects.create(name="Knuth–Morris–Pratt Algorithm", parent=srch)
        djisktras = Topic.objects.create(name="Dijkstras", parent=srch, description="The algorithm that is hard to spell.")
        mintree = Topic.objects.create(name="Minimum Spanning Tree", parent=graphAlgo)
        prims = Topic.objects.create(name="Prim's", parent=mintree)
        kruskal = Topic.objects.create(name="Kruskal's", parent=mintree)
        flow = Topic.objects.create(name="Flow Networks", parent=graphAlgo)
        ffa = Topic.objects.create(name="Ford-Fulkerson algorithm", parent=flow)
        color = Topic.objects.create(name="Coloring Graphs", parent=graphAlgo)
        divcon = Topic.objects.create(name="Divide and Conquer", parent=algo)
        binSearch = Topic.objects.create(name="Binary Search", parent=divcon)
        strassen = Topic.objects.create(name="Strassen's Algorithm", parent=divcon)
        maxsub = Topic.objects.create(name="Maximal Subsequence", parent=divcon)
        Topic.objects.create(name="Merge Sort", parent=divcon)
        rec = Topic.objects.create(name="Recursion", parent=algo)
        gcd = Topic.objects.create(name="Greatest Common Divisor", parent=rec)
        hanoi = Topic.objects.create(name="Towers of Hanoi", parent=rec)
        Topic.objects.create(name="Depth First Search", parent=rec)
        Topic.objects.create(name="Quick Sort", parent=rec)
        Topic.objects.create(name="Binary Search", parent=divcon)



        #provider
        coursera=Provider.objects.create(name="Coursera", url="https://www.coursera.org/", description="A platform for onlince courses taught by professors at highly ranked universities")
        yale=Provider.objects.create(name="yale", url ="http://www.yale.edu/", description="Yale University in New Haven, Connecticut")
        mycodeschool=Provider.objects.create(name="YouTube - mycodeschool", url="http://www.youtube.com/channel/UClEEsT7DkdVO_fkrBw0OTrA", description="A YouTube channel that makes visual lessons to teach topics in Computer Science ")
        andrewhickson=Provider.objects.create(name="YouTube - andrewhickson", url="https://www.youtube.com/channel/UC3bsBSHWNrP3ni07NDrJ5hQ", description="A very small YouTube channel")
        wikipedia=Provider.objects.create(name="Wikipedia", url="https://en.wikipedia.org/", description="The Free Encyclopedia. Pages contain user generated content")
        mike=Provider.objects.create(name="YouTube - Mike Sambol", url="https://www.youtube.com/channel/UCzDJwLWoYCUQowF_nG3m5OQ", description="A YouTube channel that uses hand drawn examples to help you learn, review for exams, and prep for interviews.")
        stanford=Provider.objects.create(name="Stanford", url="https://www.stanford.edu", description="Stanford University")


        #resources
        # for now hard code mapping from int to learning style. Later when resources are only added online, django_forms will handle this automatically
        VIDEO = 1
        WIKI = 2
        SLIDES = 3
        LECTURE = 4
        COURSE = 5
        PAPER = 6
        PDF = 7
        PROBLEM_SET = 8

        ytbst = Resource.objects.create(name = "Data Structures: Binary Search Trees", type = VIDEO, url = "https://www.youtube.com/watch?v=pYT9F8_LFTM",provider=mycodeschool)
        wikimst = Resource.objects.create(name="Minimum Spanning Trees", type=WIKI, url="https://en.wikipedia.org/wiki/Minimum_spanning_tree", provider=wikipedia)
        ytPrimAlgo = Resource.objects.create(name="Prim's Algorithm", type=VIDEO, url="https://www.youtube.com/watch?v=BtGuZ-rrUeY", provider=andrewhickson)
        wikiPrimAlgo = Resource.objects.create(name="Prim's algorithm", type=WIKI, url="https://en.wikipedia.org/wiki/Prim%27s_algorithm", provider=wikipedia)
        ytKruskalAlgo = Resource.objects.create(name="Kruskal's algorithm in 2 minutes", type=VIDEO, url="https://www.youtube.com/watch?v=71UQH7Pr9kU", provider=mike)
        wikiFFA = Resource.objects.create(name="Ford-Fulkerson algorithm", type=WIKI, url="https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm", provider=wikipedia)
        stanGraph = Resource.objects.create(name="Basic Graph Algorithms", type=SLIDES, url="https://web.stanford.edu/class/cs97si/06-basic-graph-algorithms.pdf", provider=stanford)
        
        #covertopics
        CoveredTopic.objects.create(topic=bst,resource=ytbst)
        CoveredTopic.objects.create(topic=mintree, resource=wikimst)
        CoveredTopic.objects.create(topic=prims, resource=ytPrimAlgo)
        CoveredTopic.objects.create(topic=prims, resource=wikiPrimAlgo)
        CoveredTopic.objects.create(topic=kruskal, resource=ytKruskalAlgo)
        CoveredTopic.objects.create(topic=ffa, resource=wikiFFA)
        CoveredTopic.objects.create(topic=graphAlgo, resource=stanGraph)


        #example user
        upost = User.objects.create_user("sample_user", "asdf@fakemail.com", "password1")
        
        #discussion
        def add_comment_thread(source):
            root_1 = Post.objects.create(text="I found this resource to very useful.", user=upost.profile, forum=source)
            reply_1 = Post.objects.create(text="Me too, though some of the verbiage was a smidgen dense.", user=upost.profile, parent=root_1)
            reply_2 = Post.objects.create(text="Meh, did it really help your conceptual understanding? I don't think it went into more than basic detail.", user=upost.profile, parent=root_1)

            sub_reply_1 = Post.objects.create(text="Me three!", user=upost.profile, parent=reply_1)

            root_2 = Post.objects.create(text="Wow, I learned a lot! EduHub is the best knowledge resource on the 'net!", user=upost.profile, forum=source)
            reply = Post.objects.create(text="The nineties called; they want your \"'net\" back.", forum=source, user=upost.profile, parent=root_2)

        commented_sources = [wikimst, ytbst, wikiFFA, ytPrimAlgo, ytKruskalAlgo]
        for src in commented_sources:
            add_comment_thread(src) # 5:19 AM questions: is Mike Fowle truly my father?
       
        #uiuc_math_531_fa2015.number_theory.add()
    def handle(self, *args, **options):
        self._create_topics()
