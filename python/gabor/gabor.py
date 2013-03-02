#!/usr/bin/env python

import json;
import random;
from string import Template
def main():    
    quotes = read_Quotes()    
    name = raw_input("Your name:")
    sub = {"name" : name }    
    
    while True:        
        choice = raw_input("What do you want to do (ask, add)")        
        if choice == "ask":
            while True:
                question = raw_input("")
                if question == "exit":               
                    break                
                print Template(quotes[random.randint(0, len(quotes)-1)]).substitute(sub)    
        
        elif choice == "add":
            while True:
                quote = raw_input("Write a quote you want to add (or exit to exit)")
                if quote == "exit":
                    write_Quotes(quotes)
                    break
                else:
                    quotes.append(quote)
        elif choice == "exit":
            break

def write_Quotes(quotes):
    with open("x.txt", 'w+') as f:
        f.write(json.dumps(quotes))

def read_Quotes():
    with open("x.txt", 'r') as f:
        return json.loads(f.read())

if __name__ == '__main__':
    main()
