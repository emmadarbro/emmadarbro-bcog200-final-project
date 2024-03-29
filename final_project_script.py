import pandas as pd

def compute_score_difference(user_profile, profiles):
  
    score_differences = {}
    for key in user_profile.keys():
        if key == 'name':
            continue
        user_score = user_profile[key]
        profile_scores = [profile[key] for profile in profiles]
        differences = [abs(user_score - score) for score in profile_scores]
        score_differences[key] = differences
    
    return score_differences
def compute_weighted_differences(score_differences, importance_list):
    
    weighted_differences = {}
    for key, differences in score_differences.items():
        weighted_differences[key] = [difference * importance_list[key] for difference in differences]
    
    return weighted_differences

def compute_similarity(user_profile, profiles, importance_list):
    """
    computes the similarity score between user's profile and other profiles in the profile pool
    """

    similarity_scores = []
    score_differences = compute_score_difference(user_profile, profiles)
    weighted_differences = compute_weighted_differences(score_differences, importance_list)
    
    for i, profile in enumerate(profiles):
        similarity_score = sum(weighted_differences[key][i] for key in weighted_differences.keys())
        similarity_scores.append((similarity_score, profile))
    
    return similarity_scores

def store_profile(user):
    """
   this is where users "set up" their profile by inputing integer answers to the following survey questions that are appended to the respoective lists for comparison in the main function
    """
    print(f"Welcome, {user}! Please answer the following survey questions to create your profile.")
    
    age = int(input("Please list your age in years: "))
    height = int(input("Please list your height in inches: "))
    distance = float(input("Please list your (mailing address) distance from the Illini Union in miles (fractions of miles are fine): "))
    social_outings = int(input("In the average week, how many times do you go out to bars, clubs, shows, etc? "))
    texts_sent = int(input("In the past 24 hours, how many individual/different people did you text? "))
    income = int(input("How much money do you hope to make when you graduate from UIUC (in USD)? "))
    attractiveness = int(input("On a scale of 1-10 with 1 being the least, how attractive do you think you are? "))
    calls_to_mom = int(input("How many times a month do you call your mom? "))
    
    profile = {
        'name': user,
        'age': age,
        'height': height,
        'distance': distance,
        'social_outings': social_outings,
        'texts_sent': texts_sent,
        'income': income,
        'attractiveness': attractiveness,
        'calls_to_mom': calls_to_mom
    }
    
    return profile
    def rank_importance(profile_categories):
    """
    user ranks the importance of each category so that it may be multiplied by the difference amongst scores to calculate magnitide of similarity
    
    """
    importance_dict = {}
    print("Great! Thank you! In the next set of questions we will ask you to rank how important the following qualities in a partner are to YOU on a scale of 1-10 with 1 being the least important attributes and 10 being the most imporant.")
    print("Please rank the importance of each category:")
    for category in profile_categories:
        importance = int(input(f"How important is {category.replace('_', ' ')} to you? "))
        importance_dict[category] = importance
    
    return importance_dict
def main(profiles, similarity_scores):
    #make example profiles with the below format:
     profiles = [
        {'name': 'Becky', 'age': 20, 'height': 50, 'distance': 0.9, 'social_outings': 1, 'texts_sent': 19, 'income': 90000, 'attractiveness': 6, 'calls_to_mom': 3},
    ]  
    
    similarity_scores = compute_similarity(user_profile, profiles, importance_list)
    
    # returns the similary score for each profile
    print("Similarity scores:")
    for score, profile in similarity_scores:
        print(f"Similarity score with {profile['name']}: {score}")