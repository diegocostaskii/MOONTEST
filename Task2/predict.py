import fasttext
import re
def predict(predict_file, model_file):
    model = fasttext.load_model(model_file)
    predicted_label = []
    text_list = []
    with open(predict_file,'r') as f:
        for line in f:
            line = re.sub(r"[\n]", '', line)
            text_list.append(line)
            predicted_label.append(model.predict(line))
    with open('predictResult.txt','a') as fpr:
        for i in range(len(text_list)):
            fpr.writelines(text_list[i]+ str(predicted_label[i])+'\n')

predict('predict.txt','fasttext.bin')