#final_project_script.py
def convert_range_to_number(value):
    # this function converts the a/b/c range values for numbers to be able to compute the difference between profiles
    if value == 'a':
        return 1
    elif value == 'b':
        return 2
    elif value == 'c':
        return 3
    else:
        return 0  



def compute_similarity(user_profile, initial_profiles):

    #function calculates the differences between inputed user values and stored profile values for each category and then multiplies them by the user weight for importance

    similarity_scores = []
    user_weights = user_profile['weights']
    for profile in initial_profiles:
        profile_weights = profile['weights']
        score = 0
        #uses the defined keys of profile chaaracterisitscs so the differences are calculated separate from others, and the correct weights are applied
        for key, value in user_profile.items():
            if key in profile and key != 'name' and key != 'weights':
                if key in ['age','distance', 'social_outings', 'text_sent', 'income', 'attractiveness' 'calls_to_mom']:
                    user_value = convert_range_to_number(value)
                    profile_value = convert_range_to_number(profile[key])
                    #calculates the absolute difference between the user input and the stored profile values for each profile
                    difference = abs(user_value - profile_value) * user_weights[key]  # applies the users selected importance weight
                else:
                    difference = abs(value - profile[key]) * user_weights[key]  #for categories not aligned, calculate those separately
                score += difference
        similarity_scores.append((score, profile)) #stores the similarity score with the respective profile

    similarity_scores.sort(key=lambda x: x[0])
    #show similarity scores from lowest to highest
    return similarity_scores

def store_profile():
    """
    This is where users "set up" their profile by inputting integer answers to the following survey questions 
    that are appended to the respective lists for comparison in the main function.
    """
    print("Welcome to Brain Bae; where the Brain and Cognitive Science students of UIUC find you a bae! Below you will be asked a series of numerical questions related to some components that we will use to test your compatability with others in our candidate pool.")
    user = input("Please enter your name: ")
    print(f"Welcome, {user}! Please answer the following survey questions to help set up your profile!")
    while True:
        try:
            age = int(input("Please list your age in years: "))
            break  # exit loop is number is an integer
        except ValueError:
            print("Please enter a valid age (numeric value).")

    while True:
        try:
            height = int(input("Please list your height in inches: "))
            break  # exit loop if number is valid
        except ValueError:
            print("Please enter a valid height (numeric value).")
    valid_distance_options = {'a', 'b', 'c'}
    while True:
        distance = input("Please select the distance range from your current mailing address to the Illini Union in miles: \n\
                      a) Less than 1 mile \n\
                      b) 1-3 miles \n\
                      c) More than 3 miles \n\
                      Enter your choice (a/b/c): ").lower()
        if distance in valid_distance_options:
            break #exit loop if valid letter
        else:
            print("Please enter a valid option (a/b/c).")

    valid_social_options = {'a', 'b', 'c'}
    while True:
        social_outings = input("Please select the approriate range for the number of social outings you attended in an average week (going out to bars, club events, shows, etc): \n\
                            a) 0-2 times \n\
                            b) 3-5 times \n\
                            c) More than 5 times \n\
                            Enter your choice (a/b/c): ").lower()
        if social_outings in valid_social_options:
            break
        else:
            print("Please enter a valid option (a/b/c).")
    
    valid_text_options = {'a', 'b', 'c'}
    while True:
        text_sent = input("Please select the appropriate range for the number of individual people you have sent texts to in past 24 hours: \n\
                        a) 0-5 people \n\
                        b) 6-10 people \n\
                        c) More than 10 people \n\
                        Enter your choice (a/b/c): ").lower()
        if text_sent in valid_text_options:
            break
        else:
            print("Please enter a valid option (a/b/c).")
    valid_income_options = {'a', 'b', 'c'}
    while True:
        income = input("Please select your predicted/ desired income range when you graduate from UIUC: \n\
                     a) Less than $50,000 \n\
                     b) $50,000-$100,000 \n\
                     c) More than $100,000 \n\
                     Enter your choice (a/b/c): ").lower()
        if income in valid_income_options:
            break
        else:
            print("Please enter a valid option (a/b/c).")
    
    attractiveness = int(input("On a scale of 1-10 with 1 being the least, how attractive do you think you are? "))
    valid_calls_to_mom_options = {'a', 'b', 'c'}
    while True:
        calls_to_mom = input("Please select the range that best matches the number of calls you make to your mom in an average month: \n\
                              a) 0-2 times \n\
                              b) 3-5 times \n\
                              c) More than 5 times \n\
                              Enter your choice (a/b/c): ").lower()
        if calls_to_mom in valid_calls_to_mom_options:
            break
        else:
            print("Please enter a valid option (a/b/c).")
    print(f"Thanks {user}! We will now compare your responses to others in our candidate pool based on the importance each of these factors")
    print("Now, please rank the importance of each variable on a scale of 1 to 10:")
    weights = {}
    weights['age'] = int(input("How important is age similarity to you? (1-10): "))
    weights['height'] = int(input("How important is height similarity to you? (1-10): "))
    weights['distance'] = int(input("How important is distance similarity to you? (1-10): "))
    weights['social_outings'] = int(input("How important is sociability similarity to you? (1-10): "))
    weights['text_sent'] = int(input("How important is extroversion similarity to you? (1-10): "))
    weights['income'] = int(input("How important is income similarity to you? (1-10): "))
    weights['attractiveness'] = int(input("How important is attractiveness similarity to you? (1-10): "))
    weights['calls_to_mom'] = int(input("How important is familiy closeness similarity to you? (1-10): "))
    
    profile = {
        'name': user,
        'weights':weights,
        'age': age,
        'height': height,
        'distance': distance,
        'social_outings': social_outings,
        'text_sent': text_sent,
        'income': income,
        'attractiveness': attractiveness,
        'calls_to_mom': calls_to_mom,
        'weights': weights 
        }
    
    return profile
    
    


