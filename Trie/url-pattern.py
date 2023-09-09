'''
Given a list of patterns and a URL, find the most matching pattern for the URL.
Exanple: url = https://google.com/about/careers/jobs?location=London
patterns = [
    "about/careers/j*",
    "about/careers/jobs?loca*",
    "about/care/cloud*",
]

Answer :  "about/careers/jobs?loca*"
Note: careers* does not match with careers/jobs but matches with careersjobs if it was this.
Solve with Trie

'''

class Node:
    def __init__(self) -> None:
        self.children = {}
        self.isParam = False
        self.isEnd = False

def extend_params(cur,params):
    for ch in params:
        if ch not in cur.children:
            cur.children[ch]=Node()
        cur=cur.children[ch]
        cur.isParam=True
    cur.isEnd = True

def match_url(url,patterns):

    trie= Node()

    # building trie with all the patterns
    for pattern in patterns:
        temp=pattern.split("/")
        cur=trie
        for idx,node in enumerate(temp):
            if idx==len(temp)-1:
                extend_params(cur,node)
            else:
                if node not in  cur.children:
                    cur.children[node]=Node()
                cur=cur.children[node]
    
    # search for the longest pattern which match with the url
    url=url.split(".")[1].split("/")[1:] # about/careers/jobs?location=London
    path = ""
    cur=trie

    for idx, node in enumerate(url):
        if idx==len(url)-1:
            break
        
        if node not in cur.children:
            return
        path+="/"+node
        cur=cur.children[node]

    for ch in url[-1]:
        if ch not in cur.children:
            if "*" not in cur.children: return 
            path+="*"
            return path
        
        path+=ch
        cur=cur.children[ch]

    return path if cur.isEnd else None

    
        
url = "https://google.com/about/careers/jobs?location=London"
patterns = [
    "about/careers*",
    "about/careers/jobs?location=Londo*",
    "about/care/cloud*",
]

print(match_url(url,patterns))

# time complexity : O(mk) where m = length of patterns and k is max length of a pattern

