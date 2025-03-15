import streamlit as st
import re  # Regular expression module which check the given condition/pattern is in or not.
import random

common_passwords = {"password123", "123456", "qwerty", "letmein", "admin", "welcome"}

def check_length(password):
    return len(password) >= 8

def check_letter(password):
    return bool(re.search(r"[A-Z]", password) and re.search(r"[a-z]", password))

def check_digit(password):
    return bool(re.search(r"\d", password))

def check_special_char(password):
    return bool(re.search(r"[!@#$%^&*]", password))

def check_common_pass(password):
    return password.lower() not in common_passwords



def check_pass(password):
    score = 0
    feedback = []

    if not check_common_pass(password):
        feedback.append("❌ Avoid using common passwords like 'password123'.")

    if check_length(password):
        score += 1
    else:
        feedback.append("Password must be at least 8 characters long")

    if check_letter(password):
        score =+ 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.") 

    if check_digit(password):
        score =+ 1 
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if check_special_char(password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*)")     

    if score == 2:
        return "✅ Strong Password!", feedback
    elif score >= 3:
        return "⚠️ Moderate Password", feedback
    else:
        return "❌ Weak Password - Improve it using the suggestions below", feedback
                    


def generate_auto_strong_pass():
    upper= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    special ="!@#$%^&*"  

    all_letters = upper +lower + digits + special
    password = (
        random.choice(upper) +
        random.choice(lower) +
        random.choice(digits) +
        random.choice(special) +
        "".join(random.choices(all_letters, k=4)) 
    )  

    return "".join(random.sample(password, len(password)))
  




st.title("🔐 Password Strength Meter")

password = st.text_input("Enter a password to check it's strength and get suggestions!")

if st.button("Check Strength"):
    if password:
        strength, suggestions = check_pass(password)
        st.subheader(strength)

        for fd in suggestions:
            st.write(fd)

        if "❌ Weak Password" in strength:
            st.warning("🔑 Suggested Strong Password:" + generate_auto_strong_pass())
            st.toast("🔑 Suggested Strong Password:" + generate_auto_strong_pass())

    else:
        st.error("⚠️ Please enter a password to check its strength!")        

