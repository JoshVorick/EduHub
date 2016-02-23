from django.core.management.base import BaseCommand
from hub.models import Topic, EduSource, EduProvider, CoveredTopic, Rating, UserProfile, Post
from django.contrib.auth.models import User

class Command(BaseCommand):
    args = 'help'
    help = 'Run this command after deleting the old db to get a base DB with some topics'

    def _create_topics(self):
        Topic.objects.all().delete()
        EduSource.objects.all().delete()
        EduProvider.objects.all().delete()

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

        prim = Topic.objects.create(name="Primitives", parent=cs, description="Primitive variable types.")
        twos = Topic.objects.create(name="Two's Complement", parent=prim, description="")
        flt = Topic.objects.create(name="Floating Point Numbers", parent=prim, description="")
        uint = Topic.objects.create(name="Unsigned Integers", parent=prim, description="")
        bit = Topic.objects.create(name="Bitwise Operators", parent=prim, description="")

        sec = Topic.objects.create(name="Computer Security", parent=cs, description="")
        crypt = Topic.objects.create(name="Cryptography", parent=sec, description="")
        hashing = Topic.objects.create(name="Hashing", parent=sec)
        enc = Topic.objects.create(name="Encryption", parent=sec)

        blockchain = Topic.objects.create(name="Blockchain", parent=cs, description="A decentralized database implementation. Anyone can write to this database, but no one can delete from it. It is the technology that allows Bitcoin to be secure and incorruptible.")
        
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

        graphics = Topic.objects.create(name="Graphics", parent=cs)


        math = Topic.objects.create(name="Mathematics", description="MATHEMATICS. NOT MATH. -Matt Faust")
        calc = Topic.objects.create(name="Calculus", parent=math, description="The study of calulators starting from the 1600s")
        algebra = Topic.objects.create(name="Algebra", parent=math, description="The study of mermaid clothing. Usually all they wear is algae bras, since there is no need to cover their fish parts")
        algrebraic_geo = Topic.objects.create(name="Algebraic Geometry", parent=algebra, description="EXPLODE THE X")
        metamath = Topic.objects.create(name="Metamathematics", parent=math, description="My homies Russ and Godel be rocking.")
        proof_theory = Topic.objects.create(name="Proof Theory", parent=metamath, description="OOOOOOOOOO boi, lets check out some sick sequents")
        model_theory = Topic.objects.create(name="Model Theory", parent=metamath, description="I like to think that we can all be models with the proper social axioms")
        lin_algebra = Topic.objects.create(name="Linear Algebra", parent=algebra, description="O man sick matrices bro, really digging those standard bases. O man is that a linear vector space. I want a hat but all eigen't is sadenss.")
        number_theory = Topic.objects.create(name="Number Theory", parent=math, description="My boy Euclid was tripping when Euler was all like broo check our these CFs, Euclid read CP and called for the MODS")
        analytical_numb = Topic.objects.create(name="Analytical Number Theory", parent=number_theory, description="")
        analysis = Topic.objects.create(name="Analysis", parent=math, description="AKA Real mathematics")
        real_analysis = Topic.objects.create(name="Real Analysis", parent=analysis, description="What's wrong man, we were almost complete? I don't know I just felt so compact as we were closing that space... I just felt all this accumulation and shit just got too Real")
        complex_analysis = Topic.objects.create(name="Complex Analysis", parent=analysis, description="Two variables instead of one! Dude what are you saying? We can't even compare the two.")


        bio = Topic.objects.create(name="Biology", description="It's barely a science, but we'll count it")
        bchem = Topic.objects.create(name="Brain Chemistry", parent=bio, description="The study of how chemicals in the brain interact and affect our moods, and thoughts")
        micro = Topic.objects.create(name="Microbiology", parent=bio, description="The study of itsy bitsy living things. Like bacteria.")

        phys = Topic.objects.create(name="Physics", description="The study of matter and its motion through space and time")
        classical = Topic.objects.create(name="Classical", parent=phys, description="Traditional branches, including classical mechanics, acoustics, optics, thermodynamics, and electromagnetism")
        modern = Topic.objects.create(name="Modern", parent=phys, description="Concerned more with the behavior of matter under extreme conditions or on a very small scale")



        #eduprovider
        uiuc = EduProvider.objects.create(name = "University of Illinois Urbana-Champaign", url = "http://illinois.edu", description = "It's alright")
        coursera = EduProvider.objects.create(name = "Coursera", url = "https://www.coursera.org/", description = "It's alright")
        yale = EduProvider.objects.create(name = "yale", url ="http://www.yale.edu/", description="We are yale, is exactly what Yale would say.")
        mycodeschool = EduProvider.objects.create(name = "mycodeschool", url = "http://www.mycodeschool.com/", description = "Good person")
        andrewhickson = EduProvider.objects.create(name="YouTube - andrewhickson", url="https://www.youtube.com/channel/UC3bsBSHWNrP3ni07NDrJ5hQ", description="Random YouTuber")
        wikipedia = EduProvider.objects.create(name="Wikipedia", url="https://en.wikipedia.org/", description="The Free Encyclopedia")
        mike = EduProvider.objects.create(name="YouTube - Mike Sambol", url="https://www.youtube.com/channel/UCzDJwLWoYCUQowF_nG3m5OQ")
        stanford = EduProvider.objects.create(name="Stanford", url="https://www.stanford.edu")
        chainthat = EduProvider.objects.create(name="YouTube - Chainthat", url="https://www.youtube.com/channel/UCanQY4BfDIgcFzjQF7_Cuyg")
        asapscience = EduProvider.objects.create(name="YouTube - AsapSCIENCE", url="https://www.youtube.com/user/AsapSCIENCE")
        minphys = EduProvider.objects.create(name="YouTube - MinutePhysics", url="https://www.youtube.com/channel/UCUHW94eEFW7hkUMVaZz4eDg")


        #edusources
        uiuc_math_531_fa2015 = EduSource.objects.create(name = "Analytical Number Theory Math 531 UIUC", type = "Notes and Problem Sets", url = "http://www.math.illinois.edu/~berndt/math531.html",provider=uiuc)
        cera_crypt = EduSource.objects.create(name = "Cryptography I: Stanford University", type = "Full Course", url = "https://www.coursera.org/learn/crypto",provider=coursera)
        ytbst = EduSource.objects.create(name = "Data Structures: Binary Search Trees", type = "Online Video", url = "https://www.youtube.com/watch?v=pYT9F8_LFTM",provider=mycodeschool)
        ytrieman = EduSource.objects.create(name = "The Riemann Hypothesis", type = "Lecture Video", url = "https://www.youtube.com/watch?v=yhtcJPI6AtY",provider=yale)
        wikimst = EduSource.objects.create(name="Minimum Spanning Trees", type="Wiki", url="https://en.wikipedia.org/wiki/Minimum_spanning_tree", provider=wikipedia)
        ytPrimAlgo = EduSource.objects.create(name="Prim's Algorithm", type="Video", url="https://www.youtube.com/watch?v=BtGuZ-rrUeY", provider=andrewhickson)
        wikiPrimAlgo = EduSource.objects.create(name="Prim's algorithm", type="Wiki", url="https://en.wikipedia.org/wiki/Prim%27s_algorithm", provider=wikipedia)
        ytKruskalAlgo = EduSource.objects.create(name="Kruskal's algorithm in 2 minutes", type="Video", url="https://www.youtube.com/watch?v=71UQH7Pr9kU", provider=mike)
        wikiFFA = EduSource.objects.create(name="Ford-Fulkerson algorithm", type="Wiki", url="https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm", provider=wikipedia)
        stanGraph = EduSource.objects.create(name="Basic Graph Algorithms", type="PDF", url="https://web.stanford.edu/class/cs97si/06-basic-graph-algorithms.pdf", provider=stanford)
        ytmerkle = EduSource.objects.create(name="Blockchain Basics Explained - Hashes with Mining and Merkle trees", type="Video", url="https://www.youtube.com/watch?v=lik9aaFIsl4", provider=chainthat)
        ytmotivation = EduSource.objects.create(name="The Science of Motivation", type="Video", url="https://www.youtube.com/watch?v=pZT-FZqfxZA", provider=asapscience)
        ytcolor = EduSource.objects.create(name="Computer Color is Broken", type="Video", url="https://www.youtube.com/watch?v=LKnqECcg6Gw", provider=minphys)
        wikigravwaves = EduSource.objects.create(name="Gravitational Waves", type="Wiki", url="https://en.wikipedia.org/wiki/Gravitational_wave", provider=wikipedia)
        
        #covertopics
        CoveredTopic.objects.create(topic=crypt,edusource=cera_crypt)
        CoveredTopic.objects.create(topic=analytical_numb,edusource=uiuc_math_531_fa2015)
        CoveredTopic.objects.create(topic=number_theory,edusource=ytrieman)
        CoveredTopic.objects.create(topic=bst,edusource=ytbst)
        CoveredTopic.objects.create(topic=mintree, edusource=wikimst)
        CoveredTopic.objects.create(topic=prims, edusource=ytPrimAlgo)
        CoveredTopic.objects.create(topic=prims, edusource=wikiPrimAlgo)
        CoveredTopic.objects.create(topic=kruskal, edusource=ytKruskalAlgo)
        CoveredTopic.objects.create(topic=ffa, edusource=wikiFFA)
        CoveredTopic.objects.create(topic=graphAlgo, edusource=stanGraph)
        CoveredTopic.objects.create(topic=blockchain, edusource=ytmerkle)
        CoveredTopic.objects.create(topic=bchem, edusource=ytmotivation)
        CoveredTopic.objects.create(topic=graphics, edusource=ytcolor)
        CoveredTopic.objects.create(topic=modern, edusource=wikigravwaves)


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

        #ratings
        rate1 = Rating.objects.create(review="This course taught me I have a big weeeeeweeeee",stars=4,poster=upost.profile,source=cera_crypt)
       
        #uiuc_math_531_fa2015.number_theory.add()
    def handle(self, *args, **options):
        self._create_topics()