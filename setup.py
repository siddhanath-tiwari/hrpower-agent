from setuptools import setup, find_packages

setup(
    name='ai_hr_agents',
    version='1.0.0',
    description='AI-Powered HR Agents for Customer Support and Recruitment Assistance',
    author='siddhanath-tiwari',
    author_email='your-email@example.com',
    url='https://github.com/siddhanath-tiwari/ai_hr_agents',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'spacy==3.7.2',
        'transformers==4.37.2',
        'flask==2.0.2',
        'flask-cors==3.0.10',
        'twilio==7.1.0',
        'google-api-python-client==2.26.1',
        'google-auth-httplib2==0.1.0',
        'google-auth-oauthlib==0.4.6',
        'chromadb==0.3.26',
        'pandas==2.2.0',
        'pydantic==1.10.12',
        'werkzeug==2.0.3'
    ],
    entry_points={
        'console_scripts': [
            'start-ai-hr-agents=main:main',
        ],
    },
)