def main():
    user_profile = store_profile()
    # initial profiles are defined and the weights are assigned based on the categories
    initial_profiles = [
        {'name': 'Noah', 'age': 20, 'height': 50, 'distance': 1, 'social_outings': 1, 'income': 3, 'attractiveness': 6, 'text_sent': 1,
         'weights': {'age': 2, 'height': 6, 'distance': 2, 'social_outings': 2, 'income': 3, 'attractiveness': 2, 'text_sent': 2}},

        {'name': 'Riley', 'age': 25, 'height': 68, 'distance': 2, 'social_outings': 2, 'income': 2, 'attractiveness': 8, 'text_sent': 1,
         'weights': {'age': 7, 'height': 9, 'distance': 8,  'social_outings': 7, 'income': 5, 'attractiveness': 6, 'text_sent': 4}},

        {'name': 'Alex', 'age': 19, 'height': 58, 'distance': 3, 'social_outings': 3, 'income': 1, 'attractiveness': 7, 'text_sent': 2,
         'weights': {'age': 1, 'height': 3, 'distance': 3, 'social_outings': 4, 'income': 8, 'attractiveness': 9, 'text_sent': 5}},

        {'name': 'Quinn', 'age': 22, 'height': 65, 'distance': 1, 'social_outings': 1, 'income': 2, 'attractiveness': 3, 'text_sent': 3,
         'weights': {'age': 5, 'height': 7, 'distance': 1,  'social_outings': 3, 'income': 7, 'attractiveness': 4, 'text_sent': 7}},

        {'name': 'Taylor', 'age': 18, 'height': 61, 'distance': 2, 'social_outings': 3, 'income': 1, 'attractiveness': 5, 'text_sent': 2,
         'weights': {'age': 4, 'height': 2, 'distance': 4, 'social_outings': 9, 'income': 4, 'attractiveness': 5, 'text_sent': 9}},

        {'name': 'Rowan', 'age': 24, 'height': 60, 'distance': 3, 'social_outings': 3, 'income': 1, 'attractiveness': 6, 'text_sent': 2,
         'weights': {'age': 3, 'height': 5, 'distance': 9, 'social_outings': 6, 'income': 6, 'attractiveness': 3, 'text_sent': 6}},

        {'name': 'Dakota', 'age': 23, 'height': 68, 'distance': 3, 'social_outings': 3, 'income': 3, 'attractiveness': 9, 'text_sent': 1,
         'weights': {'age': 4, 'height': 6, 'distance': 8, 'social_outings': 3, 'income': 6, 'attractiveness': 9, 'text_sent': 5}},
       
    ]

    
    similarity_scores = compute_similarity(user_profile, initial_profiles)
    similarity_scores.sort(key=lambda x: x[0])
    
    
    # this print statement will return the profiles and the difference amongst them, where the lowest scores are the most similar and the highest score are the most different
    print("Similarity scores:")
    for score, profile in similarity_scores:
        print(f"Similarity score with {profile['name']}: {score}")



	

if __name__ == "__main__":
    main()
