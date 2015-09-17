from math import sqrt

# create a dictionary of movies ratings and a small 
# set of movies
critics = {
        'Lisa Rose': {
            'Lady in the Water': 2.5,
            'Snakes on a plane': 3.5,
            'Just My Luck': 1.0,
            'Superman Returns': 3.5,
            'You, Me and Dupree': 2.5,
            'The Night Listener': 3.0
        },
        'Gene Seymour': {
            'Lady in the Water': 3.0,
            'Snakes on a plane': 3.4,
            'Just My Luck': 1.5,
            'Superman Returns': 5.0,
            'You, Me and Dupree': 3.5,
            'The Night Listener': 3.0
        },
        'Michael Phillips': {
            'Lady in the Water': 2.5,
            'Snakes on a plane': 3.0,
            'Superman Returns': 3.5,
            'The Night Listener': 4.0
        },
        'Claudia Puig': {
            'Snakes on a plane': 3.5,
            'Just My Luck': 3.0,
            'Superman Returns': 4.0,
            'You, Me and Dupree': 2.5,
            'The Night Listener': 4.5
        },
        'Mick LaSalle': {
            'Lady in the Water': 3.0,
            'Snakes on a plane': 4.0,
            'Just My Luck': 2.0,
            'Superman Returns': 3.0,
            'You, Me and Dupree': 2.0,
            'The Night Listener': 3.0
        },
        'Jack Matthews': {
            'Lady in the Water': 3.0,
            'Snakes on a plane': 4.0,
            'Superman Returns': 5.0,
            'You, Me and Dupree': 3.5,
            'The Night Listener': 3.0
        },
        'Toby': {
            'Snakes on a plane': 4.5,
            'Superman Returns': 1.0,
            'You, Me and Dupree': 4.0,
        },
    }

# Returns a distance based similarity score for person1 and person2
def sim_distance(prefs, person1, person2):
    # Get the list of shared items
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    # if they have no ratings in common return zero
    if len(si) == 0 : return 0
    
    print (si)

    # Add up the squares of all the differences
    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2) for item, _ in si.items()])
    return 1/(1 + sqrt(sum_of_squares))


# print (sim_distance(critics, "Lisa Rose", "Gene Seymour"))