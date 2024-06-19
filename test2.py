import re
from murmur import murmurhash3_16

class Node:
    def __init__(self, word, position):
        self.word = word
        self.position = position
        self.next = None

class WordRep:

    def __init__(self, size =  33554432):
        self.first = None
        self.size = size
        self.table = [[] for _ in range(size)]
        self.coll_words = set()
        
    def hash_function(self, word):
        assert murmurhash3_16(word) < self.size
        return murmurhash3_16(word)

    def insert(self, node):
        assert True == isinstance(node, Node)
        index = self.hash_function(node.word)    
        while True:
            if self.table[index] == [] or self.table[index][0].word == node.word:
                assert self.table[index] == [] or self.table[index][0].word.lower() == word
                self.table[index].append(node)
                break
            else:
                index2 = self.hash_function(node.word[::-1])
                if self.table[index2] == [] or self.table[index2][0].word == node.word:
                    assert self.table[index2] == [] or self.table[index2][0].word.lower() == word
                    self.table[index2].append(node)
                    break
            index += 1
            index2 += 1
            self.coll_words.add(node.word)

    def replace(self):
        index = self.search()
        if index:
            word = self.table[index][0].word
            word_to_replace = input('Enter new word: ')
            index2 = self.search(word_to_replace, search_p = True)   
                
            for data in self.table[index]:
                data.word = word_to_replace
                self.table[index2].append(data)
            print(f'{word} was replaced with {word_to_replace}')
            self.table[index].clear()
            
    def print_pos(self):
        word = input('Enter a word: ')
        index = self.search(word, search_p = True)
        if index:
            for data in self.table[index]:
                assert data.word == word
                print(data.position)
            print(f'Reoccurance:{len(self.table[index])}')
    
    def search(self, word = False,  search_p = False):
        if word == False:
            word = input('Enter a word: ')  
        index = self.hash_function(word.lower())
        if self.table[index] == []:
            print(f'The {word} is not found in the text.') 
            return
        alt_word = word[::-1]
        
        if search_p:
            while self.table[index]:
                if self.table[index][0].word.lower() == word:
                    assert self.table[index][0].word.lower() == word
                    return index
                else:
                    index2 = self.hash_function(alt_word.lower())
                    if self.table[index2][0].word.lower() == word:
                        assert self.table[index2][0].word.lower() == word
                        return index
            index += 1
            index2 += 1
        else:
            while self.table[index]:
                if self.table[index][0].word.lower() == word or self.table[index] == []:
                    assert self.table[index][0].word.lower() == word or self.table[index] == []
                    return index
                else:
                    index2 = self.hash_function(alt_word.lower())
                    if self.table[index2][0].word.lower() == word or self.table[index2] == []:
                        assert self.table[index2][0].word.lower() == word or self.table[index2] == []
                        return index
            index += 1
            index2 += 1
                
    
    def output(self):
        var = ''
        temp = self.first
        while temp != None:
            var += f'{temp.word} '
            temp = temp.next  
        assert temp == None
        word_name = input('Enter the name of new text file: ')
        with open(f'{word_name}.txt', 'w', encoding='utf-8') as f:
            f.write(var)
            print('File creation complete exiting....')
                    
wordrep = WordRep()      

with open('output.txt', 'r', encoding='utf-8') as file:
    text = file.read().lower()
    words = re.findall(r'\b\w+\b', text)
    temp = None
    check = ''
    for position, word in enumerate(words, start=1):
        node = Node(word, position)
        wordrep.insert(node)
        if position == 1:
            wordrep.first = node
            check = node
        else:
            temp.next = node
        assert check == wordrep.first
        temp = node
    print(f'Collisions: {len(wordrep.coll_words)}')
        
while True:
    print('Choose one option:')
    user_choice = input('1. Find\n2. Replace\n3. Output\nEnter any key to quit\n')
    if user_choice == '1':
        wordrep.print_pos()
    elif user_choice == '2':
        wordrep.replace()
    elif user_choice == '3':
        wordrep.output()
        break
    else:
        break