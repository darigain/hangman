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

# Initialize session state variables to store word and game state
if 'word' not in st.session_state:
    st.session_state.word = ''
if 'hidden_word' not in st.session_state:
    st.session_state.hidden_word = ''
if 'mistake_counter' not in st.session_state:
    st.session_state.mistake_counter = 5
if 'picked_letters' not in st.session_state:
    st.session_state.picked_letters = set()

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

# Game setup: choose between random word or manual input
choice = st.radio("Choose how to provide a word:", ('Random word', 'Manual input'))

if choice == 'Manual input':
    word_input = st.text_input('Type a word: ')
    if word_input:
        st.session_state.word = word_input.upper()
else:
    if st.button("Generate random word"):
        st.session_state.word = random.choice(list_of_words).upper()

# Once the word is chosen
if st.session_state.word:
    if not st.session_state.hidden_word:
        st.session_state.hidden_word = '_ ' * len(st.session_state.word)

    # Show the hidden word
    st.write(f'The hidden word is: {st.session_state.hidden_word}')

    # Pick a letter
    picked_letter = st.text_input("Pick a letter:", "").upper()

    if picked_letter and picked_letter not in st.session_state.picked_letters:
        st.session_state.picked_letters.add(picked_letter)

        if picked_letter in st.session_state.word:
            # Update hidden word
            hidden_word_list = list(st.session_state.hidden_word)
            for index, letter in enumerate(st.session_state.word):
                if letter == picked_letter:
                    hidden_word_list[index * 2] = picked_letter
            st.session_state.hidden_word = ''.join(hidden_word_list)

            if st.session_state.hidden_word.replace(' ', '') == st.session_state.word:
                st.success(f'CONGRATULATIONS! You guessed the word: {st.session_state.word}')
        else:
            st.session_state.mistake_counter -= 1
            st.write(f'WRONG! Mistakes left: {st.session_state.mistake_counter}')
            st.text(hangman_pic[st.session_state.mistake_counter])

        # End game if no mistakes left
        if st.session_state.mistake_counter == 0:
            st.error(f'HANGED! The correct word was: {st.session_state.word}')
            st.text(hangman_pic[st.session_state.mistake_counter])
