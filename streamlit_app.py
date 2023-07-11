import streamlit as st
import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Initialize CountVectorizer
cv = CountVectorizer()

# Streamlit app
def main():
    st.title("Resume Selection App")
    
    # Job description file
    job_desc_file = st.file_uploader("Upload Job Description (.docx)", type=["docx"])
    
    # resume file
    resume_file = st.file_uploader("Upload Resume (.docx)", type=["docx"])
    
    if job_desc_file and resume_file:
        # Extract text from uploaded files
        job_desc = docx2txt.process(job_desc_file)
        resume = docx2txt.process(resume_file)
        
        # Combine the job description and resume texts
        texts = [job_desc, resume]
        
        # Convert the texts into a matrix of token counts
        matrix = cv.fit_transform(texts)
        
        # Calculate cosine similarity between the texts
        tracker = cosine_similarity(matrix)[0][1]
        
        # Print the similarity score
        similarity_score = round(tracker * 100, 2)
        st.write(f"Similarity Score: {similarity_score}%")
        
        # Determine if the resume is selected based on the similarity score
        if similarity_score > 70:
            st.write("Resume Selected")
        else:
            st.write("Resume Not Selected")


if __name__ == "__main__":
    main()
