from project.album import Album


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        for alb in self.albums:
            if album_name == alb.name:
                if alb.published:
                    return f"Album has been published. It cannot be removed."

                else:
                    self.albums.remove(alb)
                    return f"Album {album_name} has been removed."
            else:
                return f"Album {album_name} is not found."
        # try:
        #     album = next(filter(lambda a: a.name == album_name, self.albums))
        # except StopIteration:
        #     return f"Album {album_name} is not found"
        # if album.published:
        #     return f"Album has been published. It cannot be removed."
        #
        # self.albums.remove(album)
        # return f"Album {album_name} has been removed."

    def details(self):
        alb = "\n".join([s.details() for s in self.albums])
        return f"Band {self.name}\n" + \
               f"{alb}"
