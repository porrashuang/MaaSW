import time
from enum import Enum

def how_to_squat():
    print("1. Inhale until your abdominal is full to support your lower back.")
    print("2. Squat with exhale and use your core muscles.")
    print("3. Imagine your coccyx is lowering and make sure your lower back doesn't bend forward.")
    print("4. Stand up with a breath and hip tilt forward.")
    
def start_focused_work():
    print("Imagine yourself as an expert in the work you are about to do.")
    time.sleep(5) # sleep for 5 second to give time to imagine
    print("Starting brown noise https://www.youtube.com/watch?v=RqzGzwTY-6w.") 


def set_next_goal(goal_type):
    print("Creating a mind map with a word in the center...")
    mind_map_center = input("Enter the word in the center of the mind map: ")
    print(f"Word in the center of the mind map: {mind_map_center}")
    print("Linking at least two layers of more words...")
    layer1_words = input("Enter the words in the first layer: ").split(",")
    print(f"Words in the first layer: {layer1_words}")
    layer2_words = input("Enter the words in the second layer: ").split(",")
    print(f"Words in the second layer: {layer2_words}")
    print("Circle a few words you're interested in...")
    interested_words = input("Enter the words you're interested in: ").split(",")
    print(f"Words you're interested in: {interested_words}")
    if goal_type == "extreme":
        goal_duration = "within 3 months"
    elif goal_type == "long term":
        goal_duration = "achievable to continue"
    print(f"Goal type: {goal_type}, Duration: {goal_duration}")
    ikigai_score = calculate_ikigai()
    print(f"Ikigai score: {ikigai_score}")

def calculate_ikigai():
    print("Calculating Ikigai...")
    passion = input("What are you passionate about? ")
    mission = input("What is your mission in life? ")
    profession = input("What is your profession? ")
    vocation = input("What is your vocation? ")
    ikigai_score = (passion + mission + profession + vocation) / 4
    return ikigai_score

def how_to_dolphin_kick():
    print("How to do the dolphin kick:")
    print("1. Raise your hips up when your feet kick down.")
    print("2. Lower your hips when your feet rise up.")
    print("3. Speed up the kicking motion to increase your speed.")

def how_to_flip_turn():
    print("How to do a flip turn:")
    print("1. Keep your palms against your hips.")
    print("2. When you see the end of the pool edge, tuck your chin to your chest.")
    print("3. Flip quickly until your face is facing up.")
    print("4. Straighten your back.")
    print("5. Kick your feet against the T printed on the wall.")
    print("6. Perform a drill turn until you're facing down.")
    how_to_dohpin_kick()

def how_to_transform_knowledge_to_action():
    print("How to transform knowledge to action:")
    print("1. Admit that knowledge and short-term action are both emotions.")
    print("2. Start with very small actions to create neural pathways in your brain.")
    print("3. Visualize the action you want to take to overcome any current incentives that may be holding you back.")



