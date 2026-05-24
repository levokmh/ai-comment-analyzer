import streamlit as st
import pandas as pd
import plotly.express as px

from src.data_loader import load_data
from src.sentiment import analyze_sentiments
from src.metrics import (
    get_sentiment_counts,
    get_total_comments,
    get_sentiment_percentage
)

st.set_page_config(
    page_title="AI Comment Analyzer",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    padding-left: 2.5rem;
    padding-right: 2.5rem;
    max-width: 100%;
}

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0B1020 0%, #111827 45%, #050816 100%);
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

.main-title {
    font-size: 58px;
    font-weight: 900;
    letter-spacing: -2px;
    margin-bottom: 0;
    background: linear-gradient(90deg, #FFFFFF, #94A3B8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    color: #94A3B8;
    font-size: 18px;
    margin-bottom: 30px;
}

div[data-testid="stMetric"] {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 22px;
    padding: 22px;
    backdrop-filter: blur(10px);
}

.stAlert {
    border-radius: 18px;
}

div[data-testid="stFileUploader"] section {
    background: rgba(255,255,255,0.04);
    border: 1px dashed rgba(148,163,184,0.35);
    border-radius: 20px;
}

.stButton > button {
    border-radius: 14px;
    border: 1px solid rgba(148,163,184,0.25);
    background: rgba(255,255,255,0.05);
    color: white;
    transition: 0.2s ease;
}

.stButton > button:hover {
    border-color: #60A5FA;
    background: rgba(96,165,250,0.12);
}

div[data-baseweb="select"] > div,
div[data-testid="stTextInput"] input,
div[data-testid="stNumberInput"] input {
    border-radius: 14px;
    background: rgba(255,255,255,0.05);
}

.comment-card {
    padding: 18px 20px;
    margin-bottom: 14px;
    border-radius: 18px;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    transition: 0.2s ease;
}

.comment-card:hover {
    transform: translateY(-2px);
    border-color: rgba(96,165,250,0.4);
    background: rgba(255,255,255,0.06);
}

.comment-text {
    margin: 0;
    color: #F8FAFC;
    font-size: 15px;
    line-height: 1.5;
}

.badge {
    color: white;
    padding: 6px 12px;
    border-radius: 999px;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111827 0%, #0B1020 100%);
    border-right: 1px solid rgba(255,255,255,0.08);
}

.creator-credit {
    margin-top: 30px;
    padding-top: 16px;
    border-top: 1px solid rgba(255,255,255,0.08);
    color: #64748B;
    font-size: 12px;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<h1 class="main-title">AI Comment Analyzer</h1>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Smart comment analysis with interactive AI dashboard.</p>',
    unsafe_allow_html=True
)

with st.sidebar:

    st.subheader("Filters")

    uploaded_file = st.file_uploader(
        "Upload CSV",
        type=["csv"]
    )

    selected_sentiment = st.selectbox(
        "Sentiment",
        ["All", "Positive", "Neutral", "Negative"]
    )

    search_query = st.text_input(
        "Search",
        placeholder="Ex: sound, thanks, long..."
    )

    items_per_page = st.number_input(
        "Comments per page",
        min_value=5,
        max_value=30,
        value=10,
        step=5
    )

df = (
    pd.read_csv(uploaded_file)
    if uploaded_file is not None
    else load_data("data/comments_sample.csv")
)

if "comment" not in df.columns:
    st.error("The CSV file must contain a column named `comment`.")
    st.stop()

df["sentiment"] = analyze_sentiments(
    df["comment"].astype(str).tolist()
)

total = get_total_comments(df)
positive = get_sentiment_percentage(df, "positive")
neutral = get_sentiment_percentage(df, "neutral")
negative = get_sentiment_percentage(df, "negative")

sentiment_map = {
    "All": "all",
    "Positive": "positive",
    "Neutral": "neutral",
    "Negative": "negative"
}

selected_value = sentiment_map[selected_sentiment]
filtered_df = df.copy()

if selected_value != "all":
    filtered_df = filtered_df[
        filtered_df["sentiment"] == selected_value
    ]

if search_query.strip():
    filtered_df = filtered_df[
        filtered_df["comment"].str.contains(
            search_query,
            case=False,
            na=False
        )
    ]

with st.sidebar:

    st.divider()

    st.subheader("Actions")

    csv_export = filtered_df.to_csv(
        index=False,
        sep=";",
        encoding="utf-8-sig"
    ).encode("utf-8-sig")

    st.download_button(
        label="Export Results",
        data=csv_export,
        file_name="comments_analysis.csv",
        mime="text/csv",
        use_container_width=True
    )

    st.markdown(
        """
        <div class="creator-credit">
            Developed by <strong>LevoKMH</strong>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("## Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Comments", total)
col2.metric("Positive", f"{positive}%")
col3.metric("Neutral", f"{neutral}%")
col4.metric("Negative", f"{negative}%")

if positive > negative:
    st.success(
        "Overall positive trend: comments are mostly favorable."
    )
elif negative > positive:
    st.warning(
        "Overall negative trend: many comments appear critical."
    )
else:
    st.info(
        "Balanced trend: opinions are mixed or neutral."
    )

st.markdown("## Sentiment Distribution")

sentiment_percentages = pd.DataFrame({
    "sentiment": ["Positive", "Neutral", "Negative"],
    "percentage": [positive, neutral, negative]
})

fig = px.bar(
    sentiment_percentages,
    x="percentage",
    y="sentiment",
    orientation="h",
    text="percentage",
    color="sentiment",
    color_discrete_map={
        "Positive": "#22C55E",
        "Neutral": "#60A5FA",
        "Negative": "#EF4444"
    }
)

fig.update_traces(
    texttemplate="%{x}%",
    textposition="inside",
    marker_line_width=0,
    opacity=0.95
)

fig.update_layout(
    height=360,
    paper_bgcolor="#0B1020",
    plot_bgcolor="#111827",
    font_color="#E5E7EB",
    showlegend=False,
    margin=dict(l=20, r=40, t=30, b=20),
    xaxis=dict(
        title="Percentage",
        range=[0, 100],
        ticksuffix="%",
        gridcolor="rgba(255,255,255,0.08)"
    ),
    yaxis=dict(
        title="",
        categoryorder="array",
        categoryarray=["Positive", "Neutral", "Negative"]
    )
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("## Analyzed Comments")

st.caption(f"{len(filtered_df)} comment(s) found.")

total_pages = max(
    1,
    (len(filtered_df) - 1) // int(items_per_page) + 1
)

if "page" not in st.session_state:
    st.session_state.page = 1

if st.session_state.page > total_pages:
    st.session_state.page = total_pages

start_index = (
    (st.session_state.page - 1)
    * int(items_per_page)
)

end_index = start_index + int(items_per_page)

paginated_df = filtered_df.iloc[start_index:end_index]

for _, row in paginated_df.iterrows():

    sentiment = row["sentiment"]

    badge_color = {
        "positive": "#22C55E",
        "neutral": "#60A5FA",
        "negative": "#EF4444"
    }.get(sentiment, "#94A3B8")

    st.markdown(
        f"""
        <div class="comment-card">
            <div style="display:flex;justify-content:space-between;align-items:center;gap:16px;">
                <p class="comment-text">{row["comment"]}</p>
                <span class="badge" style="background:{badge_color};">
                    {sentiment}
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

page_left, page_center, page_right = st.columns([1, 1, 1])

with page_left:

    previous_clicked = st.button(
        "⬅️ Previous",
        use_container_width=True,
        disabled=st.session_state.page <= 1
    )

with page_center:

    st.markdown(
        f"""
        <div style="text-align:center;padding:12px 0;color:#CBD5E1;">
            Page <strong>{st.session_state.page}</strong>
            of <strong>{total_pages}</strong>
        </div>
        """,
        unsafe_allow_html=True
    )

with page_right:

    next_clicked = st.button(
        "Next ➡️",
        use_container_width=True,
        disabled=st.session_state.page >= total_pages
    )

if previous_clicked:
    st.session_state.page -= 1
    st.rerun()

if next_clicked:
    st.session_state.page += 1
    st.rerun()