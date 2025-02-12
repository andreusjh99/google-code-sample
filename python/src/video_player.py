"""A video player class."""

from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.currently_playing = ""
        self.paused = False
        self.playlists_dict = {}
        self.playlists = []
        self.flagged = {}

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
            print(
                f"{video._title} ({video._video_id}) [{' '.join(video._tags)}]"
                + (
                    f" - FLAGGED (reason: {self.flagged[video._video_id] if self.flagged[video._video_id] else 'Not supplied'})"
                    if video._video_id in self.flagged
                    else ""
                )
            )

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        if video_id in self.flagged:
            print(
                f"Cannot play video: Video is currently flagged "
                f"(reason: {self.flagged[video_id] if self.flagged[video_id] else 'Not supplied'})"
            )
        else:
            if self.currently_playing and self._video_library.get_video(video_id):
                self.stop_video()
                if self.paused:
                    self.paused = False

            if self._video_library.get_video(video_id):
                print(
                    f"Playing video: {self._video_library.get_video(video_id)._title}"
                )
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
        for i, x in self.flagged.items():
            video_ids.remove(i)

        if len(video_ids) == 0:
            print("No videos available")
        else:
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
        # if self.playlists.get(playlist_name.lower()):
        if playlist_name.lower() in self.playlists_dict:
            print(
                "Cannot create playlist: A playlist with the same name already exists"
            )
        else:
            print(f"Successfully created new playlist: {playlist_name}")
            self.playlists_dict[playlist_name.lower()] = []
            self.playlists.append(playlist_name)

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        if playlist_name.lower() not in self.playlists_dict:
            print("Cannot add video to another_playlist: Playlist does not exist")
        elif video_id not in self._video_library._videos:
            print(f"Cannot add video to {playlist_name}: Video does not exist")
        elif video_id in self.playlists_dict[playlist_name.lower()]:
            print(f"Cannot add video to {playlist_name}: Video already added")
        elif video_id in self.flagged:
            print(
                f"Cannot add video to {playlist_name}: Video is currently flagged "
                f"(reason: {self.flagged[video_id] if self.flagged[video_id] else 'Not supplied'})"
            )
        else:
            self.playlists_dict[playlist_name.lower()].append(video_id)
            print(
                f"Added video to {playlist_name}: {self._video_library.get_video(video_id)._title}"
            )

    def show_all_playlists(self):
        """Display all playlists."""
        if self.playlists:
            print("Showing all playlists:")
            self.playlists.sort()
            for i in self.playlists:
                print(i)
        else:
            print("No playlists exist yet")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in self.playlists_dict:
            print(f"Showing playlist: {playlist_name}")
            if self.playlists_dict[playlist_name.lower()]:
                # self.playlists_dict[playlist_name.lower()].sort()
                for video_id in self.playlists_dict[playlist_name.lower()]:
                    video = self._video_library.get_video(video_id)
                    print(
                        f"{video._title} ({video._video_id}) [{' '.join(video._tags)}]"
                        + (
                            f" - FLAGGED (reason: {self.flagged[video_id] if self.flagged[video_id] else 'Not supplied'})"
                            if video_id in self.flagged
                            else ""
                        )
                    )
            else:
                print("No videos here yet")
        else:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        # playlist exists
        # if self.playlists_dict.get(playlist_name.lower()):
        if playlist_name.lower() in self.playlists_dict:
            # video exists
            if self._video_library.get_video(video_id):
                # video in playlist
                if video_id in self.playlists_dict[playlist_name.lower()]:
                    self.playlists_dict[playlist_name.lower()].remove(video_id)
                    print(
                        f"Removed video from {playlist_name}: {self._video_library.get_video(video_id)._title}"
                    )
                else:  # video not in playlist
                    print(
                        f"Cannot remove video from {playlist_name}: Video is not in playlist"
                    )
            else:  # video does not exist
                print(f"Cannot remove video from {playlist_name}: Video does not exist")
        else:  # playlist does not exist
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in self.playlists_dict:
            self.playlists_dict[playlist_name.lower()] = []
            print(f"Successfully removed all videos from {playlist_name}")
        else:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in self.playlists_dict:
            del self.playlists_dict[playlist_name.lower()]
            self.playlists.remove(playlist_name)
            print(f"Deleted playlist: {playlist_name}")
        else:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        results = []
        for i, x in self._video_library._videos.items():
            if search_term.lower() in x._title.lower() and i not in self.flagged:
                results.append(x)

        if len(results) == 0:
            print(f"No search results for {search_term}")

        else:
            results.sort(key=lambda x: x._title)

            print(f"Here are the results for {search_term}:")
            for i in range(len(results)):
                video = results[i]
                print(
                    f"{i+1}) {video._title} ({video._video_id}) [{' '.join(video._tags)}]"
                )

            print(
                "Would you like to play any of the above? If yes, "
                "specify the number of the video.\n"
                "If your answer is not a valid number, we will assume "
                "it's a no."
            )
            num = input()
            if num.isnumeric() and (int(num) > 0 and int(num) <= len(results)):
                self.play_video(results[int(num) - 1]._video_id)

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        results = []
        for i, x in self._video_library._videos.items():
            if video_tag in x._tags and i not in self.flagged:
                results.append(x)

        if len(results) == 0:
            print(f"No search results for {video_tag}")

        else:
            results.sort(key=lambda x: x._title)

            print(f"Here are the results for {video_tag}:")
            for i in range(len(results)):
                video = results[i]
                print(
                    f"{i+1}) {video._title} ({video._video_id}) [{' '.join(video._tags)}]"
                )

            print(
                "Would you like to play any of the above? If yes, "
                "specify the number of the video.\n"
                "If your answer is not a valid number, we will assume "
                "it's a no."
            )
            num = input()
            if num.isnumeric() and (int(num) > 0 and int(num) <= len(results)):
                self.play_video(results[int(num) - 1]._video_id)

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """

        if video_id not in self._video_library._videos:
            print("Cannot flag video: Video does not exist")
        elif video_id in self.flagged:
            print("Cannot flag video: Video is already flagged")
        else:
            if video_id == self.currently_playing:
                self.stop_video()
            self.flagged[video_id] = flag_reason
            print(
                f"Successfully flagged video: {self._video_library.get_video(video_id)._title} "
                f"(reason: {flag_reason if flag_reason else 'Not supplied'})"
            )

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        if not self._video_library.get_video(video_id):
            print("Cannot remove flag from video: Video does not exist")
        elif video_id in self.flagged:
            del self.flagged[video_id]
            print(
                f"Successfully removed flag from video: {self._video_library.get_video(video_id)._title}"
            )
        else:
            print("Cannot remove flag from video: Video is not flagged")

