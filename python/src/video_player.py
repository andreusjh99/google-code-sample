"""A video player class."""

from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.currently_playing = ""
        self.paused = False

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        print("Here's a list of all available videos:")
        videos = self._video_library.get_all_videos()
        videos = sorted(videos, key=lambda video: video._title)
        for video in videos:
            # video: Video object
            print(f"{video._title} ({video._video_id}) [{' '.join(video._tags)}]")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        if self.currently_playing and self._video_library.get_video(video_id):
            self.stop_video()
            if self.paused:
                self.paused = False

        if self._video_library.get_video(video_id):
            print(f"Playing video: {self._video_library.get_video(video_id)._title}")
            self.currently_playing = video_id
        else:
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""

        if self.currently_playing == "":
            print("Cannot stop video: No video is currently playing")
        else:
            print(
                f"Stopping video: {self._video_library.get_video(self.currently_playing)._title}"
            )
            self.currently_playing = ""

    def play_random_video(self):
        """Plays a random video from the video library."""
        import random

        video_ids = list(self._video_library._videos.keys())
        randid = random.choice(video_ids)
        self.play_video(randid)

    def pause_video(self):
        """Pauses the current video."""
        if self.paused:
            print(
                f"Video already paused: {self._video_library.get_video(self.currently_playing)._title}"
            )
        elif self.currently_playing:
            print(
                f"Pausing video: {self._video_library.get_video(self.currently_playing)._title}"
            )
            self.paused = True
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""
        if self.paused:
            print(
                f"Continuing video: {self._video_library.get_video(self.currently_playing)._title}"
            )
            self.paused = False
        elif self.currently_playing:
            print("Cannot continue video: Video is not paused")
        else:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""

        if self.currently_playing:
            video = self._video_library.get_video(self.currently_playing)
            if self.paused:
                print(
                    f"Currently playing: {video._title} ({video._video_id}) "
                    f"[{' '.join(video._tags)}] - PAUSED"
                )
            else:
                print(
                    f"Currently playing: {video._title} ({video._video_id}) [{' '.join(video._tags)}]"
                )
        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
