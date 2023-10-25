import argparse # For positional command-line arguments

import nltk
from nltk import parse
import csv  # For writing to train.tsv file
global args  # Store arguments like input_path and output_path

def create_argument_parser():
    """ Create a parser and add 2 arguments to it
    first argument: input_path like "data/dev"
    Second argument: output_path like "output/dev.csv"

    Returns:
        args: store input_path and output_path and we can access to these by "args.input_path" and "args.output_path"
    """
    parser = argparse.ArgumentParser(
        "Correctness of grammar of a sentence")
    parser.add_argument("input_data_path", help="Path to the data directory")
    parser.add_argument("input_grammar_path", help="Path to the grammar file")
    parser.add_argument("output_path", help="Path to the output TSV file")
    args = parser.parse_args()
    #print(type(args))
    return args

def create_tsv_file(path):
    with open(path, 'wt') as out_file:
        tsv_writer = csv.writer(out_file, delimiter='\t')
        tsv_writer.writerow(['id', 'ground_truth','prediction'])
    
def read_grammar_file(path):
      with open(path, 'r') as grammar_file:
        return grammar_file.read()
def read_ground_truth_data(path):
    data = []
    with open(path) as fd:
        rd = csv.reader(fd, delimiter="\t", quotechar='"')
        for row in rd:
            data.append(row)
        fd.close()
    return data

def write_to_tsv(id, ground_truth, prediction,path):
     with open(path, 'a') as out_file:
        tsv_writer = csv.writer(out_file, delimiter='\t')
        tsv_writer.writerow([id, ground_truth,prediction])

def precision_recall(path):
    TP = 0
    TN =0 
    FP= 0
    FN = 0
    with open(path) as fd:
        rd = csv.reader(fd, delimiter="\t", quotechar='"')
        for row in rd:
            if row[1] ==row[2] == '1':
                TP+=1
            elif row[1] ==row[2] == '0':
                TN +=1
            elif row[1] !=row[2] and row[2]=='0':
                FN +=1
            elif row[1] !=row[2]and row[2]=='1':
                FP +=1
        print(FP)
        precision = TP/(TP+ FP)
        recall = TP/(TP + FN)
        fd.close()
        return precision,recall
    

if __name__ == '__main__':
    args = create_argument_parser()
    create_tsv_file(args.output_path)
    cp = parse.load_parser(args.input_grammar_path)
    data = read_ground_truth_data(args.input_data_path)
    data = data[1:] 
    i=0
    for row in data:
        prediction = 1
        for tree in cp.parse_all(row[3].split()):
                prediction = 0
                # if row[1]=='1':
                #     print(tree)
                #print(tree)
                break
        # except:
         

        #     write_to_tsv(row[0], row[1], prediction,args.output_path)
        write_to_tsv(row[0], row[1], prediction,args.output_path)
    
    precision, recall =  precision_recall(args.output_path)
    print("Precision :", precision,"Recall:", recall)
    # print(Tree.fromstring('["PRP", "VBP", "."]',
    #               brackets='[]'))
    # nltk.data.show_cfg(args.input_grammar_path)
   #cp = parse.load_pa
    # print("`` DT VBZ PRP . '' ".split())
    for tree in cp.parse("PRP MD RB VB . ".split()):
    #  prediction = 0
        print(tree)
        break