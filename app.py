
import streamlit as st
from rag_engine import get_answer

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Karnataka AI Chatbot",
    page_icon="💜",
    layout="wide"
)

# ---------------- CUSTOM DESIGN ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f8efff, #f0e6ff, #e7f4ff);
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #301052, #673ab7, #8b5bd6);
}
[data-testid="stSidebar"] * {
    color: white !important;
}
.main-title {
    font-size: 42px;
    font-weight: 800;
    background: linear-gradient(90deg, #7628c9, #e044a7, #347eea);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.subtitle {
    color: #65458c;
    font-size: 17px;
}
.topic-card {
    background: white;
    padding: 20px;
    border-radius: 18px;
    border: 1px solid #e5d5fa;
    box-shadow: 0px 4px 15px rgba(120, 70, 170, 0.12);
    margin-bottom: 12px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("## 💜 Karnataka AI")
    st.caption("District Information Chatbot")
    st.markdown("---")

    page = st.radio(
        "Navigation",
        [
            "🏠 Home / Chat",
            "⚙️ Project Pipeline",
            "ℹ️ About Project",
            "📚 Topics",
            "👥 Team Members"
        ]
    )

    st.markdown("---")
    st.markdown("### 🏛️ Project Information")
    st.write("📍 Karnataka, India")
    st.write("🗺️ 31 Districts")
    st.write("📖 4 Knowledge Topics")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.caption("Made with Python & Streamlit 💜")

# ---------------- HOME / CHAT ----------------
if page == "🏠 Home / Chat":

    st.markdown(
        '<div class="main-title">💜 Karnataka AI Chatbot</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Explore Karnataka district information with AI</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown("""
    <div class="topic-card">
    👋 Welcome! Ask me about any district of Karnataka.
    <br><br>
    Explore history, geography, culture, tourism, economy and development.
    </div>
    """, unsafe_allow_html=True)

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous chat
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    question = st.chat_input("Ask about any Karnataka district...")

    if question:
        # Display and store user message
        st.session_state.messages.append(
            {"role": "user", "content": question}
        )

        with st.chat_message("user"):
            st.markdown(question)

        # Get chatbot answer
        with st.chat_message("assistant"):
            with st.spinner("Finding district information..."):
                try:
                    answer = get_answer(question)
                except Exception as e:
                    answer = (
                        "Sorry, an error occurred while finding the answer. "
                        "Please try again."
                    )
                    st.error(str(e))

            st.markdown(answer)

        # Store assistant message
        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

# ---------------- PROJECT PIPELINE ----------------
elif page == "⚙️ Project Pipeline":

    st.markdown('<div class="main-title">⚙️ Project Pipeline</div>',
                unsafe_allow_html=True)

    st.write("### 🔄 How the Karnataka AI Chatbot Works")

    pipeline = [
        ("📥 1. Data Collection",
         "Collect information about Karnataka districts and their topics."),
        ("📄 2. Document Storage",
         "Store the information in organized text files."),
        ("✂️ 3. Text Processing",
         "Read and organize the district information from documents."),
        ("📍 4. District Detection",
         "Identify which district the user mentioned in the question."),
        ("📚 5. Topic Detection",
         "Identify History, Geography, Culture or Economy."),
        ("🔎 6. Information Retrieval",
         "Retrieve information for the selected district and topic."),
        ("🤖 7. Answer Generation",
         "Generate a clear answer using the retrieved information."),
        ("💬 8. User Response",
         "Display the answer in the chatbot.")
    ]

    for title, description in pipeline:
        st.markdown(f"""
        <div class="topic-card">
        <h4>{title}</h4>
        <p>{description}</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------- ABOUT PROJECT ----------------
elif page == "ℹ️ About Project":

    st.markdown('<div class="main-title">ℹ️ About Project</div>',
                unsafe_allow_html=True)

    st.markdown("""
    <div class="topic-card">
    <h3>💜 Karnataka AI Chatbot</h3>
    <p>
    Karnataka AI Chatbot is an interactive information assistant
    developed to provide district-specific information about Karnataka.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🎯 Project Objectives")

    st.markdown("""
    - Provide information about Karnataka districts.
    - Help users explore Karnataka's history and heritage.
    - Provide geographical and natural resource information.
    - Explore culture, festivals and tourism.
    - Understand economy and development.
    - Deliver simple and organized answers.
    """)

    st.markdown("### 🛠️ Technologies Used")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="topic-card">
        <h4>🐍 Python</h4>
        Chatbot programming language
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="topic-card">
        <h4>📄 Text Files</h4>
        District information storage
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="topic-card">
        <h4>🌐 Streamlit</h4>
        Web application interface
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="topic-card">
        <h4>🔎 Retrieval System</h4>
        District and topic-based information retrieval
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🌍 Project Scope")
    st.write("31 Karnataka districts • 4 topics • District-based question answering")

# ---------------- TOPICS ----------------
elif page == "📚 Topics":

    st.markdown('<div class="main-title">📚 Knowledge Topics</div>',
                unsafe_allow_html=True)

    topics = [
        (
            "🏰 History & Heritage",
            "Historical background, dynasties, monuments, forts and heritage."
        ),
        (
            "🌍 Geography & Natural Resources",
            "Location, rivers, climate, landscape, soil and natural resources."
        ),
        (
            "🎭 Culture & Tourism",
            "Festivals, traditions, tourist attractions, temples and local food."
        ),
        (
            "🏭 Economy & Development",
            "Agriculture, industries, business, employment and development."
        )
    ]

    for title, description in topics:
        st.markdown(f"""
        <div class="topic-card">
        <h3>{title}</h3>
        <p>{description}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🗺️ District Coverage")
    st.write("The chatbot is designed to cover all 31 districts of Karnataka.")

# ---------------- TEAM MEMBERS ----------------
elif page == "👥 Team Members":

    st.markdown('<div class="main-title">👥 Team Members</div>',
                unsafe_allow_html=True)

    st.markdown("""
    <div class="topic-card">
    <h3>💜 Project Team</h3>
    <p>Karnataka AI Chatbot</p>
    <p>Computer Science and Engineering</p>
    <p>Shridevi Institute of Engineering and Technology</p>
    </div>
    """, unsafe_allow_html=True)

    # Replace these placeholders with your actual team names
    team_members = [
        "Team Member 1",
        "Team Member 2",
        "Team Member 3",
        "Team Member 4"
    ]

    st.markdown("### 🧑‍💻 Team Members")

    for i, member in enumerate(team_members, start=1):
        st.markdown(f"""
        <div class="topic-card">
        <h4>👤 Member {i}</h4>
        <p>{member}</p>
        </div>
        """, unsafe_allow_html=True)

    st.info("Edit the team member names in the code to add your actual names.")
