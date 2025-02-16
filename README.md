# README.md

# conda create -n hr_agent python=3.11 -y

# conda activate hr_agent


"""
 pip install --upgrade pip

 pip install --upgrade certifi

 dependency problem with resolved

Invoke-WebRequest -Uri https://win.rustup.rs -OutFile rustup-init.exe; Start-Process .\rustup-init.exe -Wait

than
rustup default stable   (run this command in powershell as administrator)

rustup update

"""
# 1 Upgrade pip and certifi:

pip install --upgrade pip
pip install --upgrade certifi

# 2 Install
pip install -r requirements.txt

# 3 Install the Package:

pip install -e .


# 4 Load Initial Data:

python interfaces/chromadb_service.py

# 5 Train NER Model:

python training/train_ner_model.py

# 6 Run the Project:

start-ai-hr-agents

# 7 Run the Tests:

pytest tests/


yadi ye install nahi he terminuls me run karna hoga windows ke liye
python -m spacy download en_core_web_sm


python -m nltk.downloader stopwords
python -m spacy download en_core_web_sm
