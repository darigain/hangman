import random
import streamlit as st

# List of words
list_of_words = ['apple', 'banana', 'grape', 'orange', 'strawberry', 'pear', 'peach', 'cherry', 'plum', 'kiwi', 
'mango', 'lemon', 'lime', 'pineapple', 'coconut', 'blueberry', 'raspberry', 'blackberry', 'watermelon', 'melon', 
'tiger', 'lion', 'giraffe', 'elephant', 'zebra', 'kangaroo', 'penguin', 'dolphin', 'whale', 'shark', 
'wolf', 'bear', 'fox', 'rabbit', 'deer', 'squirrel', 'monkey', 'parrot', 'owl', 'eagle', 
'computer', 'laptop', 'keyboard', 'mouse', 'monitor', 'printer', 'scanner', 'smartphone', 'tablet', 'camera', 
'television', 'radio', 'speaker', 'headphones', 'microphone', 'guitar', 'piano', 'violin', 'drums', 'trumpet', 
'car', 'truck', 'bicycle', 'motorcycle', 'airplane', 'helicopter', 'train', 'bus', 'subway', 'boat', 
'doctor', 'nurse', 'teacher', 'engineer', 'scientist', 'lawyer', 'policeman', 'firefighter', 'chef', 'pilot', 
'sun', 'moon', 'star', 'planet', 'comet', 'asteroid', 'galaxy', 'universe', 'earth', 'mars', 
'chair', 'table', 'sofa', 'bed', 'desk', 'lamp', 'mirror', 'clock', 'shelf', 'cabinet']

# Initialize session state variables
if 'word' not in st.session_state:
    st.session_state.word = ''
if 'hidden_word' not in st.session_state:
    st.session_state.hidden_word = ''
if 'mistake_counter' not in st.session_state:
    st.session_state.mistake_counter = 5

# Function to start the game
def start_game(manual_word):
    if manual_word:
        st.session_state.word = st.text_input("Type a word: ").upper()
    else:
        st.session_state.word = random.choice(list_of_words).upper()
    
    st.session_state.hidden_word = '_ ' * len(st.session_state.word)
    st.session_state.mistake_counter = 5

# Hangman pictures
hangman_pic = [
'''
    ____________
     |
     O
    / \\
     |
    / \\
''', '''
    ____________
     |
     O
    / \\
     |
    /
''', '''
    ____________
     |
     O
    / \\
     |
''', '''
    ____________
     |
     O
    / \\
''', '''
    ____________
     |
     O
    /
''', '''
    ____________
     |
     O
'''
]

# Game logic
def pick_letter():
    picked_letter = st.text_input("Pick a letter:", "").upper()

    if picked_letter and picked_letter in st.session_state.word:
        letter_index = 0
        updated_word = list(st.session_state.hidden_word)

        for letter in st.session_state.word:
            if letter == picked_letter:
                updated_word[letter_index] = picked_letter
            letter_index += 2

        st.session_state.hidden_word = ''.join(updated_word)

        if st.session_state.hidden_word.replace(' ', '') == st.session_state.word:
            st.success(f"CONGRATULATIONS! The hidden word was: {st.session_state.word}")
    elif picked_letter:
        if st.session_state.mistake_counter == 0:
            st.error(f"HANGED! The hidden word was: {st.session_state.word}")
            st.text(hangman_pic[st.session_state.mistake_counter])
        else:
            st.session_state.mistake_counter -= 1
            st.warning(f"WRONG! Number of mistakes left: {st.session_state.mistake_counter}")
            st.text(hangman_pic[st.session_state.mistake_counter])

# User interface
st.title("Hangman Game")

# Game start options
choice = st.radio("Choose how to start:", ('Random word', 'Manual input'))
if st.button("Start Game"):
    start_game(choice == 'Manual input')

# Display hidden word and allow guessing if the game has started
if st.session_state.word:
    st.text(f"The hidden word is: {st.session_state.hidden_word}")
    pick_letter()
