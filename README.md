# conf
This project creates and trains a model on the confused/not confused dataset.
To run the code:
1) download the dataset from :https://drive.google.com/file/d/1b0FqoLd0FFLeknhS_LvCQw85Wgkg3OtW/view?usp=sharing.
2) change the 'root_dir' in line 80 for the datpp3 function to the location of downloaded files(example can be seen in train_2.py).
3) change line 44 of dataload according to your os. I tested this on Cedar.computecanada.ca cluster.
4) for balanced mode run train2_.py or train2.py(these are suppose to be the latest and working on the cluster).
5) change name varaible on line 52 to where you want the data to be logs and saved models to be saved.
6) args --NN sets the model, choose 1 for Facenet+LSTM, --modeR 0 freezes the weights of Facenet(1 for not frozen), --numpc number of epochs to run. --lr intiate learning rate, --Sc enable learning rate schedular. --patience set the patience for learning rate schedualer.

this algorithm saves 3 files per run. the loss and accuracy progression are saved in log. scorlist contains the outputs of test dataset of best model. the pth file is the best model.

Saved folder contain the scorelist of all 4 version. Confusion matrix folder contatins the condusion matrix. The .xlsx file contatins all of the four runs accuracy loss progession for train test validation and the figures.
