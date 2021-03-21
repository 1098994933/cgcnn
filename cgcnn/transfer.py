import torch
from torch.autograd import Variable
from cgcnn.data import collate_pool, get_train_val_test_loader
if __name__ == '__main__':

    PATH = r"C:\Users\10989\PycharmProjects\8_CGCNN\cgcnn\pre-trained\band-gap.pth.tar"
    model_dict = torch.load(PATH, map_location=torch.device('cpu'))
    dict_name = list(model_dict)
    for i, p in enumerate(dict_name):
        print(i, p)
    for i, p in enumerate(model_dict["state_dict"]):
        print(i, p,'\t',model_dict["state_dict"][p].size())
    from cgcnn.model import CrystalGraphConvNet
    from cgcnn.data import CIFData

    model = CrystalGraphConvNet(92, 41,
                                    atom_fea_len=64,
                                    n_conv=4,
                                    h_fea_len=32,
                                    n_h=1,
                                    classification=False)
    model.load_state_dict(model_dict["state_dict"])
    # load data
    cif_data = CIFData(r"C:\Users\10989\PycharmProjects\8_CGCNN\cgcnn\data\sample-classification")
    dataset = CIFData(r"C:\Users\10989\PycharmProjects\8_CGCNN\cgcnn\data\sample-classification")
    collate_fn = collate_pool
    train_loader, val_loader, test_loader = get_train_val_test_loader(
        dataset=dataset,
        collate_fn=collate_fn,
        batch_size=3,
        train_ratio=0.5,
        num_workers=2,
        val_ratio=0.2,
        test_ratio=0.3,
        pin_memory=False,
        train_size=5,
        val_size=3,
        test_size=2,
        return_test=True)

    idx = 4
    #input, target, batch_cif_ids = cif_data.__getitem__(idx)
























    for input, target, batch_cif_ids in val_loader:
        input_var = (Variable(input[0]),
                     Variable(input[1]),
                     input[2],
                     input[3])
        predict  = input_var
        output = model(*input_var)
        print("output",output)
