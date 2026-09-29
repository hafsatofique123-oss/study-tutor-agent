import streamlit as st

from agent import create_study_tutor, run_study_tutor


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Study Tutor AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       MAIN APP BACKGROUND
    ======================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(0, 212, 255, 0.14),
                transparent 30%
            ),
            radial-gradient(
                circle at 90% 20%,
                rgba(99, 102, 241, 0.14),
                transparent 30%
            ),
            radial-gradient(
                circle at 50% 90%,
                rgba(0, 255, 200, 0.08),
                transparent 30%
            ),
            #050816;

        color: #f5f7ff;
    }


    /* ========================================================
       MAIN CONTAINER
    ======================================================== */

    .block-container {
        max-width: 1250px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }


    /* ========================================================
       SIDEBAR
    ======================================================== */

    section[data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #07111f 0%,
                #050816 100%
            );

        border-right: 1px solid rgba(0, 212, 255, 0.18);
    }


    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #ffffff;
    }


    /* ========================================================
       HERO
    ======================================================== */

    .hero {
        padding: 2.2rem;
        border-radius: 24px;
        margin-bottom: 1.5rem;

        background:
            linear-gradient(
                135deg,
                rgba(0, 212, 255, 0.12),
                rgba(79, 70, 229, 0.12)
            );

        border: 1px solid rgba(0, 212, 255, 0.22);

        box-shadow:
            0 0 40px rgba(0, 212, 255, 0.07);

        backdrop-filter: blur(12px);
    }


    .hero-title {
        font-size: clamp(2.4rem, 5vw, 4rem);
        font-weight: 800;
        line-height: 1.05;

        background:
            linear-gradient(
                90deg,
                #ffffff,
                #00d4ff,
                #7c7cff
            );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;

        margin-bottom: 0.7rem;
    }


    .hero-subtitle {
        color: #9ca9c7;
        font-size: 1.05rem;
        max-width: 760px;
        line-height: 1.7;
    }


    /* ========================================================
       BADGES
    ======================================================== */

    .badge-container {
        display: flex;
        flex-wrap: wrap;
        gap: 0.6rem;
        margin-top: 1.3rem;
    }


    .badge {
        padding: 0.45rem 0.85rem;
        border-radius: 999px;

        background: rgba(0, 212, 255, 0.08);

        border: 1px solid rgba(0, 212, 255, 0.22);

        color: #8eeaff;

        font-size: 0.82rem;
        font-weight: 600;
    }


    /* ========================================================
       SECTION TITLES
    ======================================================== */

    .section-title {
        color: #ffffff;

        font-size: 1.25rem;

        font-weight: 700;

        margin-top: 1.7rem;
        margin-bottom: 0.8rem;
    }


    /* ========================================================
       GLASS CARDS
    ======================================================== */

    .glass-card {
        padding: 1.3rem;

        border-radius: 18px;

        background:
            rgba(10, 20, 38, 0.65);

        border:
            1px solid rgba(255, 255, 255, 0.08);

        box-shadow:
            0 10px 35px rgba(0, 0, 0, 0.25);

        backdrop-filter: blur(15px);

        min-height: 130px;
    }


    .card-title {
        color: #ffffff;

        font-weight: 700;

        font-size: 1rem;

        margin-bottom: 0.5rem;
    }


    .card-text {
        color: #94a3b8;

        font-size: 0.88rem;

        line-height: 1.6;
    }


    /* ========================================================
       INPUTS
    ======================================================== */

    textarea,
    input {
        background-color:
            rgba(8, 16, 31, 0.8) !important;

        color:
            #ffffff !important;

        border:
            1px solid rgba(0, 212, 255, 0.18) !important;

        border-radius:
            14px !important;
    }


    textarea:focus,
    input:focus {
        border-color:
            #00d4ff !important;

        box-shadow:
            0 0 15px rgba(0, 212, 255, 0.15) !important;
    }


    /* ========================================================
       BUTTON
    ======================================================== */

    .stButton > button {
        width: 100%;

        border-radius: 14px;

        border:
            1px solid rgba(0, 212, 255, 0.5);

        background:
            linear-gradient(
                90deg,
                #00a8ff,
                #0066ff
            );

        color: white;

        font-weight: 700;

        padding: 0.75rem 1rem;

        transition:
            all 0.25s ease;

        box-shadow:
            0 0 20px rgba(0, 174, 255, 0.18);
    }


    .stButton > button:hover {
        transform:
            translateY(-2px);

        box-shadow:
            0 0 30px rgba(0, 212, 255, 0.35);

        border-color:
            #00d4ff;
    }


    /* ========================================================
       SELECT BOX
    ======================================================== */

    div[data-baseweb="select"] > div {
        background-color:
            rgba(8, 16, 31, 0.8);

        border-radius:
            12px;

        border:
            1px solid rgba(0, 212, 255, 0.18);
    }


    /* ========================================================
       RESPONSE HEADER
    ======================================================== */

    .response-header {
        display: flex;

        align-items: center;

        gap: 0.7rem;

        margin-top: 1.8rem;

        margin-bottom: 1rem;
    }


    .response-icon {
        width: 44px;

        height: 44px;

        display: flex;

        align-items: center;

        justify-content: center;

        border-radius: 13px;

        background:
            linear-gradient(
                135deg,
                #00d4ff,
                #6366f1
            );

        box-shadow:
            0 0 20px rgba(0, 212, 255, 0.25);

        font-size: 1.25rem;
    }


    .response-title {
        color: #ffffff;

        font-size: 1.3rem;

        font-weight: 700;
    }


    /* ========================================================
       STATUS CARDS
    ======================================================== */

    .status-card {
        padding: 1rem;

        border-radius: 16px;

        background:
            rgba(10, 20, 38, 0.7);

        border:
            1px solid rgba(255, 255, 255, 0.07);

        margin-bottom: 0.8rem;
    }


    .status-dot {
        display: inline-block;

        width: 8px;

        height: 8px;

        border-radius: 50%;

        background:
            #00ffb3;

        box-shadow:
            0 0 10px #00ffb3;

        margin-right: 7px;
    }


    .status-text {
        color: #cbd5e1;

        font-size: 0.85rem;
    }


    /* ========================================================
       CHAT HISTORY
    ======================================================== */

    .history-card {
        padding: 1rem;

        border-radius: 16px;

        background:
            rgba(10, 20, 38, 0.55);

        border:
            1px solid rgba(0, 212, 255, 0.10);

        margin-bottom: 0.8rem;
    }


    .history-label {
        color: #00d4ff;

        font-size: 0.75rem;

        font-weight: 700;

        text-transform: uppercase;

        margin-bottom: 0.35rem;
    }


    .history-question {
        color: #ffffff;

        font-size: 0.9rem;

        line-height: 1.5;
    }


    /* ========================================================
       FOOTER
    ======================================================== */

    .footer {
        text-align: center;

        color: #64748b;

        font-size: 0.8rem;

        margin-top: 3rem;

        padding-top: 1.5rem;

        border-top:
            1px solid rgba(255, 255, 255, 0.06);
    }


    /* ========================================================
       MOBILE
    ======================================================== */

    @media (max-width: 768px) {

        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .hero {
            padding: 1.4rem;

            border-radius: 18px;
        }

        .hero-title {
            font-size: 2.3rem;
        }

        .hero-subtitle {
            font-size: 0.95rem;
        }

        .glass-card {
            margin-bottom: 1rem;
        }

    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SESSION STATE
# ============================================================

if "study_tutor" not in st.session_state:

    with st.spinner("Initializing your AI Study Tutor..."):

        try:

            st.session_state.study_tutor = (
                create_study_tutor()
            )

        except Exception as e:

            st.error(
                "Could not initialize the Study Tutor Agent."
            )

            st.exception(e)

            st.stop()


if "conversation_history" not in st.session_state:

    st.session_state.conversation_history = []


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div style="
            padding: 1rem 0;
            margin-bottom: 1rem;
        ">

            <div style="
                font-size: 1.7rem;
                font-weight: 800;
                color: #ffffff;
            ">
                🧠 Study Tutor
            </div>

            <div style="
                color: #64748b;
                font-size: 0.8rem;
                margin-top: 0.3rem;
            ">
                AI-powered learning companion
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


    st.markdown("### 🎯 Learning Settings")


    subject = st.selectbox(
        "Subject",
        [
            "General",
            "Computer Science",
            "Artificial Intelligence",
            "Machine Learning",
            "Mathematics",
            "Science",
            "Business",
            "Law",
            "English",
        ],
    )


    level = st.selectbox(
        "Learning Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced",
        ],
    )


    st.markdown("---")


    st.markdown("### ⚙️ Tutor Status")


    st.markdown(
        """
        <div class="status-card">

            <span class="status-dot"></span>

            <span class="status-text">
                Study Tutor Agent
            </span>

        </div>

        <div class="status-card">

            <span class="status-dot"></span>

            <span class="status-text">
                Conversation Memory
            </span>

        </div>

        <div class="status-card">

            <span class="status-dot"></span>

            <span class="status-text">
                Calculator Tool
            </span>

        </div>

        <div class="status-card">

            <span class="status-dot"></span>

            <span class="status-text">
                Study Plan Tool
            </span>

        </div>
        """,
        unsafe_allow_html=True,
    )


    st.markdown("---")


    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True,
    ):

        st.session_state.conversation_history = []

        st.rerun()


    st.markdown(
        """
        <div style="
            color: #475569;
            font-size: 0.72rem;
            text-align: center;
            margin-top: 2rem;
        ">
            Powered by CrewAI + Groq
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# HERO SECTION
# ============================================================

st.markdown(
    """
    <div class="hero">

        <div class="hero-title">
            Learn Smarter.
            <br>
            Think Deeper.
        </div>

        <div class="hero-subtitle">
            Meet your AI Study Tutor - an intelligent
            learning companion that explains concepts,
            creates study plans, helps you practice,
            and remembers your recent learning context.
        </div>

        <div class="badge-container">

            <span class="badge">⚡ Groq</span>

            <span class="badge">🤖 CrewAI</span>

            <span class="badge">🧠 AI Memory</span>

            <span class="badge">🛠️ Smart Tools</span>

        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# INFORMATION CARDS
# ============================================================

col1, col2, col3 = st.columns(3)


with col1:

    st.markdown(
        """
        <div class="glass-card">

            <div class="card-title">
                📖 Learn
            </div>

            <div class="card-text">
                Understand difficult topics through
                simple explanations, examples,
                and clear step-by-step guidance.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


with col2:

    st.markdown(
        """
        <div class="glass-card">

            <div class="card-title">
                🧠 Remember
            </div>

            <div class="card-text">
                Your recent questions and tutor
                responses provide context for
                your next learning request.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


with col3:

    st.markdown(
        """
        <div class="glass-card">

            <div class="card-title">
                🎯 Practice
            </div>

            <div class="card-text">
                Practice concepts with examples,
                questions, calculations, and
                personalized study activities.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# QUESTION AREA
# ============================================================

st.markdown(
    '<div class="section-title">💬 What do you want to learn?</div>',
    unsafe_allow_html=True,
)


question = st.text_area(
    "Your question",

    placeholder=(
        "Ask your Study Tutor anything...\n\n"
        "Example: Explain recursion in Python "
        "like I am a beginner."
    ),

    height=180,

    label_visibility="collapsed",
)


# ============================================================
# ASK BUTTON
# ============================================================

ask_button = st.button(
    "⚡ Ask My Study Tutor",
    use_container_width=True,
)


# ============================================================
# RUN AGENT
# ============================================================

if ask_button:

    if not question.strip():

        st.warning(
            "Please enter a topic or question first."
        )

    else:

        with st.spinner(
            "🧠 Your Study Tutor is thinking..."
        ):

            try:

                result = run_study_tutor(
                    study_tutor=st.session_state.study_tutor,
                    subject=subject,
                    level=level,
                    question=question,
                    conversation_history=(
                        st.session_state.conversation_history
                    ),
                )


                # Save conversation memory

                st.session_state.conversation_history.append(
                    {
                        "question": question,
                        "answer": str(result),
                    }
                )


                # =================================================
                # RESPONSE HEADER
                # =================================================

                st.markdown(
                    """
                    <div class="response-header">

                        <div class="response-icon">
                            🧠
                        </div>

                        <div class="response-title">
                            Your Study Tutor
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True,
                )


                # =================================================
                # RESPONSE
                # =================================================

                st.markdown(str(result))


            except Exception as e:

                st.error(
                    "Something went wrong while asking "
                    "the Study Tutor."
                )

                st.exception(e)


# ============================================================
# RECENT CONVERSATION
# ============================================================

if st.session_state.conversation_history:

    st.markdown(
        '<div class="section-title">🧠 Recent Learning Context</div>',
        unsafe_allow_html=True,
    )


    recent_history = (
        st.session_state.conversation_history[-3:]
    )


    for item in reversed(recent_history):

        st.markdown(
            f"""
            <div class="history-card">

                <div class="history-label">
                    Student Question
                </div>

                <div class="history-question">
                    {item["question"]}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

        Study Tutor AI - Built with Streamlit + CrewAI + Groq

        <br><br>

        Learn | Practice | Improve

    </div>
    """,
    unsafe_allow_html=True,
)

