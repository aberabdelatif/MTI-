#!/usr/bin/env python
# -*- coding: utf-8 -*-
# mvc-ann.py

directory = [
    {"firstname":'Ahmed', "familyname":'Mahdi', 'tel':'0778787887'},
    {"firstname":'Mohamed', "familyname":'Mahdi','tel':'0778787887'},
    {"firstname":'Mounir', "familyname":'Katibi','tel':'0778787887'},
    {"firstname":'Noui', "familyname":'Brahimi','tel':'0778787887'},
]

def main():
    print("Finding a telephone")
    familyname = input("Give a family name: ")
    
    nb_found = 0
    for person in directory:
        if person['familyname'] == familyname:
            print(familyname, person['firstname'], person['tel'])
            nb_found += 1
    if nb_found == 0:
        print(f"This familyname {familyname} doesn't exist")

if __name__ == '__main__':
    main()
