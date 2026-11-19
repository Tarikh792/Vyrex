
import streamlit as st
from datetime import datetime

from agent import run_agent


# ============================================
# PAGE CONFIGURATION
# ============================================

st.set_page_config(
    page_title="Vyrex | AI Agent Workspace",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================
# PREMIUM STYLING
# ============================================

st.markdown("""
<style>

    .stApp {
        background: #0c0e14;
        color: #e8eaf0;
    }

    [data-testid="stSidebar"] {
        background: #11141c;
        border-right: 1px solid #292d38;
    }

    .block-container {
        max-width: 1050px;
        padding-top: 2rem;
        padding-bottom: 5rem;
    }

    .vyrex-logo {
        font-size: 1.75rem;
        font-weight: 800;
        letter-spacing: 3px;
        color: #f8fafc;
    }

    .vyrex-label {
        font-size: 0.7rem;
        color: #a0a5b4;
        letter-spacing: 1.6px;
        margin-top: 5px;
    }

    .hero {
        text-align: center;
        padding: 50px 12px 28px;
    }

    .hero-icon {
        display: inline-block;
        background: #301923;
        border: 1px solid #663144;
        padding: 18px;
        border-radius: 25px;
        font-size: 2.4rem;
        margin-bottom: 15px;
    }

    .hero-title {
        font-size: 2rem;
        font-weight: 750;
        color: #f8fafc;
        margin-bottom: 10px;
    }

    .hero-desc {
        color: #9aa2b2;
        font-size: 0.95rem;
        line-height: 1.7;
    }

    .section-title {
        color: #e5e7eb;
        font-size: 0.9rem;
        font-weight: 650;
        margin: 18px 0 12px;
    }

    .tool-card {
        background: #151922;
        border: 1px solid #2c3240;
        border-radius: 15px;
        padding: 18px;
        min-height: 105px;
    }

    .tool-card-title {
        color: #f1f5f9;
        font-weight: 650;
        margin-bottom: 5px;
    }

    .tool-card-desc {
        color: #929baa;
        font-size: 0.8rem;
        line-height: 1.5;
    }

    [data-testid="stChatMessage"] {
        background: #141821;
        border: 1px solid #292f3b;
        border-radius: 14px;
        padding: 15px;
        margin-bottom: 12px;
    }

    [data-testid="stChatInput"] {
        border: 1px solid #633044;
        border-radius: 14px;
        background: #171b25;
    }

    .stButton > button {
        background: #1c202b;
        border: 1px solid #363c4a;
        border-radius: 10px;
        color: #f1f5f9;
        font-weight: 500;
    }

    .stButton > button:hover {
        border-color: #fb7185;
        color: #fda4af;
        background: #29202a;
    }

    .stDownloadButton > button {
        background: #421e2b;
        border: 1px solid #a3455d;
        color: #ffe4e6;
        border-radius: 10px;
    }

    .stDownloadButton > button:hover {
        background: #64283c;
        border-color: #fb7185;
        color: #ffffff;
    }

    .stSlider {
        padding-top: 8px;
    }

    .status-line {
        color: #fda4af;
        font-size: 0.8rem;
        padding: 5px 0;
    }

    .footer {
        color: #697181;
        text-align: center;
        font-size: 0.75rem;
        margin-top: 45px;
        padding-top: 15px;
        border-top: 1px solid #252b36;
    }

</style>
""", unsafe_allow_html=True)


# ============================================
# SESSION STATE
# ============================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pending_prompt" not in st.session_state:
    st.session_state.pending_prompt = None


# ============================================
# HELPER FUNCTIONS
# ============================================

def new_chat():
    st.session_state.messages = []
    st.session_state.pending_prompt = None


def create_report():
    lines = [
        "# Vyrex AI Agent Report",
        "",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "---",
        ""
    ]

    for message in st.session_state.messages:
        role = (
            "User"
            if message["role"] == "user"
            else "Vyrex"
        )

        lines.extend([
            f"## {role}",
            "",
            message["content"],
            ""
        ])

    return "\n".join(lines)


def queue_prompt(prompt):
    st.session_state.pending_prompt = prompt


# ============================================
# SIDEBAR
# ============================================

with st.sidebar:

    st.markdown(
        '<div class="vyrex-logo">◈ VYREX</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="vyrex-label">'
        'INTELLIGENT AGENT WORKSPACE'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    if st.button(
        "＋ New Chat",
        use_container_width=True,
        type="primary"
    ):
        new_chat()
        st.rerun()

    st.markdown("### Workspace")

    st.caption("Available tools")

    st.markdown("🌐 Web Research")
    st.markdown("🧮 Calculator")

    st.divider()

    st.markdown("### Agent Settings")

    max_steps = st.slider(
        "Maximum reasoning steps",
        min_value=1,
        max_value=5,
        value=3,
        help="Limits the number of tool-calling rounds."
    )

    st.divider()

    st.markdown("### Export")

    if st.session_state.messages:

        st.download_button(
            label="⬇ Download Report",
            data=create_report(),
            file_name="vyrex_report.md",
            mime="text/markdown",
            use_container_width=True
        )

    else:
        st.caption(
            "Your report will be available "
            "after the first response."
        )

    st.divider()

    st.caption("Powered by Groq + Python")
    st.caption("Vyrex V1.0")


# ============================================
# MAIN HEADER
# ============================================

header_left, header_right = st.columns(
    [5, 1],
    vertical_alignment="center"
)

with header_left:
    st.markdown("### ◈ Vyrex")

with header_right:
    st.caption("🟢 Ready")

st.divider()


# ============================================
# EMPTY STATE
# ============================================

if not st.session_state.messages:

    st.markdown("""
    <div class="hero">
        <div class="hero-icon">◈</div>
        <div class="hero-title">
            What can Vyrex do for you?
        </div>
        <div class="hero-desc">
            Your intelligent research and productivity agent.
            <br>
            Discover information, execute tools, and
            turn questions into actionable insights.
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="tool-card">
            <div class="tool-card-title">
                🌐 Web Research
            </div>
            <div class="tool-card-desc">
                Search the web and generate source-aware
                research summaries.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="tool-card">
            <div class="tool-card-title">
                🧮 Smart Calculations
            </div>
            <div class="tool-card-desc">
                Solve numerical problems using
                executable Python tools.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">'
        'TRY A TASK'
        '</div>',
        unsafe_allow_html=True
    )

    prompt1, prompt2 = st.columns(2)

    with prompt1:

        if st.button(
            "Research AI agent trends",
            use_container_width=True
        ):
            queue_prompt(
                "Research current trends in AI agents. "
                "Summarize three findings with source URLs."
            )
            st.rerun()

    with prompt2:

        if st.button(
            "Calculate 125 × 48",
            use_container_width=True
        ):
            queue_prompt(
                "What is 125 multiplied by 48? "
                "Use the calculator tool."
            )
            st.rerun()


# ============================================
# DISPLAY CHAT HISTORY
# ============================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        # Show real activity logs for assistant replies
        if message["role"] == "assistant":

            activities = message.get("activities", [])

            if activities:

                with st.expander(
                    "View Agent Activity",
                    expanded=False
                ):

                    for activity in activities:

                        event = activity.get(
                            "event",
                            "activity"
                        )

                        details = activity.get(
                            "details",
                            ""
                        )

                        st.caption(
                            f"• {event}: {details}"
                        )


# ============================================
# CHAT INPUT
# ============================================

typed_prompt = st.chat_input(
    "Describe a task for Vyrex..."
)

# Example prompt buttons use the same execution flow
if st.session_state.pending_prompt:

    prompt = st.session_state.pending_prompt
    st.session_state.pending_prompt = None

else:
    prompt = typed_prompt


# ============================================
# EXECUTE AGENT
# ============================================

if prompt:

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        activities = []

        with st.status(
            "Vyrex is working...",
            expanded=True
        ) as status:

            def activity_callback(activity):

                activities.append(activity)

                event = activity.get(
                    "event",
                    "activity"
                )

                details = activity.get(
                    "details",
                    ""
                )

                if event == "thinking":
                    status.update(
                        label="Vyrex is reasoning..."
                    )

                elif event == "tool_running":
                    status.update(
                        label="Executing tools..."
                    )

                elif event == "generating_answer":
                    status.update(
                        label="Preparing your answer..."
                    )

                st.write(
                    f"**{event.replace('_', ' ').title()}**"
                    f" — {details}"
                )

            try:

                answer = run_agent(
                    prompt,
                    max_steps=max_steps,
                    on_activity=activity_callback
                )

                status.update(
                    label="Task completed",
                    state="complete",
                    expanded=False
                )

            except Exception as error:

                answer = (
                    "I couldn't complete this task. "
                    "Please try again."
                )

                activities.append({
                    "event": "error",
                    "details": type(error).__name__
                })

                status.update(
                    label="Task failed",
                    state="error",
                    expanded=True
                )

                st.error(
                    f"{type(error).__name__}: {error}"
                )

        st.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "activities": activities
    })


# ============================================
# FOOTER
# ============================================

st.markdown("""
<div class="footer">
    VYREX — INTELLIGENT AGENT WORKSPACE
    <br>
    Research • Tools • Reasoning
</div>
""", unsafe_allow_html=True)
