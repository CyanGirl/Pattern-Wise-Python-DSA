'''
PROBLEM STATEMENT:
Given all files in the system, return absolute path for given array of selected files with following condition

- If all files are selected in folder, return path to the folder, otherwise
- Return absolute path for the selected files.
Example:

String[] allFiles = {
	"/home/user/documents/file1.txt",
	"/home/user/documents/file2.txt",
	"/home/user/pictures/photo1.jpg",
	"/home/user/documents/report.doc"
};
		
String[] selectedFiles = {
	"/home/user/documents/file1.txt",
	"/home/user/documents/report.doc",
	"/home/user/pictures/photo1.jpg"
};

Output:
[/home/user/documents/file1.txt, /home/user/pictures, /home/user/documents/report.doc]

'''


######### solution with dictionary ##########
# idea is to group all the files together acc their dirs. then check if they are all selected #

from collections import defaultdict

def selectFiles_dict(allFilesList, selectFilesList):
    allFiles = defaultdict(set)
    for file in allFilesList:
        d, f = file.rsplit('/', 1)[0], file.rsplit('/', 1)[1]
        allFiles[d].add(f)
    selFiles = defaultdict(set)
    for file in selectFilesList:
        d, f = file.rsplit('/', 1)[0], file.rsplit('/', 1)[1]
        selFiles[d].add(f)
    ans = []
    for d in selFiles:
        if len(selFiles[d]) == len(allFiles[d]):
            ans.append(d)
        else:
            for file in selFiles[d]:
                ans.append(d+'/'+file)
    return ans
    


######### solution with Trie ##########

class Node:
    def __init__(self) -> None:
        self.dirs = {} # total we will get from this
        self.selected = 0
        self.isFile = False


def selectFiles_trie(allFilesList, selectFilesList):

    trie= Node()

    # make trie
    for temp in allFilesList:
        files = temp.split("/")
        cur=trie
        for file in files:
            if not file: continue
            if file not in cur.dirs:
                cur.dirs[file]=Node()
            cur=cur.dirs[file]
        cur.isFile=True

    # mark selected
    for temp in selectedFilesList:
        files = temp.split("/")
        cur=trie
        prev=None
        for file in files:
            if not file: continue
            prev=cur
            cur=cur.dirs[file]
        
        prev.selected+=1

    res = []
    for temp in selectedFilesList:
        files = temp.split("/")
        cur=trie
        path=""
        for file in files:
            if not file: continue
            if cur.selected == len(cur.dirs):
                res.append(path)
                path=""
                break
            path+="/"+file
            cur=cur.dirs[file]
        if path: res.append(path)

    return res



allFilesList = [
	"/home/user/documents/file1.txt",
	"/home/user/documents/file2.txt",
	"/home/user/pictures/photo1.jpg",
	"/home/user/documents/report.doc"
]
		
selectedFilesList = [
	"/home/user/documents/file1.txt",
    "/home/user/documents/file2.txt",
	"/home/user/documents/report.doc",
	"/home/user/pictures/photo1.jpg"
]

#print(selectFiles_dict(allFilesList, selectedFilesList))
#print(selectFiles_trie(allFilesList,selectedFilesList))

