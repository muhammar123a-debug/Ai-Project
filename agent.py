import os
import datetime
import streamlit as st
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# Import DB functions
from db import init_db, insert_entry, fetch_entry


api_key = st.secrets["GOOGLE_API_KEY"]

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)

# 2. Prompt Template
PROMPT_TEMPLATE = """
You are a daily reflection and planning assistant. Your goal is to:
1. Reflect on the user's journal and dream input
2. Interpret the user's emotional and mental state
3. Understand their intention and 3 priorities
4. Generate a practical, energy-aligned strategy for their day

INPUT:
Morning Journal: {journal}
Intention: {intention}
Dream: {dream}
Top 3 Priorities: {priorities}

OUTPUT:
1. Inner Reflection Summary
2. Dream Interpretation Summary
3. Energy/Mindset Insight
4. Suggested Day Strategy
"""

reflection_prompt = PromptTemplate(
    input_variables=["journal", "intention", "dream", "priorities"],
    template=PROMPT_TEMPLATE
)

reflection_chain = LLMChain(llm=llm, prompt=reflection_prompt)

# 3. Run
if __name__ == "__main__":
    # Init DB
    init_db()

    # Input
    journal = input("Enter your journal: ")
    intention = input("Enter your intention: ")
    dream = input("Enter your dream: ")
    priorities = input("Enter your top 3 priorities: ")

    # AI Response
    response = reflection_chain.run({
        "journal": journal,
        "intention": intention,
        "dream": dream,
        "priorities": priorities
    })

    print("\n=== AI Reflection Output ===\n")
    print(response)

    # Save to DB
    today = datetime.date.today().strftime("%Y-%m-%d")
    insert_entry(today, journal, intention, dream, priorities, response)

    # Verify
    print("\n=== Saved Entry from DB ===")
    saved = fetch_entry(today)
    print(saved)
