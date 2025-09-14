import streamlit as st
from agent import reflection_chain, insert_entry, fetch_entries

st.set_page_config(page_title="Daily Reflection Agent", layout="centered")

st.title("🧘 Daily Reflection & Planning Assistant")

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

        # Save entry to database
        insert_entry(journal, intention, dream, priorities, response)

        st.success("✅ Strategy Generated!")
        st.write(response)

# History Section
st.subheader("📂 Previous Reflections")
entries = fetch_entries()
for e in entries:
    st.write(f"📝 Journal: {e[1]} | 🎯 Intention: {e[2]} | 📌 Priorities: {e[4]}")
    st.text_area("AI Reflection", e[5], height=120, disabled=True)
