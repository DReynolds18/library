# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 20:19:14 2022

@author: dreynolds18
"""

classes = {
           36303: 'Introduction to Logic',
           36169: 'College Algebra for Lib Arts',
           }

def add_class(CRN, Description):
    
    classes.update({CRN: Description})
    
def print_class(CRN):
    
    if CRN in classes:
        print(classes[CRN])
    else:
        print(f"No Course {CRN} classes taken.")
    
#####################################################################      

if __name__ == '__main__':
    
    add_class(70406, "Microcomputer Operating System")
    add_class(78221, "Introduction to Programming and Algorithms")
    add_class(70436, "Introduction to C Programming")
    add_class(77693, "Introduction to Python Programming")
    
    print_class(70406)
    print_class(78221)
    print_class(70436)
    print_class(77693)
    
    print_class(99999)
    
    