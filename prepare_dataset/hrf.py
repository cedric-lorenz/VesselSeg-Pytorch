import os
from os.path import join


def get_path_list(root_path, img_path, label_path, fov_path):
    tmp_list = [img_path, label_path, fov_path]
    res = []
    for i in range(len(tmp_list)):
        data_path = join(data_root_path, tmp_list[i])
        filename_list = os.listdir(data_path)
        filename_list.sort()
        res.append([join(data_path, j) for j in filename_list])
    return res


def write_path_list(name_list, save_path, file_name):
    f = open(join(save_path, file_name), 'w')
    for i in range(len(name_list[0])):
        f.write(str(name_list[0][i]) + " " + str(name_list[1]
                [i]) + " " + str(name_list[2][i]) + '\n')
    f.close()


if __name__ == "__main__":
    # ------------Path of the dataset --------------------------------
    data_root_path = "/dhc/groups/bp2021cl1/data/retina"
    # if not os.path.exists(data_root_path): raise ValueError("data path is not exist, Please make sure your data path is correct")
    # train
    img = "HRF/images"
    gt = "HRF/manual1"
    fov = "HRF/mask"
    # ---------------save path-----------------------------------------
    save_path = "./prepare_dataset/data_path_list/HRF"
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    # -----------------------------------------------------------------
    data_list = get_path_list(data_root_path, img, gt, fov)
    print('Numbers of all imgs:', len(data_list[0]))
    test_range = (0, 10)
    train_list = [data_list[i][:test_range[0]] + data_list[i]
                  [test_range[1]:] for i in range(len(data_list))]
    test_list = [data_list[i][test_range[0]:test_range[1]]
                 for i in range(len(data_list))]

    print('Number of train imgs:', len(train_list[0]))
    write_path_list(train_list, save_path, 'train.txt')

    print('Number of test imgs:', len(test_list[0]))
    write_path_list(test_list, save_path, 'test.txt')

    print("Finish!")
