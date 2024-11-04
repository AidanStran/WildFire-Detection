# WildFire-Detection
Using object detection to identify early signs of wildfire in UAV drones

## Training
Using yolo11n-seg.pt as the current model since it is the fastest

Trained on [this](https://ieee-dataport.org/open-access/flame-dataset-aerial-imagery-pile-burn-detection-using-drones-uavs) dataset

### Images from training
![val_batch1_pred](https://github.com/user-attachments/assets/57ebaa24-0a9f-41ab-9045-fb4c02411bb3)

![val_batch2_labels](https://github.com/user-attachments/assets/c2014bfd-618b-404c-b7dd-f030ad5b85dc)


## TODO List
   - learn validates charts
   - Increase the predict ability 
      - by running more epochs, current: 10
      - test on larger image sizes? (might not be necessary?)
   - incorporate nonfire images
    
