from CLRec import CLRec
from util.conf import ModelConf
import random

if __name__ == '__main__':
    random.seed(2022)
    graph_models = ['LightGCN', 'SGL', 'SimGCL', 'XSimGCL', 'PAGCL']

    print('Choose Models:')
    print('=' * 80)
    print('   '.join(graph_models))

    print('=' * 80)
    model = input('Please enter the model you want to run:')
    if model in graph_models:
        conf = ModelConf('./conf/' + model + '.conf')
    else:
        print('Model does not exist!')
        exit(-1)
    rec = CLRec(conf)
    rec.execute()
