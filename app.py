import streamlit as st
import pickle
import numpy as np

# -----------------------------
# Load Data
# -----------------------------
popular_df = pickle.load(open("models/popular.pkl", "rb"))
pt = pickle.load(open("models/pt.pkl", "rb"))
books = pickle.load(open("models/books.pkl", "rb"))
similarity_scores = pickle.load(open("models/similarity_scores.pkl", "rb"))


# -----------------------------
# Recommendation Function
# -----------------------------
def recommend(book_name):
    try:
        index = np.where(pt.index == book_name)[0][0]
    except:
        return []

    similar_items = sorted(
        list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True
    )[
        1:9
    ]  # 8 recommendations (2 rows of 4)

    data = []

    for i in similar_items:
        temp_df = books[books["Book-Title"] == pt.index[i[0]]]

        title = temp_df.drop_duplicates("Book-Title")["Book-Title"].values[0]
        author = temp_df.drop_duplicates("Book-Title")["Book-Author"].values[0]
        image = temp_df.drop_duplicates("Book-Title")["Image-URL-M"].values[0]

        data.append([title, author, image])

    return data


# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Book Recommender", layout="wide")

st.title("📚 Book Recommender System")

# Sidebar
option = st.sidebar.selectbox(
    "Choose Recommendation Type", ["Popularity Based", "Collaborative Filtering"]
)

# -----------------------------
# Popularity Based
# -----------------------------
if option == "Popularity Based":
    st.subheader("🔥 Top 50 Popular Books")

    for i in range(0, 50, 4):
        cols = st.columns(4)

        for j in range(4):
            if i + j < 50:
                with cols[j]:
                    st.image(
                        popular_df["Image-URL-M"].values[i + j],
                        width="content",
                    )
                    st.markdown(f"**{popular_df['Book-Title'].values[i+j]}**")
                    st.caption(popular_df["Book-Author"].values[i + j])
                    st.write("⭐", round(popular_df["avg_rating"].values[i + j], 2))


# -----------------------------
# Collaborative Filtering
# -----------------------------
else:
    st.subheader("🔍 Get Book Recommendations")

    selected_book = st.selectbox("Type or Select a Book", pt.index.values)

    if st.button("Recommend"):
        with st.spinner("Finding similar books..."):
            recommendations = recommend(selected_book)

        if len(recommendations) == 0:
            st.error("Book not found in dataset")
        else:
            for i in range(0, len(recommendations), 4):
                cols = st.columns(4)

                for j in range(4):
                    if i + j < len(recommendations):
                        with cols[j]:
                            st.image(
                                recommendations[i + j][2], width='content'
                            )
                            st.markdown(f"**{recommendations[i+j][0]}**")
                            st.caption(recommendations[i + j][1])
