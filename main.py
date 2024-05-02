from utils import read_video, save_video
from trackers import Tracker 

def main(): 
    # Read video 
    video_frames = read_video('data/input/football_video.mp4')
    
    # Initialize Tracker 
    tracker = Tracker('models/yolo_best.pt')
    
    tracks = tracker.get_object_tracks(video_frames)
    
    # Save Video 
    save_video(video_frames, 'data/output/football_video_yolo.avi')

if __name__ == '__main__':
    main()