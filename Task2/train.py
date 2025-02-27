import fasttext

def train(train_file, word2vec_file, model_file, w2v_dim):
    ### Train the FastText classifier using the pre-trained embeddings
    if word2vec_file:
        model = fasttext.train_supervised(input=train_file, dim=w2v_dim, label_prefix="__label__", epoch=10, lr=1.0, wordNgrams=3, pretrainedVectors=word2vec_file)
    else:
        model = fasttext.train_supervised(input=train_file, dim=w2v_dim, label_prefix="__label__", epoch=10, lr=1.0, wordNgrams=3)

    ### Save the trained model
    model.save_model(model_file)

train('./train.txt', './cc.en.300.vec', './fasttext.bin', 300)
