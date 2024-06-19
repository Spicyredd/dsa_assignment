import re
from murmur import murmurhash3_16

class Node:
    def __init__(self, word, position):
        self.word = word
        self.position = position
        self.next = None

class WordRep:

    def __init__(self, size = 33554432):
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
                index += 1
            self.coll_words.add(node.word)

    def replace(self):
        word = input('Enter a word: ').lower()
        index = self.search(word)
        if index:
            word_to_replace = input('Enter new word: ')
            index2 = self.search(word, replace = True)  
            counter = 0
            for data in self.table[index]:
                if counter > 3:
                    print('Error')
                counter += 1
                data.word = word_to_replace
                self.table[index2].append(data)
            print(f'{word} was replaced with {word_to_replace}')
            del self.table[index]   
            
    def print_pos(self):
        word = input('Enter a word: ').lower()
        index = self.search(word)
        if index:
            for data in self.table[index]:
                assert data.word == word
                print(data.position)
            print(f'Reoccurance:{len(self.table[index])}')
    
    def search(self, word = False, replace = False):
        index = self.hash_function(word.lower())
        if self.table[index] == []:
            if replace:
                print(f'The {word} is not found in the text.') 
                return 
            else:
                return index
                
        while self.table[index]:
            if self.table[index][0].word.lower() == word:
                assert self.table[index][0].word.lower() == word
                return index
            else:
                index += 1
                
    
    def output(self):
        var = ''
        temp = self.first
        counter = 0
        while temp != None:
            var += f'{temp.word} '
            temp = temp.next
            counter += 1
            print(counter)
        assert temp == None  
        word_name = input('Enter the name of new text file: ')
        with open(f'{word_name}.txt', 'w', encoding='utf-8') as f:
            f.write(var)
            
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
    user_choice = input('1. Find\n2. Replace\n3. Output\n4. Quit\n')
    if user_choice == '1':
        wordrep.print_pos()
    elif user_choice == '2':
        wordrep.replace()
    elif user_choice == '3':
        wordrep.output()
        break
    elif user_choice == '4':
        break