'''
Suppose we are creating a string replacement library. Given a map of string replacements, replace the value in the input string

Given map {X=>123, Y=456}
Input: %X%_%Y%
Output: 123_456

Given map {USER=>admin, HOME=>/%USER%/home}
Input: I am %USER% My home is %HOME%
Output: I am admin My home is /admin/home

'''

from collections import defaultdict

def string_replace(library: dict, sentence: str):
    
    # build the graph
    indegree = defaultdict(int)
    adj = defaultdict(list)
    for key1,val1 in library.items():
        for key2,val2 in library.items():
            if key1==key2: continue

            if f"%{key1}%" in val2:
                adj[key1].append(key2)
                indegree[key2]=indegree.get(key2,0)+1

    q=[]
    for key in library:
        if indegree.get(key,0)==0:
            q.append(key)
    if len(q)<1 and len(library)>0: return "String Cannot be Replaced!"

    while q:
        curnode = q.pop(0)

        for nei in adj.get(curnode,[]):
            indegree[nei]-=1
            tempvar=library[nei].replace(f"%{curnode}%",library[curnode])
            library[nei]=tempvar # syntax <text>.replace(pattern,to_replace)

            if indegree[nei]==0: # add when dependencies are over
                q.append(nei)

    for key,val in library.items():
        if f"%{key}%" in sentence:
            tempvar=sentence.replace(f"%{key}%", val)
            sentence=tempvar

    return sentence


#print(string_replace({"USER":"admin", "HOME":"/%USER%/home"},"I am %USER% My home is %HOME%"))



def test_string_replace():
    test_cases = [
        ({"X": "123", "Y": "456"}, "%X%_%Y%", "123_456"),
        ({"USER": "admin", "HOME": "/%USER%/home"}, "I am %USER%. My home is %HOME%", "I am admin. My home is /admin/home"),
        ({"X": "abc", "Y": "def"}, "%X%_%X%_%X%", "abc_abc_abc"),
        ({"X": "%Y%", "Y": "%X%"}, "%X%", "String Cannot be Replaced!"),
        ({"X": "123"}, "", ""),
        ({}, "Hello, %NAME%!", "Hello, %NAME%!"),
        ({"X": "%Y%", "Y": "%Z%", "Z": "%X%"},"%X%","String Cannot be Replaced!"),
        ({"A": "%B%","B": "%C%","C": "%D%","D": "%E%","E": "%F%","F": "%G%","G": "%H%","H": "%I%","I": "123"},"%A%","123")
    ]

    for i, (library, sentence, expected_output) in enumerate(test_cases):
        print(f"Test case {i+1}:")
        print("Library:", library)
        print("Sentence:", sentence)
        output = string_replace(library, sentence)
        print("Output:", output)
        assert output == expected_output
        print("Test Passed!\n")

test_string_replace()
   


    



