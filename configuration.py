general_configuration = {
    'num_classes' : 4,
    'dataset_path' : 'datasets',
    'log_path' : 'log',
    'model_path' : 'models',
    'results_path' : 'results',
    'dataset_info' : {
        'iSeg2017' : {
            'format' : 'analyze',
            'dimensions' : (144, 192, 256)
            'num_volumes' : 10,
            'modalities' : 2,
            'general_pattern' : 'subject-{}-{}.hdr',
            'path' : 'iSeg2017/iSeg-2017-Training',
            'inputs' : ['T1', 'T2', 'label']
        },
        'IBSR18' : {
            'format' : 'nii',
            'dimensions' : (256, 128, 256),
            'num_volumes' : 18,
            'modalities' : 1,
            'general_pattern' : 'IBSR_{0:02}/IBSR_{0:02}_{}.nii.gz',
            'path' : 'IBSR18',
            'inputs' : ['ana_strip', 'segTRI_ana']
        },
        'MICCAI2012' : {
            'format' : 'nii',
            'dimensions' : (256, 287, 256),
            'num_volumes' : [15, 20],
            'modalities' : 1,
            'general_pattern' : ['{}/1{:02}.nii.gz', '{}/1{:02}_3C.nii.gz'],
            'path' : 'MICCAI2012',
            'folder_names' : ['training_images', 'training-labels', 'testing-images', 'testing-labels']
        }
    }
}

training_configuration = {
    'activation' : 'softmax',
    'approach' : 'DolzMulti',
    'dataset' : 'iSeg2017',
    'dimension' : 3,
    'extraction_step' : (9, 9, 9),
    'loss' : 'categorical_crossentropy',
    'metrics' : ['acc'],
    'num_epochs' : 20,
    'optimizer' : 'Adam'
    'output_shape' : (9, 9, 9),
    'patch_shape' : (27, 27, 27),
    'patience' : 1,
    'validation_split' : 0.20,
    'verbose' : 1,
}