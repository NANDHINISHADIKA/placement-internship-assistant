import streamlit as st

st.set_page_config(page_title="Placement & Internship Assistant", page_icon="🎓", layout="wide")

st.title("🎓 AI Placement & Internship Assistant")
st.subheader("Your complete guide to finding internships and placements!")
st.divider()

# Skills input
st.subheader("📝 Enter Your Details")
name = st.text_input("Your Name")
branch = st.selectbox("Your Branch", ["CSE", "CSE - AI & DS", "ECE", "EEE", "Mechanical", "Civil"])
year = st.selectbox("Your Year", ["1st Year", "2nd Year", "3rd Year", "4th Year"])
skills_input = st.text_area("Enter your skills (comma separated)",
                             placeholder="python, machine learning, sql, data analysis")

if st.button("Analyze & Find Internships", use_container_width=True):
    if skills_input and name:
        skills = [s.strip().lower() for s in skills_input.split(",")]
        st.session_state['skills'] = skills
        st.session_state['name'] = name
        st.session_state['year'] = year

        # ── Resume Score ──
        st.divider()
        st.subheader("📊 Your Resume Score")
        score = min(100, len(skills) * 8 + 20)
        st.progress(score)
        st.metric("Resume Score", str(score) + "/100")
        if score < 50:
            st.error("Add more skills to improve your score!")
        elif score < 75:
            st.warning("Good! Add 3-4 more skills to stand out.")
        else:
            st.success("Excellent resume skill set!")

        # ── Internship Matcher ──
        st.divider()
        st.subheader("💼 Matching Internship Roles")

        internship_roles = {
            "Data Science Intern": {
                "skills": ["python", "machine learning", "data analysis", "pandas", "numpy"],
                "companies": ["TCS", "Zoho", "Mu Sigma", "Fractal Analytics"],
                "link": "https://internshala.com/internships/data-science-internship"
            },
            "ML Engineer Intern": {
                "skills": ["python", "machine learning", "deep learning", "tensorflow"],
                "companies": ["Wipro", "Infosys", "Amazon", "IBM"],
                "link": "https://internshala.com/internships/machine-learning-internship"
            },
            "Web Developer Intern": {
                "skills": ["html", "css", "javascript", "react"],
                "companies": ["Zoho", "Freshworks", "Capgemini"],
                "link": "https://internshala.com/internships/web-development-internship"
            },
            "Data Analyst Intern": {
                "skills": ["sql", "excel", "data analysis", "power bi", "tableau"],
                "companies": ["Deloitte", "Accenture", "EY", "KPMG"],
                "link": "https://internshala.com/internships/data-analytics-internship"
            },
            "Python Developer Intern": {
                "skills": ["python", "flask", "django", "sql"],
                "companies": ["HCL", "Tech Mahindra", "Persistent"],
                "link": "https://internshala.com/internships/python-internship"
            },
            "AI Research Intern": {
                "skills": ["python", "deep learning", "nlp", "computer vision"],
                "companies": ["Google", "Microsoft", "DRDO", "IIT Labs"],
                "link": "https://internshala.com/internships/artificial-intelligence-internship"
            }
        }

        for role, info in internship_roles.items():
            matched = [s for s in info["skills"] if s in skills]
            match_score = int((len(matched) / len(info["skills"])) * 100)

            if match_score > 0:
                st.markdown(f"### {role}")
                st.progress(match_score)
                col1, col2 = st.columns(2)
                with col1:
                    st.write("Match: " + str(match_score) + "%")
                    st.write("Matched: " + ", ".join(matched))
                    missing = [s for s in info["skills"] if s not in skills]
                    if missing:
                        st.warning("Missing: " + ", ".join(missing))
                with col2:
                    st.write("Top Companies: " + ", ".join(info["companies"]))
                    st.markdown("[Apply on Internshala](" + info["link"] + ")")
                st.divider()

        # ── Interview Questions ──
        st.subheader("🎤 Interview Questions Based on Your Skills")

        questions_db = {
            "python": [
                "What are Python decorators?",
                "Explain list vs tuple in Python.",
                "What is a lambda function?"
            ],
            "machine learning": [
                "What is overfitting and how do you prevent it?",
                "Explain the difference between supervised and unsupervised learning.",
                "What is cross validation?"
            ],
            "sql": [
                "What is the difference between JOIN and UNION?",
                "Explain primary key vs foreign key.",
                "What is normalization?"
            ],
            "data analysis": [
                "How do you handle missing values in a dataset?",
                "What is EDA?",
                "Explain the difference between mean, median, and mode."
            ],
            "deep learning": [
                "What is a neural network?",
                "Explain backpropagation.",
                "What is dropout regularization?"
            ],
            "nlp": [
                "What is tokenization?",
                "Explain TF-IDF.",
                "What is word embedding?"
            ]
        }

        count = 1
        for skill in skills:
            if skill in questions_db:
                st.markdown(f"**{skill.upper()}**")
                for q in questions_db[skill]:
                    st.write(str(count) + ". " + q)
                    count += 1

        # ── 30 Day Roadmap ──
        st.divider()
        st.subheader("🗺 Your 30-Day Learning Roadmap")

        roadmaps = {
            "python": "Week 1: Python basics → Week 2: OOP → Week 3: Libraries (Pandas, NumPy) → Week 4: Build a project",
            "machine learning": "Week 1: ML concepts → Week 2: Scikit-learn → Week 3: Model building → Week 4: Deploy a model",
            "sql": "Week 1: Basic queries → Week 2: Joins & aggregations → Week 3: Subqueries → Week 4: Real project",
            "data analysis": "Week 1: Excel basics → Week 2: Pandas → Week 3: Visualization → Week 4: EDA project",
            "deep learning": "Week 1: Neural networks → Week 2: TensorFlow → Week 3: CNN/RNN → Week 4: Build a model",
        }

        for skill in skills:
            if skill in roadmaps:
                st.markdown(f"**{skill.upper()} Roadmap:**")
                st.info(roadmaps[skill])

        # ── Apply Links ──
        st.divider()
        st.subheader("🔗 Quick Apply Links")
        st.markdown("- [Internshala](https://internshala.com)")
        st.markdown("- [LinkedIn Jobs](https://linkedin.com/jobs)")
        st.markdown("- [Forage Virtual Internships](https://www.theforage.com)")
        st.markdown("- [Naukri Internships](https://www.naukri.com/internship-jobs)")
        st.markdown("- [Indeed India](https://in.indeed.com)")

    else:
        st.error("Please enter your name and skills!")