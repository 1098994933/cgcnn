import torch
from torch.autograd import Variable
from cgcnn.data import collate_pool, get_train_val_test_loader
from cgcnn.model import CrystalGraphConvNet
from cgcnn.data_muti import CIFData
if __name__ == '__main__':
    dataset = CIFData(r"C:\Users\10989\PycharmProjects\8_CGCNN\cgcnn\data\sample-regression-muti-output")
    (atom_fea, nbr_fea, nbr_fea_idx), target, cif_id = dataset.__getitem__(0)
    print(target)

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
    _, sample_target, _ = collate_pool(sample_data_list)
    normalizer = Normalizer(sample_target)

    # build model
    structures, _, _ = dataset[0]
    orig_atom_fea_len = structures[0].shape[-1]
    nbr_fea_len = structures[1].shape[-1]
    model = CrystalGraphConvNet(orig_atom_fea_len, nbr_fea_len,
                                atom_fea_len=4,
                                n_conv=3,
                                h_fea_len=32,
                                n_h=1,
                                classification=False)
