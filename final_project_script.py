def convert_range_to_number(value):
    """
    Function converts survey range values a,b,c to integers to compute the numerical similarity between user and stored profiles
    """
    if value == 'a':
        return 1
    elif value == 'b':
        return 2
    elif value == 'c':
        return 3
    else:
        return 0 


def compute_similarity(user_profile, initial_profiles):
    """
    Compute similarity scores between user profile and initial profiles.
    """
    similarity_scores = []
    user_weights = user_profile['weights']
    for profile in initial_profiles:
        profile_weights = profile['weights']
        score = 0
        for key, value in user_profile.items():
            if key in profile and key != 'name' and key != 'weights':
                if key in ['distance', 'social_outings', 'texts_sent', 'income', 'calls_to_mom']:
                    user_value = convert_range_to_number(value)
                    profile_value = convert_range_to_number(profile[key])
                    difference = abs(user_value - profile_value) * user_weights[key]  # Apply user's weight
                else:
                    difference = abs(value - profile[key]) * user_weights[key]  # Apply user's weight
                score += difference
        similarity_scores.append((score, profile))
    return sorted(similarity_scores)

def store_profile():
    """
    This is where users "set up" their profile by inputting integer answers to the following survey questions 
    that are appended to the respective lists for comparison in the main function.
    """
    user = input("Please enter your name: ")
    print(f"Welcome, {user}! Please answer the following survey questions to create your profile.")
    while True:
        try:
            age = int(input("Please list your age in years: "))
            break  # If conversion is successful, exit the loop
        except ValueError:
            print("Please enter a valid age (numeric value).")

    while True:
        try:
            height = int(input("Please list your height in inches: "))
            break  # If conversion is successful, exit the loop
        except ValueError:
            print("Please enter a valid height (numeric value).")
    valid_distance_options = {'a', 'b', 'c'}
    while True:
        distance = input("Please select your distance range from the Illini Union: \n\
                      a) Less than 1 mile \n\
                      b) 1-3 miles \n\
                      c) More than 3 miles \n\
                      Enter your choice (a/b/c): ").lower()
        if distance in valid_distance_options:
            break
        else:
            print("Please enter a valid option (a/b/c).")

    valid_social_options = {'a', 'b', 'c'}
    while True:
        social_outings = input("Please select your social outings range in a week: \n\
                            a) 0-2 times \n\
                            b) 3-5 times \n\
                            c) More than 5 times \n\
                            Enter your choice (a/b/c): ").lower()
        if social_outings in valid_social_options:
            break
        else:
            print("Please enter a valid option (a/b/c).")
    
    valid_texts_options = {'a', 'b', 'c'}
    while True:
        text_sent = input("Please select the appropriate range for the number of people you have sent texts to in past 24 hours: \n\
                        a) 0-5 people \n\
                        b) 6-10 people \n\
                        c) More than 10 people \n\
                        Enter your choice (a/b/c): ").lower()
        if text_sent in valid_texts_options:
            break
        else:
            print("Please enter a valid option (a/b/c).")
    valid_income_options = {'a', 'b', 'c'}
    while True:
        income = input("Please select your income range when you graduate from UIUC: \n\
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
        calls_to_mom = input("Please select the number of calls you make to your mom range in a month: \n\
                              a) 0-2 times \n\
                              b) 3-5 times \n\
                              c) More than 5 times \n\
                              Enter your choice (a/b/c): ").lower()
        if calls_to_mom in valid_calls_to_mom_options:
            break
        else:
            print("Please enter a valid option (a/b/c).")

    print("Now, please rank the importance of each variable on a scale of 1 to 10:")
    weights = {}
    weights['age'] = int(input("How important is age similarity to you? (1-10): "))
    weights['height'] = int(input("How important is height similarity to you? (1-10): "))
    weights['distance'] = int(input("How important is distance similarity to you? (1-3): "))
    weights['social_outings'] = int(input("How important is sociability similarity to you? (1-3): "))
    weights['texts_sent'] = int(input("How important is extroversion similarity to you? (1-3): "))
    weights['income'] = int(input("How important is income similarity to you? (1-3): "))
    weights['attractiveness'] = int(input("How important is attractiveness similarity to you? (1-10): "))
    weights['calls_to_mom'] = int(input("How important is familiy closeness similarity to you? (1-3): "))
    
    profile = {
        'name': user,
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
    #def rank_importance(profile_categories):
    """
    user ranks the importance of each category so that it may be multiplied by the difference amongst scores to calculate magnitide of similarity
    
    
    print("Great! Thank you! In the next set of questions, we will ask you to rank how important it is for the following qualities in a partner to be similar to YOU on a scale of 1-10 with 1 being the least important of similarity and 10 being the most important.")
    importance_dict = {}
    categories = ['age','height', 'distance' ,'extroversion', 'sociability', 'income', 'attractiveness', 'family_closeness']
    for category in categories:
    	importance = int(input(f"How important is partner compatibility in {category.replace('_', ' ')} to you? "))
    	importance_dict[category] = importance


    
    
    profile_weights = {
        'age': 2,
        'height': 6,
        'distance': 8,
        'extroversion': 10,
        'sociability': 7,
        'income': 5,
        'attractiveness': 6,
        'family_closeness': 4
    }
    """
    


def main():
    user_profile = store_profile()
    # Define initial profiles
    initial_profiles = [
        {'name': 'Becky', 'age': 20, 'height': 50, 'distance': 'a', 'social_outings': 'b', 'text_sent': 'a', 'income': 'c', 'attractiveness': 6, 'calls_to_mom': 'a',
         'weights': {'age': 2, 'height': 6, 'distance': 2, 'extroversion': 1, 'sociability': 2, 'income': 3, 'attractiveness': 6, 'family_closeness': 2}},
        {'name': 'John', 'age': 25, 'height': 68, 'distance': 1.5, 'extroversion': 8, 'sociability': 8, 'income': 75000, 'attractiveness': 8, 'family_closeness': 6,
         'weights': {'age': 2, 'height': 6, 'distance': 8, 'extroversion': 10, 'sociability': 7, 'income': 5, 'attractiveness': 6, 'family_closeness': 4}},
        # Add more profiles as needed
    ]
    
    similarity_scores = compute_similarity(user_profile, initial_profiles)
    
    # returns the similarity score for each profile
    print("Similarity scores:")
    for score, profile in similarity_scores:
        print(f"Similarity score with {profile['name']}: {score}")




# Call the main function with the user's profile as an argument

	

if __name__ == "__main__":
    main()
