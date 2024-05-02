# Football Analysis 

## Introduction

This project delves into the world of football (soccer) match analysis using computer vision techniques. By leveraging powerful deep learning models (potentially beyond YOLO) and image processing methods, we aim to extract valuable insights from video footage of football games.

**Before analyzing:**

![Input](data/input/before.png)

**After analyzing:**

![Output](data/output/after.png)

## Key functionalities:

- Player, Referee, and Football Tracking: We utilize advanced methods (potentially beyond YOLO) to effectively track players, referees, and the football throughout the video, enabling detailed analysis of their movements and interactions.
- Team Assignment: Players are assigned to teams based on t-shirt color analysis. This can be achieved through K-means clustering or other segmentation techniques to isolate player pixels and identify their dominant color.
- Ball Control Analysis: By utilizing optical flow and player tracking, we can estimate ball control by analyzing player proximity and movement relative to the football.
- Player Speed and Distance Calculation: We calculate player speed and distance covered throughout the game using optical flow and player tracking data. This can be further refined by employing perspective transformation to represent the scene's depth and convert pixel movements to meters.

## Challenges and Considerations

- Object Detection: While YOLO offers a starting point, consider exploring more football-specific object detection models that can more effectively differentiate players, referees, and the football, especially in challenging situations (e.g., crowded scenes).
- Goalkeeper Detection: Develop strategies to distinguish goalkeepers from other players, potentially using additional cues like positioning or distinctive equipment.
- Dataset: Leverage football-specific datasets for training models. The Kaggle competition dataset [DFL - Bundesliga Data Shootout](https://www.kaggle.com/competitions/dfl-bundesliga-data-shootout/overview) can be a starting point, but exploring other options might be beneficial.

## Files structure

```
├── camera_movement_estimator             
├── data           
├── developement_and_analysis   
├── player_ball_assigner            
├── runs            
├── speed_and_distance_estimator                
├── stubs         
├── team_assigner             
├── trackers         
├── training  
├── utils
├── view_transformer            
├── .gitignore 
├── LICENSE     
├── main.py
├── README.md
├── requirements.txt
├── yolo_inference.py
```
Installation

1. Clone the Repository:

```
git clone https://github.com/lenam1072004/football-analysis.git
```
2. Install Dependencies:
```
pip install -r requirements.txt
```

3. Prepare Your Video:

Place your video file in a designated directory within the project structure (check main.py for the specific path).

Adjust Input Path (if necessary):

4. Open main.py and modify the video input path variable to point to the location of your video file. Run the analysis:


```
python main.py
```

5. View Results:

The processed video with analysis overlays (if applicable) will be saved in a designated folder (check the project structure for details).

## License

This project is licensed under the MIT License. Refer to the LICENSE file for details.

## Contact

For any inquiries, feel free to reach out via email: lenam1072004@gmail.com.