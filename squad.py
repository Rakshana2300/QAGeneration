%env DATA_DIR=./data/squad 

# download the data
def download_squad(version=1):
    if version == 1:
        !wget -P $DATA_DIR https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v1.1.json
        !wget -P $DATA_DIR https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v1.1.json
    else:
        !wget -P $DATA_DIR https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v2.0.json
        !wget -P $DATA_DIR https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v2.0.json
            
download_squad(version=2)
