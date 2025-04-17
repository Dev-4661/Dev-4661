class DivyeshBoddu:
    def __init__(self):
        self.username = 'Dev-4661'
        self.full_name = 'Divyesh Boddu'
        self.roles = ['Data Scientist', 'AI Engineer', 'Machine Learning Enthusiast']
        self.education = {
            'Bachelors': 'Artificial Intelligence and Data Science',
            'Institute': 'New Horizon Institute of Technology and Management'
        }
        self.skills = {
            'Programming Languages': ['Python', 'C'],
            'Frameworks': ['Flask', , 'Streamlit','ReFlex','LangChain','CrewAI'],
            'Machine Learning': ['Scikit-learn', 'PyTorch'],
            'Deep Learning': ['PyTorch'],
            'NLP': ['NLTK', 'SpaCy', 'Transformers'],
            'Databases': ['MySQL', 'PostgreSQL', 'MongoDB'],
            'Tools': ['Git', 'GitHub', 'Jupyter', 'Colab', 'Kaggle']
        }
        self.projects = {
            'FoodVision': 'https://github.com/Dev-4661/Food-Vision',
            'Leaf Disease Detection': 'https://github.com/Dev-4661/Leaf-Disease-Detection',
           
        }
        self.contact_info = {
            'LinkedIn': 'https://www.linkedin.com/in/divyesh03/',
            'Email': 'divyeshboddu2003@gmail.com'
        }
        self.location = 'India'
        self.languages = {
            'Hindi': 'Native',
            'English': 'Fluent'
        }

    def __str__(self):
        return self.full_name

if __name__ == '__main__':
    me =DivyeshBoddu()
    print(str(me))
