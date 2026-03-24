lama_ct_reconstruction_desc = {
    "description": "使用 LAMA（Learned Alternating Minimization Algorithm）对稀疏视角 CT 正弦图进行双域高质量图像重建。",
    "name": "lama_ct_reconstruction",
    "optional_parameters": [
        {
            "default": 64,
            "description": "稀疏视角数量，支持 64 或 128",
            "name": "n_views",
            "type": "int",
        },
        {
            "default": "mayo",
            "description": "数据集类型，支持 mayo 或 NBIA",
            "name": "dataset",
            "type": "str",
        },
    ],
    "required_parameters": [
        {
            "default": None,
            "description": "输入稀疏视角 CT 正弦图路径（.mat 格式，shape: n_views x 512）",
            "name": "input_path",
            "type": "str",
        },
        {
            "default": None,
            "description": "重建结果保存路径（.mat 格式，重建图像 shape: 256 x 256）",
            "name": "output_path",
            "type": "str",
        },
    ],
}