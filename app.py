import streamlit as st
import datetime
from agent import reflection_chain
from db import insert_entry, fetch_entries, init_db

st.set_page_config(page_title="Daily Reflection Agent", layout="centered")

st.title("🧘 Daily Reflection & Planning Assistant")


# Initialize DB
init_db()

st.set_page_config(page_title="Daily Reflection Agent", layout="centered")

# Input form
with st.form("reflection_form"):
    journal = st.text_area("📝 Morning Journal")
    intention = st.text_input("🎯 Intention for Today")
    dream = st.text_area("💭 Last Night’s Dream")
    priorities = st.text_input("📌 Top 3 Priorities (comma separated)")

    submitted = st.form_submit_button("Generate Strategy")

if submitted:
    with st.spinner("✨ Thinking..."):
        response = reflection_chain.run({
            "journal": journal,
            "intention": intention,
            "dream": dream,
            "priorities": priorities
        })
        today = datetime.date.today().isoformat()

        # Save entry to database
        insert_entry(today, journal, intention, dream, priorities, str(response))

        st.success("✅ Strategy Generated!")
        st.write(response)

# History Section
st.subheader("📂 Previous Reflections")
entries = fetch_entries()  # ab plural wala function se sari history milegi
for e in entries:
    st.write(e)
