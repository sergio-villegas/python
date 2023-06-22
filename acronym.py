"""
package com.pferruzco.interview.two

/*
Given a phrase convert it into its acronym
Eg: “Three Letter Acronyms” -> “TLA”
*/
fun getAcronym(title: String): String {
    //TODO: write your code here!
    return ""
}
"""
phrase = "Three Letter Acronyms"

def getAcronym(phrase):
    acronym = ""

    phrase = phrase.split()
    for x in phrase:
        acronym = acronym + x[0] 

    return acronym

print(getAcronym(phrase))