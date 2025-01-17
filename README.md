# A-template-is-all-you-need
A-template is all you need: 2D to 3D reconstruction with templates learned by contrastive learning<br>
![Phase 1](./imgs/Phase_1.png)
![Phase 2](./imgs/Phase_2.png)

## Presentation and report
- [Presentation link](https://www.youtube.com/watch?v=TvMIE-EjeD8) (mandarin)
- [Report link](./report/109_2_3DDLCV_FINAL.pdf)
- [Slide link](./report/slide.pdf)


## 1. Prepare required data
**You must have a GUI for 2D image and SDF rendering!!** <br>
*Environment of Ubuntu with GUI is recommended.* <br>
*If you are unable to generate required 2D images and SDF ground truth, please jump to next section. We do provide some examples for you to download.*
### 1.1 Prepare ShapeNet dataset
1. Please prepare `secret.json`, which should include:
```json
{"pascal_root":"path-to-save-PASCAL3D+_release1.1.zip",
 "pascal_folder":"path-of-PASCAL3D+_release1.1-folder",
 "shapenet_url":"download-link-of-ShapeNetCore.v2.zip",
 "shapenet_root":"path-to-save-ShapeNetCore.v2.zip",
 "shapenet_folder":"path-of-ShapeNetCore.v2-folder"}
```
2. Utilize `initialize.py` to prepare everyting required.
```script
python3 initialize.py
```

### 1.2 Render 2D images
The code is heavily based on [link](https://github.com/Xharlie/ShapenetRender_more_variation). However, only `images` and `albedo` defined there will be generated. You **should build the environment accurately first to avoid any erroneous 2D image rendering**!
1. Download [blender](https://download.blender.org/release/Blender2.79/) v2.79. You **must use v2.79** because some functions are deprecated in the latest version.
2. Test if the command `blender` works or not.
```script
blender
```
3. Install OpenCV in the blender python env. Please (cd) to [blender]/2.79/python/bin
```script
./python3.5m -m ensurepip
./python3.5m -m pip install --upgrade pip
./python3.5m -m pip install opencv-python
./python3.5m -m pip install opencv-contrib-python
```
4. Try to `import numpy` in this python env. If there is any error, re-install numpy by **deleting the numpy folder in the following path `[blender]/2.79/python/lib/site-packages/`**. Then,
```script
./python3.5m -m pip install numpy
```
5. Start generate the 2D images by the following command. Please notice that the `jsons_root` denotes `./examples/splits/`, `data_root` denotes `ShapeNetCore.v2/`, and `output_root` is where you want to save the 2D images.
```script
python batch.py --jsons_root $jsons_root --data_root $data_root --output_root $output_root
```

### 1.3 Render ground truth SDF and PLY
Please refer to [link](https://blog.csdn.net/qq_38677322/article/details/110957634). In short, dependencies of `CLI11`, `Pangolin`, `nanoflann`, and `Eigen3` should be built first. However, the whole process is arduous and various bugs do exist!

### 1.4 Covert 2D image from RGBA to RGB
```script
python rgba2rgb.py -d [data_source] -c 'chairs', --level 'easy'
```

## 2. Downloading data and pretrained models
### 2.1 Complete examples (RECOMMENDED)
[gdown](https://pypi.org/project/gdown/) is recommended for downloading these pre-generated 2D images and SDF ground truth.
```script
pip install gdown
```
#### 2D images
```script
gdown --id 1BORVFh5ODnyhQqGTvCFtSUFrD7XCcSOr #02691156 planes
gdown --id 1WkyrOmvw2G3JgRutWvl_WucYn9RmFA8O #02958343 cars
gdown --id 1M53cyqhkyPo8IZgQaDjo4qNZc9hhkSsi #03001627 chairs
gdown --id 1NBwU309G4FT2SP_gxZzne2uADqbD4Rce #03636649 lamps
gdown --id 1DplfrOr98VEW5xAV8jEy2yNrlOetjNGF #04256520 sofas
gdown --id 1GetjpIDWa7NOIN06tuQQJmR0MuVKwoal #04379243 tables
```
#### SDF ground truth
```script
gdown --id 11y3A8RI4n4vlUVTDu56FO2mc7rhASjr6 #02691156 planes
gdown --id 1_ogLvFOZTg6YFak-_WIvLneMoYYcLRvs #02958343 cars
gdown --id 1lLm0yyrGfEjT7ye3xjbrgW7p2neYHgZ2 #03001627 chairs
gdown --id 1ObsXX4TJjADnlyuFPVJxz00w-fZFK2ak #03636649 lamps
gdown --id 18k8LqWlc2AYr5-gn2u_KQsodGg9macqx #04256520 sofas
gdown --id 1TzUSNe4kAB3plnUf_ZUsxTnVgNq0gqzJ #04379243 tables
```
#### PLY ground truth (TESTING SET ONLY)
```script
gdown --id 1W1oP4zHWP0gPXFAGWGm9rIhCrUlXfhtA #02691156 planes
gdown --id 17UsiUaeSF2O9BbOoCONg-BEfW6_3GTZm #03001627 chairs
gdown --id 1FKSDTitAmIQNODEj5mSQUMFyoPJOpnY0 #04256520 sofas
```

#### NormalizationParameters ground truth (TESTING SET ONLY)
```script
gdown --id 156WckbItDBjmDL89J7yrNxuL2MOQSmam #02691156 planes
gdown --id 1F7xs-3v0yA0IcIhEn5AaeKdaAEaZYlOA #03001627 chairs
gdown --id 1vI0qsAtJ2kwSx8KpyH9sJu_2fCGh1DOu #04256520 sofas
```

#### Pretrained models
```script
gdown --id 1cLW_B_EmhQNeM-pJ2iJIKGFdf7Cyzk6E #planes #end2end with contrastive
gdown --id 11kGrEJqINyfqwcT0aIEoHRC2uwgcz_GF #planes #two phases
gdown --id 1GXpNWaz5njg8x1zC9Ntf83CDfsRtSGdS #chairs #end2end
gdown --id 1bN3B4ws-PXd1kmCrkGSl_4VAcgRgfK7I #chairs #two phases
gdown --id 1lq1-cK86g10EK53E4gskUwnqc-zd9n7p #sofas #end2end
gdown --id 10I4sWk6XjfV6koe00jUkUmhi792YQ-Ot #sofas #two phases
```


### 2.2 Small examples
The training data of chairs `03001627_train.tar.gz` can be downloaded from 
[this link](https://drive.google.com/file/d/17j9uOb3cVXm4sqHcRcgkPBFdCmsYAv3J/view?usp=sharing). 
There will be a folder named `03001627` when the file is extracted.  

To download the file and merge all the extracted data to your dataset folder, run  
```bash
bash download_chairs_train.sh [data_source_name]  
```  
where `[data_source_name]` should be the path to yor dataset folder. 
To be more explicit, it should be the parent folder of `SdfSamples`. 
Therefore, before running this script, please make sure that all the other data has been prepared 
and the folder structure is the same as the one specified in [Data Layouts](https://github.com/Kaminyou/Template-is-all-you-need#data-layouts).     

For example, run  
```bash
bash download_chairs_train.sh data/  
```  

## 3. Data Layouts
**The data must be organized as the following hierarchical structure.**
```script
<data_source_name>/
    .datasources.json
    SdfSamples/
        <dataset_name>/
            <class_name>/
                <instance_name>/
                      <instance_name>.npz
    SurfaceSamples/
        <dataset_name>/
            <class_name>/
                <instance_name>/
                      <instance_name>.ply
    NormalizationParameters/
        <dataset_name>/
            <class_name>/
                <instance_name>/
                      <instance_name>.npz
    <class_name>/         
        <instance_name>/
            <easy/hard>
                 <image>/
                     XXXXXXXX.png
                     XXXXXXXX.png
                     .
                 <image_rgb>/
                     XXXXXXXX.png
                     XXXXXXXX.png
                     .
                              
```
## 4. Extract pretrained embedding
Please use `extract_embedding.py` in the environment of [Deep Implicit Template](https://github.com/ZhengZerong/DeepImplicitTemplates/tree/db65db3c22e0f5111236e48deab7cffb38bd60c3). This code will automatically extract the embedding from the pretrained `Embedding` weights and store in a dictionary, which can be accessed by the `instance_name`.
```
python generate_training_meshes.py -e ./pretrained/${obj}_dit
```
We also provided the pre-extracted one in `./pretrained_embedding/` folder.

## 5. Training
### 5.1 Two-phase training
*Phase-1 training can also be conducted by the original code in deep implicit template. However, the required embedding obtained in this step has been provided in `./pretrained_embedding/` and our program will directly load the embedding there. Thus, you don't need to do the phase-1 training but need to copy the pretrained models of wrapping and SDF network provided [here](https://github.com/ZhengZerong/DeepImplicitTemplates/tree/db65db3c22e0f5111236e48deab7cffb38bd60c3/pretrained). Please prepare `/ModelParameters/latest.pth` for every object category.*
#### Train the encoder (phase 2)
```script
python train_solution1.py -e pretrained/${obj}_dit/ -d ./data/
```

### 5.2 End-to-end training
#### **Version 1**
```script
python train_deep_implicit_templates.py -e examples/${obj}_dit --debug --batch_split 2 -d ./data
```
**To expedite training, the mixed precision mode is provided:**<br>
*Package [apex](https://pypi.org/project/apex/) is required! Please make sure that you have installed it first!*
```script
python train_deep_implicit_templates.py -e examples/${obj}_dit --debug --batch_split 2 -d ./data --mixed_precision --mixed_precision_level O1
```
Plese note that `mixed_precision_level` has four options, `O0`, `O1`, `O2`, `O3`, corresponding to different settings. 
- `O0`: FP32 training
- `O1`: Mixed Precision (recommended for typical use)
- `O2`: “Almost FP16” Mixed Precision
- `O3`: FP16 training

For more information, please refer to the [official document](https://nvidia.github.io/apex/amp.html).<br>
If you cannot successfully install `apex` from pypl. Please refer to [link](https://stackoverflow.com/questions/66610378/unencryptedcookiesessionfactoryconfig-error-when-importing-apex) to build from source, and add argument to indicate where your `apex` is.
```script
--apex_path path_to_apex
```
#### **Version 2**
```script
python train_deep_implicit_templates_v2.py \
-e examples/${obj}_dit \
--debug \
--batch_split 2 \
-d ./data \
[--mixed_precision] \
[--pretrained_weights exps/checkpoints/checkpont_latest.pt]
```  
`train_deep_implicit_templates_v2.py` contains a few updates compared to the original one, including:  
1. start training with weights obtained from contrastive learning.  
    - please use `--pretrained_weights` to specify the path to the checkpoint obtained from `train_contrastive.py`.
    - here a slightly different encoder `_Encoder` (check it out in [`networks/encoder.py`](networks/encoder.py)) 
      is used for easy weight transfer.
2. use [torch.cuda.amp](https://pytorch.org/docs/stable/amp.html) for mixed precision training.
    - please add `--mixed_precision` to enable such feature.
3. train with a dataset that includes both hard and easy 2d images.
    - if you want to train with certain level of difficulty instead, please modify `*` to `easy/hard` in 
      [this line](train_deep_implicit_templates_v2.py#L199).  
      
We can eventually replace `train_deep_implicit_templates.py` with `train_deep_implicit_templates_v2.py` if everyone has 
no problem running this version of training code.  


### 5.3 Pretrained encoder with Contrastive learning
Encoders that apply different contrastive learning frameworks can be found in 
the folder `contrastive/encoders`.  
For more details please refer to [ENCODER.md](contrastive/encoders/ENCODER.md).  

Run the following to perform contrastive learning: 
```script
python train_contrastive.py -e experiments/planes
```

Note that the experiment directory should include a `config.yaml` to specify the configurations. 
An example of `config.yaml` can be found [here](contrastive/config.yaml).  

To use the pretrained weights for the later deep implicit templates training, please refer to 
[ENCODER.md](contrastive/encoders/ENCODER.md).

## 6. Generate meshes
### 6.1 Template
```script
python generate_template_mesh.py -e examples/${obj}_dit --debug 
```
### 6.2 Training data
`view_id` starts from `0` to `50`. If it is set to `-1`, random `view_id` will be selected for each instance. 
```
python generate_training_meshes.py -e examples/${obj}_dit --debug --start_id 0 --end_id 20 --octree --keep_normalization --view_id $id
```
### 6.3 Testing data
`view_id` starts from `0` to `50`. If it is set to `-1`, random `view_id` will be selected for each instance. 
```
python generate_training_meshes.py -e examples/${obj}_dit --debug --start_id 0 --end_id 20 --octree --keep_normalization --mode test --view_id $id
```
### 6.4 Real-world images
```
python generate_general_meshes.py -e examples/${obj}_dit --octree --image_path $where_you_put_the_real_world_images
```

## 7. Evaluate
```script
python evaluate.py -c $class_name -d $data_src -i $mesh_output_folder
```
e.g.
```script
python evaluate.py -c sofas -d ./data/ -i examples/sofas_dit/TrainingMeshes/2000/ShapeNetV2/04256520/
```

## 8. Analyze
1. To analyze the pretrained embedding
```
python analyze.py -e examples/${obj}_dit -p --thread 16
```
2. To analyze the embedding yield from own encoder
- *`early_stop` is to prevent the time-consuming inference process and only extract some data for analysis*
```
python analyze.py -e examples/${obj}_dit -d $data_path -c latest --early_stop 20 --thread 16
```

## Acknowledgements
This code repo is heavily based on [Deep Implicit Template](https://github.com/ZhengZerong/DeepImplicitTemplates/tree/db65db3c22e0f5111236e48deab7cffb38bd60c3). We thank the authors for their great job!
