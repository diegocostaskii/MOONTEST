import os
import fasttext

def test(test_file, model_file):
    if os.path.exists(model_file):
        model = fasttext.load_model(model_file)
    else:
        raise
    print(model.test(test_file))

test('test.txt','fasttext.bin')